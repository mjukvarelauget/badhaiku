#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import math
import json

# 5-7-5

# TODO
# Make own composite nouns
# Pattern definition syntax
# Improved syllable fill logic (more than just nouns)
# Passing pattern list til line composer should give a random pattern
# Richer dictionary, proper adjective conjugation wrt noun gender etc
# Richer grammar, context free rules to allow generating the structure of a sentence
# Implement the NGL lexer and parser as frontend, provide backend for the haiku generator
# Vektmønster
# Rhyme

# If more syllables are needed, add nouns
# 1: ADJ-NOUN | ADJ | NOUN | VERB | PREP-NOUN
# 2: VERB-PREP-NOUN
# 3: ADJ-NOUN

def parse_json(filename = "words.json"):
    with open(filename) as json_file:
        raw_json_data = json_file.read()
        try:
            json_data = json.loads(raw_json_data)
            return json_data
        except json.decoder.JSONDecodeError as e:
            print(e)
            print("invalid format of word list.\nExiting.")
            exit(1)



# General procedure: pick a pattern -> pick words -> add random words to pad if there are syllables left

def compose_line(patterns, syllables):

    WORDS = parse_json()
    wordclasses = list(WORDS.keys())
    
    pattern_index = math.floor(random.random()*len(patterns))
    pattern = patterns[pattern_index]

    # Go through all word classes in the provided pattern,
    # and replace them with words within the syllable budget
    result = ""
    for word_class in pattern:
        length = min(math.ceil(random.random()*syllables), len(WORDS[word_class]))

        # Edge case where a word class have no words of a specific length
        # In this case, try again!
        while(len(WORDS[word_class][length-1]) < 1):
            length = min(math.ceil(random.random()*syllables), len(WORDS[word_class]))

        word_index = math.floor(random.random()*len(WORDS[word_class][length-1]))
        
        result += WORDS[word_class][length-1][word_index] + " "
        syllables -= length
        if(syllables < 1): break


    # If there are any remaining syllables to be filled,
    # pad with random words untill the syllable budget is spent 
    while(syllables > 0):
        num_wordclasses = len(wordclasses)
        random_wordclass_index = math.floor(random.random()*num_wordclasses)
        random_wordclass = wordclasses[random_wordclass_index]
        
        length = min(math.ceil(random.random()*syllables), len(WORDS[random_wordclass]))
        word_index = math.floor(random.random()*len(WORDS[random_wordclass][length-1]))
        
        result += WORDS[random_wordclass][length-1][word_index] + " "
        syllables -= length

    # Trim the trailing space and return
    return result.rstrip()


def haiku_as_list():
    return [
        compose_line([["ADJ", "NOUN", "ADJ"], ["ADJ", "ADJ", "NOUN"]], 5),
        compose_line([["VERB", "PREP", "NOUN"]], 7),
        compose_line([["ADJ", "NOUN"], ["VERB", "VERB"]], 5)
    ]

def main():
    result = ""
    result += compose_line([["ADJ", "NOUN", "ADJ"], ["ADJ", "ADJ", "NOUN"]], 5) + "\n"
    result += compose_line([["VERB", "PREP", "NOUN"]], 7) + "\n"
    result += compose_line([["ADJ", "NOUN"], ["VERB", "VERB", "VERB"]], 5)

    print(result, end = '')
    
main()
