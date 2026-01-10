# Will have different NodeTypes starting with these
class NodeType:
    PROGRAM = "PROGRAM"
    NUMERIC_LITERAL = "NUMERIC_LITERAL"
    IDENTIFIER = "IDENTIFIER"
    BINARY_EXPR = "BINARY_EXPR"

class Node:
    def __init__(self, type: NodeType):
        self.type = type

class Program(Node):
    def __init__(self):
        super().__init__(NodeType.PROGRAM)
        self.body = []
    def __repr__(self):
        return f"Program({self.type}, {self.body})"

class NumericLiteral(Node):
    def __init__(self, value):
        super().__init__(NodeType.NUMERIC_LITERAL)
        self.value = value

class Identifier(Node):
    def __init__(self, value):
        super().__init__(NodeType.IDENTIFIER)
        self.value = value


