# create functions for different operations

def addition():
    num1 = int(input("Adjon meg egy számot:"))
    num2 = int(input("Adjon meg egy számot:"))
    num3 = num1 + num2
    print(num3)

def subtraction():
    num1 = int(input("Adjon meg egy számot: "))
    num2 = int(input("Adjon meg még egy számot: "))
    print(f'A(z) {num1} és a(z) {num2} számok különbsége : {num1 - num2}')

def multiplication():
    num1 = int(input("kerek egy szamot: "))
    num2 = int(input("kerek egy masik szamot: "))
    eredmeny = num1*num2
    print("a szorzas eredmenye: ", eredmeny)

def division():
    pass

def pow():
    num1 = int(input("Adjon meg egy számot: "))
    num2 = int(input("Adjon meg egy számot: "))
    result = num1 ** num2
    print(f'A {num1} a(z) {num2}. hatványon: {result} ')

def modulo():
    pass

def absolute():
    num1 = int(input("Adjon meg egy számot: "))
    
    if num1 > 0:
        print(f'"A megadott szám értéke:" {num1}')
    elif num1 < 0:
        print(f'"A megadott szám értéke:" {-1*num1}')
    else:
        print("A megadott szám 0!")

def maxnumber():
    
def minnumber():
    pass

