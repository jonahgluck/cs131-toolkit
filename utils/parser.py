import os
from typing import List, Dict, Optional


class parser():
    '''takes a file and creates tokens for tree'''
    def __init__(self, file, token_vocab: Optional[Dict[str, str]] = None):
        self.file = file
        self.data = []
        self.token_vocab = {
            'xor': 'XOR',
            'or': 'OR',
            'and': 'AND',
            'not': 'NOT',
            'true': 'TRUE',
            'false': 'FALSE',
            'if': 'IF',
            'iff': 'IFF',
            'nand': 'NAND',
            'nor': 'NOR',
            'xnor': 'XNOR',
            '+': 'OR',
            '*': 'AND',
            '~': 'NOT',
            '\\\\': 'NEWLINE',
        }

        self.parse()
        self.lexical_analysis(token_vocab)

    def parse(self):
        '''gather data to tokenize operators'''
        with open(self.file, 'r') as f:
            for line in f:
                self.data.append(line.strip())

    def get(self, index):
        '''return data at index'''
        return self.data[index]

    def get_all(self):
        '''return all data'''
        return self.data

    def get_length(self):
        '''return length of data'''
        return len(self.data)

    def lexical_analysis(self, token_list):
        if token_list is None:
            token_list = self.token_list

        for i in range(self.get_length()):
            for key, value in token_list.items():
                self.data[i] = self.data[i].replace(key, value)

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    '''test parser'''
    os.chdir('..')

    # testing file is called: sample.txt
    p = parser('tests/sample.txt', {'+': 'OR', '*': 'AND'})
    print(p)
