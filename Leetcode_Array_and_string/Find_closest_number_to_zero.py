# assigning the size of the array
n=int(input("enter the size of the list:"))

#taking the inputs in the array
nums=[]
for _ in range(n):
    num=int(input())
    nums.append(num)
#assuming the closest as the 1st element
closest=nums[0]
#comparing the elements in the array and update it
for x in nums:
    if abs(x) < abs(closest):
        closest=x
    elif abs(x)==abs(closest):
        closest=max(closest,x)
if abs(closest) < 0 and closest in nums:
    print(abs(closest))
else :
    print(closest)