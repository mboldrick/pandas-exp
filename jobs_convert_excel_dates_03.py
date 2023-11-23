import pandas as pd
import re

# Replace with the path to your Excel file
input_file = "data/BS Jobs.xlsx"
output_file = "data/BS Jobs processed.xlsx"


# Function to pad job numbers with zeros to make them 4 digits long
def pad_job_no(job_no):
    # Split the job_no into numeric and non-numeric parts
    match = re.match(r"(\d+)(\D*)", str(job_no))
    if match:
        # Extract numeric and non-numeric parts
        numeric_part, non_numeric_part = match.groups()

        # Pad the numeric part with zeros to make it 4 digits
        numeric_part = numeric_part.zfill(4)

        # Combine the parts back together
        return numeric_part + non_numeric_part
    else:
        # Return the original job_no if no numeric part is found
        return job_no


# Function to convert date to YYYY-MM-DD format
def convert_date(date):
    try:
        # If the date is already in the correct format, return as is
        if isinstance(date, str) and len(date) == 10:
            return date
        # Otherwise, parse the date and format it
        return pd.to_datetime(date).strftime("%Y-%m-%d")
    except:
        # In case of any parsing error, return None or a default value
        return None


def process_data(input_file):
    # Read the Excel file into a DataFrame
    # TODO - set po_no as string so that leading zeros are not removed,
    # the column is not treated as numeric, and the cell alignment is consistent
    df = pd.read_excel(input_file)

    # Apply the padding function to the 'job_no' column
    df["job_num"] = df["job_no"].apply(pad_job_no)

    # Apply the conversion function to the 'date' column
    df["start_date"] = df["date"].apply(convert_date)

    # Print the 'job_no' and 'date' columns
    print(df[["job_no", "date"]])

    # Export the DataFrame to an Excel file
    df.to_excel(output_file, index=False)


# Execute the function
process_data(input_file)
