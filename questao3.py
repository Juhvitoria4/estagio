import json

faturamento_json = '''
{
    "01": 5000.00,
    "02": 7000.00,
    "03": 8000.00,
    "04": 0.00,
    "05": 6000.00,
    "06": 10000.00
}
'''

dados = json.loads(faturamento_json)
faturamentos = list(dados.values())

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias acima da média: {dias_acima_da_media}")
