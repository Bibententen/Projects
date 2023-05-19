from pymongo import MongoClient
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
from gensim import corpora, models
from gensim.utils import simple_preprocess
from nltk.sentiment import SentimentIntensityAnalyzer
from rake_nltk import Rake

client = MongoClient('localhost',27017)
db= client.Practical4

# return list of words without stopwords
def remove_stopwords(words):
    list = word_tokenize(words)
    for i in list:
        if i in stopwords.words("english"):
            list.remove(i)
    return list

#return root of words
def stem_words(words):
    result =[]
    for i in words:
        result.append(PorterStemmer().stem(i))
    return result

#remove non-alphabetical symbols then remove stopwords, then return list of root words
def clean_text(text):
    text = re.sub(r"(([a-z]{3,6}://)|(^|\s))([a-zA-Z0-9\-]+\.)+[a-z]{2,13}[\.\?\=\&\%\/\w\-]*\b([^@]|$)","", text)
    text = re.sub(r"http"," ", text)
    text = re.sub(r"[^\w]"," ", text)
    text = re.sub(" \d+", " ", text)
    words = remove_stopwords(text)
    words = stem_words(words)
    return words

#get keywords from text
rake_nltk_var = Rake()
def get_keywords(cleaned):
    rake_nltk_var.extract_keywords_from_text(','.join(cleaned))

# Get ranked phrases (keywords)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    return keyword_extracted

# Create name/value pair in comma seperate value
def keywords_to_csv(keywords):
    csv_keywords =''
    for i in keywords:
        csv_keywords = csv_keywords + ' ' + i
    return csv_keywords

#write a txt file with text from all the tweets
output_file_path = "task2.txt"
with open(output_file_path, "w") as file:
    for text in db.asm.find():
        cleaned = " ".join(clean_text(text["body"]))
        file.write(cleaned + "\n")

#write a txt file with locations of all tweets
output_file_path = "task3.txt"
with open(output_file_path, "w") as file:
    for text in db.asm.find():
        # if 'locality' in text["gnip"]['profileLocations'][0]['address']:
        if 'profileLocations' in text["gnip"]:
            if text["gnip"]['profileLocations'][0]['address']['country'].lower() == 'australia':
                if 'locality' in text["gnip"]['profileLocations'][0]['address']:   
                    file.write(text["gnip"]['profileLocations'][0]['address']['locality'] + "\n")
                else:
                    file.write("No city info"+ "\n")
            else:
                file.write("Other country"+ "\n")
        else:
            file.write('No location info'+ "\n")

#write a txt file with text and tweet ID from all the tweets
output_file_path = "task4.txt"
with open(output_file_path, "w") as file:
    for text in db.asm.find():
        id = text['id'].split(',')[-1]
        id = ''.join(id.split(':'))
        cleaned = " ".join(clean_text(text["body"]))
        file.write(id + ',' + cleaned + "\n")

#write a txt file with keywords from all the tweets
output_file_path = "task5.txt"
with open(output_file_path, "w") as file:
    for text in db.asm.find():
        cleaned = clean_text(text["body"])
        keywords = get_keywords(cleaned)
        csv_keywords= keywords_to_csv(keywords)
        file.write(csv_keywords + ' ')

