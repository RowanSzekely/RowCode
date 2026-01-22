from lexer import tokenize
from parser import Parser
from interpreter import evaluate
from environment import Environment
from values import TRUE, FALSE, NULL

env = Environment()

env.declare_var("true", TRUE, True)
env.declare_var("false", FALSE, True)
env.declare_var("null", NULL, True)

while True:
    try:
        source = input("    > ")
        if (source == "" or source == "exit"):
            break
        
        tokens = tokenize(source)
        parser = Parser(tokens)
        ast = parser.produce_ast()
        # print(ast)
        result = evaluate(ast, env)
        print(result)
        
    except Exception as e:
        print("Error:", e)