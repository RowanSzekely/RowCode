from nodes import Node, NodeType
from values import NumberVal, NullVal, BoolVal
from environment import Environment

def evaluate(node, env):
    match node.type:
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
        case NodeType.ASSIGNMENT_EXPR:
            return eval_assignment_expr(node, env)
        case NodeType.BLOCK:
            return eval_block(node, env)
        case NodeType.IF_STMT:
            return eval_if_stmt(node, env)
        case NodeType.COMPARISON_EXPR:
            return eval_comp_expr(node, env)
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

def eval_block(node, env):
    # Creates a new env under the env the block was declared in
    block_env = Environment(parent = env)

    last = NullVal()
    for stmt in node.body:
        last = evaluate(stmt, block_env)
    return last

def eval_if_stmt(node, env):
    condition = evaluate(node.condition, env)

    if(condition.type != "boolean"):
        raise Exception("If condition must be a boolean")
    if(condition.value):
        return evaluate(node.body, env) # A new env is created because eval_block() will be called
    
    for elif_condition, elif_block in node.elif_branches:
        condition_val = evaluate(elif_condition, env)

        if(condition_val.type != "boolean"):
            raise Exception("Elif condition must be a boolean")
        if(condition_val.value):
            return evaluate(elif_block, env)
        
    if (node.else_block is not None):
        return evaluate(node.else_block, env)
    
    return NullVal()

def eval_var_declaration(node, env):

    value = evaluate(node.value, env)
    env.declare_var(node.identifier.value, value, node.isConst)
    return NullVal()

def eval_identifier(node, env):
    return env.lookup_var(node.symbol)

def eval_assignment_expr(node, env):
    # To make sure something like (1+2) = 5 isn't allowed
    if (node.assignee.type != NodeType.IDENTIFIER):
        raise Exception("Invalid assignment target")
    value = evaluate(node.value, env)
    env.assign_var(node.assignee.symbol, value)
    return value

def eval_comp_expr(node, env):
    left = evaluate(node.left, env)
    right = evaluate(node.right, env)

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
