from lexer import tokenize
from parser import Parser

while True:
    try:
        source = input("    > ")
        if (source == "" or source == "exit"):
            break

        tokens = tokenize(source)
        parser = Parser(tokens)
        ast = parser.produce_ast()
        print(ast)
        
    except Exception as e:
        print("Error:", e)