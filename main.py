from lexer import tokenize
from parser import Parser
from interpreter import evaluate

while True:
    try:
        source = input("    > ")
        if (source == "" or source == "exit"):
            break

        tokens = tokenize(source)
        parser = Parser(tokens)
        ast = parser.produce_ast()
        # print(ast)
        result = evaluate(ast)
        print(result)
        # print(result.value)
        
    except Exception as e:
        print("Error:", e)