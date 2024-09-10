import pandas as pd

# Create a simple DataFrame with some data
data = {
    'Name': ['John', 'Oliver', 'Emily', 'Sophia', 'Jack'],
    'Age': [28, 32, 25, 35, 30],
    'City': ['Sydney', 'Brisbane', 'Melbourne', 'Adelaide', 'Perth'],
    'Score': [85, 92, 88, 79, 95]
}

df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Calculate the average score
average_score = df['Score'].mean()
print("\nAverage Score:", average_score)

# Filter the DataFrame for people older than 30
filtered_df = df[df['Age'] > 30]
print("\nPeople older than 30:")
print(filtered_df)

# Add a new column 'Passed' based on the Score
df['Passed'] = df['Score'] > 80
print("\nDataFrame with 'Passed' column:")
print(df)

# Group by 'City' and get the average score per city
grouped_df = df.groupby('City')['Score'].mean()
print("\nAverage Score per City:")
print(grouped_df)

