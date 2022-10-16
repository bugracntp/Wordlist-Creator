import itertools

language = input("Choose your language Tr/En: ")
word_count = int(input("kaç kelimeden harf seçmek istiyorsunuz? "if language == "Tr" else "How much word you want to use? " )) 
words = []
for i in range(word_count):
    words.append(input(f"{i+1}. kelime " if language == "Tr" else f"word {i+1} "))


n = int(input("kaç haneli şifreler istiyorsunuz : " if language == "Tr" else "How many digit password do you want? "))

count = 0
total =sorted("".join(words))
chrs = []

for i in range(len(total)):
    if i != len(total)-1 and total[i] != total[i+1]:
        chrs.append(total[i])

print(f"Oluşturulacak şifrelerde kullanılan karakterler : {chrs}" if language == "Tr" else f"Characters used in passwords to be created : {chrs}")

with open ("file.txt","+w",encoding = "UTF-8") as file:
    for password in itertools.product(chrs, repeat=n):
        file.write(''.join(password)+"\n")
        count+=1
    print(f"Girdiğiniz kelimelerden alınan benzersiz harflerden oluşabilecek {n} haneli şifre sayısı : {count}" if language == "Tr" 
    else f"Number of {n} digit passwords that can consist of unique letters from the words you entered: {count}")