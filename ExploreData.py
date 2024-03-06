import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading data
df_listings = pd.read_csv('listings.csv')
df_calendar = pd.read_csv('calendar.csv')
df_reviews = pd.read_csv('reviews.csv')

# Eploring listings data
# ---------------------
print(df_listings.head()) # Getting a glimpse of the data

# Q1: What is the top 10 neighborhoods with the highest number of listings?
neighborhood_counts = df_listings['host_neighbourhood'].value_counts() # Group the data by neighborhood and count the number of listings in each neighborhood 

df = neighborhood_counts.to_frame()
df = df.rename(columns={'host_neighbourhood': 'Number of Listings'})
df = df.reset_index().rename(columns={'index': 'Host Neighbourhood'})

# Showing the 10 neighborhoods with the highest number of listings 
fig, ax = plt.subplots()
ax.axis('off')
ax.table(cellText=df.head(10).values, colLabels=df.columns, loc='center', cellLoc='center')
plt.show() 

# Q2: What is the average price per neighborhoods?
df  = df_listings
df['price'] = df['price'].str.replace('$', '')
df['price'] = df['price'].str.replace(',', '').astype(float)  # Replace the dollar sign in a specific column
neighborhood_prices = round(df.groupby('host_neighbourhood')['price'].mean(), 1) # Group the data by neighborhood and calculate the average price for each neighborhood
sorted_neighborhoods = neighborhood_prices.sort_values(ascending=False) # Sort the neighborhoods by average price in descending order

sorted_neighborhoods = sorted_neighborhoods.to_frame()
sorted_neighborhoods = sorted_neighborhoods.rename(columns={'price': 'Avarage Price($)'})
sorted_neighborhoods = sorted_neighborhoods.reset_index().rename(columns={'index': 'Host Neighbourhood'})

# Showing the top 10 most expensive neighborhoods of average
fig, ax = plt.subplots()
ax.axis('off')
ax.table(cellText=sorted_neighborhoods.head(10).values, colLabels=sorted_neighborhoods.columns, loc='center', cellLoc='center')
plt.show() 

# Eploring reviews data
# ---------------------
# Q1: Are there any reviewers with more than one review?
print(df_reviews.head()) #  Getting a glimpse of the data
print(df_reviews.info()) # Getting information about the columns, data types, and missing values

duplicates = df_reviews.duplicated(subset=['reviewer_name', 'reviewer_id']).sum() # Clculating the sum of duplicates per reviewer
print("Number of reviews is", df_reviews.shape[0],"and the number of reviewers with more that one review is", duplicates,". Based on reviews, this means that",(duplicates/df_reviews.shape[0])*100,"percent of people use Seattle Airbnb more than once.")
    
# Exploring calendar data
# -----------------------
# Q1: What is the price trends of time?
print(df_calendar.head()) # Getting a glimpse of the data
print(df_calendar.info()) # Getting information about the columns, data types, and missing values

df = df_calendar
df.dropna(subset=['price'], inplace=True) # Removing NaNs

df['date'] = pd.to_datetime(df['date']) # Coverting date to datetime
df['price'] = df['price'].str.replace('$', '').str.replace(',', '').astype(float) # Removing '$' and ',' so we can convert to float

# Plotting price trends of time
sns.lineplot(x='date', y='price', data=df)
plt.title('Price Trends over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


