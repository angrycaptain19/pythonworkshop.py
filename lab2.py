#Write a program that reads the length of the base and the height of a right-angled triangle and prints the area.
# Every number is given on a separate line.
base= int(input('Enter the base'))
height= int(input('Enter the height'))
Area= 1/2*base*height
#the floor division // rounds the result down to the nearest whole number
print(f'The area of right-angled triangle is {Area}')
