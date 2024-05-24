name1 = input("name1 is")
name2 = input("name2 is")
score1 = 0
score2 = 0
name1_length = len(name1)
name2_length = len(name2)

def fcheck_true(letter):
    if letter == "t" or letter == "r" or letter =="u" or letter == "e":
        
        return 1
    else:
        return 0

def fcheck_love(letter):
    if letter == "l" or letter == "o" or letter =="v" or letter == "e":
        
        return 1
    else:
        return 0

for i in range(0, name1_length):
    score1 += fcheck_true(name1[i])
    score2 += fcheck_love(name1[i])

for i in range(0, name2_length):
    score1 += fcheck_true(name2[i])
    score2 += fcheck_love(name2[i])


print(f"{score1}+{score2}")