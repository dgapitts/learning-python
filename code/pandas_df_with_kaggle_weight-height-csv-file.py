import pandas as pd

# Define the path to the CSV file
file_path = '../kaggle/weight-height.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Convert the DataFrame to a dictionary with records orientation
data = df.to_dict(orient='records')

# Display the dictionary
print(data)
