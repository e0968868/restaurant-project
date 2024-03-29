# Chen Si An Amber
# Technical Assessment Task 1 Q1

import pandas as pd
import json 
import csv

# map country id to country name based on excel file
country_mapping = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zealand",
    162: "Phillipines",
    166: "Qatar",
    184: "Singapore",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "UAE",
    215: "United Kingdom",
    216: "United States"
}

# set local path
path = "/Users/Amber/Downloads/restaurant_data.json"

# tried to read json using pd.read_json but structure changed resulting in issue.
# hence, used json.load 
with open(path, 'r', encoding='utf-8') as json_file: 
    data = json.load(json_file)

# create empty list to append info
restaurant_info = []

# intiially obtained 20 restaurants only by iterating through only the first dictionary
# thus, added this line to iterate through every dictionary, after realizing there are multiple dictionaries in the main list
for d in data:  
    restaurants_list = d.get("restaurants", [])
    for r in restaurants_list:
        res_id = r["restaurant"]["R"].get("res_id", "")
        name = r["restaurant"].get("name", "") 
        city = r["restaurant"]["location"].get("city", "")
        user_rating_votes = r["restaurant"]["user_rating"].get("votes", "")
        user_aggregate_rating = r["restaurant"]["user_rating"].get("aggregate_rating", "")
        cuisines = r["restaurant"].get("cuisines", "")
        
        # map country id to country name using above defined function
        country_id = r["restaurant"]["location"].get("country_id", "")
        country_name = country_mapping.get(country_id, "")

        # append to restaurant_info empty list
        restaurant_info.append({
            "Restaurant ID": res_id,
            "Restaurant Name": name,
            "City": city,
            "User Rating Votes": user_rating_votes,
            "User Aggregate Rating": user_aggregate_rating,
            "Cuisines": cuisines,
            "Country": country_name
        })

# csv file name
csv = 'restaurants.csv'

# convert list to dataframe
df = pd.DataFrame(restaurant_info)
 
# convert dataframe to csv file
df.to_csv(csv)

# for debugging purpose; check if code has been run successfully
print(f'Data written')



