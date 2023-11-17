import pandas as pd


# Function to print details of each sheet in a tabular format
def print_sheet_details_in_table(file_path):
    # Read the Excel file
    excel_file = pd.ExcelFile(file_path)

    # Prepare a list to store the results
    results = []

    # Iterate over each sheet
    for sheet in excel_file.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet)

        # Get the number of rows and columns
        num_rows, num_cols = df.shape
        print(num_rows, num_cols)

        # Get the column names as a comma-separated string
        column_names = ", ".join(df.columns)

        # Append the details to the results list
        results.append([sheet, num_rows, num_cols, column_names])

    # Convert results to a DataFrame for tabular display
    result_df = pd.DataFrame(
        results,
        columns=["Sheet Name", "No. of Rows", "No. of Columns", "Column Headers"],
    )

    # Print the result
    print(result_df)


# Replace 'file_path' with the path to your Excel file
# Example usage:
# print_sheet_details_in_table("sample.xlsx")
print_sheet_details_in_table("data/BS Jobs.xlsx")
