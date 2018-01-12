from nltk.corpus import stopwords

def jaccard_similarity_btw_tweets(tweet_a,tweet_b):
    #stop words in english
    stop_words = set(stopwords.words('english'))
    #list of words split by ' '
    word_a= tweet_a.split(' ')
    word_b = tweet_b.split(' ')
    #remove the stop words
    without_spt_a = []
    without_spt_b = []

    for word in word_a:
        if word not in stop_words:
            without_spt_a.append(word)
    for word in word_b:
        if word not in stop_words:
            without_spt_b.append(word)

    #find similar words in tweets_a and tweet_b
    similar_words = set()
    for word in without_spt_a:
        if word in without_spt_b:
            similar_words.add(word)

    #union of words in tweet_a and tweet_b
    union_of_words = list(set().union(without_spt_a,without_spt_b))

    #compute jaccard similarity
    js = float(len(similar_words)/len(union_of_words))
    return js

