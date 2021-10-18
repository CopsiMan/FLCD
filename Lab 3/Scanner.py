import re

import Utils
from HashTable import HashTable


class Scanner:
    def __init__(self):
        self.symbol_table = HashTable()
        self.content = None
        self.tokens = Utils.read("tokens.txt").split("\n")
        # self.tokens.append("\n")

    def scan(self, filename):
        self.content = Utils.read(filename)
        for line in self.content.split("\n"):
            print(line)

    def write_symbol_table(self):
        Utils.write("ST.out", str(self.symbol_table))

    def initialize_symbol_table(self):
        string = list(filter(''.__ne__, re.split('|'.join([' ', '\n']), self.content)))
        # print(string)
        all_tokens = []
        split_rule = '(' + ('|'.join(self.tokens)) + ')'
        # split_rule = '|'.join(self.tokens)
        # print(split_rule)
        print(self.tokens)
        for token in string:
            all_tokens.extend(list(filter(''.__ne__, re.split(split_rule, token))))
        all_tokens = list(filter(None.__ne__, all_tokens))
        # print(all_tokens)

        for token in all_tokens:
            # if token not in self.tokens and (not '(' and not ')'):
            self.symbol_table.add(token)
