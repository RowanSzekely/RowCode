import sys
from lexer import tokenize
from parser import Parser
from eval.interpreter import evaluate
from environment import Environment
from values import TRUE, FALSE, NULL, NativeFunctionVal
from native_functions import native_print, native_length, native_random

def create_global_env():
    env = Environment(in_function=False)
    env.declare_var("true", TRUE, True)
    env.declare_var("false", FALSE, True)
    env.declare_var("null", NULL, True)
    env.declare_var("print", NativeFunctionVal(native_print), True)
    env.declare_var("length", NativeFunctionVal(native_length), True)
    env.declare_var("random", NativeFunctionVal(native_random), True)
    return env

env = create_global_env()

def run(source, env):
    tokens = tokenize(source)
    parser = Parser(tokens)
    ast = parser.produce_ast()
    # print(ast)
    result = evaluate(ast, env)
    return result

# File Mode
if (len(sys.argv) > 1):
    filename = sys.argv[1]

    with (open(filename, "r") as f):
        source = f.read()

    result = run(source, env)
    # print(result)
    sys.exit(0)

# REPL Mode
while True:
    try:
        source = input("    > ")
        if (source == "" or source == "exit"):
            break
        
        result = run(source, env)
        # print(result)
        
    except Exception as e:
        print("Error:", e)