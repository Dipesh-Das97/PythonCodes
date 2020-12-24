a = "Hello World!"
print("a = " + a)

print("""1.Slicing
2.Size
3.Upper
4.Lower
5.Strip
6.Replace
7.Split
8.Format""")

choice = input("Enter the choice: ")

if(choice == "1"):
    x = int(input("Enter first index : "))
    y = int(input("Enter second index : "))
    print("Between index " + " = " + a[x:y])
    
elif(choice == "2"):
    print("length of var a : ", len(a))
    
elif(choice == "3"):
    print("Upper Case : " + a.upper())
    
elif(choice == "4"):
    print("Lower Case : " + a.lower())
              
elif(choice == '5'):
    print("Strip whitespaces : " + a.strip())
    
elif(choice == '6'):
    x = int(input("Enter what is to be replaced : "))
    y = int(input("Enter what is to be placed : "))
    print("Replaced var a : " + a.replace(x,y))
    
elif(choice == '7'):
    x = int(input("Enter the string where to be splitted : "))
    print("Splitted value : " + a.replace(x,y))

elif(choice == '8'):
    #we can concat different data types in the placeholders {} from a.format(1,2,3,.......)
    x = input("Enter the string where to be splitted : ")
    b =("Hello World! {}")
    print(b.format(x));

else :
    print("Wrong o/p")


