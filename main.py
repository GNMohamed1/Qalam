from interpreter import Interpreter

while True:
    try:
        code = input("Qalam >> ")
        if code == 'exit':
            break
        interpreter = Interpreter()
        val_return = interpreter.evaluate(code)
        print(val_return)
    except EOFError:
        break