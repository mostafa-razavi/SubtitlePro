from flask import Flask, render_template, request
from pretty_table import generate_html_from_dictionary
from get_subtitle import get_movie_index_info, download_one_movie_subtitle
from get_difficult_words import get_top_n_difficult_words

import shutil
import os
import zipfile
import json

movie_index = 1
subtitle_index = 2






output_dictionary = {}
#output_dictionary['Difficult words'] = meaningful_words
#output_dictionary = {'hi':{"boyo":{"definitions":["boyo (plural boyos)","(Ireland) A boy or lad.","(sometimes derogatory) A stereotypically Welsh form of address for a man, usually younger than the speaker."],"examples":[],"partOfSpeech":"noun"},"doorframe":{"definitions":["doorframe (plural doorframes)","The frame into which a door is fitted."],"examples":[],"partOfSpeech":"noun"},"fascinate":{"definitions":["fascinate (third-person singular simple present fascinates, present participle fascinating, simple past and past participle fascinated)","To evoke an intense interest or attraction in someone.","To make someone hold motionless; to spellbind.","To be irresistibly charming or attractive to."],"examples":[],"partOfSpeech":"verb"},"forthe":{"definitions":["forthe (not comparable)","Obsolete spelling of forth"],"examples":[],"partOfSpeech":"adverb"},"gangway":{"definitions":["gangway (plural gangways)","A passageway through which to enter or leave, such as one between seating areas in an auditorium, or between two buildings.","An articulating bridge or ramp, such as from land to a dock or a ship.","A temporary passageway, such as one made of planks.","(rare, obsolete outside dialects) A clear path through a crowd or a passageway with people.","(Britain) An aisle.","(nautical) A passage along either side of a ship's upper deck.","(nautical) A passage through the side of a ship or an opening in the railing through which the ship may be boarded.","(agricultural) An earthen and plank ramp leading from the stable yard into the upper storey or mow of a dairy barn.","(Chicago) The narrow space between two buildings or houses, used to access the backyard/alleyway from the front.","A passageway through a passenger car"],"examples":[],"partOfSpeech":"noun"},"goddamned":{"definitions":["goddamned (not comparable)","(derogatory) Damned by God.","(often offensive) Used as an intensifier expressing anger."],"examples":[],"partOfSpeech":"adjective"},"halfa":{"definitions":["halfa (uncountable)","Synonym of esparto (\u201cNorth African grass\u201d)"],"examples":[],"partOfSpeech":"noun"},"impugn":{"definitions":["impugn (third-person singular simple present impugns, present participle impugning, simple past and past participle impugned)","(transitive, obsolete) To assault, attack.","(transitive) To verbally assault, especially to argue against an opinion, motive, or action; to question the truth or validity of."],"examples":[],"partOfSpeech":"verb"},"ofan":{"definitions":["ofan (plural ofanim)","Alternative form of ophan"],"examples":[],"partOfSpeech":"noun"},"presumptuous":{"definitions":["presumptuous (comparative more presumptuous, superlative most presumptuous)","Going beyond what is right, proper, or appropriate because of an excess of self-confidence or arrogance."],"examples":[],"partOfSpeech":"adjective"},"purser":{"definitions":["purser (plural pursers)","The person responsible for handling the accounts on a ship, or for dealing with the passengers on a ship or aircraft."],"examples":[],"partOfSpeech":"noun"},"regale":{"definitions":["regale (plural regales)","A feast, meal."],"examples":[],"partOfSpeech":"noun"},"rootless":{"definitions":["rootless (comparative more rootless, superlative most rootless)","Of a plant or another thing, having no roots.","Being a wanderer; having no ties to a particular locale.","(computing) Without (the use of) a root user account."],"examples":[],"partOfSpeech":"adjective"},"shipbuilder":{"definitions":["shipbuilder (plural shipbuilders)","A person who builds vessels such as ships and boats.","A firm that specializes in building ships."],"examples":[],"partOfSpeech":"noun"},"sidesaddle":{"definitions":["sidesaddle (plural sidesaddles)","A saddle, usually for a woman, in which the rider sits with both legs on the same side of the horse."],"examples":[],"partOfSpeech":"noun"},"sping":{"definitions":["sping (plural spings)","(Internet) The use of blogs' trackback functionality to generate link spam."],"examples":[],"partOfSpeech":"noun"},"stairwell":{"definitions":["stairwell (plural stairwells)","A shaft in a multi-story building enclosing a stairway or staircase."],"examples":[],"partOfSpeech":"noun"},"steerage":{"definitions":["steerage (countable and uncountable, plural steerages)","(uncountable) The art of steering.","(countable) The section of a passenger ship that provided inexpensive accommodation with no individual cabins.","(countable) The effect of the helm on a ship."],"examples":[],"partOfSpeech":"noun"},"uncouth":{"definitions":["uncouth (comparative uncouther or more uncouth, superlative uncouthest or most uncouth)","(archaic) Unfamiliar, strange, foreign.","Clumsy, awkward.","Unrefined, crude."],"examples":[],"partOfSpeech":"adjective"},"unsinkable":{"definitions":["unsinkable (comparative more unsinkable, superlative most unsinkable)","Of a ship: that cannot be sunk.","(figuratively) That cannot be overcome or defeated."],"examples":[],"partOfSpeech":"adjective"}}}





app = Flask(__name__)

@app.route('/')
def submit_form():
    return render_template('input_form.html')


@app.route('/', methods=['POST'])
def home():
    movie_name = request.form['movie_name']
    work_dir = 'C:/myProjects/SubtitlePro/'

    subtitle_index, movie_index, movie_name, movie_year =  get_movie_index_info(movie_name)
    subtitle_zip = work_dir + 'Srt/imov_' + str(movie_index) + '-isub_' + str(subtitle_index) + '.zip'
    download_one_movie_subtitle(movie_index, 'English', subtitle_zip)


    try: 
        os.mkdir(work_dir + 'temp_srt/') 
    except:
        shutil.rmtree(work_dir + 'temp_srt/')
        os.mkdir(work_dir + 'temp_srt/') 

    with zipfile.ZipFile(subtitle_zip, 'r') as zip_ref:
        zip_ref.extractall(work_dir + 'temp_srt/')
    srt_file_name = work_dir + 'temp_srt/' + os.listdir(work_dir + 'temp_srt/')[0]

    with open(work_dir + 'Data/unigram_meaning_Wiktionary.json') as json_file: 
        wiktionary = json.load(json_file)

    difficult_words = get_top_n_difficult_words(srt_file_name=srt_file_name, top_n=5, dictionary_dict=wiktionary, work_dir=work_dir)
    output_dictionary['Difficult words'] = difficult_words
    out_html_path = 'C:/myProjects/SubtitlePro/Scripts/templates/' + str(movie_index) + '_' + str(subtitle_index) + '.html'
    html_file = generate_html_from_dictionary(output_dictionary, out_html_path)

    return render_template(html_file)



if __name__ == '__main__':
   app.run()