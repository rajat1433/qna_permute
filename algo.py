import csv
from itertools import product
import random
import json
ans2idx = dict()
question2answer = dict()

# populate ans2idx
idx = 0
with open("answers.txt", 'r', encoding='utf-8') as f:
    for line in f:
        ans2idx[line.strip()] = idx
        idx += 1

# index to question
quest = dict()
idx = 0
# populate question2answer
with open("msf_baby_bonus.csv", 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        question2answer[row[1].strip()] = ans2idx[row[2].strip()]
        quest[idx] = row[1].strip()
        idx += 1

# load from json file generated questions:
with open('output.json', 'r') as f:
    quest_gen = json.load(f)

y = 1000000
n = 294 # number of classes
x = int(y/n)
z = int(x/n)
idx = 0
with open("3_permutations_original.csv", 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for i in range(n):
        for j in range(n):
            for k in range(z):
                lab = []
                comb = []
                lab.append(question2answer[quest[i]])
                lab.append(question2answer[quest[j]])

                if( quest[i].strip() in quest_gen ):
                    a = random.randrange(0, len(quest_gen[quest[i].strip()]))
                    comb.append(quest_gen[quest[i].strip()][a])
                else:
                    comb.append(quest[i].strip())
                if( quest[j].strip() in quest_gen ):
                    b = random.randrange(0, len(quest_gen[quest[j].strip()]))
                    comb.append(quest_gen[quest[j].strip()][b])
                else:
                    comb.append(quest[j].strip())
                #choose a random class c
                c = random.randrange(0, n)
                lab.append(question2answer[quest[c]])
                if( quest[c].strip() in quest_gen ):
                    d = random.randrange(0, len(quest_gen[quest[c].strip()]))
                    comb.append(quest_gen[quest[c].strip()][d])
                else:
                    comb.append(quest[c].strip())
                writer.writerow([idx, lab, comb])
                idx += 1
