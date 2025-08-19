'''String methods 
          in python'''
#capitalize - capitalize first letter
str = "my name is shreya"
x=str.capitalize()
print(x)
#casefold - converts string into lower case
str2 = "I Am 22 Years Old"
y=str2.casefold()
print(y)
#center - returns a centred string
str3 = "Shreya"
z=str3.center(20)
print(z)
#encode - returns an encoded version of string
str4 = "My name is shreya maurya"
a=str4.encode()
print(a)
#find
str5 = "Welcome to my youtube channel"
b=str5.find("youtube")
print(b)

'''if condition 
       statement 1
       statement 2'''
age = 18
if age>18:
    print("eligible")

else:
    print("you are not eligible")