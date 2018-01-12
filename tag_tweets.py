
import csv
write_file =  open('/Users/User/big_data/tagged_tweets.tsv','w')
writer = csv.writer(write_file, delimiter = '\t')
read_line = 0
voluntering = 0
news = 0
neutral = 0
climate = 0
with open('/Users/User/big_data/Harvey_numerical_data.tsv') as numerical_tweet:
    for line in numerical_tweet:
        read_line += 1
        if read_line% 1000 == 0:
            print('lines read',read_line)
        fields = line.strip('\n').split(',')
        numerical = []
        for i in fields:
            numerical.append(i.strip('[').strip(']'))
        max = 0
        index = 2
        for i in range(0, 4):
            if float(fields[i]) > max:
                max = float(fields[i])
                index = i
        if index == 0:

            numerical.append('volunteer')
            writer.writerow(numerical)
            voluntering += 1
        if index == 1:

            numerical.append('news')
            writer.writerow(numerical)
            news += 1
        if index == 2:

            numerical.append('neutral')
            writer.writerow(numerical)
            neutral += 1
        if index == 3:

            numerical.append('climate change')
            writer.writerow(numerical)
            climate += 1
    print('volunteer',voluntering,'news', news, 'neutral', neutral, 'climate', climate)