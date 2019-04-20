#dictionaries

ninja_belts = {"crystal": "red", "ryu": "black"}

def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')

ninja_intro(ninja_belts)