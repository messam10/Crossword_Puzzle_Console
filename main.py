import word, random

newList = random.sample(word.Words_list, 6)
words = []
crossword = [
    ["0.0", "0.1", "0.2", "0.3", "0.4", "0.5"],
    ["1.0", "1.1", "1.2", "1.3", "1.4", "1.5"],
    ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5"],
    ["3.0", "3.1", "3.2", "3.3", "3.4", "3.5"],
    ["4.0", "4.1", "4.2", "4.3", "4.4", "4.5"],
    ["5.0", "5.1", "5.2", "5.3", "5.4", "5.5"]
]
# print(newList)
max = 0
def simpleWord(num):
    if len(newList[num]['word']) > 4 :
        newList[num] = random.choice(word.Words_list)

for i in range(len(newList)):
    simpleWord(i)
    # print("",newList[i]['word'])
    # print("Q{:d}) {:s}".format(i+1, newList[i]["question"]))
    words = list(newList[i]['word'])
    # print(words)

    print("\n",newList[i]['word'])
    
    if max < len(newList[i]['word']) :
        max = len(newList[i]['word'])
        print("high : ", newList[i]['word'])

print("\t".join(crossword[0]))
print("\t".join(crossword[1]))
print("\t".join(crossword[2]))
print("\t".join(crossword[3]))
print("\t".join(crossword[4]))
print("\t".join(crossword[5]))
print("\n\n")

# print("len ",len(crossword))
for i in range(len(crossword)) :
    print("i ",i)
    for z in range(len(crossword)) :
        print("z ",z)
        if newList[z]['word'] == max :
            listMax = list(max)
            if len(listMax) <= z :
                word.crossword[i][z] = listMax[z]
                print("\t".join(crossword[i]))
            else :
                word.crossword[i][z] = "#"
                continue
        else :
            if len(words) < z :
                word.crossword[i][z] = words[z]
                print("\t".join(crossword[i]))
            else :
                word.crossword[i][z] = "#"
                continue

print("\t".join(crossword[0]))
print("\t".join(crossword[1]))
print("\t".join(crossword[2]))
print("\t".join(crossword[3]))
print("\t".join(crossword[4]))
print("\t".join(crossword[5]))