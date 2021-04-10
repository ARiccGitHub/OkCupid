OkCupid

My Python portfolio from:
Codecademy Machine Learning, Data Scientist Path.

I divided the project in two different sections:

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

----------------------------------------------------------------------------------------

+ OkCupid DI project memory management

This project requires jupyter notebook to use the python 64bit version, the 32bit version will generate a MemoryError when manipulating the provided data.
If you want to use this project code lines and you are unsure of which python bit version your Jupyter Notebook uses, you can enter the following code lines in your notebook:

```
import struct
print(struct.calcsize("P") * 8)
```

You may also consider, increasing your Jupyter Notebook defaulted maximum memory buffer value.
The Jupyter Notebook maximum memory buffer is defaulted to 536,870,912 bytes.
	- How to increase Jupyter notebook Memory limit? (https://stackoverflow.com/questions/57948003/how-to-increase-jupyter-notebook-memory-limit)
	- Configure (Jupyter notebook) file and command line options (https://jupyter-notebook.readthedocs.io/en/stable/config.html#config-file-and-command-line-options)

I increased my Jupyter Notebook maximum memory buffer value to 8GB, my PC has 16GB of RAM.
When using the full size of the provided data, you need a minimum of 3GB of free RAM to run this project.
If RAM is an issue, you may consider using a sample of the provided data instead of the entire size of the provided data.
You can also utilize:
	- Garbage Collector interface (https://docs.python.org/3/library/gc.html) library. 
			What It Is and How It Works (https://stackify.com/python-garbage-collection/) 
	- And the `del` python function. 
			What does “del” do exactly? (https://stackoverflow.com/questions/21053380/what-does-del-do-exactly)

----------------------------------------------------------------------------------------

Links:

My Project Blog Presentation: 


Project GitHub:
https://github.com/ARiccGitHub/OkCupid

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
data/profiles_nlp.h5  		# NLT Preprocessed text files
data/tfidf/*.csv		# TF-IDF files
data/sim_percentages/*.csv	# TF-IDF terms analysis files

Graphs:
grah/*.png

Image:
img/*.PNG

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

	

