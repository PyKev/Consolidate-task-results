# Consolidación de Resultados de Tareas

Este repositorio contiene un script de Python "Consolidar_resultados.py" que te permitirá consolidar los resultados de tareas de un archivo Excel. El código tomará el archivo "archivo.xlsx", el cual debe tener dos columnas: "IDTAREA" y "RESULTADO". Luego generará un nuevo archivo de Excel llamado "archivo2.xlsx" con los resultados consolidados.

## Requisitos
- Python
- Librerias pandas y numpy `pip install pandas numpy`

## Uso
- Debe crear un archivo archivo.xlsx y colocarlo en la misma carpeta que el script de Python.
- Ejecuta el script Consolidar_resultados.py.
- Una vez que se ejecute el script, se generará un nuevo archivo de Excel llamado archivo2.xlsx.
- Abre el archivo archivo2.xlsx para ver los resultados consolidados. En la columna "Texto" se mostrará la consolidación de los resultados de cada tarea, siguiendo el formato "R1, R2 y R3", "R1, R2, R3 y R4" ... si hay más de dos resultados, o "R1 y R2" si hay exactamente dos resultados. Se separarán los resultados con una coma a excepción del último que irá con la letra "y".

## Consideraciones
- Si deseas utilizar un archivo diferente, puedes modificar el nombre del archivo en el código antes de ejecutarlo.
