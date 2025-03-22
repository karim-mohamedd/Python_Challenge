import pandas

# This small project shows the power of Dictionary Comprehension and list Comprehension it replaced so many lines of code
df = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter : row.code for (index, row) in df.iterrows()} #"iterrows()" is a method to loop in the rows of dataframe

def Generate_phonetic():
    word = input("Enter a Word: ").upper()
    try:
        phonetic_list= [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("sorry only letters are accepted")
        Generate_phonetic()
    else:
        print(phonetic_list)

Generate_phonetic()
