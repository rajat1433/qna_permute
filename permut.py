import csv
from itertools import product

ans2idx = dict()
question2answer = dict()

# populate ans2idx
idx = 0
with open("answers.txt", 'r', encoding='utf-8') as f:
    for line in f:
        ans2idx[line.strip()] = idx
        idx += 1

# populate question2answer
with open("msf_baby_bonus.csv", 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        question2answer[row[1].strip()] = ans2idx[row[2].strip()]

# write to csv
with open("3_permutations_original.csv", 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for i, combination in enumerate(product(question2answer.keys(), question2answer.keys(), question2answer.keys())):
        writer.writerow([i, [question2answer[q] for q in combination], " ".join(combination)])
