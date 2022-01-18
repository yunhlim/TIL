num = int(input())

def fibonaci(num):
    numbers = [1, 1]
    a = 1
    b = 1
    c = 0
    for i in range(num-2):
        c = a+b
        numbers.append(c)
        a = b
        b = c
    return numbers

print(fibonaci(10))