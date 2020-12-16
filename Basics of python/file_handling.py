#File handling operations performed using an example
#This code takes input content for the file and then performs different operations .

content=input("Enter what you want to write into file: ")
file = open("test1.txt","a") # "a"= append mode
file.write(content)
filename="test1.txt"
with open(filename) as file:
    text =file.read()
    count_vowels = 0
    count_consonants = 0
    for char in text :
        if char in "aeiou":
            count_vowels+=1
        else:
            count_consonants+=1

print("vowels ",count_vowels)
print("consonant ",count_consonants)
print("length ",len(text))
print("percentage of vowel : ",((count_vowels)*100)/len(text),"%")
print("percentage of consonent : ",((count_consonants)*100)/len(text),"%")
file.close()

