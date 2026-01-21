from nodes import Node, NodeType, Program, NumericLiteral, Identifier, BinaryExpr, VarDeclaration, AssignmentExpr
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
    
    # Helper verifies token type is what's expected
    def expect(self, token_type):
        token = self.current_token()

        if (token.type != token_type):
            raise Exception(f"Expected {token_type}, got {token.type}")
        
        self.advance()
        return token

    def produce_ast(self):
        program = Program()

        while self.not_eof():
            stmt = self.parse_stmt()
            program.body.append(stmt)

        return program
    
    def parse_stmt(self):
        match self.current_token().type:
            # Will handle constants later
            case TokenType.DECLARE:
                return self.parse_var_declaration()
            case _:
                return self.parse_expr()
    
    def parse_var_declaration(self):
        self.advance() # Through Keyword
        identifier = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.EQUALS)

        declaration = VarDeclaration(identifier, self.parse_expr())

        self.expect(TokenType.SEMICOLON)
        return declaration
    
    def parse_expr(self):
        return self.parse_assignment_expr()
    
    def parse_assignment_expr(self):
        left = self.parse_additive_expr()

        if(self.current_token().type == TokenType.EQUALS):
            self.advance()
            value = self.parse_assignment_expr()
            return AssignmentExpr(left, value)
        
        return left
    
    def parse_additive_expr(self):
        left = self.parse_multiplicative_expr()

        while(
            self.current_token().value == '+' or 
            self.current_token().value == '-'
            ):
            operator = self.cur_token_and_advance().value

            right = self.parse_multiplicative_expr()

            left = BinaryExpr(left = left, operator = operator, right = right)
        
        return left
    
    def parse_multiplicative_expr(self):
        left = self.parse_primary_expr()

        while(
            self.current_token().value == '*' or 
            self.current_token().value == '/' or 
            self.current_token().value == '%'
            ):
            operator = self.cur_token_and_advance().value

            right = self.parse_primary_expr()
        
            left = BinaryExpr(left = left, right = right, operator = operator)

        return left

    def parse_primary_expr(self):
        token_type = self.current_token().type

        match token_type:
            case TokenType.IDENTIFIER:
                return Identifier(self.cur_token_and_advance().value)
            case TokenType.NUMBER:
                return NumericLiteral(int(self.cur_token_and_advance().value))
    
            case TokenType.OPEN_PAREN:
                self.advance()
                expr = self.parse_expr()

                # Expects to see a close paren after parsing inner expr
                if (self.current_token().type != TokenType.CLOSE_PAREN):
                    raise Exception("Expected ')")
                
                self.advance() 
                return expr

            case _:
                raise Exception(f"Unexpected token: {self.current_token()}")
