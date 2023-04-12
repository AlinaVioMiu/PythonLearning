# Sa se scrie o functie generatoare pentru numere consecutive din sirul lui Fibonacci
# class Fibonacci:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         self.a = 0
#         self.b = 1
#         return self
#
#     def __next__(self):
#         c = self.a + self.b
#         self.a = self.b
#         self.b = c
#         return c
def fibonacci():
    a = 0
    b = 1
    while True:
        c = a + b
        a = b
        b = c
        yield c





if __name__ == '__main__':
    for number in fibonacci():
        print(number)