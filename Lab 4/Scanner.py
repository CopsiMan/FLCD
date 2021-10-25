import re

import Utils
from HashTable import HashTable


class Scanner:
    def __init__(self):
        self.pif = ""
        self.symbol_table = HashTable()
        self.content = None
        self.tokens = Utils.read("tokens.txt").split("\n")
        # self.tokens.append("\n")

    def scan(self, filename):
        self.content = Utils.read(filename)
        # for line in self.content.split("\n"):
        #     print(line)

    def write_symbol_table(self):
        Utils.write("ST.out", str(self.symbol_table))

    def initialize_symbol_table(self):
        string = list(filter(''.__ne__, re.split('|'.join([' ', '\n']), self.content)))
        # print(string)
        all_tokens = []
        split_rule = '(' + ('|'.join(self.tokens)) + ')'
        # split_rule = '|'.join(self.tokens)
        # print(split_rule)
        # print(self.tokens)
        for token in string:
            all_tokens.extend(list(filter(''.__ne__, re.split(split_rule, token))))
        all_tokens = list(filter(None.__ne__, all_tokens))

        errors = []
        # print(all_tokens)
        # print(self.content)
        for token in all_tokens:
            # if token not in self.tokens and (not '(' and not ')'):
            if token not in self.tokens and token not in ['(', ')']:
                # print(token)
                if not self.is_valid_identifier(token):
                    print(token)
                    errors.append(str(self.find_error(token)))
                position = self.symbol_table.add(token)
                self.pif += str(token) + " -> (" + \
                            str(position.position_in_table) + ", " + \
                            str(position.position_in_list) + ')\n'
            else:
                self.pif += str(token) + " -> -1 \n"
        if len(errors) == 0:
            errors.append("Lexically correct")
        return errors

    def is_valid_identifier(self, token):
        if token.isnumeric():
            return True
        try:
            return token[0] != '_' and int(token[0]) not in list(range(10))
        except ValueError:
            return token[0] != '_'

    def find_error(self, token):
        line_number = 1
        for line in self.content.split('\n'):
            position = line.find(token)
            if position != -1:
                return "Lexical error at line " + str(line_number) + " at position " + str(position) + " : " + str(token)
            line_number += 1
        return '0'

    def write_pif(self):
        # for token in self.symbol_table.get_keys():
        #     position = self.symbol_table.get_position(token)
        #     self.pif += 'token ' + str(token) + " -> " + str(position) + '\n'
        Utils.write("PIF.out", self.pif)

    # def initialize_pif(self):
    #     pass
