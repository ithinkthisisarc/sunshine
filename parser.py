from rply import ParserGenerator
from ast import *


class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINTLN', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MULTIPLY', 'DIVIDE', 'EQUALTO', 'NEQUALTO']
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINTLN OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        @self.pg.production('program : program program')
        def program(p):
            line_count = 0
            for i in p:
                if p == "SEMI_COLON":
                    line_count = line_count + 1
            return Println(self.builder, self.module, self.printf, p[2 + (line_count * 4)])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULTIPLY expression')
        @self.pg.production('expression : expression DIVIDE expression')
        @self.pg.production('expression : expression EQUALTO expression')
        @self.pg.production('expression : expression NEQUALTO expression')

        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MULTIPLY':
                return Multiply(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIVIDE':
                return Divide(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'EQUALTO':
                return Equals(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'NEQUALTO':
                return Nequals(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()