import random

class Data:
    measures_list = [[[4, 4], 0], [[3, 4], 0], [[2, 4],0], [[5, 4],0], [[7, 4],0], 
     [[6, 8], 1], [[9, 8], 1], [[12, 8], 1], [[6, 4], 0], [[7, 8], 1], [[2, 2], 2], [[3, 2], 2], [[4, 2], 2]]
    #measures_list = [[[4, 4], 0]]
    rhythm_cells_list = [
                    [
                        [2, 2], [2, 2], [2, 2], [2, 2],[4,4], [4,4], [4,4], [4,4], [4,4],[8,8], [8,8], [8,8],
                        [8,8], [8,8], [8,8], [16,16,16,16], [8, 4, 8], [16, 16, 8], [8, 16, 16], 
                        [16, 8, 16], ['8.', 16], ['8.', 16], [16, '8.'], [16, '8.']
                    ],
                    [    
                        [8, 8, 8], [8, 8, 8], [16,16,16,16,8], [16,16,8,8], [16,8,8,16],['4.'], [4, 8], [8, 4], 
                        [8,16,16,16,16], [8,8,16,16]
                    ],
                    [
                        [2, 2], [2, 2], [4, 4, 4, 4], [4, 2, 4], [1], [1], [2, 4], [4, 2], [4, 8, 8], [8, 4, 8]
                    ]
                ]

    rhythm_atomic = [1, 2, 4, 8, 16]
    keys = ['*k[]', #C maj
            '*k[f#]', #G maj
            '*k[f#c#]', #D maj
            '*k[f#c#g#]', #A maj
            '*k[f#c#g#d#]', #E maj
            '*k[f#c#g#d#a#]', #B maj
            '*k[f#c#g#d#a#e#]', #F# maj
            '*k[f#c#g#d#a#e#b#]', #C# maj
            '*k[b-]', #F maj
            '*k[b-e-]', #Bb maj
            '*k[b-e-a-]', #Eb maj
            '*k[b-e-a-d-]', #Ab maj
            '*k[b-e-a-d-g-]', #Db maj
            '*k[b-e-a-d-g-c-]', #Gb maj
            '*k[b-e-a-d-g-c-f-]'] #Cb maj 

    tesitures = [['B','c', 'd', 'e', 'f', 'g', 'a', 'b', 'cc', 'dd', 'ee', 'ff', 'gg', 'aa', 'bb', 'ccc'],
                 ['B','c', 'd', 'e', 'f#', 'g', 'a', 'b', 'cc', 'dd', 'ee', 'ff#', 'gg', 'aa', 'bb', 'ccc'],
                 ['B','c#', 'd', 'e', 'f#', 'g', 'a', 'b', 'cc#', 'dd', 'ee', 'ff#', 'gg', 'aa', 'bb', 'ccc#'],
                 ['B','c#', 'd', 'e', 'f#', 'g#', 'a', 'b', 'cc#', 'dd', 'ee', 'ff#', 'gg#', 'aa', 'bb', 'ccc#'],
                 ['B','c#', 'd#', 'e', 'f#', 'g#', 'a', 'b', 'cc#', 'dd#', 'ee', 'ff#', 'gg#', 'aa', 'bb', 'ccc#'],
                 ['B','c#', 'd#', 'e', 'f#', 'g#', 'a#', 'b', 'cc#', 'dd#', 'ee', 'ff#', 'gg#', 'aa#', 'bb', 'ccc#'],
                 ['B','c#', 'd#', 'e#', 'f#', 'g#', 'a#', 'b', 'cc#', 'dd#', 'ee#', 'ff#', 'gg#', 'aa#', 'bb', 'ccc#'],
                 ['B#','c#', 'd#', 'e#', 'f#', 'g#', 'a#', 'b#', 'cc#', 'dd#', 'ee#', 'ff#', 'gg#', 'aa#', 'bb#', 'ccc#'],
                  
                 ['B-','c', 'd', 'e', 'f', 'g', 'a', 'b-', 'cc', 'dd', 'ee', 'ff', 'gg', 'aa', 'bb-', 'ccc'],
                 ['B-','c', 'd', 'e-', 'f', 'g', 'a', 'b-', 'cc', 'dd', 'ee-', 'ff', 'gg', 'aa', 'bb-', 'ccc'],
                 ['B-','c', 'd', 'e-', 'f', 'g', 'a-', 'b-', 'cc', 'dd', 'ee-', 'ff', 'gg', 'aa-', 'bb-', 'ccc'],
                 ['B-','c', 'd-', 'e-', 'f', 'g', 'a-', 'b-', 'cc', 'dd-', 'ee-', 'ff', 'gg', 'aa-', 'bb-', 'ccc'],
                 ['B-','c', 'd-', 'e-', 'f', 'g-', 'a-', 'b-', 'cc', 'dd-', 'ee-', 'ff', 'gg-', 'aa-', 'bb-', 'ccc'],
                 ['B-','c-', 'd-', 'e-', 'f', 'g-', 'a-', 'b-', 'cc-', 'dd-', 'ee-', 'ff', 'gg-', 'aa-', 'bb-', 'ccc-'],
                 ['B-','c-', 'd-', 'e-', 'f-', 'g-', 'a-', 'b-', 'cc-', 'dd-', 'ee-', 'ff-', 'gg-', 'aa-', 'bb-', 'ccc-']]
    #tesiture = ['B','c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'b', 'cc','cc#', 'dd','dd#', 'ee', 'ff', 'ff#', 'gg', 'gg#', 'aa', 'bb', 'ccc', 'ccc#']
    range = 5
    bass_range = 3

    colors = ['#f5dfa2', '#e0dbbf', '#e6eda4', '#cfb97e', '#9e7946']
    
    global tesiture
    global key
    global camera
    global measure
    global rhythm_cells
    global change_background
    global bg_color

    def change_color():
        Data.bg_color = random.choice(Data.colors)

    def set_globals(args): 
        idx = random.randint(0, len(Data.tesitures)-1)

        Data.tesiture = Data.tesitures[idx]
        idx = random.randint(idx-1, idx+1)
        if idx < 0:
            idx = 0
        if idx == len(Data.keys):
            idx -= 1
        Data.key = Data.keys[idx]

        Data.camera = args.camera


        if args.background:
            Data.change_background = args.background
            Data.change_color()
        else:
            Data.change_background = False

        idx = random.randint(0, len(Data.measures_list)-1)
        Data.measure = Data.measures_list[idx][0]
        Data.rhythm_cells = Data.rhythm_cells_list[Data.measures_list[idx][1]]