# Analysis_of_Hurricane_Harvey_Tweets

Dataset Description: The dataset contains 1000 tweets from from twitter about Har- vey.
Dataset Source: The dataset was taken from https://www.kaggle.com/datasets Methodology used: In order to find the similar tweets, Jaccard similarity is used. Jaccard Similarity: Let S and T be two sets.
The Jaccard similarity of sets S and T is defined as (|ST|)/(|ST|), i.e., the ratio of the size of the intersection of S and T to the size of their union.

Identify Donation Related Tweets

numerical_data - converts tweets to numbers
tag_tweets - tags tweets as volunteer(all donation related tweets), news, climate change and neutral
knn_donation_tweets - classifies tweets using knn
tweets_knn.tsv - contains all the classified tweets
donation_tweets_knn - contains all volunteer(donation) related tweets that was classified by knn
Harvey_tweets_1000.tsv - input dataset

Identify the frequent itemset

Here is a small description about the important functions used,
load_input_file: Returns list of tweets removing the stop words and returns the set of words used in the entire file
subset_with_length: returns the subset of the set with specific length
subset: returns all the subset of the set
occurrence_of_subset: returns the occurrence count of each subset in the list of tweets
frequent_itemset: returns the frequent item set (in this case, it return the frequent words used)
find_associativity_rules: finds the associativity rules for frequent item set

Identify similar tweets

Dataset Description: The dataset contains 1000 tweets from from twitter about Har- vey.
Dataset Source: The dataset was taken from https://www.kaggle.com/datasets Methodology used: In order to find the similar tweets, Jaccard similarity is used. Jaccard Similarity: Let S and T be two sets.
The Jaccard similarity of sets S and T is defined as (|ST|)/(|ST|), i.e., the ratio of the size of the intersection of S and T to the size of their union.
Result: The result file is in the form of a tab separated (.tsv) file. The tweets in the file are minimum of 40% similar (>= 40%). Also contains the percentage similarity between tweets.

