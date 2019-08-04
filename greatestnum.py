n1=float(input("Enter the 1st number:"))
n2=float(input("Enter the 2nd number:"))
n3=float(input("Enter the 3rd number:"))
if (n1>=n2) and (n1>=n3):
 print("The greatest number is ",n1)
elif (n2>=n1) and (n2>=n3):
  print("The greatest number is ",n2)
else:
   print("The greatest number is ",n3)
