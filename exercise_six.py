# Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Defining function
def divisible (number_list):
    for numbers in number_list:
        if numbers % 5 == 0:
            print (numbers)

# Display given list. 

number_list = [10, 20, 33, 46, 55]
print ('The given list is:', number_list)

# Display the numbers divisible by five from the list 

print ('The numbers divisible by 5 are:', divisible(number_list))


