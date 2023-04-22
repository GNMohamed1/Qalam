
# Creating a table class to store the global scoop variables and local scoop variables variables for my programming language
class SymbolTable:
    def __init__(self):
        self.vars = {}
        
    def set_variable(self, name, value):
        self.vars[name] = value
        
    def get_variable(self, name):
        if name in self.vars:
            return self.vars[name]
        
    def is_variable(self, name):
        return name in self.vars