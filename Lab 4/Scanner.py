import re

import Utils
from HashTable import HashTable


class Scanner:
    def __init__(self):
        self.pif = []
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

        errors = self.check_for_errors(all_tokens)
        # print(all_tokens)
        # print(self.content)
        x = 0
        while x < len(all_tokens):
            token = all_tokens[x]
            # if not self.is_valid_identifier(token):
            if token == '"':
                string_constant = ""
                x += 1
                while x < len(all_tokens) and all_tokens[x] != '"':
                    string_constant += str(all_tokens[x]) + " "
                    x += 1
                if x == len(all_tokens) and all_tokens[x - 1] != '"':
                    errors.append("No ending quotes")
                position = self.symbol_table.add('"' + string_constant + '"')
                self.pif.append(['"' + string_constant + '"', position])
            elif token == "=":
                if all_tokens[x + 1] == "=":
                    x += 1
                    token = "=="
                    self.pif.append([self.tokens.index(token), -1])
                else:
                    self.pif.append([self.tokens.index(token), -1])
            elif token in ["+", "-"]:
                if all_tokens[x - 1] in ["=", "("]:
                    x += 1
                    position = self.symbol_table.add(int(str(token) + str(all_tokens[x])))
                    self.pif.append([str(token) + str(all_tokens[x]), position])
                else:
                    self.pif.append([self.tokens.index(token), -1])
            elif token not in self.tokens and token not in ['(', ')']:
                # print(token)
                position = self.symbol_table.add(token)
                self.pif.append([token, position])
            else:
                if token == '(':
                    self.pif.append([28, -1])
                elif token == ')':
                    self.pif.append([29, -1])
                else:
                    self.pif.append([self.tokens.index(token), -1])
            x += 1

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
                return "Lexical error at line " + str(line_number) + " at position " + str(position) + " : " + str(
                    token)
            line_number += 1
        return '0'

    def write_pif(self):
        # for token in self.symbol_table.get_keys():
        #     position = self.symbol_table.get_position(token)
        #     self.pif += 'token ' + str(token) + " -> " + str(position) + '\n'
        pif = ""
        for token in self.pif:
            pif += str(token[0]) + " -> (" + str(token[1]) + ')\n'
        Utils.write("PIF.out", pif)

    # def initialize_pif(self):
    #     pass
    def check_for_errors(self, all_tokens):
        errors = []
        for token in all_tokens:
            if token not in self.tokens and token not in ['(', ')']:
                # print(token)
                if not self.is_valid_identifier(token):
                    print(token)
                    errors.append(str(self.find_error(token)))
        return errors
