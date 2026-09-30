# # l = [10,20,30,40,50,60]

# # for items in l:
# #     print(items) 
    
# for i in range(0,10,2):
#     print(i)
    
# # Pattern 
    
# for i in range(1, 6):
#     print("*" * i)
    
# # for i in range(1,11):
# #     print(3 * i)

# for i in range(13 , 131, 13):
#     print(i)
    
# m = [10, 20, " " , 30,40]

# for j in m:
#     print(j)
    
    
# num = [1,2,3,4,5]
# dict = {1 : 'apple', 2: 'kannu', 3 : 'kiwi', 4 : 'banana'}

# for n in num:
#     print(n)
#     for d in dict:
#         print(dict)
        
# k = 0

# while k < 10:
#     # k = k + 1 
#     # print(k)
#     if k == 5:
#         break
#     print(k)
#     k += 1
    
    
# # wap to print table of given no.
#  by using for loop
# j = int(input("Enter value: "))

# for i in range(1, 11):
#     print(i * j)

# by using while loop
# num = int(input("enter a no. : "))
# i = 1
# while i <= 10:
#     print(num, "x" , i , "=" , num*i)
#     i = i+1
    
# # wap to print the sum of n numbers

# by using for loop
# n = int(input("enter a value: "))
# sum=0
# for i in range(n+1):
#     sum=sum+i
#     print("sum of first",n,"numbers:",sum)
    
# by using while loop

# n = int(input("Enter a value: "))
# i = 1
# total = 0

# while i <= n:
#     total = total + i
#     i = i + 1

# print("Sum =", total)

# i = 0
# while i < n:
#     print(i)
#     i += n
    
# i=int(input("Enter num1:"))
# j=int(input("Enter num2:"))
# if i>j:
#     print(i,"is greater than",j)
# else:
#     if i<j:
#         print(i,"is less than ",j)
#     else:
#         print(i,"is equal to",j)
        

# numlist=[1,2,3]
# charlist=['a','b']
# for n in numlist:
#     print(n)
#     for c in charlist:
#         print(c)
        
# s = 'Rajat'

# print(s[4:1])
# print(s[:3])
# print(s[1:])
# print(s[0:5:2])
# print(s[::])

s1 = 'python is very easy language is follow oop'
s2 = 3
print((s1 + " ")*s2)

s3 = s1.split(" ")
s4 = s1.find("is")
print(s4)
print(s3)

# max split
s5 = s1.split(" ", 2)
print(s5)

s6 = s1.title() # Capitalize every word of every letter
print('title s1: ', s6)

s10 = "MY NAme is KANisHaK"
print(s10.title()) # if any letter of the is capital rather than 1st word then it will convert into lower case
s8 = s1.capitalize() #it will capitalize the first character
print(s8)

print(s10.upper()) # Capitialize the whole string
print(s10.lower()) # Convert all string into the smaller case
# i = 0
# while i <= 10:
#     i = i+1
#     if i == 5:
#         continue
#     print(i,end=" ")