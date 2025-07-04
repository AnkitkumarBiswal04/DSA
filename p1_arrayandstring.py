# this is a list
A=[1,2,3]
print("printing a list :"+str(A))

#Append - insert an element at the end of an array(on average O(1))
A.append(5)
print("Appending an element :"+str(A))

#pop - deleting an element at the end of an array (O(1))
A.pop()
print("deleting an element :"+str(A))

#inserting an element (which is not at the end of an array) the (O(n))
A.insert(2,5) # this means at position 2 we are inserting an element 5
print("inserting an element :"+str(A))

#modifying an element (O(1))
A[0]=7
print("modifying an element in an array :"+str(A))

#Acessing an element in an array (O(1))
print("Acessing an element in an array :" +str(A[2]))

#check if the value is available in the array or not (O(n))
if 7 in A:
    print("checking if the value is present in array/list:", True)


#String
s='hello'

#Appending in the end of the string (O(n))
b=s+'z'
print("Appending an element in string :"+b)

#check if something is available in the string or not (O(n))
if 'e' in s:
    print("checking if the value is present in string:",True)

#Access the element in a string
print("Access the element in a string :"+s[2])

#length of array and string (O(1))
print("length of the array :"+str(len(A)))
print("length of the string :"+str(len(s)))