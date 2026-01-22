from lexer import tokenize
from parser import Parser
from interpreter import evaluate
from environment import Environment
from values import TRUE, FALSE, NULL

env = Environment()
# These need to be constants or they can be reassigned
env.declare_var("true", TRUE)
env.declare_var("false", FALSE)
env.declare_var("null", NULL)

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