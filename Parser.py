import re


#Add a log file to keep track of the systems logic.  V1 

def split_into_sentences(text):
    sentences = re.split(r'[.!?]\s*', text)
    return [sentence for sentence in sentences if sentence]

def split_into_words(sentence):
    words = sentence.split()
    return words

def basic_pos_tagger(words):
    pos_tags = []
    for word in words:
        if word.endswith('ly'):
            pos_tags.append((word, 'ADVERB'))
        elif word.endswith('ing') or word.endswith('ed'):
            pos_tags.append((word, 'VERB'))
        elif re.match(r'\d+', word):
            pos_tags.append((word, 'NUMBER'))
        else:
            pos_tags.append((word, 'NOUN'))  
    return pos_tags

def identify_clauses(pos_tags):
    clauses = []
    current_clause = []
    for word, tag in pos_tags:
        current_clause.append((word, tag))
        if tag == 'VERB':
            clauses.append(current_clause)
            current_clause = []
    if current_clause:  
        clauses.append(current_clause)
    return clauses


text = input("Please enter your text here: ")
sentences = split_into_sentences(text)

for sentence in sentences:
    words = split_into_words(sentence)
    pos_tags = basic_pos_tagger(words)
    clauses = identify_clauses(pos_tags)
    print(f"Sentence: {sentence}")
    print(f"Words: {words}")
    print(f"POS Tags: {pos_tags}")
    print(f"Clauses: {clauses}")
    print("------")



#NTS for future updated version(s):

#Keep track of sentence endings for meaning behind text files.   v1.5


#Add a CSV file  to store words and clauses  from users inputs  V2
#Amend any new or unused words/ clauses 


#Make a path to file that can hold multiple text files to be parsed. V3

#Note that .  and space in the middle of a sent.  Ie DR. Mann or Mrs. Smith V4
#Keep note of the pattern that each noun/ word following will most likely be a
#Pnoun.

#Accronyms, and how they handle.  Thought 1) dictionary 2) or table with terms V4.5
#and spelt out Accro.  Ie Mr = Mister, Dr = Doctor,  etc.  PB&J Sandwhich


#Account for comma. check against posible  subjects.  If no subject is found compare to other nouns.   V5+

#Consider useing bubble sorts/ swords(?) 
