# app.py
import os
from flask import Flask, render_template, request
from scripts import parse_file, markov_tokenise, markov_walk

app = Flask(__name__)

#PARSE INDIVIDUAL SCRIPTS AND COLOR CODE THEM FOR OUR OUTPUT

parsed_text = parse_file('Quotes1') #white
markov = markov_tokenise(parsed_text, 'default')

parsed_text = parse_file('BrainyQuote') #blue
markov = markov_tokenise(parsed_text, 'default', markov)

parsed_text = parse_file('Funny') #blue
markov = markov_tokenise(parsed_text, 'default', markov)

parsed_text = None

@app.route('/')
def index():
    """Return homepage"""
    wordlist = []
    colored_wordlist = []
    words = request.args.get('num')
    num_words = int(words) if (words != None and words != "" and int(words)>8) else 8
    used_words = 0
    look_for_STOP = False
    end = False

    data = None 
    phrase = ""
    color = ""
    while end is False:
        if used_words == num_words:
            look_for_STOP = True
        #Generate word based on needs
        if used_words == 0:
            data = markov_walk("START START", markov, False)
            word = data[0] #grab both words
            color = data[1]
            used_words += 1 #add one ADDITIONAL here, as we add one each cycle 
        else:
            data = markov_walk(phrase, markov, look_for_STOP)
            word = data[0].split(" ")[1]
            color = data[1]
        
        phrase = data[0] #store our phrase to be used in the next loop
        used_words += 1

        if color == 'red':
            color = "text-danger"
        elif color == 'blue':
            color = "text-primary"
        elif color == 'pink':
            color = "text-info"
        else:
            color = ""
        
        if word == '888' or word == 'STOP':
            end = True
            break #if random word doesn't return another connection, 888 is returned to end the chain prematurely
        else:
            wordlist.append(word)
            colored_wordlist.append( [word, color])

        #print (f'\nwordlist length = {used_words} looking for stop = {look_for_STOP} end = {end}')
        #print (f' phrase = {phrase}, \n "{wordlist}"')

    return render_template('index.html', f_wordlist = colored_wordlist, wordlist = wordlist)

if app.name == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
    