from lexer import Lexer
from parse import Parser



class Interpreter:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

        self.lexer.build()
        self.parser.build()

    def evaluate(self, input_str):
        return self.parser.parser.parse(input_str, lexer=self.lexer.lexer)


if __name__ == '__main__':
    interpreter = Interpreter()
    print(interpreter.evaluate("2 + 3 * 4"))
