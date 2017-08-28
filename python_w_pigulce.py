# Listy


mylist = ["a", "b", "c", "d", "e"]
mylist2 = [1,2,3,4,5]

print mylist[0]
print mylist2[1]

print mylist[2:] # od indeksu 2
print mylist2[:2] # do indeksu 2
print mylist[0:3] # zakres

print mylist[-3:] # trzy od konca

# Slowniki / Hashe

d = { "Python": "programming",
      "English": "natural",
      "French": "natural",
      "Ruby": "programming",
      "Javascript": "programming"
}

print type(d)
print d["Python"]
d["Scala"] = "programming" # dodawanie do hasha
print d
d["languages known"] = 6 # hashe sa nietypowane
print d
print d.keys() # wyswietlenie kluczy
print d.values() # wyswietlenie wartosci
print len(d) #rozmiar

# Petle

for item in d.keys():
    print item

x = [item for item in d.values()] # inna skladnia
print(x)

for item in d.keys():
    print item + " dodatkowy tekst" # przy pomieszanych typach (w wartosciach slownika) bedzie blad

newlist = [item + " is a fun language" for item in d.keys()] # nowa lista na podstawie starej
for item in newlist:
    print item

# Warunki

x = 10
if x > 5:
    print "Looks like x is gt 5"
else:
    print "Looks like x is lt 5"

number_list = [1,2,3,4,5,6,7,8,9,10]
for number in number_list:
    if number%2==0:
        print str(number) + " is even" # konwersja typu
    elif number ==7 :
        print str(number) + " is seven"
    else:
        print str(number) + " is an odd number"

# Funkcje

def my_function(something): # definicja
    return str(something) + " was passed. Length = " + str(len(str(something)))

print my_function("blaa")
print my_function(2)
