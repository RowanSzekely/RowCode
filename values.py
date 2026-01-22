class RuntimeVal:
    def __init__(self, type):
        self.type = type

class NumberVal(RuntimeVal):
    def __init__(self, value: int):
        super().__init__("number")
        self.value = value

    def __repr__(self):
        return str(self.value)

class NullVal(RuntimeVal):
    def __init__(self):
        super().__init__("null")
        
    def __repr__(self):
        return "Null"

class BoolVal(RuntimeVal):
    def __init__(self, value):
        super().__init__("boolean")
        self.value = value

    def __repr__(self):
        return "true" if self.value else "false"

TRUE = BoolVal(True)
FALSE = BoolVal(False)
NULL = NullVal()