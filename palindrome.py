def palin(num):

    rev_num = num[::-1] # leaving the start and stop to empty, so it consider entire list, then using -1 as step to reverse the list completely.
        
    if num == rev_num:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

#input the string from the user
no = input("Enter A Word Or A Number: ") # input prompt.
no = no.lower() # Converting the string to lowercase

#passing the input to palin func.
palin(no) 

