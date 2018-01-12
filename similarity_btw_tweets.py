from nltk.corpus import stopwords
import codecs
import jaccard_similarity as js
import json

def similar_tweets(tweet_a):
    skip_count = 0
    with codecs.open('/Users/User/big_data/harvey_tweets_1000.csv', "r", encoding='utf-8', errors='ignore') as read_file:
        list_of_similar_tweets = {}
        for tweet in read_file:
            list_of_tweet_b = tweet.split(',')
            try:
                tweet_b = list_of_tweet_b[3]
                similarity = js.jaccard_similarity_btw_tweets(tweet_a,tweet_b)

                #Tweets that are 40 % or more similar
                if similarity >= 0.4:
                    if tweet_b not in list_of_similar_tweets:
                        list_of_similar_tweets[tweet_b] = similarity
            except:
                skip_count += 1
        del list_of_similar_tweets[tweet_a]
    #return a list of tweets similar to tweet_a
    return list_of_similar_tweets

read_line = 0
skip_line = 0
write_line = 0
stop_words = set(stopwords.words('english'))
write_file = open('/Users/User/big_data/similar_tweets.tsv','w+')

with codecs.open('/Users/User/big_data/harvey_tweets_1000.csv', "r",encoding='utf-8', errors='ignore') as read_file:
    for tweet in read_file:
        read_line += 1
        if read_line % 100 == 0:
            print ('lines read',read_line,'lines written',write_line,'lines skipped',skip_line)
        tweet_a_list = tweet.split(',')
        try:
            tweet_a = tweet_a_list[3]
            list_of_similar_tweets = similar_tweets(tweet_a)

        except:
            skip_line += 1
        if len(list_of_similar_tweets) > 0:
            for similar_tweet in list_of_similar_tweets:
                convert_to_percent = (list_of_similar_tweets[similar_tweet]) * 100
                write_file.write('\t'.join([tweet_a,similar_tweet,json.dumps(convert_to_percent)]) + '\n')
                write_line += 1








