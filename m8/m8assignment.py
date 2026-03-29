"""
This script analyzes air quality data from a CSV file using pandas.
The analysis finds which New York
locations have the highest average air pollution.
"""

import pandas
import matplotlib.pyplot as plt
# read csv file
aq = pandas.read_csv('m8/Air_Quality.csv')

# ------------------------------------------------------------------------------------------
# ANALYSIS QUESTION - Which New York locations have the highest average air pollution?
# ------------------------------------------------------------------------------------------

# remove empty Message column since it's only values are NaN
aq = aq.drop(columns=["Message"])

# fix date format because the csv file has it stored as text instead of as datetime 
aq["Start_Date"] = pandas.to_datetime(aq["Start_Date"])

# drop any duplicates that may exist in the csv file
aq = aq.drop_duplicates()

# for each location calculate the average air pollution and then sort by highest amount
avg_pollution_by_location = (
    aq.groupby("Geo Place Name")["Data Value"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

# returns locations where the level of pollution (data value) is greater than 50
most_polluted = aq[aq["Data Value"] > 50]

print("Most polluted areas: ", most_polluted['Geo Place Name'])
# summary statistics - get the mean and max 
mean = aq["Data Value"].mean().round(2)
max = aq["Data Value"].max().round(2)

print("Mean: ", mean)
print("Max: ", max)

# this bar chart shows the top 10 New York locations with the highest average air pollution
avg_pollution_by_location.head(10).plot(kind="bar")
plt.title("Top 10 Locations by Average Air Pollution")
plt.xlabel("Location")
plt.ylabel("Average Air Pollution")
plt.xticks(rotation=45)
plt.show()

# this histogram shows how air quality values are distributed across the Bayside/Little Neck area so we can see how often different pollution levels occur 
location_data = aq[
    (aq["Geo Place Name"] == "Bayside - Little Neck") |
    (aq["Geo Place Name"] == "Bayside and Little Neck (CD11)") |
    (aq["Geo Place Name"] == "Bayside Little Neck-Fresh Meadows")
]

location_data["Data Value"].plot(kind="hist", bins=20)
plt.title("Air Quality Distribution in Bayside - Little Neck")
plt.xlabel("Air Quality")
plt.ylabel("Frequency")
plt.show()