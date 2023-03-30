import random
from wonderwords import RandomSentence
import pyphen
from googletrans import Translator

class Lyrics:
    
    def addLyrics(last_lyric_selection, syllable_list):
        prob = random.random()
        # Generate lyrics or not
        if prob > 0.4:
            prob = random.random()
            # Multi time syllables or not
            if prob > 0.8:
                # See if last_selection was multi time
                if last_lyric_selection:
                    prob = random.random()
                    # see if we continue the syllable or not
                    if prob >=0.5:
                        last_lyric_selection = False
                        return syllable_list[0]+'-', last_lyric_selection, syllable_list[1:]
                    else:
                        return syllable_list[0]+'-', last_lyric_selection, syllable_list[1:]
                else:
                    last_lyric_selection = True
                    return syllable_list[0]+'-', last_lyric_selection, syllable_list[1:]
                    
            else:
                return syllable_list[0], last_lyric_selection, syllable_list[1:]
        else:
            return '.', last_lyric_selection, syllable_list[1:]



    def googleTrans():
        """
            Sometimes  is not working due to goolge's api
        """
        translator = Translator() #defining the translator object
        #translator_google = google_translator()
        sentence = RandomSentence() #defining the random sentence

        # español, alemán, francés, latin, italiano
        dest_list = ['es', 'de', 'fr', 'la', 'it']
        #dest_list = ['la']
        language = random.choice(dest_list)

        translated_sentence = ""

        for _ in range(3):
            #translated_sentence += translator_google.translate(sentence.sentence(), lang_tgt=language)[:-1]

            #translated_sentence += translator.translate(sentence.sentence(),'es', 'en' ).text[:-1]
            translated_sentence += sentence.sentence()
        

        translated_wanted_sentence = translated_sentence.split()

        return translated_wanted_sentence

    def addPunctuation(sl):
        result = []
        for s in sl:
            prob = random.random()
            if prob > 0.8:
                s += random.choice([',', '!', '?', ';'])
            
            result.append(s)

        return result

    def pyphen(sentence):
        syllable_list = []
        for word in sentence:
            dic = pyphen.Pyphen(lang='nl_NL')
            separated_word = dic.inserted(word)
            syllable_list.extend(separated_word.split('-'))


        syllable_list = Lyrics.addPunctuation(syllable_list)

        return syllable_list

    def genSyllables():
        return Lyrics.pyphen(Lyrics.googleTrans())

if __name__ == "__main__":
    # Lyrics.generator()
    s= Lyrics.googleTrans()
    a = Lyrics.pyphen(s)
    print(a)
    a.pop(0)
    print(a)
    