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

#Task 0
# return list of words without stopwords
def remove_stopwords(words):
    list = word_tokenize(words) # tokenize the text
    for i in list: # remove if the words is stopwords
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
    text = re.sub(r"[^\w]"," ", text)
    text = re.sub(" \d+", " ", text)
    words = remove_stopwords(text)
    words = stem_words(words)
    return words

#Task 1.1

# Initialize Rake object
rake_nltk_var = Rake()

# Extract keywords
def get_keywords(cleaned):
    rake_nltk_var.extract_keywords_from_text(','.join(cleaned))

# Get ranked phrases (keywords)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    return keyword_extracted

# Create name/value pair in comma seperate value
def keywords_to_csv(keywords):
    csv_keywords =''
    n = 1
    for i in keywords:
        csv_keywords = csv_keywords + str(n) + ',' + i + '\n'
        n += 1
    return csv_keywords


#Task 1.2
# find name entity
def find_name_entity(cleaned):
    entity = nltk.pos_tag(cleaned)
    return entity

def entity_to_csv(entity):
    csv_entity =''
    for i in entity:
        pair = ','.join(i)
        csv_entity = csv_entity + pair + '\n'
    return csv_entity

#Task 1.3
# extract topics
def extract_topic(cleaned):
    dictionary = corpora.Dictionary([cleaned])
    corpus = [dictionary.doc2bow(doc) for doc in [cleaned]]
# Build LDA model
    lda_model = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1)
# Get topics list
    topics = lda_model.get_topic_terms(topicid=0, topn=10)
    topic_list = []
    for word_id, prob in topics:
        topic = [dictionary[word_id], prob]
        topic_list.append(topic)      
    return topic_list

# Create name/value pair in comma seperate value
def topic_to_csv(topic_list):
    csv_topics = "" 
    for i in topic_list:
        csv_topics = csv_topics + i[0] + "," + str(i[1]) +"\n"
    return csv_topics

# Task 1.4
# extract sentiment
def extract_sentiment(text):
# create a SentimentIntensityAnalyzer object
    sid = SentimentIntensityAnalyzer()
# analyze the sentiment of the text
    scores = sid.polarity_scores(text)
    del scores['compound']
    sentiment = [max(scores, key = scores.get),max(scores.values())]
    return sentiment

# Create name/value pair in comma seperate value
def sentiment_to_csv(sentiment):
    csv_sentiment = sentiment[0] + "," + str(sentiment[1])
    return csv_sentiment


#Making database connection
client = MongoClient('localhost',27017)
db= client.Practical4
# Update the original tweet with:
for text in db.asm.find(): 
    cleaned = clean_text(text["body"])
#keywords
    keywords = get_keywords(cleaned)
    csv_keywords= keywords_to_csv(keywords)
    db.asm.update_many({"actor.id": text['actor']['id']},{'$set':{'keyword': csv_keywords}})
#entity
    entity = find_name_entity(cleaned)
    csv_entity = entity_to_csv(entity)
    db.asm.update_many({"actor.id": text['actor']['id']},{'$set':{'entity': csv_entity}})
#topics
    if cleaned != []:
        topics = extract_topic(keywords)
        csv_topics = topic_to_csv(topics)
        db.asm.update_many({"actor.id": text['actor']['id']},{'$set':{'topics': csv_topics}})
#sentiment
    sentiment = extract_sentiment(" ".join(cleaned))
    csv_sentiment = sentiment_to_csv(sentiment)
    db.asm.update_many({"actor.id": text['actor']['id']},{'$set':{'sentiment': csv_sentiment}})
