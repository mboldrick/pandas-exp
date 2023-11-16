import pandas as pd

# Path to your Excel file
file_path = "sample.xlsx"

# Create an ExcelFile object
excel_file = pd.ExcelFile(file_path)

# List all sheet names
sheet_names = excel_file.sheet_names

print(sheet_names)
