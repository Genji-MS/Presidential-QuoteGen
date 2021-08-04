# Presidential Quote Generator
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/demo.png" height="350"> 

Generates quotes. Sometimes we get nonsenese, other times it's pure gold.
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/quote1.png" height="70">
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/quote2.png" height="70">
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/quote3.png" height="70">
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/quote4.png" height="70">


## Demo
https://presidential-quote-gen.herokuapp.com


## Installing / Getting started
Install Python, Flask 
Run flask, then browse the local address in your browser 

```shell
Export flask_env=development; flask run
```
http://127.0.0.1:5000/

## Cleaning Data
Presidential quotes were pulled from Kaggle, Parade, BrainyQuote, and YourTango
Each of these pages had custom regex applied to remove Presidential indentifying information, webpage garbage, duplicates, and advertisements.
<img src="https://github.com/Genji-MS/2D-to-Stereoscopic/blob/main/static/regex.png" height="350"> 

## How it works
The code uses a 2nd order Markov chain to create a dictionary of words that naturally occur based on the quotes sampled. When a quote is generated, it randomly selects from any of our starter words, then selects randomly from the probable words that follow. While it's possible to select words that occur more frequently, this code selects randomly.

In this example we start with the words "Don't worry". The next step uses our 2nd word 'worry' and looks at all of the pairs that begin with worry. In this case, "worry over" and "worry when". Our random function selected the prior. The following two words didn't have any additional options to select from. This continues to the end, selecting randomly where there were multiple options available until "Congress. STOP". The "STOP" word triggers the end of our quote.
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/dictionary_walk.png" height="80"> 
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/dictionary.png" height="350"> 


## Configuration
Replacing, adding, editing the quotes used in our Markov Dictionary are specified near the start of our app.py file.
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/colorcoded_code.png" height="350">

There is the built in option to color code words based on their source text. It is not used in the online demo.
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/colorcoded.png" height="70"> 
Simply specify after the file name, one of the valid color choices as shown above.
Our colors are specified (and limited) by the BootStrap theme.
<img src="https://github.com/Genji-MS/Presidential-QuoteGen/blob/main/static/colorcoded_color.png" height="250"> 

## Limitations of the Markov Chain
The Markov chain is an introduction into generating text. As seen, often large blocks of text have no other options, and the original quote is reproduced. This is because we do not have any other quotes with similar word patterns. 

While we could throw thousands of quotes into our dictionary, it has the drawback of generating text that doesn't make sense, or end up stuck in a circle of repeating text.

Raising the Markov chain order from two to three (or more) will make our text read more naturally but repeats the first problem where we end up creating no significant change to our original text.

## Further reading
For further developments in text generation:
> Machine Learning using an LSTM for smarter text generation
> NLTK (Natural Language Tool Kit) which allows for parts of speech tagging
> The ever developing "Natural Language Processing" models that derive from BERT
> The huge pre-trained models Megatron, or GPT-3

## Licensing
Presidents Image used under CreativeCommons-NonCommercial
https://griffonagedotcom.wordpress.com/2016/07/04/averaged-portraits-of-u-s-presidents-1789-1829/