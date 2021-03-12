import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import numpy as np
import os.path
from os import path

def get_movie_title_years_from_index_range(from_i, to_i):
    movie_titles_list = []
    for i in range(from_i, to_i): #23540
        movie_url = "http://www.moviesubtitles.org/movie-"  + str(i) + ".html"
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.text, "lxml")
        movie_title_year = soup.find_all('h2')[0].string

        if movie_title_year == ' ()':   # This happens when the link is empty
            append = [i, None, None]
        else:
            movie_title_year_list = movie_title_year.split()
            year = movie_title_year_list[-1]
            title = movie_title_year.replace( " " + year, '')
            year = int(year.replace(")", "").replace("(", ""))
            append = [i, title, year]
        movie_titles_list.append(append)

    return movie_titles_list

def get_all_movie_title_years():
    for item in np.arange(1,23500,50):
        from_i = item
        to_i = item + 50
        out_path = 'C:/myProjects/TDI/CapstoneProject/srt/MSO/' + str(from_i) + '-' + str(to_i) + '.csv'
    
        if path.exists(out_path):
            print("File exists:", out_path)
        else:
            print("Extracting movie titles from", from_i, "to", to_i)
            movie_titles_list = get_movie_title_years_from_index_range(from_i, to_i)            
            with open(out_path, 'w', newline='', encoding="utf-8") as f: 
                write = csv.writer(f) 
                write.writerows(movie_titles_list) 
#get_all_movie_title_years()        

def generate_mso_index():
    
    for item in np.arange(1,23500,50):
        from_i = item
        to_i = item + 50
    
        if item == 1:
            df = pd.read_csv('C:/myProjects/TDI/CapstoneProject/srt/MSO/1-51.csv', names=['index', 'name', 'year'])
        else:
            out_path = 'C:/myProjects/TDI/CapstoneProject/srt/MSO/' + str(from_i) + '-' + str(to_i) + '.csv'
            df_temp = pd.read_csv(out_path, names=['index', 'name', 'year'])
            df = pd.concat([df, df_temp], ignore_index=True)
    df.to_csv('mso_index.csv', index=False)
#generate_mso_index()        



def get_movie_index_info(movie_name):
    #df0 = pd.read_csv('mso_index.csv',delimiter=',')
    #df1 = pd.read_csv('mso_movie_subtitle_index.txt',delimiter=',')
    #df = pd.merge(df0, df1, left_on='index', right_on='index')
    #df.to_csv('mso_index_name_year_subindex.csv', index=False)
    df = pd.read_csv('C:/myProjects/SubtitlePro/Data/mso_index_name_year_subindex.csv')
    movie_row = df[df['name'] == movie_name].values[0]
    movie_index = movie_row[0]
    movie_name = movie_row[1]
    movie_year = movie_row[2]
    subtitle_index = movie_row[3]

    return subtitle_index, movie_index, movie_name, movie_year

subtitle_index, movie_index, movie_name, movie_year =  get_movie_index_info('Madagascar')
#print(subtitle_index, movie_index, movie_name, movie_year)    


def save_subtitle_zipfile(url, out_file_name):
    response = requests.get(url)
    with open(out_file_name, 'wb') as f:
        f.write(response.content)
    return response, out_file_name
#url = 'http://www.moviesubtitles.org/download-5613.html'
#file_out = 'C:/myProjects/TDI/CapstoneProject/file.zip'
#_, _ = save_subtitle_zipfile(url, file_out)


def get_subtitle_url_from_movie_index(movie_index, target_language):
    movie_url = "http://www.moviesubtitles.org/movie-"  + str(movie_index) + ".html"
    response = requests.get(movie_url)
    soup = BeautifulSoup(response.text, "lxml")

    languages_soup = soup.find_all('span', attrs={'style':'color:#666666'})
    languages = []
    for item in languages_soup:
        languages.append(item.find_all('b')[0].string.split()[0])

    subtitle_links_soup = soup.find_all('div', attrs={'class':'subtitle'})
    assert len(subtitle_links_soup) > 0

    movie_subtitles_dict = {}
    subtitle_language = 'some_lang'
    for item in subtitle_links_soup:
        subtitle_index = item.find('a')['href'][:-5].split('-')[-1]
        #print(subtitle_index)
        subtitle_positive = item.find('span', attrs={'style':'color:green'}).string
        subtitle_negative = item.find('span', attrs={'style':'color:red'}).string
        subtitle_parts = item.find('td', attrs={'title':'parts'}).string
        subtitle_download_count = item.find('td', attrs={'title':'downloaded'}).string
        subtitle_upload_date = item.find('td', attrs={'title':'uploaded'}).string
        subtitle_rip = item.find('td', attrs={'title':'Rip'}).string
        subtitle_tile = item.find('b').string

        for language in languages:
            key_word = language.lower() + " subtitles ("
            if subtitle_tile.find(key_word) != -1:
                subtitle_language = target_language
                break 
        net_rate = int(subtitle_positive) - int(subtitle_negative)
        movie_subtitles_dict[int(subtitle_index)] = (subtitle_language, net_rate, int(subtitle_download_count), int(subtitle_parts), subtitle_upload_date, subtitle_rip, subtitle_tile[0:10])
    
    #print(movie_subtitles_dict)
    #movie_subtitles_in_target_language = dict(filter(lambda x: x[1][0] == target_language, movie_subtitles_dict.items()))
    #movie_subtitles_in_target_language = dict(filter(lambda x: x[1][3] == 1, movie_subtitles_in_target_language.items()))

    selected_subtitle_index = list(movie_subtitles_dict.keys())[0]
    #print(selected_subtitle_index)

    subtitle_url = "http://www.moviesubtitles.org/download-"  + str(selected_subtitle_index) + ".html"
    return subtitle_url, selected_subtitle_index




def download_all_movie_subtitles(language):
    for movie_index in np.arange(100,23540):
        try:
            subtitle_url, subtitle_index = get_subtitle_url_from_movie_index(movie_index, language)
        except:
            print("Warning: Subtitle url was not generated for movie index " + str(movie_index))
        else:
            out_file_name = 'C:/myProjects/TDI/CapstoneProject/srt/MSO_subtitles/imov_' + str(movie_index) + '-isub_' + str(subtitle_index) + '.zip'
            if path.exists(out_file_name):
                print('File exists: ' + out_file_name)
            else:
                save_subtitle_zipfile(subtitle_url, out_file_name)
                print('Subtitle was downloaded for movie ' + str(movie_index) + ' subtitle ' + str(subtitle_index))

#download_all_movie_subtitles('English')            


#subtitle_url, subtitle_index = get_subtitle_url_from_movie_index(85, 'English')
#print(subtitle_url, subtitle_index)


def download_one_movie_subtitle(movie_index, language, out_file_name):
    try:
        subtitle_url, subtitle_index = get_subtitle_url_from_movie_index(movie_index, language)
    except:
        print("Warning: Subtitle url was not generated for movie index " + str(movie_index))
    else:
        #out_file_name = 'C:/myProjects/TDI/CapstoneProject/srt/MSO_subtitles/imov_' + str(movie_index) + '-isub_' + str(subtitle_index) + '.zip'
        if path.exists(out_file_name):
            print('File exists: ' + out_file_name)
        else:
            save_subtitle_zipfile(subtitle_url, out_file_name)
            print('Subtitle was downloaded for movie ' + str(movie_index) + ' subtitle ' + str(subtitle_index))
