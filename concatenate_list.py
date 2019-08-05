def concat_list(list):
    res=''
    for x in list:
      res+=str(x)
    return res
num=[2,3,4,5]
print("before concatenation:",num)
print("After concatenation:",concat_list(num))
