from nodes import (
    Program, NumericLiteral, Identifier, BinaryExpr, 
    VarDeclaration, AssignmentExpr, Block, ComparisonExpr, 
    IfStmt, FunctionDeclaration, CallExpr, WhileLoop, 
    StringLiteral, UnaryExpr
    )
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
            case TokenType.WHILE:
                return self.parse_while_loop()
            case TokenType.FDECLARE:
                return self.parse_function_declaration()
            case TokenType.DECLARE:
                return self.parse_var_declaration()
            case TokenType.CONST:
                return self.parse_var_declaration()
            case TokenType.IF:
                return self.parse_if_statement()
            case TokenType.OPEN_CURLY_PAREN:
                return self.parse_block()
            case _:
                expr = self.parse_expr()
                self.expect(TokenType.SEMICOLON)
                return expr
    
    def parse_function_declaration(self):
        self.expect(TokenType.FDECLARE)
        name = self.expect(TokenType.IDENTIFIER).value

        self.expect(TokenType.OPEN_PAREN)
        params = []

        if (self.current_token().type != TokenType.CLOSE_PAREN):
            params.append(self.expect(TokenType.IDENTIFIER).value)
            while(self.current_token().type == TokenType.COMMA):
                self.advance()
                params.append(self.expect(TokenType.IDENTIFIER).value)
        self.expect(TokenType.CLOSE_PAREN)

        body = self.parse_block()
        return FunctionDeclaration(name, params, body)
    
    def parse_while_loop(self):
        self.expect(TokenType.WHILE)
        self.expect(TokenType.OPEN_PAREN)
        condition = self.parse_expr()
        self.expect(TokenType.CLOSE_PAREN)
        body = self.parse_block()

        return WhileLoop(condition, body)


    def parse_if_statement(self):
        self.expect(TokenType.IF)
        self.expect(TokenType.OPEN_PAREN)
        condition = self.parse_expr()
        self.expect(TokenType.CLOSE_PAREN)
        body = self.parse_block()

        # Go through all elif statements
        elifs = []
        while (self.current_token().type == TokenType.ELIF):
            self.advance()
            self.expect(TokenType.OPEN_PAREN)
            elif_condition = self.parse_expr()
            self.expect(TokenType.CLOSE_PAREN)
            elif_block = self.parse_block()
            elifs.append((elif_condition, elif_block))
        
        # Else statement
        else_block = None
        if (self.current_token().type == TokenType.ELSE):
            self.advance()
            else_block = self.parse_block()

        return IfStmt(condition, body, elifs, else_block)


    def parse_block(self):
        self.expect(TokenType.OPEN_CURLY_PAREN)
        # self.advance()
        body = []
        while(self.current_token().type != TokenType.CLOSE_CURLY_PAREN):
            body.append(self.parse_stmt())
        self.expect(TokenType.CLOSE_CURLY_PAREN)
        return Block(body)


    def parse_var_declaration(self):
        isConst = self.current_token().type == TokenType.CONST
        self.advance() # Through Keyword
        identifier = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.EQUALS)

        declaration = VarDeclaration(identifier, self.parse_expr(), isConst)

        self.expect(TokenType.SEMICOLON)
        return declaration
    
    def parse_expr(self):
        return self.parse_assignment_expr()
    
    def parse_assignment_expr(self):
        left = self.parse_comparison_expr()

        if(self.current_token().type == TokenType.EQUALS):
            self.advance()
            value = self.parse_assignment_expr()
            return AssignmentExpr(left, value)
        
        return left

    # Comp Exprs are parsed here so something like 1 + 2 < 4 won't be treated as 1 + (2 < 4)
    # and declare y = (x == 2) will succesfully set y to a bool value
    def parse_comparison_expr(self):
        left = self.parse_additive_expr()

        while (self.current_token().type in 
               (
                   TokenType.EQUALS_EQUALS,
                   TokenType.NOT_EQUALS,
                   TokenType.GREATER_THAN,
                   TokenType.LESS_THAN,
                   TokenType.GREATER_THAN_OR_EQ,
                   TokenType.LESS_THAN_OR_EQ,
               )
            ):
            operator = self.cur_token_and_advance().value
            right = self.parse_additive_expr()
            left = ComparisonExpr(left, operator, right)
        
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
        left = self.parse_unary_expr()

        while(
            self.current_token().value == '*' or 
            self.current_token().value == '/' or 
            self.current_token().value == '%'
            ):
            operator = self.cur_token_and_advance().value

            right = self.parse_unary_expr()
        
            left = BinaryExpr(left = left, right = right, operator = operator)

        return left
    
    def parse_unary_expr(self):
        if (self.current_token().value == '-'):
            operator = self.cur_token_and_advance().value
            operand = self.parse_unary_expr()
            return UnaryExpr(operator, operand)

        return self.parse_primary_expr()

    def parse_primary_expr(self):
        token_type = self.current_token().type

        match token_type:
            case TokenType.IDENTIFIER:
                identifier = Identifier(self.cur_token_and_advance().value)

                if(self.current_token().type == TokenType.OPEN_PAREN):
                    self.advance()
                    args = []

                    if (self.current_token().type != TokenType.CLOSE_PAREN):
                        args.append(self.parse_expr())
                        while(self.current_token().type == TokenType.COMMA):
                            self.advance()
                            args.append(self.parse_expr())
                    self.expect(TokenType.CLOSE_PAREN)
                    return CallExpr(identifier, args)
                return identifier
            
            case TokenType.NUMBER:
                return NumericLiteral(int(self.cur_token_and_advance().value))

            case TokenType.STRING:
                return StringLiteral(self.cur_token_and_advance().value)
            
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
