def test_list(arr):
    len_lst=len(arr)
    a=0
    print(arr)
    n=int(input("Enter the check number:"))
    for i in range(0,len_lst):
        if(arr[i]<n):
         a+=1
         break
    if a==0:
        print("True\nAll List numbers are greater than ",n)
    else:
         print("False\n List no. are NOT greater than ",n)
lst=[47,36,88,9,6,3,33,56,8,34,7]
test_list(lst)
         
    

