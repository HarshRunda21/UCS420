print("Hello World!")

print("Harsh")
print("Harsh")
print("Harsh")

x = 10
y = 20
z = x+y
print(x,"+",y,"=",z)

string1 = "Hello"
string2 = "World"
print(string1 + " " + string2)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = a+b
print(a, "+", b, "=", c)

for i in range(1,11):
     print(i)
     
i = 1
while i<=10:
    print("5 x",i, "= ", 5*i)
    i = i+1
    
n = int(input("Enter number (for table) : "))
i = 1
while i<=10:
    print(n,"x",i, "= ", n*i)
    i = i+1

n2= int(input("Enter number (for sum) : "))
sum = 0
for i in range(n2+1):
    sum = sum+i
print("Sum till n : " ,sum)

if a>b:
    print("a>b")
else:
    print("a<b")

if a%2:
    print("Number is odd")
else:
    print("Number is even")

n3 = int(input("Enter a number: "))

for i in range(2, n3):
    if n3 % i == 0:
        print(n3, "is not a prime number.")
        break
else:
    print(n3, "is a prime number.")

if a == b:
    print("a=b")
elif a > b:
    print("a>b")
else:
    print("a<b")