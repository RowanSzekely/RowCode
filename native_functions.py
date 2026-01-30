from values import NullVal

# Very simple print function
# Only supports a comma-seperated list of NumVals, BoolVals, and NullVals
def native_print(args, env):
    output = []
    for arg in args:
        output.append(str(arg))

    print("".join(output))
    return NullVal()