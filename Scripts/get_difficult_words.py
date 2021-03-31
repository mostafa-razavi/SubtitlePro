import pandas as pd
import numpy as np
from srt_to_wordfreq import srt_to_frequency_dict
from dictionary import get_dictionary_meaning
import math

def get_word_difficulty_index(word, df):
        try:
            freq = df.loc[df['word'] == word.lower()]['count'].values[0]
            return 1000 / math.log10(freq)**3 / 14.465082*10
        except:
                return np.nan

def get_top_n_difficult_words(srt_file_name, top_n, dictionary_dict, work_dir):
    profanity_list_file = work_dir + 'Data/profane_list_less.txt'
    web_word_freq_csv = work_dir + 'Data/unigram_freq.csv'
    df = pd.read_csv(web_word_freq_csv)
    df_profane = pd.read_csv(profanity_list_file)

    movie_word_frequency_dict = srt_to_frequency_dict(srt_file_name)
    new_movie_word_frequency_dict = {}
    for key, value in movie_word_frequency_dict.items():
        if key not in df_profane.values:
            new_movie_word_frequency_dict[key] = (value, get_word_difficulty_index(key, df))

        df_freq_diff = pd.DataFrame.from_dict(data=new_movie_word_frequency_dict, orient='index', columns=[ 'freq', 'difficulty'])
        df_freq_diff = df_freq_diff.sort_values(by=['difficulty'], ascending=False)


    meaningful_words = {}
    count = 0
    difficulty_top_n = []
    most_difficult_words = df_freq_diff.index.tolist()
    for word in most_difficult_words:
        meaning = get_dictionary_meaning(word, dictionary_dict)
        if meaning != None:
            count += 1
            meaningful_words[word] = meaning
        if count == int(top_n):
            break
        
    return meaningful_words



if __name__ == '__main__':
    import json
    work_dir = 'C:/myProjects/SubtitlePro/'
    srt_file_name = 'C:/myProjects/SubtitlePro/temp_srt/Titanic.HDRIP.TLF.part1.en.srt'

    with open(work_dir + 'Data/unigram_meaning_Wiktionary.json') as json_file: 
        wiktionary = json.load(json_file)

    print(get_top_n_difficult_words(srt_file_name, 5, wiktionary, work_dir))
