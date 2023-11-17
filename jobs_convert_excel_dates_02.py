import pandas as pd
from dateutil import parser


def custom_date_parser(date_str):
    try:
        # Parse the date string and ignore timezone information
        dt = parser.parse(date_str, ignoretz=True)
        return dt.strftime("%Y-%m-%d")
    except Exception as e:
        # Handle exceptions (you might want to log these or handle them differently)
        return None


# Replace with the path to your Excel file
file_path = "data/BS Jobs cropped.xlsx"


def process_dates_and_job_no(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Convert 'job_no' to string and pad with zeros to make it of length 4
    df["job_no"] = df["job_no"].astype(str).str.zfill(4)

    # Apply the custom date parser to the 'date' column
    df["date"] = df["date"].apply(custom_date_parser)

    # Print the 'job_no' and 'date' columns
    print(df[["job_no", "date"]])


# Execute the function
process_dates_and_job_no(file_path)
