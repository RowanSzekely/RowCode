# Types of Tokens to look for
class TokenType:
    NUMBER = "NUMBER"
    STRING = "STRING"
    IDENTIFIER = "IDENTIFIER"
    OPERATOR = "OPERATOR"

    SEMICOLON = "SEMICOLON"
    COMMA = "COMMA"

    EQUALS = "EQUALS"

    EQUALS_EQUALS = "EQUALS_EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_THAN_OR_EQ = "GREATER_THAN_OR_EQ"
    LESS_THAN_OR_EQ = "LESS_THAN_OR_EQ"

    EXCLAMATION = "EXCLAMATION"

    OPEN_PAREN = "OPEN_PAREN"
    CLOSE_PAREN = "CLOSE_PAREN"
    OPEN_SQR_PAREN = "OPEN_SQR_PAREN"
    CLOSE_SQR_PAREN = "CLOSE_SQR_PAREN"
    OPEN_CURLY_PAREN = "OPEN_CURLY_PAREN"
    CLOSE_CURLY_PAREN = "CLOSE_CURLY_PAREN"

    DECLARE = "DECLARE"
    CONST = "CONST"

    IF = "IF"
    ELIF = "ELIF"
    ELSE = "ELSE"

    WHILE = "WHILE"

    FDECLARE = "FDECLARE"
    RETURN = "RETURN"

    EOF = "EOF"

class Token:
    def __init__(self, value: str, type: TokenType):
        self.value = value
        self.type = type
    def __repr__(self):
        return f"Token({self.type}, {self.value!r})"

KEYWORDS = {
    "declare": TokenType.DECLARE,
    "const": TokenType.CONST,
    "if": TokenType.IF,
    "elif": TokenType.ELIF,
    "else": TokenType.ELSE,
    "fdeclare": TokenType.FDECLARE,
    "return": TokenType.RETURN,
    "while": TokenType.WHILE,
}

# Takes in the sourcecode (a string) as input
# Returns an array of Tokens
def tokenize(source_code: str):

    tokens = []
    source = source_code

    i = 0
    while (i < len(source)):

        # Current character
        c = source[i]

        # Skip single-line comments
        if (c == "/" and i + 1 < len(source) and source[i + 1] == "/"):
            while (i < len(source) and source[i] != '\n'):
                i += 1
            continue

        # Skip multi-line comments
        if (c == '/' and i + 1 < len(source) and source[i + 1] == '*'):
            while (i + 1 < len(source)):
                if (source[i] == '*' and source[i + 1] == '/'):
                    i += 2
                    break
                i += 1
            else:
                raise Exception("Must end multi-line comment")
            continue

        # Skip whitespace
        if (c == " " or c == "\n" or c == "\t"):
            i += 1
            continue

        if (c == '+' or c == '-' or c == '*' or c == '/' or c == '%'):
            tokens.append(Token(c, TokenType.OPERATOR))
            i += 1
            continue

        if (c == '='):
            if (i + 1 < len(source) and source[i + 1] == '='):
                tokens.append(Token("==", TokenType.EQUALS_EQUALS))
                i += 2
                continue
            tokens.append(Token(c, TokenType.EQUALS))
            i += 1
            continue

        if (c == '!'):
            if(i + 1 < len(source) and source[i + 1] == '='):
                tokens.append(Token("!=", TokenType.NOT_EQUALS))
                i += 2
                continue
            tokens.append(Token(c, TokenType.EXCLAMATION))
            i += 1
            continue

        if (c == ';'):
            tokens.append(Token(c, TokenType.SEMICOLON))
            i += 1
            continue
        
        if (c == '('):
            tokens.append(Token(c, TokenType.OPEN_PAREN))
            i += 1
            continue

        if (c == ')'):
            tokens.append(Token(c, TokenType.CLOSE_PAREN))
            i += 1
            continue

        if (c == '['):
            tokens.append(Token(c, TokenType.OPEN_SQR_PAREN))
            i += 1
            continue

        if (c == ']'):
            tokens.append(Token(c, TokenType.CLOSE_SQR_PAREN))
            i += 1
            continue

        if (c == '{'):
            tokens.append(Token(c, TokenType.OPEN_CURLY_PAREN))
            i += 1
            continue

        if (c == '}'):
            tokens.append(Token(c, TokenType.CLOSE_CURLY_PAREN))
            i += 1
            continue

        if (c == '>'):
            if (i + 1 < len(source) and source[i + 1] == '='):
                tokens.append(Token(">=", TokenType.GREATER_THAN_OR_EQ))
                i += 2
                continue
            tokens.append(Token(c, TokenType.GREATER_THAN))
            i += 1
            continue
        
        if (c == '<'):
            if (i + 1 < len(source) and source[i + 1] == '='):
                tokens.append(Token("<=", TokenType.LESS_THAN_OR_EQ))
                i += 2
                continue
            tokens.append(Token(c, TokenType.LESS_THAN))
            i += 1
            continue

        if (c == ','):
            tokens.append(Token(c, TokenType.COMMA))
            i += 1
            continue        

        if (c == '"'):
            i += 1
            start = i

            while (i < len(source) and source[i] != '"'):
                i += 1

            tokens.append(Token(source[start:i], TokenType.STRING))
            i += 1
            continue

        # If it's an integer, add NUMBER Token
        if (c.isdigit()):
            start = i

            while (i < len(source) and source[i].isdigit()):
                i += 1
            # For now only allow one period
            if (i < len(source) and source[i] == '.'):
                i += 1
                while (i < len(source) and source[i].isdigit()):
                    i += 1

            tokens.append(Token(source[start:i], TokenType.NUMBER))
            continue

        # If it's a word
        if (c.isalpha()):
            
            start = i
            while (i < len(source) and source[i].isalpha()):
                i += 1

            word = source[start:i]
            # Checks if the word found is a keyword, otherwise it's an identifier
            if (word in KEYWORDS):
                tokens.append(Token(word, KEYWORDS[word]))
            else:
                tokens.append(Token(source[start:i], TokenType.IDENTIFIER))

            continue

        # All characters I haven't written conditions for
        raise Exception(f"Unexpected character: {c}")

    
    tokens.append(Token("EndOfFile", TokenType.EOF))

    return tokens
    



