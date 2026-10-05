sentence=input("enter your string: ").lower()

Length= len(sentence)
Letters= 0
Digits= 0
Spaces= 0
Vowels= 0
Consonants= 0

for char in sentence:

    if char.isalpha():
        Letters+=1

        if char in "aeiou":
            Vowels+=1
        else:
            Consonants+=1

    elif char==" ":
        Spaces+=1

    else:
        Digits+=1

print(f'the length of the string is: {Length}')
print(f'the number of letters in the string is: {Letters}')
print(f'the number of digits in the string is: {Digits}')
print(f'the number of spaces in the string is: {Spaces}')
print(f'the number of vowels in the string is: {Vowels}')
print(f'the number of consonants in the string is: {Consonants}')