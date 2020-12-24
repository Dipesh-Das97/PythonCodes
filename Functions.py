# Normal Arguments
def myfunc1(val):
    return "The first name is : " + val

print(myfunc1("Dipesh"))

# Arbitrary Arguments
def my_function(*val):
  return "The youngest child is " + val[2]


print(my_function("Emil", "Tobias", "Linus"))

# Keyword Arguments
def my_func3(val1, val2, val3):
    return "The youngest child is : " + val2

print(my_func3(val1="Gary",val2="Simon",val3="Eric"))

# Arbitrary Keyword Arguments:
def my_func3(**val):
    return "The youngest child is : " + val["val1"]

print(my_func3(val1="Gary",val2="Simon",val3="Eric"))

# Lambda function :
def add(n):
    return lambda a : a + n
print(add(2)(11))
# or
adder = add(2)
print(adder(15))

# Lambda Function:
def add(a):
    return lambda n: n + a


print(add(2)(14))