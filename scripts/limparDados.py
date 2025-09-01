import pandas as pd

# Caminho do arquivo CSV original
arquivo_entrada = "MICRODADOS_CADASTRO_CURSOS_2023.csv"

# Caminho para salvar o arquivo limpo
arquivo_saida = "T_MICRODADOS_CADASTRO_CURSOS_2023.csv"

# Ler o arquivo com separador ";" e codificação latin1
df = pd.read_csv(arquivo_entrada, encoding="latin1", sep=";")

# Filtrar apenas as linhas onde a coluna NO_CURSO contém "letras"
df_filtrado = df[df["NO_CURSO"].str.contains("letras", case=False, na=False)]

# Salvar em latin1 (para abrir no Excel sem bug) OU em utf-8-sig (para evitar caracteres zoado)
df_filtrado.to_csv(arquivo_saida, index=False, sep=";", encoding="utf-8-sig")

print(f"Arquivo limpo gerado com sucesso: {arquivo_saida}")
