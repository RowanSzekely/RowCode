from nodes import NodeType
from values import NumberVal, NullVal, BoolVal, ArrayVal
from environment import Environment
from signals import ReturnSignal
# evaluate is imported locally to avoid circular import

def eval_binary_expr(node, env):
    from .interpreter import evaluate

    left = evaluate(node.left, env)
    right = evaluate(node.right, env)

    if (left.type != "number" or right.type != "number"):
        raise Exception("Only numbers supported when evaluating binary expressions")

    if (node.operator == "+"):
        return NumberVal(left.value + right.value)
    if (node.operator == "-"):
        return NumberVal(left.value - right.value)
    if (node.operator == "*"):
        return NumberVal(left.value * right.value)
    if (node.operator == "/"):
        return NumberVal(left.value // right.value)
    if (node.operator == "%"):
        return NumberVal(left.value % right.value)
    
    raise Exception(f"Unknown operator {node.operator}")

def eval_unary_expr(node, env):
    from .interpreter import evaluate

    operand = evaluate(node.operand, env)

    if (node.operator == "-"):
        if (operand.type != "number"):
            raise Exception("Unary '-' expects a number")
        return NumberVal(-operand.value)
    if (node.operator == "!"):
        if (operand.type != "boolean"):
            raise Exception("Unary '!' expects a boolean")
        return BoolVal(not operand.value)

    raise Exception(f"Unknown unary operator {node.operator}")

def eval_assignment_expr(node, env):
    from .interpreter import evaluate

    if (node.assignee.type == NodeType.IDENTIFIER):
        value = evaluate(node.value, env)
        env.assign_var(node.assignee.symbol, value)
        return value
    
    if (node.assignee.type == NodeType.INDEX_EXPR):
        value = evaluate(node.value, env)
        array_val = evaluate(node.assignee.array, env)
        index_val = evaluate(node.assignee.index, env)

        if (array_val.type != "array"):
            raise Exception("Can only index arrays")
        if (index_val.type != "number"):
            raise Exception("Array index must be a number")

        array_val.elements[index_val.value] = value
        return value
    
    # To make sure something like (1+2) = 5 isn't allowed
    raise Exception("Invalid assignment target")

def eval_call_expr(node, env):
    from .interpreter import evaluate

    # env is where the function is called
    # fn.env is where the function was defined
    # call_env will be a new env created for each call

    # Get the FunctionVal
    fn = evaluate(node.callee, env)

    # Native functions
    if (fn.type == "native_function"):
        args = []
        for arg in node.args:
            value = evaluate(arg, env)
            args.append(value)
        return fn.fn(args, env)

    if (fn.type != "function"):
        raise Exception("Can only call functions")

    if (len(node.args) != len(fn.params)):
        raise Exception("Incorrect number of arguments")

    # An env to hold local variables and params
    call_env = Environment(parent=fn.env, in_function=True)

    # Setting up the params
    i = 0
    while (i < len(fn.params)):
        param = fn.params[i]
        arg = node.args[i]

        # We use the env with the variables available when the function was called (env)
        # The params will be kept in the local env (call_env)
        value = evaluate(arg, env)
        call_env.declare_var(param, value)

        i += 1

    result = NullVal()

    # If "return" is parsed, a ReturnSignal is called, otherwise functions return the last statement evaluated
    try:
        # eval_block() creates a new env so I'll avoid using it
        for stmt in fn.body.body:
            # The function body runs in the local env (call_env), not the caller's env (env)
            result = evaluate(stmt, call_env)
            
    except ReturnSignal as return_signal:
        return return_signal.value

    return result

def eval_comp_expr(node, env):
    from .interpreter import evaluate

    left = evaluate(node.left, env)
    right = evaluate(node.right, env)

    # Comparisons with null (which doesn't have a .value)
    if (left.type == "null" or right.type == "null"):
        if (node.operator == "=="):
            return BoolVal(left.type == "null" and right.type == "null")
        if (node.operator == "!="):
            return BoolVal(not (left.type == "null" and right.type == "null"))
        raise Exception(f"Cannot compare null {right.type} with {left.type}")

    if (left.type != right.type):
        raise Exception("Cannot compare values of different types")
    
    if node.operator == "==":
        return BoolVal(left.value == right.value)
    if node.operator == "!=":
        return BoolVal(left.value != right.value)
    if node.operator == ">":
        return BoolVal(left.value > right.value)
    if node.operator == ">=":
        return BoolVal(left.value >= right.value)
    if node.operator == "<":
        return BoolVal(left.value < right.value)
    if node.operator == "<=":
        return BoolVal(left.value <= right.value)
    
def eval_identifier(node, env):
    return env.lookup_var(node.symbol)

def eval_array_literal(node, env):
    from .interpreter import evaluate

    elements = []
    for element in node.elements:
        value = evaluate(element, env)
        elements.append(value)
    return ArrayVal(elements)

def eval_index_expr(node, env):
    from .interpreter import evaluate

    array_val = evaluate(node.array, env)
    index_val = evaluate(node.index, env)

    if (array_val.type != "array"):
        raise Exception("Can only index arrays")
    if (index_val.type != "number"):
        raise Exception("Array index must be a number")

    return array_val.elements[index_val.value]