import json
import nltk
import re

def find_wiktionary_ngrams_in_subtitle(imov, n_gram):
    with open("C:/myProjects/TDI/CapstoneProject/srt/Corpus/corpus.json") as json_file: 
        movies_corpus = json.load(json_file) 

    file_path = 'C:/myProjects/SubtitlePro/Data/wiktionary_' + str(n_gram) + 'grams.json'

    with open(file_path) as f:
        wiktionary_ngrams = json.load(f)   

    imov = str(imov)
    isub = list(movies_corpus[imov].keys())[0]
    movie_text_list = movies_corpus[imov][isub]
    count = 0
    for ngram in wiktionary_ngrams:
        for text in movie_text_list:
            if ngram in text:
                pattern = r'\b' + re.escape(ngram) + r'\b'
                if re.search(pattern, text):
                    count += 1
                    print(count, ngram, '  ---------->  ', text)


if __name__ == '__main__':
    #imov = 330
    imov = 420
        
    find_wiktionary_ngrams_in_subtitle(imov, 1)
    print(1)
    find_wiktionary_ngrams_in_subtitle(imov, 2)
    print(2)
    find_wiktionary_ngrams_in_subtitle(imov, 3)
    print(3)
    find_wiktionary_ngrams_in_subtitle(imov, 4)
    print(4)
    find_wiktionary_ngrams_in_subtitle(imov, 5)
    print(5)
    find_wiktionary_ngrams_in_subtitle(imov, 6)
    print(6)
    find_wiktionary_ngrams_in_subtitle(imov, 7)
    print(7)
    find_wiktionary_ngrams_in_subtitle(imov, 8)
    print(8)
    find_wiktionary_ngrams_in_subtitle(imov, 9)
    print(9)
    find_wiktionary_ngrams_in_subtitle(imov, 10)
    print(10)