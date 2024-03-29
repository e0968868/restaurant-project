#Chen Si An Amber
#Technical Assessment Task 1 Q2

import pandas as pd
import json

# set local path
path = "/Users/Amber/Downloads/restaurant_data.json"

# tried to read json using pd.read_json but structure changed resulting in issue.
# hence, used json.load 
with open(path, 'r', encoding='utf-8') as json_file: 
    data = json.load(json_file)

# function to check if event occurs in Apr 2019
def april(start_date, end_date):
    start_month, start_year = int(start_date[5:7]), int(start_date[:4])
    end_month, end_year = int(end_date[5:7]), int(end_date[:4])
    return start_month == 4 and end_month == 4 and end_year == 2019

# create empty list to store the events
restaurant_events = []

# iterate through each dictionary of restaurant lists in the overall list
for d in data: 
    restaurants_list = d.get("restaurants", [])
    
    # iterate through each restaurant in the restaurant list in each dictionary
    for r in restaurants_list:
        events_list = r["restaurant"].get("zomato_events", [])

        # iterate through each event in the event list in each restaurant list
        for event in events_list:
            event_data = event["event"]
            
            # use above defined function to ensure event is Apr 2019
            if april(event_data["start_date"], event_data["end_date"]):
                
                # append info to restaurant_events list
                # populate null values with "NA"
                restaurant_events.append({
                    "Event Id": event_data["event_id"],
                    "Restaurant Id": r["restaurant"]["R"].get("res_id", "NA"),
                    "Restaurant Name": r["restaurant"].get("name", "NA"),

                    # initially obtained IndexError: list index out of range
                    # so must also handle cases where "photos" key not present
                    "Photo URL": event_data["photos"][0]["photo"]["url"] if event_data["photos"] else "NA",
                    "Event Title": event_data["title"], 

                    # use friendly dates for easier readability; e.g. 06 March instead of 2019-03-06
                    "Event Start Date": event_data["friendly_start_date"],
                    "Event End Date": event_data["friendly_end_date"]
                })

# csv file name
csv = 'restaurant_events.csv'

# convert list to dataframe
df = pd.DataFrame(restaurant_events)
 
# convert dataframe to csv file
df.to_csv(csv)

# for debugging purpose; check if code has been run successfully
print(f'Data written')
