def x(number1,number2):
    #print(number1*number2)
    return number1*number2,number2-number1

f =x(12,13)
print(f)
print(type(f))

l = list(f)
print(type(l))