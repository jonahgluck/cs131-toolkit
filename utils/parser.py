import os
from typing import List


class parser():
    '''takes a file and creates tokens for tree'''
    def __init__(self, file, token_list: List = []):
        self.file = file
        self.data = []
        self.token_list = {
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
        self.tokenize(token_list)

    def parenthesis_validator(self, data):
        '''validate parenthesis'''
        open_parenthesis = 0
        close_parenthesis = 0

        for char in data:
            if char == '(':
                open_parenthesis += 1
            elif char == ')':
                close_parenthesis += 1

        if open_parenthesis != close_parenthesis:
            raise Exception('Parenthesis mismatch in file: ' + self.file + ' at line: ' + str(self.get_length()) + '\n' + data)

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

    def tokenize(self, token_list):
        if token_list == []:
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
    p = parser('tests/sample.txt')
    print(p)
