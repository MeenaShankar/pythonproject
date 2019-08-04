def vowels(char):
    vow_let='aeiou'
    return char in vow_let
n=str(input("Enter the character:"))
print("Given string is vowel:",vowels(n))
