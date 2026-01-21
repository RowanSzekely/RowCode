from nodes import Node, NodeType
from values import NumberVal, NullVal

def evaluate(node, env):
    match node.type:
        # Will create seperate functions for evaluating program and future nodes
        case NodeType.PROGRAM:
            return eval_program(node, env)
        case NodeType.NUMERIC_LITERAL:
            return NumberVal(node.value)
        case NodeType.BINARY_EXPR:
            return eval_binary_expr(node, env)
        case NodeType.IDENTIFIER:
            return eval_identifier(node, env)
        case NodeType.VAR_DECLARATION:
            return eval_var_declaration(node, env)
        case _:
            raise Exception(f"No evaluation rule for {node.type}")

# Will move these
def eval_binary_expr(node, env):

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
    
def eval_program(node, env):

    last = NullVal()
    for stmt in node.body:
        last = evaluate(stmt, env)
    return last

def eval_var_declaration(node, env):

    value = evaluate(node.value, env)
    env.declare_var(node.identifier.value, value)
    return NullVal()

def eval_identifier(node, env):
    return env.lookup_var(node.symbol)

