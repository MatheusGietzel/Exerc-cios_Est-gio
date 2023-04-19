# Valores de faturamento mensal por estado
faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

# Valor total mensal da distribuidora
valor_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

# Cálculo do percentual de representação de cada estado
percentual_sp = (faturamento_sp / valor_total) * 100
percentual_rj = (faturamento_rj / valor_total) * 100
percentual_mg = (faturamento_mg / valor_total) * 100
percentual_es = (faturamento_es / valor_total) * 100
percentual_outros = (faturamento_outros / valor_total) * 100

# Impressão dos resultados
print("Percentual de representação por estado:")
print("SP: {:.2f}%".format(percentual_sp))
print("RJ: {:.2f}%".format(percentual_rj))
print("MG: {:.2f}%".format(percentual_mg))
print("ES: {:.2f}%".format(percentual_es))
print("Outros: {:.2f}%".format(percentual_outros))