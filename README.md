# Task Results Consolidation

This repository contains a Python script called "Consolidate_results.py" that allows you to consolidate task results from an Excel file. The code takes the "file.xlsx" file as input, which should have two columns: "TASKID" and "RESULT". It will then generate a new Excel file called "file2.xlsx" with the consolidated results.

## Requirements
- Python
- Pandas and Numpy libraries `pip install pandas numpy`

## Usage
- Create an "file.xlsx" file and place it in the same folder as the Python script.
- Run the Consolidate_results.py script.
- Once the script is executed, a new Excel file called "file2.xlsx" will be generated.
- Open the file "file2.xlsx" to view the consolidated results. The "Text" column will display the consolidation of the results for each task, following the format "R1, R2, and R3", "R1, R2, R3, and R4" ... if there are more than two results, or "R1 and R2" if there are exactly two results. The results will be separated by commas, except for the last one, which will be preceded by the word "and".

## Considerations
- If you want to use a different file, you can modify the file name in the code before executing it.
