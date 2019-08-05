def test_num(x,y):
    if (x==y) or abs(x-y)==5 or (x+y==5):
        return True
    else:
        return False
print(test_num(2,3))
print(test_num(5,10))
print(test_num(3,3))
        
