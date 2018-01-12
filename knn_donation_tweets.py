
import csv
import operator
import random
import math
import matplotlib.pyplot as plt

def split_data_train_test(filename,split,training_set,test_set):
    read_line = 0
    with open(filename) as tagged_tweets:
        for line in tagged_tweets:
            read_line += 1
            numerical_fields = line.strip('\t').strip('\n').split('\t')
            for x in range(0,4):
                numerical_fields[x] = float(numerical_fields[x].strip('\t'))
            if random.random() < split:
                training_set.append(numerical_fields)
            else:
                test_set.append(numerical_fields)
    return training_set,test_set

def calculate_euclidean_dist(a,b,length):
    distance = 0
    for x in range(0,length):
        distance += pow((a[x]-b[x]),2)
    return math.sqrt(distance)

def fetch_neighbours(test_item,training_set,k):
    distance  =[]
    for x in range(0,len(training_set)):
        euclidean_distance = calculate_euclidean_dist(test_item,training_set[x],len(test_item)-2)
        distance.append((training_set[x],euclidean_distance))
    distance.sort(key=operator.itemgetter(1))
    neighbours =[]
    for x in range(0,k):
        neighbours.append(distance[x][0])
    return neighbours

def get_response(neighbours):
    class_votes = {}
    for x in range(0,len(neighbours)):
        response = neighbours[x][-1]
        if response in class_votes:
            class_votes [response] += 1
        else:
            class_votes[response] = 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]

def get_accuracy(actual,prediction):
    correct = 0
    wrong = 0
    for x in range(0,len(actual)):
        if actual[x] is prediction[x]:
            correct += 1
        else:
            wrong += 1
    return (correct/float(len(actual)))

def calculate_recall_precision_fmeasure(predicted,actual):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for x in range(0, len(predicted)):
        if predicted[x] == 1 and actual[x] == 1:
            TP += 1
        if predicted[x] == 0 and actual[x] == 0:
            TN += 1
        if predicted[x] == 1 or actual == 0:
            FP += 1
        if predicted[x] == 0 and actual[x] == 1:
            FN += 1
    precision = float(TP/(TP+FP))
    recall = float(TP/(TP+FN))
    f_measure = float((2*TP)/((2*TP)+FN+FP))
    print (TP,TN,FP,FN)
    return precision,recall,f_measure

write_file = open('/Users/User/big_data/rescue_tweets_knn.tsv','w')
writer = csv.writer(write_file,delimiter = '\t')
filename = '/Users/User/big_data/tagged_tweets.tsv'
training_set =[]
test_set =[]
split =0.65
train_test_data = split_data_train_test(filename,split,training_set,test_set)
training_set = train_test_data[0]
test_set = train_test_data[1]
print ('training set',len(training_set),'testing set',len(test_set))
prediction = []
actual =[]
k = 2
voluntering = 0
news = 0
neutral = 0
climate = 0
accuracy = []
recall = []
precision = []
f_measure = []

for x in range(0,len(test_set)):
    if x%1000 == 0:
        print ('testing set --->',x,'volunteering',voluntering,'news',news,'neutral',neutral,'climate',climate)
    neighbour = fetch_neighbours(test_set[x],training_set,k)
    result = get_response(neighbour)
    if result == 'volunteer':
        prediction.append(1)
    else:
        prediction.append(0)
    if test_set[x][-1] == 'volunteer':
        actual.append(1)
    else:
        actual.append(0)
    writer.writerow([result] + [test_set[x][-1]] + [test_set[x][-2]])
    if result == 'volunteer':

        voluntering +=1
    if result == 'neutral':
        neutral += 1
    if result == 'news':
        news+=1
    if result == 'climate change':
        climate +=1
r_p_f = calculate_recall_precision_fmeasure(prediction,actual)
print ('accuracy',get_accuracy(actual,prediction),'recall',r_p_f[1],'precision',r_p_f[0],'f_measure',r_p_f[2])