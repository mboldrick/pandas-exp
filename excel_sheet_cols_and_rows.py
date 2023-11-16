import pandas as pd

# Replace with the path to your Excel file
file_path = "sample.xlsx"


# Function to print details of each sheet
def print_sheet_details(file_path):
    # Read the Excel file
    excel_file = pd.ExcelFile(file_path)

    # Iterate over each sheet
    for sheet in excel_file.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet)

        # Get the number of rows and columns
        num_rows, num_cols = df.shape

        # Get the column names
        column_names = df.columns.tolist()

        # Print the details
        print(f"Sheet: {sheet}")
        print(f"Number of Rows: {num_rows}")
        print(f"Number of Columns: {num_cols}")
        print(f"Column Names: {column_names}")
        print()


# Call the function
print_sheet_details(file_path)
