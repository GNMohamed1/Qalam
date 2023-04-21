from interpreter import Interpreter

vars = {}

while True:
    try:
        code = input("Qalam >> ")
        if code == 'exit':
            break
        interpreter = Interpreter(vars)
        val_return, vars = interpreter.evaluate(code)
        print(val_return)
    except EOFError:
        break