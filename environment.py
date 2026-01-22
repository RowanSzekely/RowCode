
class Environment:
    def __init__(self, parent = None):
        self.parent = parent
        self.variables = {}
        self.constants = set()

    def declare_var(self, name, value, isConst = False):
        if (name in self.variables):
            raise Exception(f"Cannot declare variable '{name}', it is already defined.")

        self.variables[name] = value
        if(isConst):
            self.constants.add(name)
        return value
    
    def assign_var(self, name, value):
        # Can assign variables from inner envs
        env = self.resolve(name)
        if name in env.constants:
            raise Exception(f"Cannot reassign constant '{name}'.")
        env.variables[name] = value
        return value

    def lookup_var(self, name):
        # Can lookup variables from inner envs
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