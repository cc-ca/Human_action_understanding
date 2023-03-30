
import pandas as pd

# créer une table exemple
table = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
table

# appeler la première colonne avec iloc
colonne_1 = table.iloc[:, 0]
print(colonne_1)