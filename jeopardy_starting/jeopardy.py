import pandas as pd

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', 10)
df = pd.read_csv('jeopardy.csv')
print(df.head())
df = df.rename(columns={" Air Date": "Air Date", " Round": "Round", " Category": "Category", " Value": "Value",
                        " Question": "Question", " Answer": "Answer"})
def find_questions(data, list_of_words):
    # data.Question.apply((lambda row: word.lower() in row.lower() for word in list_of_words), axis = 1)
    # return data[data.Question]
    # filter = lambda x: all(word.lower() in x.lower() for word in words)
    return data.loc[data["Question"].apply((lambda x: all(word.lower() in x.lower() for word in list_of_words)))]

print(find_questions(df, ['King', 'England']))

df['Float Value'] = df['Value'].apply(lambda string: float(string.replace('$', '').replace(',', '')) if string != "None" else 0)

print(find_questions(df, ['King'])['Float Value'].mean())

# Filtering the dataset and finding the average value of those questions
filtered = filter_data(jeopardy_data, ["King"])
print(filtered["Float Value"].mean())

# A function to find the unique answers of a set of data
def get_answer_counts(data):
    return data["Answer"].value_counts()

# Testing the answer count function
print(get_answer_counts(filtered))
