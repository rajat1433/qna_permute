import argparse
import json
import os
from collections import defaultdict
import jieba
import itertools as it
import translators as ts
import json

# Boon Peng's Model
from qgen.encoder.universal_sentence_encoder import USEEncoder
from qgen.generator import FPMGenerator, SymSubGenerator, IMTGenerator, ZeroShotGenerator, EDAGenerator

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

AQA_PATH = os.path.join(ROOT_PATH, 'active-qa')
AQA_CONFIG_PATH = os.path.join(ROOT_PATH, 'config/aqa.json')
AQA_MODEL_PATH = os.path.join(ROOT_PATH, 'model/pretrained/active-qa/translate.ckpt-1460356')
AQA_RL_MODEL_PATH = os.path.join(ROOT_PATH, 'model/pretrained/active-qa/translate.ckpt-6156696')
# IMT_PATH = os.path.join(ROOT_PATH, 'model/onmt_model_step_15000.pt')
ONMT_PATH = os.path.join(ROOT_PATH, 'OpenNMT-py')
USE_PATH = os.path.join(ROOT_PATH, 'model/pretrained/universal_sentence_encoder')

fpm = None
symsub = None
hybrid = None
imt = None
zeroshot = None
zeroshot_rl = None
eda = None

# Machine Translation Model
results_translation = dict()

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
        results_translation[st].append(trans(permutechisen(seg_list, ' ')[i].split()))

def main(input_path, output_path, batch_size=2500):

    generator1 = SymSubGenerator(USEEncoder(USE_PATH))
    generator2 = ZeroShotGenerator(AQA_PATH, AQA_CONFIG_PATH, AQA_MODEL_PATH)
    generator3 = EDAGenerator()
    generator4 = FPMGenerator()

    print("Generating questions via ...")
    results = dict()
    results1 = dict()
    results2 = dict()
    results3 = dict()
    results4 = dict()
    batch_counter = 0

    def process_batch(_batch):
        if len(_batch) > 0:
            nonlocal results1, results2, results3, batch_counter
            print("Processing batch #{}...".format(batch_counter))
            results1.update(generator1.batch_generate(_batch))
            batch_counter += 1
            results2.update(generator2.batch_generate(_batch))
            batch_counter += 1
            results3.update(generator3.batch_generate(_batch))
            batch_counter += 1
            results4.update(generator4.batch_generate(_batch))
            batch_counter += 1

    with open(input_path, 'r', encoding='utf-8') as f:
        batch_counter = 0
        batch = []
        for line in f:
            if len(line.strip()) != 0:
                batch.append(line.strip())
                if len(batch) == batch_size:
                    process_batch(batch)
                    batch = []
                eng_chi_google = ts.google(line, 'en', 'zh-CN')
                #print(eng_chi_google)
                seg_sentence = list(jieba.cut(eng_chi_google, cut_all=False))
                results_translation[line.strip()] = []
                permutechieng(seg_sentence, line.strip())

        process_batch(batch)

    print("Saving result to {}...".format(output_path))
    for k in results1.keys():
        results[k] = []
        results[k] = list(results[k] + results1[k])
        #print(results[k])
        results[k] = list(results[k] + results2[k])
        #print(results[k])
        results[k] = list(results[k] + results3[k])
        #print(results[k])
        results[k] = list(results[k] + results4[k])
        #print(results[k])
        results[k] = list(results[k] + results_translation[k])
        #print(results[k])
        results[k] = list(set(results[k]))


    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f)

    num_generated = sum([len(v) for v in results.values()])
    print("Done. Number of questions generated: {} ({}%% increases)".format(num_generated, num_generated / len(results) * 100))

if __name__ == '__main__':
    input_path = "input_questions"
    output_path = "output.json"
    main(input_path, output_path)
