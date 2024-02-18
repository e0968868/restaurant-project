# restaurant-project

## Prerequisites

- Python version used: 3.10.6
- Required Python libraries: `json`, `csv `, `pandas`

## Getting Started

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/e0968868/restaurant-project.git

2. **Navigate to the project directory:**

   ```bash
   cd restaurant-project

2. **Run the script:**

   ```bash
   python q1.py
   python q2.py
   python q3.py

## Q1 Restaurant Information
This script extracts the following fields and store the data as restaurants.csv.
- Restaurant Id
- Restaurant Name
- Country
- City
- User Rating Votes
- User Aggregate Rating (in float)
- Cuisines


## Q2 Restaurant Events
This script extracts the list of restaurants that have past event in the month of April 2019 and stores the data as restaurant_events.csv.
Null values are populated as "NA".

- Event Id
- Restaurant Id
- Restaurant Name
- Photo URL
- Event Title
- Event Start Date
- Event End Date
  

## Q3 Restaurant Rating Thresholds
This script analyzes restaurant rating data and determines the minimum aggregate rating thresholds for specific rating texts. The calculated thresholds are then printed for the following ratings:

- Excellent
- Very Good
- Good
- Average
- Poor

