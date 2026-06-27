import pandas as pd
import argparse
import logging
import os

# -------------------------
# Logging Configuration
# -------------------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_data(df):
    """
    Clean and normalize the dataframe.
    """

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Rename columns (example)
    rename_columns = {
        "Name": "Employee_Name",
        "DOB": "Date_of_Birth"
    }

    df.rename(columns=rename_columns, inplace=True)

    # Fill missing values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")
        else:
            df[column] = df[column].fillna(0)

    # Convert date columns
    if "Date_of_Birth" in df.columns:
        df["Date_of_Birth"] = pd.to_datetime(
            df["Date_of_Birth"],
            errors="coerce"
        )

    return df


def csv_to_excel(input_file, output_file):
    try:

        # Check if file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"{input_file} not found.")

        # Read CSV
        df = pd.read_csv(input_file)

        logging.info("CSV loaded successfully.")

        # Clean data
        df = clean_data(df)

        # Save to Excel
        df.to_excel(output_file, index=False)

        logging.info("Excel file created successfully.")

        print(f"\nSuccessfully converted:")
        print(f"{input_file} --> {output_file}")

    except FileNotFoundError as e:
        logging.error(e)
        print("Error:", e)

    except pd.errors.EmptyDataError:
        logging.error("CSV file is empty.")
        print("Error: CSV file is empty.")

    except Exception as e:
        logging.exception(e)
        print("Unexpected Error:", e)


def main():
    parser = argparse.ArgumentParser(
        description="CSV to Excel Converter"
    )

    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Input CSV File"
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output Excel File"
    )

    args = parser.parse_args()

    csv_to_excel(args.input, args.output)


if __name__ == "__main__":
    main()