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
        return "null"

class BoolVal(RuntimeVal):
    def __init__(self, value):
        super().__init__("boolean")
        self.value = value

    def __repr__(self):
        return "true" if self.value else "false"

class StringVal(RuntimeVal):
    def __init__(self, value):
        super().__init__("string")
        self.value = value
    
    def __repr__(self):
        return self.value

class FunctionVal(RuntimeVal):
    def __init__(self, params, body, env):
        super().__init__("function")
        self.params = params
        self.body = body
        # This is the env where the function was created
        self.env = env
    
    def __repr__(self):
        return f"<function params={self.params}>"
    
class NativeFunctionVal(RuntimeVal):
    def __init__(self, fn):
        super().__init__("native_function")
        self.fn = fn

    def __repr__(self):
        return "<native function>"

TRUE = BoolVal(True)
FALSE = BoolVal(False)
NULL = NullVal()