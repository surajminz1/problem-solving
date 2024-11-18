# Inheritance:
# Write 3 classes, where class B will inherit class A and class C will inherit class B and A both.
# If C is instantiated then what will be printed.

class a():
    def __init__(self):
        self.name = "ravi"
    def display(self):
        print("a")
        print(self.name)

class b(a):
    def __init__(self):
        self.name = "vivek"
        super().__init__()
    def display(self):
        print("b")
        print(self.name)

class c(b,a):
    def __init__(self):
        super().__init__()
        
def main():
    obj = c()
    obj.display()
    
if __name__ == "__main__":
    main()