word=str(input("enter a word: ")).lower().strip()
reversed_text=""

# simple traditional method 
if word==word[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

# reversing using a loop
for i in range(len(word)-1,-1,-1):
    reversed_text+=word[i]

print(reversed_text)
if reversed_text==word:
    print("it is a palindrome")
else:
    print("it is not a palindrome")