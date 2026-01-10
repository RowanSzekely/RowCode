# Will have different NodeTypes starting with these
class NodeType:

    # Statements
    PROGRAM = "PROGRAM"
    NUMERIC_LITERAL = "NUMERIC_LITERAL"

    # Expressions
    IDENTIFIER = "IDENTIFIER"
    BINARY_EXPR = "BINARY_EXPR"

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

class NumericLiteral(Node):
    def __init__(self, value):
        super().__init__(NodeType.NUMERIC_LITERAL)
        self.value = value
    def __repr__(self):
        return f"NumericLiteral({self.value})"

class Identifier(Node):
    def __init__(self, symbol):
        super().__init__(NodeType.IDENTIFIER)
        self.symbol = symbol
    def __repr__(self):
        return f"Identifier({self.symbol!r})"

class BinaryExpr(Node):
    def __init__(self, left, right, operator):
        super().__init__(NodeType.BINARY_EXPR)
        self.left = left
        self.right = right
        self.operator = operator
    def __repr__(self):
        return f"BinaryExpr({self.left} {self.operator} {self.right})"


