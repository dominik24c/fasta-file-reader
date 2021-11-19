#!/usr/bin/python3

from config import FILES_FORMAT, AMINO_ACIDS, NUCLEOTIDES, \
    DATA_DIR, TYPE_AMINO_ACIDS, TYPE_NUCLEOTIDES
from exceptions import InvalidFormatFile, InvalidSequence, StopTranslationException


class FastaFileReader(object):
    def __init__(self, filename: str):
        self.validate_format_file(filename)
        self.__filename = DATA_DIR / filename
        self.__data = {}
        self.__type_of_sequence = "Unknown"
        # self.__length_of_sequence: int

    def get_data(self) -> dict:
        return self.__data

    def get_type_of_sequence(self) -> str:
        return self.__type_of_sequence

    def calculate_number_of_sequence(self) -> int:
        count = 0
        for key, value in self.__data.items():
            if key not in ['*', '-']:
                count += value
        return count

    def validate_format_file(self, filename: str) -> None:
        f = filename.split('.')
        if len(f) != 2 or f[1] not in FILES_FORMAT:
            raise InvalidFormatFile()

    def parse_data(self, line: str) -> None:
        for sign in line:
            if sign in self.__data:
                self.__data[sign] += 1
            else:
                if sign in NUCLEOTIDES or sign in AMINO_ACIDS:
                    if sign == '-':
                        '''gap of indeterminate length '''
                        pass
                    elif sign == '*' and sign in AMINO_ACIDS:
                        '''translation stop '''
                        raise StopTranslationException('StopTranslationException was thrown!')
                    else:
                        self.__data.update({sign: 1})
                else:
                    raise InvalidSequence()

    def print(self) -> None:
        for key, value in self.__data.items():
            print(f"{key} - {value}")
        print(f"Length of sequence {self.calculate_number_of_sequence()}")

    def read(self) -> None:
        try:
            with open(self.__filename) as f:
                for line in f:
                    line = line.strip()
                    length = len(line)
                    if length > 0 and line[0] == '>':
                        # print(f"Comment: {line[1:]}")
                        pass
                    elif length > 0:
                        self.parse_data(line)
        except StopTranslationException as e:
            print(f'{e}')
        self.print()
        keys = set(self.__data.keys())

        if keys.issubset(set(NUCLEOTIDES)):
            self.__type_of_sequence = TYPE_NUCLEOTIDES
            print(f'It is a {TYPE_NUCLEOTIDES}')
        elif keys.issubset(set(AMINO_ACIDS)):
            self.__type_of_sequence = TYPE_AMINO_ACIDS
            print(f'It is an {TYPE_AMINO_ACIDS}')
