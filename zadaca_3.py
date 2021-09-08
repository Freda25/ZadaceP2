import re

regex = "^k.*[0-5].*\s.*v$"
regex2 = "\s"

while 1:
    unos = input("Unesite ime: ")
    rezultat = re.search(regex and regex2, unos)
    print(rezultat)
    if rezultat:
        break
    else:
        print("Pogrešan unos!") 

print("Ispravan unos") 
