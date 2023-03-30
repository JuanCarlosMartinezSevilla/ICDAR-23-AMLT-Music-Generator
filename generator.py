from rhythm import Rhythm
from pitch import Pitch
from writer import Writer
from renderer import Renderer
import cameraDistortion
from data import Data

class Generator:
    
    def generator(args, score):
        number_measures = args.measures
        space = Rhythm.getMinRhythm(score["measure"])
        number_voices = args.voices

        voice_counter = 0
        #print(score["measure"])


        """
         Score[voices] will be an array of voices that are an array of measures 
         each of them an array of notes.
        """
        score["voices"] = []

        while(voice_counter != number_voices):
            voice_container = []
            measures_counter = 0
            
            while(measures_counter != number_measures):
                notes_in_measure = []

                current_space = space

            
                
                while(current_space != 0.0):
                    note = {}
                    
                    r, tam = Rhythm.getRhythm(current_space)
                    
                    current_space -= tam
                    if isinstance(r, list):
                        for item in r:
                            note["rhythm"] = item
                            note["note_idx"] = -1
                            notes_in_measure.append(note.copy())
                    else:
                        note["rhythm"] = r
                        note["note_idx"] = -1
                        notes_in_measure.append(note.copy())


                # END OF MEASURE OF A VOICE
                measures_counter += 1

                voice_container.append(notes_in_measure)
            
            # END OF VOICE
            score["voices"].append(voice_container)

            voice_counter += 1
        score = Pitch.createPitches(score)
        if args.lyrics > 0:
            score['lyrics'] = []

        Writer.write(score)
        Renderer.renderScore("example.krn", "example.svg")
        #Renderer.renderScoreWithOtherFont("example.svg")
        if Data.camera:
            cameraDistortion.apply_distortion(path="example.png", saving_path="cameraExample.png", bg_change=False)
            if Data.change_background:
                cameraDistortion.apply_distortion(path="pruebaFondo.png", saving_path="cameraFondoExample.png", bg_change=True)
