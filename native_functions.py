from values import NullVal, NumberVal

# Very simple print function
# Only supports a comma-seperated list of NumVals, BoolVals, and NullVals
def native_print(args, env):
    output = []
    for arg in args:
        output.append(str(arg))

    print("".join(output))
    return NullVal()

def native_length(args, env):
    if len(args) != 1:
        raise Exception("length() expects exactly one argument")
    arr = args[0]
    if (arr.type != "array"):
        raise Exception("length() expects an array")
    
    return NumberVal(len(arr.elements))
