import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

user_word = input("Enter a word: ").upper()
user_phonetic = [nato_dict[letter] for letter in user_word]
print(user_phonetic)
