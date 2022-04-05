#this program prints "Hello World" a bunch of times:


value = input("how many times should I say Hello World?\n")
value = int(value)

for i in range(value):
    print(i+1,"Hello World!")
    
value = input("how many times should I say Goodbye World?\n")
value = int(value)

for i in range(value):
    print(i+1,"Goodbye World!")    


