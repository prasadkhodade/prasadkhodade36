import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("student.csv")

# Display first five records
print("First five records:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Calculate average, maximum and minimum marks
print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# Identify students scoring more than 75 marks
print("\nStudents scoring more than 75 marks:")
print(df[df["Marks"] > 75])

# Bar chart of student marks
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"], color="skyblue")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram of marks distribution
plt.hist(df["Marks"], bins=5, color="lightgreen",
         edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")
plt.show()

# Scatter plot of study hours and marks
plt.scatter(df["Study_Hours"], df["Marks"], color="red")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid(True)
plt.show()