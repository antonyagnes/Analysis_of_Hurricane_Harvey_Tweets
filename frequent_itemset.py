import itertools
import operator
from nltk.corpus import stopwords

def load_input(filename):
    stop_words = set(stopwords.words('english'))
    list_of_tweets = []
    set_of_words = {}
    with open(filename) as donation_tweets:
        for line in donation_tweets:
            fields = line.lower().strip('\n').strip('"').split('\t')
            list_of_words = fields[2].split(' ')
            without_stop_words = []
            for words in set(list_of_words):
                if words != '' or words != "":
                    if words not in stop_words:
                        if words not in set_of_words:
                            set_of_words[words] = 0
                        set_of_words[words] += 1
                        without_stop_words.append(words)
            list_of_tweets.append(list(set(without_stop_words)))
            without_stop_words = []
    return list_of_tweets,set_of_words

def subset_with_length(input_set,length):
    list_of_subsets = (list(itertools.combinations(input_set, length)))
    return list_of_subsets

def subset_count(new_dict,prev_dict):
    new_list = []
    for word in new_dict:
        length = len(word)
        for i in range(0,length):
            if word[i] not in new_list:
                new_list.append(word[i])
    subsets = subsets_of_set(new_list)
    for word in prev_dict:
        list_of_words = []
        length = len(word)
        for i in range(0,length):
            list_of_words.append(word[i])
        if list_of_words in subsets:
            new_dict[word] = prev_dict[word]
    return new_dict

def subsets_of_set(input_set):
    if input_set == []:
        return [[]]
    x = subsets_of_set(input_set[1:])
    return x + [[input_set[0]] + y for y in x]

def occuence_of_subsets(subset_with_specific_length,i,length,list_of_tweets):
    dict_of_subset = {}
    for subset in subset_with_specific_length:
        dict_of_subset[tuple(subset)] = 0
        for tweet in list_of_tweets:
            list_of_tweet_subsets = sorted(subset_with_length(tweet, i))
            sorted_list_of_tweet_subsets = []
            for tweet_subset in list_of_tweet_subsets:
                sorted_list_of_tweet_subsets.append(sorted(tweet_subset))
            if subset in sorted_list_of_tweet_subsets:
                dict_of_subset[tuple(subset)] += 1
        if dict_of_subset[tuple(subset)] / length < support:
            dict_of_subset.pop(tuple(subset))
    return dict_of_subset

def frequent_itemset(list_of_tweets,set_of_words,support):
    count = 0
    frequent_items = set()
    result = {}
    previous_result = {}
    for word in set_of_words:
        if set_of_words[word] / len(list_of_tweets) >= support:
            frequent_items.add(word)
    length_of_frequent_items = len(frequent_items)
    for i in range(1,length_of_frequent_items+1):
        list_of_subsets = []
        frequent_itmes_list = list(frequent_items)
        subset_with_specific_length = (subset_with_length(frequent_itmes_list, i))
        sorted_subset_list = []
        for each_subset in subset_with_specific_length:
            sorted_subset_list.append(sorted(each_subset))
        occ = occuence_of_subsets(sorted_subset_list, i, len(list_of_tweets), list_of_tweets)
        count += 1
        if count == 1:
            previous_result = occ
        else:
            if len(occ) > 0:
                new_dict = subset_count(occ, previous_result)
                previous_result = new_dict
    return previous_result

def rules_with_len_1(new_list,s):
    temp_list = []
    sub = str(s).strip('[').strip(']').strip("'")
    for i in new_list:
        if i != sub:
            temp_list.append(i)
    return temp_list

def rules(new_list,s):
    temp_list = []
    for i in new_list:
        if i not in s:
            temp_list.append(i)
    return temp_list

def find_associativity_rules(input_dict):
    new_list = []
    associativity_rule =[]
    for word in input_dict:
        if word not in new_list:
            new_list.append(word)
    subsets = subsets_of_set(new_list)
    for s in subsets:
        if len(s) == 1:
            rule = rules_with_len_1(new_list,s)
            associativity_rule.append((str(s)+'-->'+str(rule)))
        if len(s) >1 and len(s) < len(new_list):
            rule = rules(new_list, s)
            associativity_rule.append((str(s) + '-->' + str(rule)))
    return associativity_rule

def max_itemset_length(freq_item_set):
    maximum = 0
    for item_set in freq_item_set:
        if len(item_set) > maximum:
            maximum = len(item_set)
    return maximum

filename = '/Users/User/big_data/donation_tweets_knn.tsv'
load_input_opt = load_input(filename)
support = 0.3
list_of_tweets = load_input_opt[0]
set_of_words = load_input_opt[1]
higher_frequency = {}
for word in set_of_words:
    if set_of_words[word] > 100:
        higher_frequency[word] = set_of_words[word]/1523
freq_item_set = frequent_itemset(list_of_tweets,set_of_words,support)
print(freq_item_set)
maximum = max_itemset_length(freq_item_set)
frequent = []
for item_set in freq_item_set:
    if len(item_set) == maximum:
        frequent.append(item_set)
print('frequent item set: ',frequent)
associative_rules= []
for item in frequent:
    associative_rules.append(find_associativity_rules(item))
print('associative_rules: ',associative_rules)




