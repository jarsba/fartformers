import nltk

nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.corpus import wordnet

from string import printable
from PyDictionary import PyDictionary

en_stops = set(stopwords.words('english'))
dictionary = PyDictionary()


def remove_stopwords(text):
    words = text.split(" ")
    text_without_stopwords = []
    for word in words:
        if word not in en_stops:
            text_without_stopwords.append(word)

    return text_without_stopwords


def preprocess_tweets(tweets):
    for tweet in tweets:
        tweet = tweet.lower()
        tweet = ''.join(filter(lambda x: x in printable, tweet))
        word_list = remove_stopwords(tweet)
        print(word_list)


def generate_meanings(word):
    syns = wordnet.synsets(word)
    definitions = []
    for syn in syns:
        definitions.append(syn.definition())

    return definitions


def generate_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    return synonyms


def generate_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return antonyms


if __name__ == "__main__":
    sentences = [
        "What a boring long weekend.",
        "Expert photographers caught these athletes off guard and in the heat of the competition and the results are priceless.",
        "The most disrespectful thing you can do is sit next to me and light a cigarette.",
        "Just did a hike, nature is great for the soul.",
        "WHERE IS MY FUCKING SOCK IM ALWAYS MISSING ONE SOCK.",
        "And if Winston Churchill had been caught getting double helpings of beef at dinner he'd probably have had to resign.",
        "Can trust wallet secret code be recovered?",
        "Better to avoid the poison altogether than to try to heal from the damage it causes.",
        "Chicken used to be a delicacy in America that only rich people could afford.",
        "Is he about to look back on this frame in anger?",
        "One definitely needs Captain America's shield when frying.",
        "Starving but refuse to start moving around before this alarm goes off.",
        "Friendships is where you can mess around and play fight and tease each other and being an idiot together yet still enjoy everything together."
    ]
    preprocess_tweets(sentences)
