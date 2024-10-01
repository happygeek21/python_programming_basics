def lists():

    """LISTS ARE MUTABLE WHICH MEANS IT CAN BE MODIFIED!!"""

    listone= [1,2,3,4,5]

    print("Printing The List....")
    print(listone[0]) #Printing The elements from list accoding to their Index Position.

    print("Before Appending",listone)

    listone.append(6) #APPENDING, inserting a value/element at the end of the list.
    listone.append(7)
    listone.append(8)
    print("After Append",listone)

    listone.pop()

    print("After Popping",listone) #POP, removes a value from the end of the list.

    listone.insert(2,'hello')   #takes 2 args, first one is the index postion of the element, second one is the value

    print("After Insertion",listone)

    listone.remove(7) #Deletes the element specified NOTE: not the index position.

    print("After Deletion",listone)


    #listone.index(3) #used to find the index of specifc element, takes 3 args(value,start,end).

    #print("Indexing",listone)

    listone.extend("HELLO WORLD")
    listone.extend([1,2,3,4,5,6]) # used to add lists,strings or tuples into an existing ones. numbers are not supported.
    print("After Extension",listone)

    listone.reverse() #used to reverse a list completely.

    print("After Reversing...",listone)

    listone.clear() #Deletes The Lists Completely.

    print("After Clearing",listone)



#TUPPLES, These are immutable, meaning we cannot change/modify the elements after it has been created.

def tupp():

    tup1=(1,2,3,4,5) # Tupple Declaration

    print("My Tupple",tup1)

    pak=(21,"Hello","Hemanth") #packing a tupple 

    x,y,z = pak #unpacking the tupple into different variables.

    print(x,y,z)


# Dictionaries are Mutable and they are arranged in Key:Value Pairs whereas every key must be Unique and are immutable (Strings,tuples,numbers).

def dcnary():

    dc= { "Age":21,"Name":"Hemanth","Address":"XYZ Avenue, 21 Steeet","Phone":1234567890}

    print("Printing The Dictionary",dc)

    print("Printing specific value,",dc["Age"])








ch=int(input("Choose 1.List 2.Tupple 3.Dictionary 4.Sets"))

if(ch==1):
    lists()

elif(ch==2):
    tupp()
elif(ch==3):
    dcnary()
else:
    print("Try Again")


