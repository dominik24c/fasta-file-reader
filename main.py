#!/usr/bin/python3

import sys

from bar_graph import BarGraph
from exceptions import DoesNotPassedFilenameArg
from fasta_file_reader import FastaFileReader


def main(filename: str) -> None:
    file_reader = FastaFileReader(filename)
    file_reader.read()
    data = file_reader.get_data()
    type_of_sequence = file_reader.get_type_of_sequence()
    bargraph = BarGraph(_data=list(data.values()),
                        _keys=list(data.keys()),
                        _type_of_sequence=type_of_sequence)

    bargraph.display()


if __name__ == '__main__':
    '''
    To run code
    python3 main.py fielname.fasta
    '''
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        main(filename)
    else:
        raise DoesNotPassedFilenameArg('You have to pass fasta filename')
