import pandas
#
# nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
#
# letter_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
#
# answer = input("Please enter your name: ").upper()
#
# result = [{row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}[item] for item in input("Please enter your name: ").upper()]

print([{row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}[item] for item in input("Please enter your name: ").upper()])
