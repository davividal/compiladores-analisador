#!/usr/bin/python
# -*- coding: utf8 -*-

simbolos = {
    '0': True,
    '1': True,
    '2': True,
    '3': True,
    '4': True,
    '5': True,
    '6': True,
    '7': True,
    '8': True,
    '9': True,
    '+': True,
    '-': True,
    '*': True,
    '/': True,
    '(': True,
    ')': True,
    ' ': True,
}

tokens = {
    '0': 'T_NUM',
    '1': 'T_NUM',
    '2': 'T_NUM',
    '3': 'T_NUM',
    '4': 'T_NUM',
    '5': 'T_NUM',
    '6': 'T_NUM',
    '7': 'T_NUM',
    '8': 'T_NUM',
    '9': 'T_NUM',
    '+': 'T_OP',
    '-': 'T_OP',
    '*': 'T_OP',
    '/': 'T_OP',
    '(': 'T_AP',
    ')': 'T_FP',
    ' ': 'T_SP',
}

cadeias = [
    "2 + (5 * 2)",
    ")-3",
    "abc + 2",
    "2+(5*2)",
    "2 2",
    "22"
]

class Cadeia(object):
    errors = []
    cadeia = None
    tokenized = None

    def __init__(self, cadeia):
        self.cadeia = cadeia

    def add_error(self, error):
        self.errors.append(error)

    def valid(self):
        self.errors = []
        for char in cadeia:
            if not char in simbolos:
                self.add_error("Símbolo <{0}> não conhecido!".format(char))

        return len(self.errors) == 0

    def print_errors(self):
        if len(self.errors) == 0:
            return

        print('Erro léxico encontrado:')
        for e in self.errors:
            print("\t{0}".format(e))

    def tokenize(self):
        self.tokenized = ""
        if not self.valid():
            raise Exception("Cadeia inválida")

        for char in self.cadeia:
            self.tokenized += " " + tokens[char]

        print("Cadeia: {0}\nToken: {1}".format(self.cadeia, self.tokenized))

        

def tokenize_cadeia(cadeia):
    if not cadeia_valida(cadeia):
        pass
    for char in cadeia:
        pass

for cadeia in cadeias:
    objeto_cadeia = Cadeia(cadeia)
    if not objeto_cadeia.valid():
        objeto_cadeia.print_errors()
    else:
        objeto_cadeia.tokenize()


entrada = "2 + (5 * 2)"
saida = "T_NUM T_MAIS T_AP T_NUM T_MULT T_NUM T_FP"

entrada = ")-3"
saida = "T_FP T_MENOS T_NUM"

entrada = "3 3"
saida = "T_NUM T_SPACE T_NUM"