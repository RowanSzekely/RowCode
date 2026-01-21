from nodes import Node, NodeType
from values import NumberVal

def evaluate(node):
    match node.type:
        # Will create seperate functions for evaluating program and future nodes
        case NodeType.PROGRAM:
            last = None
            for stmt in node.body:
                last = evaluate(stmt)
            return last
        case NodeType.NUMERIC_LITERAL:
            return NumberVal(node.value)
        case NodeType.BINARY_EXPR:
            return eval_binary_expr(node)
        case _:
            raise Exception(f"No evaluation rule for {node.type}")

# Will move this
def eval_binary_expr(node):

    left = evaluate(node.left)
    right = evaluate(node.right)

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
