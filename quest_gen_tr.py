import jieba
import itertools as it
import translators as ts
import json
text_file = "input_questions.txt"
results = dict()
def permutechisen(s, char):
    if not s:
        return [s]
    binary = it.product(['', char], repeat=len(s) - 1)
    zipped = (it.zip_longest(s, comb, fillvalue='') for comb in binary)
    return [''.join(it.chain.from_iterable(x)) for x in zipped]

def trans(list1):
    mylist = []
    for i in range(len(list1)):
        chi_eng_google = ts.google(list1[i], 'zh-CN', 'en')
        mylist.append(chi_eng_google)
    result = str(" ".join(mylist)) + '\n'
    return result

def permutechieng(seg_list, st):
    for i in range(len(permutechisen(seg_list, ' '))):
        results[st].append(trans(permutechisen(seg_list, ' ')[i].split()))

fr = open(text_file, 'r')

output_path = 'output_questions_tr'

for line in fr:
    eng_chi_google = ts.google(line, 'en', 'zh-CN')
    print(eng_chi_google)
    seg_sentence = list(jieba.cut(eng_chi_google, cut_all=False))
    results[line.strip()] = []
    permutechieng(seg_sentence, line.strip())

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(results, f)

num_generated = sum([len(v) for v in results.values()])
print("Done. Number of questions generated: {} ({}%% increases)".format(num_generated, num_generated / len(results) * 100))
