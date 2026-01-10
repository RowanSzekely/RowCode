# Types of Tokens to look for
class TokenType:
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    BINARY_OPERATOR = "BINARY_OPERATOR"

    SEMICOLON = "SEMICOLON"

    EQUALS = "EQUALS"
    OPEN_PAREN = "OPEN_PAREN"
    CLOSE_PAREN = "CLOSE_PAREN"
    OPEN_SQR_PAREN = "OPEN_SQR_PAREN"
    CLOSE_SQR_PAREN = "CLOSE_SQR_PAREN"
    OPEN_CURLY_PAREN = "OPEN_CURLY_PAREN"
    CLOSE_CURLY_PAREN = "CLOSE_CURLY_PAREN"

    DECLARE = "DECLARE"
    CONST = "CONST"

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

        # Will skip commented lines here

        # Skip whitespace
        if (c == " " or c == "\n" or c == "\t"):
            i += 1
            continue

        if (c == '+' or c == '-' or c == '*' or c == '/' or c == '%'):
            tokens.append(Token(c, TokenType.BINARY_OPERATOR))
            i += 1
            continue

        if (c == '='):
            tokens.append(Token(c, TokenType.EQUALS))
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


        # If it's an integer, add NUMBER Token
        if (c.isdigit()):
            start = i

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
    



