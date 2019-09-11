#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import math

# 5-7-5

# TODO
# Read from external word list. Needs format and simple parser
# Make own composite nouns
# Pattern definition syntax
# Improved syllable fill logic (more than just nouns)
# Passing pattern list til line composer should give a random pattern
# Richer dictionary, proper adjective conjugation wrt noun gender etc

# If more syllables are needed, add nouns
# 1: ADJ-NOUN | ADJ | NOUN | VERB | PREP-NOUN
# 2: VERB-PREP-NOUN
# 3: ADJ-NOUN

WORDS = {
    "ADV": [
        ["raskt", "høyt", "fort", "svalt"],
        ["voldsomt", "sakte"],
        ["duvende", "angrende", "flygende"]
    ],

    "ADJ": [
        ["rød", "grønn", "sval", "blek"],
        ["skalla", "vannløs", "smidig", "vakker"]
    ],

    "NOUN": [
        ["katt", "bil", "hus", "tre", "måne"],
        ["Skedsmo", "Tempe", "Tåsen", "katte", "grantre"],
    ],

    "VERB": [
        ["går", "står", "får"],
        ["løper", "vever", "holder", "spiser"]
    ],

    "PREP": [
        ["på", "under", "ved"],
        ["mellom", "oppå"]
    ]
}


# General procedure: pick a pattern -> pick words -> add nouns if there are syllables left

def compose_line(pattern, syllables):
    result = ""
    for word_class in pattern:
        length = min(math.ceil(random.random()*syllables), len(WORDS[word_class]))
        word_index = math.floor(random.random()*len(WORDS[word_class][length-1]))

        result += WORDS[word_class][length-1][word_index] + " "
        syllables -= length
        if(syllables < 1): break


    # Pad with nouns (or random classes?)
    while(syllables > 0):
        length = min(math.ceil(random.random()*syllables), len(WORDS["NOUN"]))
        word_index = math.floor(random.random()*len(WORDS["NOUN"][length-1]))

        result += WORDS["NOUN"][length-1][word_index] + " "
        syllables -= length

    return result


def main():
    result = ""
    result += compose_line(["ADJ", "NOUN", "ADJ"], 5) + "\n"
    result += compose_line(["VERB", "PREP", "NOUN"], 7) + "\n"
    result += compose_line(["ADJ", "NOUN"], 5) + "\n"

    print(result)

main()
