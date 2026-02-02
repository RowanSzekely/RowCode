from values import NullVal, FunctionVal
from environment import Environment
from signals import ReturnSignal
# evaluate is imported locally to avoid circular import

def eval_program(node, env):
    from .interpreter import evaluate

    last = NullVal()
    for stmt in node.body:
        last = evaluate(stmt, env)
    return last

def eval_block(node, env):
    from .interpreter import evaluate

    # Creates a new env under the env the block was declared in
    block_env = Environment(parent = env)

    last = NullVal()
    for stmt in node.body:
        last = evaluate(stmt, block_env)
    return last

def eval_function_decl(node, env):
    # Create a new FunctionVal in env
    fn = FunctionVal(node.params, node.body, env)
    env.declare_var(node.name, fn, True)
    return NullVal()

def eval_if_stmt(node, env):
    from .interpreter import evaluate

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

def eval_while_loop(node, env):
    from .interpreter import evaluate

    result = NullVal()
    condition = evaluate(node.condition, env)

    if (condition.type == "boolean"):
        while True:
            condition = evaluate(node.condition, env)

            if (condition.type != "boolean"):
                raise Exception("While condition must be a boolean")
            if (not condition.value):
                break
            result = evaluate(node.body, env)
    
        return result
    
    # while(n){} will run the loop n times (even if n is modified during the loop)
    if (condition.type == "number"):
        iterations = condition.value

        if (iterations < 0):
            raise Exception("While loop input must be positive")

        i = 0
        while (i < iterations):
            result = evaluate(node.body, env)
            i += 1

        return result

    raise Exception("While condition must be a boolean or a number")

def eval_var_declaration(node, env):
    from .interpreter import evaluate

    value = evaluate(node.value, env)
    env.declare_var(node.identifier.value, value, node.isConst)
    return NullVal()

def eval_return_stmt(node, env):
    from .interpreter import evaluate

    if (not env.in_function):
        raise Exception("Return statement can only be used inside a function")

    if (node.value is None):
        raise ReturnSignal(NullVal())

    value = evaluate(node.value, env)
    raise ReturnSignal(value)