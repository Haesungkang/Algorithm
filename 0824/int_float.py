str = "123"
str2 = "12.3"

print(int(str), type(int(str)))
print(float(str), type(float(str)))

test = "1+2"
print(test)
print(repr(test))
print(eval(test))
print(eval(repr(test)))