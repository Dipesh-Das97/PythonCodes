b = "\n1. Print hello world\n2. Use a func to print name\n"
a = input(b + "Enter your Choice : ")
def addname(c,d):
    print ("Your Name is : " + c + " "+ d)
def writename():
    first = input("enter first name: ")
    second = input("enter second name : ")
    addname(first,second)

if a == "1":
    print("Hello", "World", sep = "-")
elif a == '2':
    writename()
else:
    print("Invalid Output")

