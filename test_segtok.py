#!/usr/bin/env python
# coding: utf-8

import os
from segtok.segmenter import split_single

"""
    Display last words of sentences split with modified segtok split_single.
    In: directory with text files, file extension
    Output: list of last words of sentences
        => potential addition to segtok/segmenter.py list
"""

din = '/charming/marcin/data/UpdateMe/manz/segmentation/annotationen-reiter-txt-clean_and_manual_check'
extension = '.txt'

# get files
files = [file for file in os.listdir(din) if file.endswith(extension)]


# get last words from sentences
last_words_in_sentence = []
for file in files:
    with open(os.path.join(din, file), 'r') as fin:
        for sent in split_single(fin.read().replace('\n', '')):
            last_words_in_sentence.append(sent.split()[-1])

# display last words
for n, word in enumerate(sorted(list(set(last_words_in_sentence)))):
    print (n, ': ', word)
