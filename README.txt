OkCupid

My Python portfolio from:
Codecademy Machine Learning, Data Scientist Path.

I divided the project in three different sections:

OKCupid ID - Data Investigation
	- Provided data investigation
	- NLP text pre-processing
OkCupid TF-IDF - NLP Term Frequency–Inverse Document Frequency (TF-IDF)
	- TF-IDF scores computation
	- TF-IDF terms results analysis


Project Goal:

Using data from OKCupid, an app that focuses on using multiple choice and short answers to match users, 
formulate questions and implement machine learning techniques to answer those questions.

----------------------------------------------------------------------------------------

Project Requirements:

Knowledge:
Machine Learning, Unsupervised Learning and Natural Language Processing

Python v3 or later:
https://www.python.org/

scikit-learn
https://scikit-learn.org/

Pandas 
https://pandas.pydata.org/

Matplotlib
https://matplotlib.org/

Numpy
https://numpy.org/

Sklearn:
https://scikit-learn.org/stable/

Gensim:
https://pypi.org/project/gensim/

Jupyter notebook:
https://jupyter.org/


+ OkCupid DI project memory management
This project requires jupyter notebook to use a python 64bit version, 
the 32bit version will generate a MemoryError when manipulating the provided data.
If you want to use this project code lines and you are unsured of what python bit version your Jupyter Notebook uses, 
you can enter the following code lines in your notebook:

import struct
print(struct.calcsize("P") * 8)

You may also consider, increasing your Jupyter Notebook defaulted maximum memory buffer value.
The Jupyter Notebook maximum memory buffer is defaulted to 536,870,912 bytes.
How to increase Jupyter notebook Memory limit?
Configure (Jupyter notebook) file and command line options

I increased my Jupyter Notebook maximum memory buffer value to 8GB, my PC has 16GB of RAM.
You need a minimum of 3GB of free RAM to run the project when using the full size of the provided data.
If RAM is an issue, you may consider to use a sample of the provided data insteat of the entire size of the provided data.
You can also utilize:

Garbage Collector interface library, Python Garbage Collection: What It Is and How It Works
And the del python function, What does “del” do exactly?

----------------------------------------------------------------------------------------

Overview

OkCupid:
In recent years, there has been a massive rise in the usage of dating apps to find love. 
Many of these apps use sophisticated data science techniques to recommend possible matches to users and to optimize the user experience. 
These apps give us access to a wealth of information that we’ve never had before about how different people experience romance.
In this portfolio project, I analyze data from OKCupid, formulate questions and implement machine learning techniques to answer the questions.

OkCupid DI:
In this section, I investigate the OkCupid provided data, formulate questions, and preprocess the data.

OkCupid TF-IDF:
In this section, I compute the TF-IDF scores from the preprocessed data, and analyze the results.

----------------------------------------------------------------------------------------

Links:

My Project Blog Presentation: 


Project GitHub:


----------------------------------------------------------------------------------------

Project map:

Python Jupiter Notebook Code Lines File:
OkCupid_DI.ipynp
OkCupid_TF-IDF.ipynp

Python Code Lines Files:
project_library.py

Provided data:
profiles.csv

Project Info. Files:
similarity_percentage_formula.pdf
okcupid_codebook.txt

Data Files:
data/*.csv     			# Data investigation 
data/profiles_nlp.h5  		# NLT Preprocessed text file
data/tfidf/*.csv		# TF-IDF files

Graphs:
grah/*.png

Image:
img/*.PNG

Code Presentation:


----------------------------------------------------------------------------------------

My Project layout:

OkCupid_DI
	- Libraries
	- Investigating the Data
	- Formulating Questions
	- Text Pre-processing
OkCupid_TF-IDF
	- Libraries
	- TF-IDF Scores Computation
	- TF-IDF Terms Results Analysis

	

