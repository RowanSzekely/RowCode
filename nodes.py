# Will have different NodeTypes starting with these
class NodeType:

    # Statements
    PROGRAM = "PROGRAM"
    NUMERIC_LITERAL = "NUMERIC_LITERAL"
    VAR_DECLARATION = "VAR_DECLARATION"
    BLOCK = "BLOCK"

    # Expressions
    IDENTIFIER = "IDENTIFIER"
    BINARY_EXPR = "BINARY_EXPR"
    ASSIGNMENT_EXPR = "ASSIGNMENT_EXPR"

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
        return f"Program(\n\t{self.body}\n)"
    
class VarDeclaration(Node):
    def __init__(self, identifier, value, isConst):
        super().__init__(NodeType.VAR_DECLARATION)
        self.identifier = identifier
        self.value = value
        self.isConst = isConst
    def __repr__(self):
        return f"VarDeclaration({self.identifier} = {self.value}, isConst: {self.isConst})"

class Block(Node):
    def __init__(self, body):
        super().__init__(NodeType.BLOCK)
        self.body = body
    def __repr__(self):
        return f"Block({self.body})"

class NumericLiteral(Expression):
    def __init__(self, value):
        super().__init__(NodeType.NUMERIC_LITERAL)
        self.value = value
    def __repr__(self):
        return f"NumericLiteral({self.value})"

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


