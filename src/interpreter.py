from src.lexer import Lexer
from src.parse import Parser
from src.table import SymbolTable



class Interpreter:
    def __init__(self):
        self.global_table = SymbolTable()
        self.lexer = Lexer()
        self.parser = Parser(self.global_table)

        self.lexer.build()
        self.parser.build()
        
    def evaluate_file(self, filename):
        with open(filename, 'r') as file:
            input_str = file.read()
        return self.evaluate(input_str)

    def evaluate(self, input_str):
        return_val = self.parser.parser.parse(input_str, lexer=self.lexer.lexer)
        self.global_table = self.parser.symbol_table
        return return_val


if __name__ == '__main__':
    interpreter = Interpreter(vars={})
    print(interpreter.evaluate("متغير أ = 10 " + "أ + 20"))
