
import random

def Fibonacci(n):
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return c


# ΣΥΝΑΡΤΗΣΗ ΤΟΥ ΚΥΡΙΟΥ ΠΡΟΓΡΑΜΜΑΤΟΣ
def f(n):
    if is_prime(n) == True:
        print("Ο ΟΡΟΣ ΤΗΣ ΑΚΟΛΟΥΘΙΑΣ FIBONACCI ΕΙΝΑΙ ΠΡΩΤΟΣ")
    else:  # is_prime==False:
        print("Ο ΟΡΟΣ ΤΗΣ ΑΚΟΛΟΥΘΙΑΣ FIBONACCI ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ")


n = int(input("ΔΩΣΕ ΟΡΟ ΑΚΟΛΟΥΘΙΑΣ FIBONACCI: "))

fibnum = Fibonacci(n)
print(fibnum)
d = 0
for i in range(0, 20):
    a = random.randrange(0, fibnum)
    if (a ** fibnum) % fibnum == (a % fibnum):
        d = d + 1
if d == 20:
    is_prime = True
else:
    is_prime = False
if is_prime == True:
    print("Ο ΟΡΟΣ ΤΗΣ ΑΚΟΛΟΥΘΙΑΣ FIBONACCI ΕΙΝΑΙ ΠΡΩΤΟΣ")
else:  # is_prime==False:
    print("Ο ΟΡΟΣ ΤΗΣ ΑΚΟΛΟΥΘΙΑΣ FIBONACCI ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ")
