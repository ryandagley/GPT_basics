# This is a script to summarize large chunks of text using GPT

import openai

# load API key

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# location of the API key.
openai.api_key = open_file('openaiapikey.txt')

# load text data

# pre-process the text data into chunks

# generate summaries of those chunks

# put them all together 

# dump them