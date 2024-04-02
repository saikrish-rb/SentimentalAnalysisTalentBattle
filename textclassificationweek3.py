# -*- coding: utf-8 -*-
"""TextClassificationWeek3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IlK2fRHklbijjEKQwQ9DI_cN1BrUm_78
"""

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "Thor eating pizza, Loki is eating pizza, Ironman ate pizza already",
    "Apple is announcing new iphone tomorrow",
    "Tesla is announcing new model-3 tomorrow",
    "Google is announcing new pixel-6 tomorrow",
    "Microsoft is announcing new surface tomorrow",
    "Amazon is announcing new eco-dot tomorrow",
    "I am eating biryani and you are eating grapes"
]

v = TfidfVectorizer()
v.fit(corpus)
transform_output = v.transform(corpus)

all_feature_names = v.get_feature_names_out()

for word in all_feature_names:
    indx = v.vocabulary_.get(word)
    idf_score = v.idf_[indx]

    print(f"{word} : {idf_score}")
