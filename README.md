# CSV → Excel Converter

A Python automation tool that reads CSV files, cleans and normalizes the data, and converts them into Excel (`.xlsx`) format. The project includes data preprocessing, command-line interface (CLI) support, logging, and error handling, making it useful for data preparation and reporting workflows.

---

## Features

* Convert CSV files to Excel (`.xlsx`)
* Clean and normalize input data
* Handle missing values automatically
* Parse date columns into proper date format
* Rename columns for consistency
* Command-line interface using `argparse`
* Logging using Python's `logging` module
* Error handling for invalid or missing files
* Export clean data to Excel using `openpyxl`

---

## Technologies Used

* Python 3
* Pandas
* OpenPyXL
* Argparse
* Logging
* OS Module

---

## Project Structure

```text
CSV-Excel-Converter/
│
├── converter.py        # Main Python script
├── sample.csv          # Sample input file
├── output.xlsx         # Generated Excel file
├── app.log             # Log file
├── requirements.txt    # Project dependencies
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/DhirajChaudhari33/Syntecxhub_CSV-Excel-Converter.git
```

### Navigate to the project

```bash
cd Syntecxhub_CSV-Excel-Converter
```

### Install dependencies

```bash
pip install pandas openpyxl
```

---

## Usage

Run the following command:

```bash
python converter.py -i sample.csv -o output.xlsx
```

### Command-Line Arguments

| Argument | Description       |
| -------- | ----------------- |
| `-i`     | Input CSV file    |
| `-o`     | Output Excel file |

Example:

```bash
python converter.py -i employees.csv -o employees.xlsx
```

---

## Sample Input

```csv
Name,DOB,Salary,Department
John,2000-05-12,45000,IT
Alice,,52000,HR
Bob,1998-09-18,,Finance
David,2001-03-20,61000,
```

---

## Sample Output

| Employee_Name | Date_of_Birth | Salary | Department |
| ------------- | ------------- | ------ | ---------- |
| John          | 2000-05-12    | 45000  | IT         |
| Alice         | NaT           | 52000  | HR         |
| Bob           | 1998-09-18    | 0      | Finance    |
| David         | 2001-03-20    | 61000  | Unknown    |

---

## Logging

All application events are stored in `app.log`.

Example:

```text
INFO - CSV loaded successfully.
INFO - Excel file created successfully.
```

---

## Error Handling

The application handles:

* Missing input files
* Empty CSV files
* Invalid data
* Unexpected runtime errors

Errors are displayed in the terminal and recorded in the log file.

---

## Future Improvements

* Automatic column width adjustment
* Excel formatting (colors, borders, bold headers)
* Multiple CSV file support
* Duplicate row removal
* Summary statistics sheet
* GUI version using Tkinter
* Batch conversion of CSV files

---

## Learning Outcomes

This project demonstrates practical experience with:

* File handling
* Data preprocessing using Pandas
* Excel automation
* Command-line applications
* Logging and debugging
* Exception handling
* Python project organization

---

## Author

**Dhiraj Chaudhari**

* GitHub: https://github.com/DhirajChaudhari33

---

## License

This project is created for learning and educational purposes.
