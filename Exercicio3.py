import xml.etree.ElementTree as ET

tree = ET.parse('"C:\Users\Matheus Gietzel.GEZELCHINE\OneDrive\Documents\GitHub\Exerc-cios_Est-gio\dados.xml"')

root = tree.getroot()

soma_faturamento = 0
maior_valor = float('-inf')
menor_valor = float('inf')
dias_acima_media = 0

for row in root.findall('row'):
    dia = int(row.find('dia').text)
    valor = float(row.find('valor').text)

    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor

    # Soma o valor de faturamento para cálculo da média
    soma_faturamento += valor

    # Verifica se o valor de faturamento é superior à média mensal
    if valor > soma_faturamento / len(root):
        dias_acima_media += 1

# Cálculo da média mensal
media_mensal = soma_faturamento / len(root)

# Resultados
print(f'Menor valor de faturamento: R${menor_valor:.2f}')
print(f'Maior valor de faturamento: R${maior_valor:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_media}')
