#maya
import pandas as pd
data = pd.read_csv('gamedev.csv')
level = data['Level'].tolist()
time = data['Time'].tolist()
rating = data['Rating'].tolist()
summary = data['Summary'].tolist()
feedback = data['Feedback'].tolist()
filter = []

def find_problems(level_rating):
    for i in range(len(rating)):
        if rating[i] < level_rating:
            filter.append(level[i])
    print(filter)
    filter.clear()

def high_time(level_time):
    for i in range(len(time)):
        if time[i] > level_time:
            if rating[i] > 4.5:
                filter.append(level[i])
    print(filter)
    filter.clear()

def find_secret():
    i = 0
    for item in feedback:
        if "secret" in item:
            print(data.loc[i])
        else:
            i = i + 1

high_time(787)
print(data.loc[79])
