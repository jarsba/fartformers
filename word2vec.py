import gensim.downloader as api

wv = api.load('word2vec-google-news-300')


def find_punchline_words(word):
    print(wv.most_similar(positive=[word, "funny"], topn=100))


if __name__ == "__main__":
    find_punchline_words("athlete")
