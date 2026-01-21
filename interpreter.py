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
        case _:
            raise Exception(f"No evaluation rule for {node.type}")