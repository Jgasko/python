import pandas

#make sure everything is working
print ("Hello World!")

#take user input and display it
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
print ("Hello " + firstName + " " + lastName)

#for loop
arr = [1,2,3,4,5,6,7,8,9]
for x in arr:
    print (x)

#add data to an array and display it afterwards
number = int(input("How many items are you adding to the list? "))
names = []
for i in range(0,number):
    name = input("Enter a name: ")
    names.append(name)
print(names)


pandas.set_option('expand_frame_repr', False)
filepath = 'sheet1.csv'
df = pandas.read_csv(filepath)
print(df)