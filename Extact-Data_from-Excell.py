import pandas as pd

# Path to the original Excel file
input_file_path = 'Sample.xlsx'
# Path to the Excel file to save the phone numbers
output_file_path = 'Sample1.xlsx'

# Read data from the Excel file
df = pd.read_excel(input_file_path)

# Drop rows where the 'Telephone number' column is empty
df.dropna(subset=['Telephone number'], inplace=True)

# Extract the 'Telephone number' column and store it in a new dataframe
phone_numbers = df['Telephone number']

# Create a new dataframe to store the phone numbers
phone_numbers_df = pd.DataFrame(phone_numbers, columns=['Telephone number'])

# Save the phone numbers column to a new Excel file
phone_numbers_df.to_excel(output_file_path, index=False)
