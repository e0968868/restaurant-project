# Chen Si An Amber
# Technical Assessment Task 1 Q3
import json

# set local path
path = "/Users/Amber/Downloads/restaurant_data.json"

with open(path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# create list of ratings that need to be included, based on question requirements
required_ratings = ["Excellent", "Very Good", "Good", "Average", "Poor"]

# create empty list to append info
ratings_info = []

# iterate through each dictionary 
for d in data:
    restaurants_list = d.get("restaurants", [])
    for r in restaurants_list:
        aggregate_rating = r["restaurant"]["user_rating"].get("aggregate_rating", "")
        rating_text = r["restaurant"]["user_rating"].get("rating_text", "")
        if rating_text in required_ratings:
            # each tuple contains an aggregate and its corresponding text
            ratings_info.append((aggregate_rating, rating_text))

# only return tuples with the specified rating text
def check_rating_text(tuples, rating_text):
    t = []
    for x in tuples:
        if x[1] == rating_text:
            t.append(x)
    return t

# for each tuple for each rating text, find the minimum aggregate rating
def calculate_threshold(t):
    min_agg = None
    for x in t:
        agg = x[0]
        # find minimum aggregate for a particular rating
        if min_agg is None or agg < min_agg:
            min_agg = agg
    return min_agg

# calculate thresholds for each of the required ratings
thresholds = {}
for rating in required_ratings:
    t = check_rating_text(ratings_info, rating)
    thresholds[rating] = calculate_threshold(t)

# print thresholds for each of the required ratings
for rating, threshold in thresholds.items():
    print(f"{rating}: {threshold}")
