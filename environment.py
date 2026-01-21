
class Environment:
    def __init__(self, parent = None):
        self.parent = parent
        self.variables = {}

    # Will probably need to do something for constant here
    def declare_var(self, name, value):
        if (name in self.variables):
            raise Exception(f"Cannot declare variable '{name}', it is already defined.")

        self.variables[name] = value
        return value

    def lookup_var(self, name):
        env = self.resolve(name)
        return env.variables[name]

    # If the variable is in the current env, return the env.
    # Otherwise keep moving up the parents until the variable is either found or not
    def resolve(self, name):

        if (name in self.variables):
            return self
        if (self.parent is None):
            raise Exception(f"Cannot resolve '{name}' as it does not exist.")

        return self.parent.resolve(name)