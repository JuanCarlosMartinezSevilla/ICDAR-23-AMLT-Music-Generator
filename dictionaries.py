import os
from data import Data
import string, itertools, json

def getRhytms():
    r_set = set()
    for rhythms in Data.rhythm_atomic:
        r_set.add(rhythms)

    for rhythms_list in Data.rhythm_cells_list:
        for r_cell in rhythms_list:
            for r in r_cell:
                r_set.add(r)
    return r_set

def getKeys():
    key_set = set()
    for key in Data.keys:
        key_set.add(key)
    
    return key_set

def getMeasures():
    measures_set = set()
    for m in Data.measures_list:
        measures_set.add(f"*M{m[0][0]}/{m[0][1]}")
    return measures_set

def getNotes():
    notes_set = set()
    for notes_list in Data.tesitures:
        for n in notes_list:
            notes_set.add(n)

    notes_set.add('r')
    return notes_set

def getSpecial():
    special_set = set()
    special_set.add("!!!filter: autobeam")
    special_set.add("**kern")
    special_set.add("**text")
    special_set.add("*clefG2")
    special_set.add("*")
    special_set.add(".")
    special_set.add("=")
    special_set.add("*-")
    special_set.add(",")
    special_set.add("!")
    special_set.add("?")
    special_set.add(";")
    special_set.add('*met(c)')
    special_set.add('*met(c|)')
    special_set.add('<b>')
    special_set.add('<t>')
    special_set.add('-')
    special_set.add('')
    return special_set

def writeDictionary(name, dict):
    with open(f'{name}.json', 'w') as f:
        json.dump(dict, f)

def create_vocab(path="vocab/"):
    os.makedirs(path, exist_ok=True)

    r_set = getRhytms()
    key_set = getKeys()
    notes_set = getNotes()
    measures_set = getMeasures()
    letters_set = set(list(string.ascii_letters))
    special_set = getSpecial()


    # Merge of dicts notes and rhythms
    product = list(itertools.product(r_set, notes_set))
    final_set = set()

    for pair in product:
        final_set.add(str(pair[0])+str(pair[1]))

    final_set.update(letters_set)
    final_set.update(key_set)
    final_set.update(measures_set)
    final_set.update(special_set)

    w2i = {}
    i2w = {}
    for idx, item in enumerate(final_set):
        w2i[item] = idx
        i2w[idx] = item

    
    writeDictionary(f'{path}w2i', w2i)
    writeDictionary(f'{path}i2w', i2w)
    

if __name__ == '__main__':
    create_vocab("vocab/")