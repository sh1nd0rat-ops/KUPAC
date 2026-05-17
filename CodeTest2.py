#発展課題
def fizz_buzz(n,x,y):
    if n % x == 0 and n % y ==0:
        a = "FuzzBuzz"
    elif n % x == 0:
        a = "Fuzz"
    elif n % y == 0:
        a = "Buzz"
    else:
        a = str(n)
    return a
n = int(input("好きな数字："))
x = int(input("好きな数字："))
y = int(input("好きな数字："))
print(fizz_buzz(n,x,y))