class RuntimeVal:
    def __init__(self, type):
        self.type = type

class NumberVal(RuntimeVal):
    def __init__(self, value: int):
        super().__init__("number")
        self.value = value
        
    def __repr__(self):
        return f"NumberVal({self.value})"

# Will add NullVal, BoolVal