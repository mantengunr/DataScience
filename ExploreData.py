import numpy as np
import pandas as pd

# Loading data
df_listings = pd.read_csv('listings.csv')
df_calendar = pd.read_csv('calendar.csv')
df_reviews = pd.read_csv('reviews.csv')

# Data preview
print(df_listings.head())
print(df_calendar.head())
print(df_reviews.head())

# Eploring reviews data
# ---------------------
# Q1: Check if there are two identical names in the 'reviewer_name' column
duplicates = df_reviews.duplicated(subset=['reviewer_name', 'reviewer_id']).any()

if duplicates:
    print("There are two identical names in the column.")
else:
    print("There are no two identical names in the column.")
    
# Exploring listings data
# -----------------------
# Q2: Waht is the statistical representation of t listings data intems of cleanliness review scores

# Q2.1: What is the total number of listings
total_listings = df_listings.shape[0] 
print("The total number of listings is", total_listings)

# Q2.2: What is the number of listings without cleanliness review scores
nan_count = df_listings['review_scores_cleanliness'].isna().sum() 
print("The number of listings with missing values for cleanliness review scores",nan_count)

# Q2.3: What is the average cleanliness review score
sum_without_nan = df_listings['review_scores_cleanliness'].notna().sum()
totalScores = df_listings['review_scores_cleanliness'].dropna().sum()

average_score = totalScores/sum_without_nan
print("The average scoring valeu for listings",average_score)

# Exploring calendar data
# -----------------------

# Checking the availabity
counts = df_calendar['available'].value_counts()

t_count = counts['t']

avilability = (t_count/df_calendar.shape[0])*100
print(f"Availability: {avilability}%")

