import pandas as pd

# Replace with the path to your Excel file
file_path = "data/BS Jobs cropped.xlsx"


def process_dates_and_job_no(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Convert 'job_no' to string and pad with zeros to make it of length 4
    df["job_no"] = df["job_no"].astype(str).str.zfill(4)

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

    # Apply the conversion function to the 'date' column
    df["date"] = df["date"].apply(convert_date)

    # Print the 'job_no' and 'date' columns
    print(df[["job_no", "date"]])

    # TODO: Append 0s to job numbers that have non-numeric suffixes but
    # numeric portions that are less than 4 digits long. For example, 105A.


# Execute the function
process_dates_and_job_no(file_path)
