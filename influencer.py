#maya
import pandas as pd
data = pd.read_csv('influencer.csv')
month = data['Month'].tolist()
views = data['Views'].tolist()
dislikes = data['Dislikes'].tolist()
subscriber = data['Subscriber(+-)'].tolist()
revenue = data['Revenue'].tolist()
filter = []

humble = data[data["Views"] <= 2000]
print("--- Humble Beginnings ---")
print(humble[["Month", "Views"]])

golden_age = data[data["Subscriber(+-)"] > 50000]
print("\n--- The Golden Age ---")
print(golden_age[["Month", "Subscriber(+-)"]])

scandal = data[data["Revenue"] == 0].head(2)
print("\n--- Scandal ---")
print(scandal[["Month", 'Revenue']])
