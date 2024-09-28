def area_of_square(a):

    area = a*a
    print("The Area of Square is ", area)

#input from the user

def area_of_rectangle(l,b):

    area = l*b
    print("The Area of rectangle is", area)

ch= int (input("Enter a Choice, 1 For Area of Square, 2 For Area of rectangle: "))
if ch==1:

    numb= int (input("Enter a number for Area of Sqr: "))
    area_of_square(numb)
elif ch==2:
    
    num1= int (input("Enter a number for Area of Rec: "))
    num2= int (input("Enter a number for Area of Rec: "))
    area_of_rectangle(num1,num2)
    
else:
    print("Wrong Choice Try Again!")