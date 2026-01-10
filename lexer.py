


# Types of Tokens to look for
class TokenType:
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    BINARY_OPERATOR = "BINARY_OPERATOR"
    EOF = "EOF"

class Token:
    def __init__(self, value: str, type: TokenType):
        self.value = value
        self.type = type
    def __repr__(self):
        return f"Token({self.type}, {self.value!r})"



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

        if (c == '+' or c == '-'):
            tokens.append(Token(c, TokenType.BINARY_OPERATOR))
            i += 1
            continue

        # If it's an integer, add NUMBER Token
        if (c.isdigit()):
            start = i

            while (i < len(source) and source[i].isdigit()):
                i += 1
            tokens.append(Token(source[start:i], TokenType.NUMBER))
            continue

        # If it's a word (for now only letters), add Identifier Token
        # (will handle keywords later)
        if (c.isalpha()):
            start = i

            while (i < len(source) and source[i].isalpha()):
                i += 1
            tokens.append(Token(source[start:i], TokenType.IDENTIFIER))
            continue

        # All character I haven't written a condition for
        raise Exception(f"Unexpected character: {c}")

    
    tokens.append(Token("EndOfFile", TokenType.EOF))

    return tokens
    



