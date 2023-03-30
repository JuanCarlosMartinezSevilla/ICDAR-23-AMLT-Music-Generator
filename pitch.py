from data import Data
import random

class Pitch:
    def initLastNotes(n_voices):
        last_notes = []
        for idx in range(0, n_voices):
            last_notes.append(-1)
        return last_notes

    def checkNewPitch(new_pitch):
        if new_pitch < 0:
            new_pitch = 0
        elif new_pitch >= len(Data.tesiture):
            new_pitch = len(Data.tesiture)-1
        return new_pitch

    def genPitch(last_pitch_idx, bass_voice):
        new_pitch = -1
        if bass_voice:
            if last_pitch_idx == -1:
                # print("First voice first note")
                # print(Data.tesiture)
                
                new_pitch = random.randint(0, len(Data.tesiture)//2)
               
            else:
                new_pitch = random.randint(last_pitch_idx-Data.bass_range, last_pitch_idx+Data.bass_range)
        else:
            new_pitch = random.randint(last_pitch_idx+1, last_pitch_idx+Data.range*2)
        
        return Pitch.checkNewPitch(new_pitch)

    def createPitches(score):
        number_voices = len(score["voices"])
        
        for idx_m, measure in enumerate(score["voices"][0]):
            last_notes = Pitch.initLastNotes(len(score["voices"]))
            measures_notes, measures = Pitch.getNumberOfNotes(score, number_voices, idx_m)
            max_notes_number = max(measures_notes)
            
            for idx_n in range(0, max_notes_number):
                voice_counter = 0
                while(voice_counter != number_voices):
                    if idx_n > len(measures[voice_counter])-1:
                        pass
                    else:
                        # print(f"Get note{voice_counter}:{idx_m}:{idx_n}")

                        if voice_counter > 0:
                            pitch_generated = Pitch.genPitch(last_notes[voice_counter-1], bass_voice = False)
                        else:
                            pitch_generated = Pitch.genPitch(last_notes[voice_counter], bass_voice = True)
                        
                        last_notes[voice_counter] = pitch_generated
                        # print(f"Voice{voice_counter}:Pitch{pitch_generated}")
                        score["voices"][voice_counter][idx_m][idx_n]['note_idx'] = pitch_generated

                    voice_counter += 1
        return score
                    

    def getNumberOfNotes(score, number_voices, idx_m):
        voice_counter = 0
        measures_notes =  []
        measures = []

        while (voice_counter != number_voices):
            measures_notes.append(len(score["voices"][voice_counter][idx_m]))
            measures.append(score["voices"][voice_counter][idx_m])
            voice_counter += 1
        return measures_notes, measures