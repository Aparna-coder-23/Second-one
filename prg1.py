
class A:
    x = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        A.x += 1

    #def __init__(self, a, b):
    #   A.x += 1

    def displayCount(self):
        print('Count : %d' %A.x)

    def display(self):
        #pass 
        print('a :', self.a, ' b :', self.b)

a1 = A('George', 25000)
a2 = A('John', 30000)
#a3 = A()
a1.display()
a2.display()

a1.displayCount()
a2.displayCount()

print(A.x)
