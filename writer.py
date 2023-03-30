from data import Data
from lyrics import Lyrics
import uuid
from rhythm import Rhythm
import random

class Writer:

    
    def idGenerator():
        return uuid.uuid4().fields[-1]

    def getSentence(generated):
        result = ""
        for g in generated:
            result += g + " "
        return result

    def lyrics(all_voices):
        all_new_voices = []
        lyrics_voice = []
        last_lyric_selection = False

        syllable_list = Lyrics.genSyllables()
       
        for item in all_voices[0]:
            
            if item == '.':
                lyrics_voice.append('.')
            elif item == '=':
                lyrics_voice.append('=')
            elif 'r' in item:
                lyrics_voice.append('.')
            elif len(syllable_list) == 0:
                lyrics_voice.append('.')
            else:
                syllable, last_lyric_selection, syllable_list = Lyrics.addLyrics(last_lyric_selection, syllable_list)
                lyrics_voice.append(syllable)

        all_new_voices.append(lyrics_voice)
        for v in all_voices:
            all_new_voices.append(v)

        return all_new_voices, lyrics_voice
    
    def write(score):
        all_voices = []
        for v in score["voices"]:
            #all_voices.append(Writer.addStems(Writer.addSubdivision(v), score["measure"]))
            all_voices.append(Writer.addSubdivision(v))

        lyrics_voice = []
        if 'lyrics' in score:
            all_voices, lyrics_voice = Writer.lyrics(all_voices)
        Writer.writeToFile(score, all_voices, lyrics_voice)
    
    def addSubdivision(v):
        min_rhy = max(Data.rhythm_atomic)
        spine = []
        for m in v:
            for n in m:
                subdivision_counter = 0
                if isinstance(n['rhythm'], str):
                    subdivision_value = Rhythm.calcSpaceWhenString(n['rhythm'])
                else:
                    subdivision_value = min_rhy / n['rhythm']
                while(subdivision_counter != subdivision_value):
                    if subdivision_counter == 0:
                        prob = random.random()
                        if prob > 0.8:
                            spine.append(str(n['rhythm']) + 'r')
                        else:
                            spine.append(str(n['rhythm']) + Data.tesiture[n['note_idx']])
                    else:
                        spine.append('.')
                    subdivision_counter+=1
            spine.append('=')
        return spine


    def writeToFile(score, all_voices, lyrics_voice):
        measure = score["measure"]
        

        #f = open(f"generatedScores/{Writer.idGenerator()}.krn", "w")
        f = open("example.krn", "w")
        f.write("!!!filter: autobeam\n")
        if lyrics_voice != []:
            f.write('**kern\t**text\n')
            f.write('*clefG2\t*\n')
            f.write(f'{Data.key}\t*\n')

            # check if we use *met
            prob = random.random()
            if prob > 0.8:
                if measure[0] == 4 and measure[1] == 4:
                    f.write(f"*met(c)\t*\n")
                elif measure[0] == 2 and measure[1] == 2:
                    f.write(f"*met(c|)\t*\n")
            else:
                f.write(f"*M{measure[0]}/{measure[1]}\t*\n")

            if len(score["voices"])> 1:
                f.write('*^\t*\n')
        else:
            f.write('**kern\n')
            f.write('*clefG2\n')
            f.write(f'{Data.key}\n')
            f.write(f"*M{measure[0]}/{measure[1]}\n")

            if len(score["voices"])> 1:
                f.write('*^\n')

             
        subdivision = int((max(Data.rhythm_atomic) / measure[1] * measure[0] +1) * score['number_measures'])
        subdivision_counter = 0
        while(subdivision_counter != subdivision):
            voice_counter = len(score["voices"])-1
            if lyrics_voice != []:
                voice_counter += 1
            while (voice_counter != -1):
                if lyrics_voice != []:
                    if voice_counter != len(score["voices"]):
                        f.write('\t')   
                elif voice_counter != len(score["voices"])-1:
                    f.write('\t')
                
                f.write(all_voices[voice_counter][subdivision_counter])
                voice_counter -= 1   
            f.write('\n')
            subdivision_counter += 1

        if len(score["voices"])> 1:
            voice_counter = 0
            while (voice_counter != len(score["voices"])):
                if voice_counter > 0:
                    f.write('\t')
                f.write("*v")
                voice_counter += 1
       
        if lyrics_voice != [] and len(score["voices"])> 1:
            f.write('\t*')
            f.write('\n')
            f.write('=\t=\n')
            f.write('*-\t*-\n')
        elif lyrics_voice != []:
            f.write('*-\t*-\n')
        else:
            f.write('\n')
            f.write('=\n')
            f.write('*-\n')


            

    