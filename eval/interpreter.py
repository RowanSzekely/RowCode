from nodes import NodeType
from values import NumberVal, StringVal
from .expressions import (
    eval_comp_expr, eval_assignment_expr, eval_binary_expr, 
    eval_call_expr, eval_identifier, eval_unary_expr, eval_array_literal
    )
from .statements import (
    eval_program, eval_if_stmt, eval_block, eval_function_decl, 
    eval_var_declaration, eval_while_loop, eval_return_stmt
    )

def evaluate(node, env):
    match node.type:
        case NodeType.PROGRAM:
            return eval_program(node, env)
        case NodeType.NUMERIC_LITERAL:
            return NumberVal(node.value)
        case NodeType.STRING_LITERAL:
            return StringVal(node.value)
        case NodeType.BINARY_EXPR:
            return eval_binary_expr(node, env)
        case NodeType.UNARY_EXPR:
            return eval_unary_expr(node, env)
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
        case NodeType.WHILE_LOOP:
            return eval_while_loop(node, env)
        case NodeType.COMPARISON_EXPR:
            return eval_comp_expr(node, env)
        case NodeType.FUNCTION_DECLARATION:
            return eval_function_decl(node, env)
        case NodeType.CALL_EXPR:
            return eval_call_expr(node, env)
        case NodeType.RETURN_STMT:
            return eval_return_stmt(node, env)
        case NodeType.ARRAY_LITERAL:
            return eval_array_literal(node, env)
        case _:
            raise Exception(f"No evaluation rule for {node.type}")


    



