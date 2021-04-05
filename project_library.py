'''

                                        Project Library
                  
Project: OkCupid
The library contains several function utilized by 
- okcupid.ipynb 
- okcupid.py

'''

########### Libraries
# Counter Dictionary class - https://docs.python.org/3/library/collections.html#collections.Counter -
from collections import Counter
# database of English  
from nltk.corpus import wordnet


'''

                    f_combinations() 

To combine different features,
I modified the combinations() function from the itertools libray into the function f_combinations() 
to better suit the combinations of features.

Author: Alex Ricciardi
'''
def f_combinations(features_list, num):
    '''
        - Takes the arguments:
            - features_list, list data type, single features names list.
            - mum, integer type, the number of features per combination desired.

        - uses the nCr combination type to combine single features names into combinations of mum features names.
        - saves the combined feature names as list data type ocjects into a combinations list.

        - returns the combinations list.
    '''
    n = len(features_list)
    # Checks if the number of wanted combinations is larger than the number of element in the feature_list
    if num > n:
        return
    # Range value of the number of wanted combinations
    indices = list(range(num))
    # Returns the beginning of the feature list ranged to the number of wanted combinations
    yield list(features_list[i] for i in indices)
    # Infinte loop no break then return
    # for loops also have an else.
    # The else clause executes after the loop completes normally.
    # This means that the loop did not encounter a break statement.
    while True:
        # Reverse range of the number of wanted combinations
        for i in reversed(range(num)):
            # Checks if the value at index i of the reverse range value of the number of wanted combinations
            # is not equal to the number of features + i minus the number of wanted combinations
            if indices[i] != i + n - num:
                break
        # If not break
        else:
            return
        # If breack true
        indices[i] += 1
        # Increments by 1 the values of indices
        for j in range(i + 1, num):
            indices[j] = indices[j - 1] + 1
        # Returns the features_list values at the index values of the incremented indices
        yield list(features_list[i] for i in indices)

        
'''
                           column_types()

Returns pandas dataframe column names, column object pandas dtypes and column python data types

The `dtype` results from `pandas.Dataframe.info()` are outputs from `pandas.DataFrame.dtypes()` method.
The `dtypes()` method does not differentiate between string iterable python objects (strings, dictionaries, lists, tuples),
it classifies all them as objects data types, the `column_types()` function returns the dataframe column names,
column object pandas dtypes and column python data types

Author: Alex Ricciardi
'''
import pandas as pd

def column_types(df):
    '''
    Takes the argumnt:
        df, pandas DataFrame data type
    Returns:
         A Dataframe of the inputed DataFrame
            column names
            column object pandas dtypes
            column python data types
    '''
    # Stores df columns names and columns pandas dtypes
    column_n = df[df.columns].dtypes.to_frame().rename(columns={0:'pandas_dtype'})
    # Stores  df columns python data types
    # Uses row indexed `0` values
    column_n['python_type'] = [type(df.loc[0][col]).__name__ for col in df.columns]
    # Checks column_n `type` values for NoneType
    for col in column_n.index:
        if column_n.loc[col]['python_type'] == 'NoneType':
            # Seach df row with no NaN
            for i in range(len(df)):
                if df.loc[i][col] != None:
                    colunm_n.loc[col]['type'] = type(df.loc[i][col]).__name__
                    break
                    # If the df column is all NaN values, the function will return a 'NoneType' for that particular column
    df_column_names = column_n.reset_index().rename(columns={'index':'columns_names'})
    return df_column_names


'''
                            get_part_of_speech()

To improve the performance of lemmatization (bring a word to his root), each word in the processed text is assigned parts of speech tag, Part-of-Speech Tagging is the process of reading text in some language and assigns parts of speech to each word (and other token), such as noun, verb, adjective, etc.

The function utlizes nlt.corpus.reader.wordnet.synsets() method
https://www.nltk.org/api/nltk.corpus.reader.html#nltk.corpus.reader.wordnet.Lemma.synset

Author: Alex Ricciardi
'''
def get_part_of_speech(word):
    '''
    + Takes the arguments:
        - word, string data type.
    + Matches word with synonyms
    + Tags word and count tags.
    + Returns:
        - The most common tag, the tag with the highest count, 
          ex: n for Noun, string data type.   
    '''
    # Synonyms matching
    probable_part_of_speech = wordnet.synsets(word)
    # Initializing Counter class object
    pos_counts = Counter()
    # Taging and counting tags
    pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  ) # Noun
    pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  ) # Verb
    pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  ) # Adjectif
    pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  ) # Adverb
    # The most common tag, the tag with the highest count, ex: n for Noun 
    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
    
    return most_likely_part_of_speech




















