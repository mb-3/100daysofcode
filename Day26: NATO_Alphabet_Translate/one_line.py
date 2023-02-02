## Because why not

print([{row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}[item] for item in input("Please enter your name: ").upper()])
