def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    if(word==word[::-1]):
        return True
    else: return False

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    fibseq = [0,1]
    if number_val<1:
        return []
    while number_val >= fibseq[-1] + fibseq[-2]:
        fibseq.append(fibseq[-1] + fibseq[-2])
    return fibseq

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    count = 0
    sub_len = len(str2)
    str1 = str1.lower()
    for i in range(len(str1)):
        if str1[i:i + sub_len] == str2:
            count += 1
    return count

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    if len(list1) == len(list2):
     sum_list = [x + y for x, y in zip(list1, list2)]
     return sum_list
    else: return []

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None

    return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    if len(password) < 8:
        return False
    
    uppercase_in_password = False
    for character in password:
        if character.isupper():
            uppercase_in_password = True
    if not uppercase_in_password:
        return False
    
    lowercase_in_password = False
    for character in password:
        if character.islower():
            lowercase_in_password = True
    if not lowercase_in_password:
        return False
    
    number_in_password = False
    for character in password:
        if character in '0123456789':
            number_in_password = True
    if not number_in_password:
        return False

    return True

