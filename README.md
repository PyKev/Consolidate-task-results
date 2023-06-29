# Task Results Consolidation

This repository contains a Python script called "Consolidar_resultados.py" that allows you to consolidate task results from an Excel file. The code takes the "archivo.xlsx" file as input, which should have two columns: "IDTAREA" (IDTASK) and "RESULTADO" (RESULT). It will then generate a new Excel file called "archivo2.xlsx" with the consolidated results.

## Requirements
- Python
- Pandas and Numpy libraries `pip install pandas numpy`

## Usage
- Create an "archivo.xlsx" file and place it in the same folder as the Python script.
- Run the Consolidar_resultados.py script.
- Once the script is executed, a new Excel file called "archivo2.xlsx" will be generated.
- Open the file "archivo2.xlsx" to view the consolidated results. The "Texto" (Text) column will display the consolidation of the results for each task, following the format "R1, R2, and R3", "R1, R2, R3, y R4" ... if there are more than two results, or "R1 y R2" if there are exactly two results. The results will be separated by commas, except for the last one, which will be preceded by the word "y" (and in spanish).

## Considerations
- If you want to use a different file, you can modify the file name in the code before executing it.
