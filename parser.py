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
    
    # Helper advances and returns cur token
    def cur_token_and_advance(self):
        tk = self.current_token()
        self.advance()
        return tk


    def produce_ast(self):
        program = Program()

        while self.not_eof():
            stmt = self.parse_stmt()
            # stmt = "statements"
            program.body.append(stmt)
            # self.advance()

        return program
    
    def parse_stmt(self):
        return self.parse_primary_expr()

    def parse_primary_expr(self):
        token_type = self.current_token().type

        match token_type:
            case TokenType.IDENTIFIER:
                return Identifier(self.cur_token_and_advance().value)
            case TokenType.NUMBER:
                return NumericLiteral(int(self.cur_token_and_advance().value))
    
            # Will handle Parens here too

            case _:
                raise Exception(f"Unexpected token: {self.current_token()}")
