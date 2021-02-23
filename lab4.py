name= input('Enter the name')
age= int(input('Enter the age'))
print("hello my name is" +name+ "and i am" +str(age)+ "years old")
#another method to print
print("hello my name is", name, "and i am", age, "years old")
#another method
print("hello my name is %s and i am %d years old" % (name,age))
#another
print('hello my name is {} amd i am {} years old'.format(name, age))
#another
name= input('Enter the name')
age= int(input('Enter the age'))
add= name+str(age)
print(f'my name and age is{add}')