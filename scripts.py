# scripts.py
import os, sys, string
from random import randint

def parse_file(document):
    """convert text file into a string of every word, removing all punctuation and converting to lower case"""
    f = open(document).read().split()
    unwanted_punctuation_table = dict.fromkeys(map(ord, '\n\r“”"‘’_…:*[]()'), None)
    #parsed_text = [line.translate(str.maketrans(unwanted_punctuation_table)).lower() for line in f]
    parsed_text = [line.translate(str.maketrans(unwanted_punctuation_table)) for line in f]
    return parsed_text

def markov_tokenise(parsed_text, color, markov_dict = {"START START":[]}):
    """converts text file into tokenized dictionary with frequency counter"""
    for index in range(len(parsed_text)-3):
        word_1 = parsed_text[index]
        word_2 = parsed_text[index+1]
        word_3 = parsed_text[index+2]
        phrase1 = word_1+" "+word_2
        phrase2 = word_2+" "+word_3
        token_STOP = None
        token_START = None

        char1 = word_1[-1:]
        char2 = word_2[-1:]
        #Tokens, check for natural ending characters '.' and put them into a special 'START' 'STOP' entry
        if index == 0:
            token_START = parsed_text[index]+" "+parsed_text[index+1]
        elif char1 == '.' or char1 == '!' or char1 == '?':
            #Create our ending token
            #Additionaly check if the following word is a valid starter
            if ((char2 == '.' or char2 == '!' or char2 == '?')== False):
                token_START = parsed_text[index+1]+" "+parsed_text[index+2]
        if char2 == '.' or char2 == '!' or char2 == '?':
            token_STOP = word_2+" STOP"

        #Append our starter token into dictionary as key 'START START' : token_START
        #This is to avoid bloating the dictionary with 'START+word' entries
        #additionaly we are starting the markov with a two-word phrase
        if token_START != None:
            hit = False
            for x in range(len( markov_dict["START START"] )):
                if token_START == markov_dict["START START"][x][0]:
                    markov_dict["START START"][x][2] += 1
                    hit = True
                    break
            if hit == False:
                new_starter = [token_START, color, 1]
                markov_dict["START START"].append(new_starter)
        
        #continue with searching and adding our normal token to the markov chain
        if phrase1 not in markov_dict.keys():
            #new word with its own new list
            markov_dict[phrase1] = [ [phrase2,color,1] ]
        else:
            existing = False
            for x in range(len( markov_dict[phrase1] )):
                if phrase2 == markov_dict[phrase1][x][0]:
                    #color from the same text document
                    if color == markov_dict[phrase1][x][1]:
                        #increase frequency of existing word
                        markov_dict[phrase1][x][2] += 1
                        existing = True
                        break
            if existing == False:
                #add new word to list
                new_list_item = [phrase2, color, 1]
                markov_dict[phrase1].append(new_list_item)
        
        #Because our end token, which is part of the current 'phrase1', may have not been inserted into the markov chain, we add it now
        if token_STOP != None:
            hit = False
            for x in range(len( markov_dict[phrase1] )):
                if token_STOP == markov_dict[phrase1][x][0]:
                    #markov_dict[phrase1][x][2] += 1
                    hit = True
                    break
            if hit == False:
                new_stopper = [token_STOP, color, 0] #it has zero frequency of being selected randomly
                markov_dict[phrase1].append(new_stopper)
    return markov_dict

def markov_walk(current_phrase, markov_dict, look_for_STOP):
    """takes a single walk of the dictionary, adding to the current_phrase, optionally looking for a STOP word"""
    try:
        next_word_list = markov_dict[current_phrase]
    except: #Ends the sentence if we run into a phrase that has no following words
        return ["888 888", '', 0]

    #print (next_word_list)
    total_words = 0
    for num in next_word_list:
        total_words += num[2]
        if look_for_STOP:#We want to end at the next natural stopping point
            if num[0].split(" ")[1] == "STOP":
                return ["STOP STOP", '', 0]

    rng = randint(0,total_words-1)
    next_phrase = ""
    color = ""
    freq = 0
    total = 0
    for word in next_word_list:
        total += word[2]
        if rng < total:
            next_phrase = word[0]
            color = word[1]
            freq = word[2]
            break     
    return [next_phrase, color, freq]