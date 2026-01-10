from nodes import Node, NodeType, Program, NumericLiteral, Identifier
from lexer import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    # Helper returns cur token
    def current_token(self):
        if (self.pos < len(self.tokens)):
            return self.tokens[self.pos]
        return Token("EOF", TokenType.EOF)

    # Helper moves to next token
    def advance(self):
        self.pos += 1

    # Helper returns true if hasn't reached EOF yet
    def not_eof(self):
        return self.current_token().type != TokenType.EOF



    def produce_ast(self):
        program = Program()

        while self.not_eof():
            # stmt = self.parse_stmt()
            stmt = "statements" # For now
            program.body.append(stmt)
            self.advance()

        return program
