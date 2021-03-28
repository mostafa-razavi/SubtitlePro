
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.collocations import *
from nltk.corpus import words
from nltk.corpus import wordnet

stop_words = stopwords.words('english')
import json
import pandas as pd
#nltk.download('words')
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
english_words = words.words()

def get_english_unigrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    unigrams = []
    for _, title in titles_df['page_title'].items():
        word = str(title)
        if len(word) > 0:
            if word[0].islower():
                stem = stemmer.stem(word)
                if stem in english_words: 
                    count += 1
                    unigrams.append(word)
                    if count % 1000 == 0:
                        print(title, count)

    with open(json_file_out, "w") as outfile:  
        json.dump(unigrams, outfile)

def get_english_bigrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    bigrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 2: 
            first = split_by_[0]
            second = split_by_[1]
            if len(first) > 0 and len(second) > 0:
                if first[0].islower() and second[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    if first in english_words and second in english_words: 
                        count += 1
                        print(title, count)
                        bigrams.append(split_by_[0] + ' ' + split_by_[1])

    with open(json_file_out, "w") as outfile:  
        json.dump(bigrams, outfile)        

def get_english_trigrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    trigrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 3: 
            first = split_by_[0]
            second = split_by_[1]
            third = split_by_[2]
            if len(first) > 0 and len(second) > 0 and len(third) > 0:
                if first[0].islower() and second[0].islower() and third[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    third = stemmer.stem(third)                
                    if first in english_words and second in english_words and third in english_words: 
                        count += 1
                        print(title, count)
                        trigrams.append(split_by_[0] + ' ' + split_by_[1] + ' ' + split_by_[2])

    with open(json_file_out, "w") as outfile:  
        json.dump(trigrams, outfile)

def get_english_quadgrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    quadgrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 4: 
            first = split_by_[0]
            second = split_by_[1]
            third = split_by_[2]
            fourth = split_by_[3]
            if len(first) > 0 and len(second) > 0 and len(third) > 0 and len(fourth) > 0:
                if first[0].islower() and second[0].islower() and third[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    third = stemmer.stem(third)                
                    fourth = stemmer.stem(fourth)                
                    if first in english_words and second in english_words and third in english_words and fourth in english_words: 
                        count += 1
                        print(title, count)
                        quadgrams.append(split_by_[0] + ' ' + split_by_[1] + ' ' + split_by_[2] + ' ' + split_by_[3])

    with open(json_file_out, "w") as outfile:  
        json.dump(quadgrams, outfile) 

def get_english_pentagrams_from_wiktioary_titles(json_file_out):
    titles_file = 'C:/myProjects/TDI/CapstoneProject/Wiktionary/enwiktionary-latest-all-titles'
    titles_df = pd.read_csv(titles_file, delimiter='\t')
    count = 0
    pentagrams = []
    for _, title in titles_df['page_title'].items():
        split_by_ = str(title).split('_')
        N_words = len(split_by_)
        if N_words == 5: 
            first = split_by_[0]
            second = split_by_[1]
            third = split_by_[2]
            fourth = split_by_[3]
            fifth = split_by_[4]
            if len(first) > 0 and len(second) > 0 and len(third) > 0 and len(fourth) > 0 and len(fifth) > 0:
                if first[0].islower() and second[0].islower() and third[0].islower() and fourth[0].islower() and fifth[0].islower():
                    first = stemmer.stem(first)
                    second = stemmer.stem(second)                
                    third = stemmer.stem(third)                
                    fourth = stemmer.stem(fourth)                
                    fifth = stemmer.stem(fifth)                
                    if first in english_words and second in english_words and third in english_words and fourth in english_words and fifth in english_words: 
                        count += 1
                        print(title, count)
                        pentagrams.append(split_by_[0] + ' ' + split_by_[1] + ' ' + split_by_[2] + ' ' + split_by_[3] + ' ' + split_by_[4])

    with open(json_file_out, "w") as outfile:  
        json.dump(pentagrams, outfile)                

if __name__ == '__main__':

    #get_english_unigrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_unigrams.json')
    #get_english_bigrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_bigrams.json')
    #get_english_trigrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_trigrams.json')
    #get_english_quadgrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_quadgrams.json')
    get_english_pentagrams_from_wiktioary_titles(json_file_out='C:/myProjects/SubtitlePro/Data/wiktionary_pentagrams.json')
