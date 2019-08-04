def group_fn(group,n):
  for value in group:
    if n==value:
       return True
  return False
print(group_fn([2,4,5,6],5))
print(group_fn([3,4,8,9,0],1))
