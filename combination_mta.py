import translators as ts
from translate import Translator

print("Please input an English question:")
english_qns = input()


def google_block(eng_qns):
    # translate the English question to Chinese using Google
    eng_chi_google = ts.google(eng_qns, 'en', 'zh-CN')
    # the list of questions translated from Chinese to English
    the_list = []
    # Google
    chi_eng_google = ts.google(eng_chi_google, 'zh', 'en')
    the_list.append(chi_eng_google)
    # Bing
    translator = Translator(from_lang="zh", to_lang="en")
    chi_eng_bing = translator.translate(eng_chi_google)
    the_list.append(chi_eng_bing)
    # Youdao
    chi_eng_youdao = ts.youdao(eng_chi_google, 'zh', 'en')
    the_list.append(chi_eng_youdao)
    # Tencent
    chi_eng_tencent = ts.tencent(eng_chi_google, 'zh', 'en')
    the_list.append(chi_eng_tencent)
    return the_list


def bing_block(eng_qns):
    # translate the English question to Chinese using Bing
    translator = Translator(from_lang="en", to_lang="zh")
    eng_chi_bing = translator.translate(eng_qns)
    # the list of questions translated from Chinese to English
    the_list = []
    # Google
    chi_eng_google = ts.google(eng_chi_bing, 'zh', 'en')
    the_list.append(chi_eng_google)
    # Bing
    translator = Translator(from_lang="zh", to_lang="en")
    chi_eng_bing = translator.translate(eng_chi_bing)
    the_list.append(chi_eng_bing)
    # Youdao
    chi_eng_youdao = ts.youdao(eng_chi_bing, 'zh', 'en')
    the_list.append(chi_eng_youdao)
    # Tencent
    chi_eng_tencent = ts.tencent(eng_chi_bing, 'zh', 'en')
    the_list.append(chi_eng_tencent)
    return the_list


def youdao_block(eng_qns):
    # translate the English question to Chinese using Youdao
    eng_chi_youdao = ts.youdao(eng_qns, 'en', 'zh-CN')
    # the list of questions translated from Chinese to English
    the_list = []
    # Google
    chi_eng_google = ts.google(eng_chi_youdao, 'zh', 'en')
    the_list.append(chi_eng_google)
    # Bing
    translator = Translator(from_lang="zh", to_lang="en")
    chi_eng_bing = translator.translate(eng_chi_youdao)
    the_list.append(chi_eng_bing)
    # Youdao
    chi_eng_youdao = ts.youdao(eng_chi_youdao, 'zh', 'en')
    the_list.append(chi_eng_youdao)
    # Tencent
    chi_eng_tencent = ts.tencent(eng_chi_youdao, 'zh', 'en')
    the_list.append(chi_eng_tencent)
    return the_list


def tencent_block(eng_qns):
    # translate the English question to Chinese using Youdao
    eng_chi_tencent = ts.tencent(eng_qns, 'en', 'zh-CN')
    # the list of questions translated from Chinese to English
    the_list = []
    # Google
    chi_eng_google = ts.google(eng_chi_tencent, 'zh', 'en')
    the_list.append(chi_eng_google)
    # Bing
    translator = Translator(from_lang="zh", to_lang="en")
    chi_eng_bing = translator.translate(eng_chi_tencent)
    the_list.append(chi_eng_bing)
    # Youdao
    chi_eng_youdao = ts.youdao(eng_chi_tencent, 'zh', 'en')
    the_list.append(chi_eng_youdao)
    # Tencent
    chi_eng_tencent = ts.tencent(eng_chi_tencent, 'zh', 'en')
    the_list.append(chi_eng_tencent)
    return the_list


# Return whole list of generated questions from the combination of machine translation applications
def combination_mta(eng_qns):
    # Combine all 4 blocks
    whole_list = google_block(eng_qns) + bing_block(eng_qns) + youdao_block(eng_qns) + tencent_block(eng_qns)
    # return whole_list
    print(*whole_list, sep="\n")

combination_mta(english_qns)


def remove_punctuation(string):
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # traverse the given string and if any punctuation
    # marks occur replace it with null
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")
    # Print string without punctuation
    return string


# Returns a unique list of generated questions
def uni_combination_mta(eng_qns):
    # Combine all 4 blocks
    whole_list = google_block(eng_qns) + bing_block(eng_qns) + youdao_block(eng_qns) + tencent_block(eng_qns)
    # Remove punctuations in all strings
    no_punc_list = []
    for i in range(len(whole_list)):
        no_punc_list.append(remove_punctuation(whole_list[i]))
    # Generate the unique list of generated questions
    new_list = []
    for j in range(len(no_punc_list)):
        new_list.append(no_punc_list[j].lower())
    uni_list = list(set(new_list))
    # return uni_list
    print(*uni_list, sep="\n")

# uni_combination_mta(english_qns)
