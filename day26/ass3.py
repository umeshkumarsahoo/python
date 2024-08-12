import pandas
words=pandas.read_csv("word.csv")
print(words)
word_dict={row['letter']:row['code'] for (index,row) in words.iterrows()}
print(word_dict)

user_word=input("write your word: ").lower()
user_list=[word_dict[i] for i in user_word if i in word_dict]
print(user_list)
