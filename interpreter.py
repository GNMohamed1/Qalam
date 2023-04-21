from lexer import Lexer
from parse import Parser



class Interpreter:
    def __init__(self, vars):
        self.vars = vars
        self.lexer = Lexer()
        self.parser = Parser(vars)

        self.lexer.build()
        self.parser.build()

    def evaluate(self, input_str):
        return self.parser.parser.parse(input_str, lexer=self.lexer.lexer), self.parser.vars


if __name__ == '__main__':
    interpreter = Interpreter(vars={})
    print(interpreter.evaluate("متغير أ = 10 " + "أ + 20"))
