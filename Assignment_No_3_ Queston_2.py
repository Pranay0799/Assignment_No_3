###Write a Python program to reverse a string.

### Way 1 Taking input from user

def rev_string(int_str):
    rev_str = int_str[::-1]
    return rev_str
    
int_str = input("Enter a string: ")
result = rev_string(int_str)
print("Reverse string:", result)



## Way 2
# def rev_string(int_str): 
#      for i in int_str[::-1]:
#           print(i, end= "")

# rev_string("1234abcd")

#### Thank You....
