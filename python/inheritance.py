# Inheritance:
# Write 3 classes A, B and inherit A & B in C. 
# If C is instantiated then what will be printed.

class a():
    def __init__(self, x):
        self.name = x
    def display(self):
        print("a")
        print(self.name)

class b():
    def __init__(self, x):
        self.name = x
    def display(self):
        print("b")
        print(self.name)

class c(b,a):
    def __init__(self, x):
        super().__init__(x)
        
def main():
    obj = c(5)
    obj.display()
    
if __name__ == "__main__":
    main()