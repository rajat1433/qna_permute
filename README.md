# Question Generation for Text Augmentation

## Introduction
This repository provides a command line script written in Python for generating multiple variations of questions (both syntactically or/and lexically) from an input question automatically. The generated questions can be used in training of automated question answering system as augmentation for training datasets. This augmentation technique is especially useful when training datasets are small and limited.This repository also contains code for forming permutations of questions for training.

## Installation
### Step 1: Clone the repository
```
git clone --recursive https://github.com/rajat1433/qna_permute
cd Question-Generation
```
### Step 2: Install dependencies
```
python -m virtualenv env
source env/bin/activate

pip install -r requirements.txt
python setup.py install
```
### Step 3: Download pretrained models
##### fastText
1. Download [fastText English vectors](https://fasttext.cc/docs/en/crawl-vectors.html) [[direct link](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz)]
2. Decompress and put `cc.en.300.bin` under `model/pretrained/fastText` directory
##### GloVe
1. Download [spaCy pretrained GloVe model](https://spacy.io/models/en#en_vectors_web_lg) [[direct link](https://github.com/explosion/spacy-models/releases/download/en_vectors_web_lg-2.1.0/en_vectors_web_lg-2.1.0.tar.gz)]
2. Decompress and put `en_vectors_web_lg-2.1.0` (the most nested folder) under `model/pretrained/spacy_glove` directory
##### Universal Sentence Encoder
1. Download the [transformer variant of Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder-large/3) [[direct link](https://tfhub.dev/google/universal-sentence-encoder-large/3?tf-hub-format=compressed)]
2. Decompress and put `assets`, `variables`, `saved_model.pb` and `tfhub_module.pb` under `model/pretrained/universal_sentence_encoder` directory
##### ActiveQA Question Reformulator (pretrained on UN+Paralex datasets)
Checkpoint without reinforcement learning:
1. Download the pretrained model from this [link](https://storage.googleapis.com/pretrained_models/translate.ckpt-1460356.zip)
2. Decompress and put `translate.ckpt-1460356.data-00000-of-00001`, `translate.ckpt-1460356.index` and `translate.ckpt-1460356.meta` under `model/pretrained/active-qa/translate.ckpt-1460356` directory

Checkpoint with reinforcement learning:
1. Download the pretrained model from this [link](https://storage.cloud.google.com/pretrained_models/translate.ckpt-6156696.zip)
2. Decompress and put `translate.ckpt-6156696.data-00000-of-00001`, `translate.ckpt-6156696.index` and `translate.ckpt-6156696.meta` under `model/pretrained/active-qa/translate.ckpt-6156696` directory

## Usage
### Question Generation
```
python script/quest_gen.py

It will generate a output.json file containing questions as keys and their corresponding generated questions
as the values.

===================================================================================================
```

## Usage
### Forming 3_permutations
```
python algo.py

It will generate 3_permutations_original.csv file corresponding to the 3_permutations which is needed.

Edit the various parameters in algo.py file to generate corresponding number of questions as required.

```
