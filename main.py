from src.interpreter import Interpreter
import sys


interpreter = Interpreter()
filename = sys.argv[1]


while True:
    try:
        if filename:
            val_return = interpreter.evaluate_file(filename)
            print(val_return)
            break
        code = input("Qalam >> ")
        if code == 'exit':
            break
        val_return = interpreter.evaluate(code)
        print(val_return)
    except EOFError:
        break