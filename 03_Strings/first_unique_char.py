word=str(input("enter a word: "))

chars_count={}
unique_char=None

# adding character count into char_count dictionary
for char in word:
    if char not in chars_count:
        chars_count[char]=1
    else:
        chars_count[char]+=1

# determining the first unique
for char,count in chars_count.items():
    if count==1:
        unique_char=char
        break

print("the first unique character is:", unique_char)