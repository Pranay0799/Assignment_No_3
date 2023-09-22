### Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

'''
Sample String : 'The quick Brow Fox'

Expected Output :

No. of Upper case characters : 3

No. of Lower case Characters : 12
'''

def count_upp_lower(int_str):
    count_upper = 0
    count_lower = 0
    for i in int_str:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    return count_upper,count_lower

upper, lower = count_upp_lower("The quick Brow Fox")
print("No. of Upper case characters : ", upper)
print("No. of Lower case characters : ", lower)




####  Taking input from user

# def count_upp_lower(int_str):
#     count_upper = 0
#     count_lower = 0
#     for i in int_str:
#         if i.isupper():
#             count_upper += 1
#         elif i.islower():
#             count_lower += 1
#     return count_upper,count_lower

# int_str = input("Enter a string to check : ")
# upper, lower = count_upp_lower(int_str)
# print("No. of Upper case characters", upper)
# print("No. of Lower case characters", lower)

##### Thank You....


