str1=str(input("Enter the string:"))
str1=str1.casefold()
k=reversed(str1)
if list(str1)==list(k):
 print("Given string is palindrome")
else:
 print("It is not palindrome")  
