from sklearn.datasets import fetch_20newsgroups  # load data from sklearn dataset
import preprocess as pre
import nltk
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import time
from heapq import nlargest
from random import randrange
nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')

timestamp = time.time()  # Very beginning


class Cat():
    def __init__(self, category_id):
        self.category_id = category_id    # The category id according to target
        self.wf_dic = dict()    # Word frequency dictionary. Key is word_id, value is frequency
        self.word_count = 0


def top10(categ):
    """ This function returns the top 10 frequent word for that class"""
    topten_list = nlargest(10, cat_dict[categ].wf_dic, key=cat_dict[categ].wf_dic.get)
    print("-------------------------")
    print("%s" % categories[categ])
    print("-------------------------")
    for i in range(len(topten_list)):
        word = ""
        for key, id in dic_dictionary.items():
            if id == topten_list[i]:
                word = key
        frq = cat_dict[categ].wf_dic[topten_list[i]]
        print("%s : %d" % (word, frq ))

data=fetch_20newsgroups()
categories=data.target_names
# Training the data on these categories
train=fetch_20newsgroups(subset='train', categories=categories)
# Testing the data for these categories
test=fetch_20newsgroups(subset='test', categories=categories)


timestamp1 = time.time()

dictionary = list() # All the words
dic_dictionary = dict() # Keeps all the words. Keys are the words. Values are numbers representing the word
cat_dict = dict()   # 20 keys each a category_id, values are Cat instances.
prior_d = dict()    # Keys are category ids. Values are the probabilty of being that document. Nc / Ntotal

# Add the words in the training set
for d in range(len(train.data)):    # For every document
    wordlist = pre.preProcessing(train.data[d])
    for i in range(len(wordlist)):  # Every single word ın the document
        dictionary.append(wordlist[i]) # Add it


# Add the words in the testing set.
for d in range(len(test.data)):    # For every document
    wordlist = pre.preProcessing(test.data[d])
    for i in range(len(wordlist)):  # Every single word ın the document
        dictionary.append(wordlist[i]) # Add it


dictionary = list(set(dictionary))  # All the words in sorted order.
print("The length of the dictionary is", len(dictionary))

# With this for loop we create a dictionary having all the unique words and a number for their id.
for w in range(len(dictionary)):
    dic_dictionary[dictionary[w]] = w

# Assigning the values of Cat classes to category dictionary.
for c in range(len(categories)):
    cat_dict[c] = Cat(c)
    prior_d[c] = 0  # Initialize with 0 for prior dict

# Initialize wf_dictionaries with zeros.
for d in range(len(dictionary)):
    for c in cat_dict.values():
        c.wf_dic[d] = 0

# Finds prior for each class assigns these probabilities to a dict.
for d in range(len(train.data)):
    c_id = train.target[d]  # ID of the category of dth document
    prior_d[c_id] += 1  # Increment the occurrence number

# Divide to the total number of elements in the training set to find prior probabilities
for i in range(len(prior_d.keys())):
    total_doc = len(train.data)
    prior_d[i] = prior_d[i]/total_doc

timestamp2 = time.time()  # End time
print("Making the dictionary took %.2f seconds" % (timestamp2 - timestamp1))






timestamp1 = time.time()
"""
THIS PART IS RECOMMENDED BY THE PROFESSOR
Getting the most frequent 50000 words
"""
# This dictionary have all the words_id as key, and frequencies as values. Initially 0.
freq_dic = dict.fromkeys(dic_dictionary.values(), 0)

for d in range(len(train.data)):
    wordlist = pre.preProcessing(train.data[d])
    for w in wordlist:  # Every single word in the document
        word_id = dic_dictionary[w]  # fetch the id of the word
        freq_dic[word_id] += 1  # Increment the frequency

most_freq = nlargest(50000, freq_dic, key=freq_dic.get)     # IDs of most frequent 50000 words
s = set(most_freq)

timestamp2 = time.time()  # End time
print("Updating the frequencies took %.2f seconds" % (timestamp2 - timestamp1))



"""
For every document in the training set we need to calculate frequencies of these word for every
category. There 20 instances of Cat class. each has a dictionary of the words with frequencies.
Somewhat I create a double matrix.
"""
timestamp1 = time.time()

for d in range(len(train.data)):
    wordlist = pre.preProcessing(train.data[d])
    c_id = train.target[d]  # ID of the category of dth document

    for w in wordlist:  # Every single word in the document
        word_id = dic_dictionary[w]  # fetch the id of the word
        if word_id in s:    # Check of frequency !!! ADDDED !!!
            cat_dict[c_id].wf_dic[word_id] += 1  # Increment the frequency of the word in that class.

for c in range(len(categories)):
    category = cat_dict[c]
    category.word_count = sum(category.wf_dic.values())   # Total words in that class

timestamp2 = time.time()  # End time
print("Filling the classes took %.2f seconds" % (timestamp2 - timestamp1))


""" Calculating top 10 words for each category Q5"""
for i in range(len(categories)):
    top10list = top10(i)



"""
Testing phase
"""
timestamp1 = time.time()

prediction_list = list()    # 0th element means what 0th testing data was predicted as
hit = 0
miss = 0
total = len(test.data)
#print(len(test.target))
for d in range(len(test.data)):
    max_prob = 0
    prediction = randrange(20)  # Predicted category(id)
    prob_list = list()
    for cat in range(len(categories)):
        curr_prob = prior_d[cat]    # We start with Prior probability and multiply...
        wordlist = pre.preProcessing(test.data[d])  # Preprocess the testing data
        for word in wordlist:   # For every word
            word_id = dic_dictionary[word]  # id of the word
            if word_id in s:  # Check of frequency !!! ADDDED !!!
                curr_prob *= (cat_dict[cat].wf_dic[word_id] + 1) / (cat_dict[cat].word_count + len(dictionary)) * pow(10,4)
        prob_list.append(curr_prob) # Add the found probability to the list
    for p in range(len(prob_list)):
        if prob_list[p] > max_prob:
            max_prob = prob_list[p]
            prediction = p

    prediction_list.append(prediction)  # Add the prediction to the prediction list

    if prediction == test.target[d]:
        hit += 1
    else:
        miss += 1

timestamp2 = time.time()  # End time
print("Testing phase took %.2f seconds" % (timestamp2 - timestamp1))

for cat in range(len(categories)):
    print("%s : %f" % (categories[cat], prior_d[cat]))

print("Number of correct predictions = %d" % hit)
print("Number of false predictions = %d" % miss)
print("Total number of tests = %d" % total)
print()
print("Accuracy rate is = ", (hit/total)*100, "%")

ttl = test.target.tolist()
target_list_name = list()
pred_list_name = list()

for i in ttl:
    target_list_name.append(categories[i])

for i in prediction_list:
    pred_list_name.append(categories[i])


timestamp2 = time.time()  # End time
print("Execution of the whole code took %.2f seconds" % (timestamp2 - timestamp))

data = {"y_Actual" : target_list_name,
        "y_Predicted" : pred_list_name
        }
df = pd.DataFrame(data, columns=['y_Actual','y_Predicted'])
confusion_matrix = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
plt.show()