# Will have different NodeTypes starting with these
class NodeType:

    # Statements
    PROGRAM = "PROGRAM"
    VAR_DECLARATION = "VAR_DECLARATION"
    BLOCK = "BLOCK"
    IF_STMT = "IF_STMT"
    FUNCTION_DECLARATION = "FUNCTION_DECLARATION"
    WHILE_LOOP = "WHILE_LOOP"
    RETURN_STMT = "RETURN_STMT"

    # Expressions
    NUMERIC_LITERAL = "NUMERIC_LITERAL"
    STRING_LITERAL = "STRING_LITERAL"
    ARRAY_LITERAL = "ARRAY_LITERAL"
    IDENTIFIER = "IDENTIFIER"
    BINARY_EXPR = "BINARY_EXPR"
    ASSIGNMENT_EXPR = "ASSIGNMENT_EXPR"
    COMPARISON_EXPR = "COMPARISON_EXPR"
    CALL_EXPR = "CALL_EXPR"
    UNARY_EXPR = "UNARY_EXPR"

# For non-expression statements
class Node:
    def __init__(self, type: NodeType):
        self.type = type
    
class Expression(Node):
    def __init__(self, type: NodeType):
        super().__init__(type)
    
class Program(Node):
    def __init__(self):
        super().__init__(NodeType.PROGRAM)
        self.body = []
    def __repr__(self):
        return f"Program(body={self.body})"

class ReturnStmt(Node):
    def __init__(self, value):
        super().__init__(NodeType.RETURN_STMT)
        self.value = value
    def __repr__(self):
        return f"Return(value={self.value})"

class WhileLoop(Node):
    def __init__(self, condition, body):
        super().__init__(NodeType.WHILE_LOOP)
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"WhileLoop(condition={self.condition}, body={self.body})"
    
class FunctionDeclaration(Node):
    def __init__(self, name, params, body):
        super().__init__(NodeType.FUNCTION_DECLARATION)
        self.name = name
        self.params = params
        self.body = body
    def __repr__(self):
        return f"FunctionDeclaration(name={self.name}, params={self.params}, body={self.body})"
    
class VarDeclaration(Node):
    def __init__(self, identifier, value, isConst):
        super().__init__(NodeType.VAR_DECLARATION)
        self.identifier = identifier
        self.value = value
        self.isConst = isConst
    def __repr__(self):
        return f"VarDeclaration({self.identifier} = {self.value}, isConst={self.isConst})"

class Block(Node):
    def __init__(self, body):
        super().__init__(NodeType.BLOCK)
        self.body = body
    def __repr__(self):
        return f"Block(body={self.body})"

class IfStmt(Node):
    def __init__(self, condition, body, elif_branches, else_block):
        super().__init__(NodeType.IF_STMT)
        self.condition = condition
        self.body = body
        self.elif_branches = elif_branches
        self.else_block = else_block
    def __repr__(self):
        return (
            f"IfStmt(if={self.condition} -> {self.body}, "
            f"elif={self.elif_branches}, else={self.else_block})"
        )
    
class UnaryExpr(Expression):
    def __init__(self, operator, operand):
        super().__init__(NodeType.UNARY_EXPR)
        self.operator = operator
        self.operand = operand
    def __repr__(self):
        return f"UnaryExpr({self.operator} {self.operand})"

class CallExpr(Expression):
    def __init__(self, callee, args):
        super().__init__(NodeType.CALL_EXPR)
        self.callee = callee
        self.args = args
    def __repr__(self):
        return f"CallExpr(callee={self.callee}, args={self.args})"

class NumericLiteral(Expression):
    def __init__(self, value):
        super().__init__(NodeType.NUMERIC_LITERAL)
        self.value = value
    def __repr__(self):
        return f"NumericLiteral({self.value})"
    
class StringLiteral(Expression):
    def __init__(self, value):
        super().__init__(NodeType.STRING_LITERAL)
        self.value = value
    def __repr__(self):
        return f'StringLiteral("{self.value}")'

class ArrayLiteral(Expression):
    def __init__(self, elements):
        super().__init__(NodeType.ARRAY_LITERAL)
        self.elements = elements
    def __repr__(self):
        return f'ArrayLiteral([{self.elements}])'

class Identifier(Expression):
    def __init__(self, symbol):
        super().__init__(NodeType.IDENTIFIER)
        self.symbol = symbol
    def __repr__(self):
        return f"Identifier({self.symbol!r})"

class BinaryExpr(Expression):
    def __init__(self, left, right, operator):
        super().__init__(NodeType.BINARY_EXPR)
        self.left = left
        self.right = right
        self.operator = operator
    def __repr__(self):
        return f"BinaryExpr({self.left} {self.operator} {self.right})"

class AssignmentExpr(Expression):
    def __init__(self, assignee, value):
        super().__init__(NodeType.ASSIGNMENT_EXPR)
        self.assignee = assignee
        self.value = value
    def __repr__(self):
        return f"AssignmentExpr({self.assignee} = {self.value})"
    
class ComparisonExpr(Expression):
    def __init__(self, left, operator, right):
        super().__init__(NodeType.COMPARISON_EXPR)
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return f"ComparisonExpr({self.left} {self.operator} {self.right})"
        


