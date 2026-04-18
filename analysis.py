import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')
#import matplotlib for data visualization(pie chart)
# Load the data
df = pd.read_csv("customer_data.csv")
# Show first few rows
print("Preview of Data:")
print(df.head())

# Total calls handled
print("\nTotal Calls:", df["Calls_Handled"].sum())

# Average resolution time
print("Average Resolution Time:", df["Avg_Resolution_Time"].mean())

# Average CSAT score
print("Average CSAT:", df["CSAT"].mean())

# Most common issue
print("\nMost Common Issue:")
print(df["Issue_Type"].value_counts())
# pie chart
issue_counts = df["Issue_Type"].value_counts()
plt.figure()
plt.pie(issue_counts, labels=issue_counts.index, autopct='%1.1f%%')
plt.title("Issue Type Distribution")
plt.show()
