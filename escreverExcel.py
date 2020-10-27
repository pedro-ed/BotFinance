import pandas as pd

# Crie um dataframe do Pandas a partir dos dados.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Crie um gravador do Pandas Excel usando XlsxWriter como mecanismo.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Converta o dataframe em um objeto Excel XlsxWriter.
df.to_excel(writer, sheet_name='Sheet1')

# Feche o gravador do Pandas Excel e gere o arquivo Excel.
writer.save()

