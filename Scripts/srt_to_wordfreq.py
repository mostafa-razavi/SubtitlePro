
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def srt_to_frequency_dict(srt_file_name):
        srt_file = open(srt_file_name)
        srt_file = srt_file.read()

        clean_tokens = nltk.tokenize.word_tokenize(srt_file)
        stop_words = stopwords.words('english')
        clean_tokens = nltk.pos_tag(clean_tokens)

        filtered_words = []
        for token in clean_tokens:
                word = token[0]
                word_type = token[1]
                if word not in stop_words:
                        if word_type == "NN" or word_type == "JJ" or word_type == "VB" or word_type == "VBG" or word_type == "RB" or word_type == "X" :
                                if word.isalpha():
                                        word = word.lower()
                                        if word[-3:] == 'ing' and word_type == "VBG":
                                                word = WordNetLemmatizer().lemmatize(word,'v')
                                        if word[-2:] == 'in':
                                                if nltk.pos_tag([word + "g"])[0][1] == "VBG":
                                                        word = WordNetLemmatizer().lemmatize(word + "g",'v')
                                        if word == 'gon':
                                                word = 'go'
                                        filtered_words.append(word)              

        word_frequency_dict = {}
        freq = nltk.FreqDist(filtered_words)
        #freq.plot(100, cumulative=False, )


        for word, frequency in freq.most_common():
                word_frequency_dict[word] = frequency

        return word_frequency_dict



if __name__ == '__main__':
        #file_name = "C:/myProjects/TDI/CapstoneProject/srt/12AngryMen.srt"
        #file_name = "C:/myProjects/TDI/CapstoneProject/srt/Inception.srt"
        file_name = "C:/myProjects/TDI/CapstoneProject/srt/Inception.srt"

        my_dict = srt_to_frequency_dict(file_name)
        print(my_dict)
