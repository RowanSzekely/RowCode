from values import NullVal, NumberVal
import random

# Very simple print function
# Only supports a comma-seperated list of runtimeVals (NumVals, BoolVals, etc.)
def native_print(args, env):
    output = []
    for arg in args:
        output.append(str(arg))

    print("".join(output))
    return NullVal()

# Returns the length of an array
def native_length(args, env):
    if (len(args) != 1):
        raise Exception("length() expects exactly one argument")
    arr = args[0]
    if (arr.type != "array"):
        raise Exception("length() expects an array")
    
    return NumberVal(len(arr.elements))

# Returns a random integer between two values inclusive
def native_random(args, env):
    if (len(args) != 2):
        raise Exception("random() expects two arguments")
    min_val = args[0]
    max_val = args[1]

    if (min_val.type != "number" or max_val.type != "number"):
        raise Exception("random() expects two numbers")
    if (min_val.value > max_val.value):
        raise Exception("random() expects min <= max")

    return NumberVal(random.randint(min_val.value, max_val.value))
