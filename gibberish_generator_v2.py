import random 

def gibberish_generate(sentence):
    """This method splits the given sentence into each word. 
    Then it takes each character of each word and searches if the character is in the choice_dictionary.keys().
    If character is not there in the choice_dictionary.keys(), it does nothing, simply look for the next character.
    If character is present, any of the corresponding choice is picked and appended to the output."""
    
    # for each character in key, any of the values can be substituted
    choice_dictionary={ "AE": ["A","E","AE"], 
                "BPV": ["B","P","V"],
                "F": ["F","FF","IF","FU"],
                "CK": ["C","K"],
                "JG":["J", "G"],
                "SXZ": ["S","X","Z"],
                "Q": ['IQ',"EQ","KWA"],
                "DT":["D","T","DU","TU"],
                "L":["L"],
                "M":["M"],
                "N":["N"], 
                "R":["R","IR","YR"], 
                "IY":["I","Y","YE","EYE"],
                 "H":["H","HU","UH"], 
                "OU":["O","U","A"],
                "W":["V","W","IV"]}
    
    gibberish = ""  # initializing output variable
    
    # choice_dictionary keys are all UPPER CASE
    # so converting the whole sentence to UPPER CASE to match with the choice_dictionary keys
    sentence = sentence.upper() 
    
    for word in sentence.split(" "):  # taking each word from the sentence 
        for char in word:  # taking each character from the word
            for key in choice_dictionary.keys(): 
                if char in key:  # if the character is in dictionary key
                    
                    choice_length = len(choice_dictionary[key])  # no. of choices we have for each character to choose from
                    choice = random.randint(0,choice_length-1)  # which option to choose from
                    new_chars = choice_dictionary[key][choice]  # new_chars length may be 1 or more depending on the choice
                    
                    # for mixing UPPER CASE and lower case in the generated gibberish
                    case=random.randint(0,1)
                    
                    # if case==0, lower case of new_chars is appended, else UPPER CASE 
                    gibberish += new_chars.lower() if case==0 else new_chars
                    
        gibberish += " " # adding a space between each word

    space_to_be_inserted = random.randint(0,1) # whether to insert an additional space in between the gibberish text

    if space_to_be_inserted:
        
        index = random.randint(1,len(gibberish[:-1])) # where to insert a space
        
        # insert a space only if a space doesn't exist there
        if gibberish[index-1]!=" " and gibberish[index]!=" " and gibberish[index+1]!=" ":
            gibberish = gibberish[:index]+" "+gibberish[index:]
            
    return gibberish[:-1]  # chopping off the last space added at the end of every sentence


def return_sample_gibberish():
    
    samples = ["hi bye", "Thomas Alva Edison", "a blessing in disguise", "a dime a dozen", "BEAt around the bush", "the", "UNIted Kingdom", "word",
            "My swimsuit", "LAws of Thermodynamics", "Better late than never", "Bite the bullet", "Break a leg", "Call it a day",
            "Under the weather", "Time flies when you're having fun", "Speak of the devil", "The best of both worlds"]
    
    # selecting just 7 random samples to print on screen
    # random.sample() returns a new list with multiple random elements from the original list without replacement
    selected_samples = random.sample(samples, 7) 
    
    examples = []  # creating an empty list to hold all example texts and their generated gibberish
    for i in selected_samples:
        examples.append((i, gibberish_generate(i)))
    return examples
