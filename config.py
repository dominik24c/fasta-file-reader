#!/usr/bin/python3

import pathlib

FILES_FORMAT = [
    'fasta'
]

BASE_DIR = pathlib.Path(__file__).parent.resolve()

DATA_DIR = BASE_DIR / 'data'

NUCLEOTIDES = [
    'A', 'C', 'G', 'T', 'U', 'R',
    'Y', 'K', 'M', 'S', 'W',
    'B', 'D', 'H', 'V', 'N', 'X', '-'
]
AMINO_ACIDS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'Y', 'Z', 'X', '*', '-',
]

TYPE_AMINO_ACIDS = 'amino acids'
TYPE_NUCLEOTIDES = 'nucleotides'
