
def calcular_calorias(sexo, idade, peso, altura, atividade, objetivo):
    """
    Calcula as calorias necessárias baseado nos dados pessoais
    """
    
    # 1️⃣ Calcular TMB (quantas calorias o corpo gasta em repouso)
    if sexo == "homem":
        TMB = 10 * peso + 6.25 * altura - 5 * idade + 5
    else:
        TMB = 10 * peso + 6.25 * altura - 5 * idade - 161
    
    # 2️⃣ Calcular TDEE (TMB vezes o nível de atividade)
    niveis = {
        "baixo": 1.2,
        "medio": 1.55,
        "alto": 1.9,
    }
    TDEE = TMB * niveis.get(atividade, 1.2)
    
    # 3️⃣ Ajustar consoante o objetivo
    if objetivo == "ganhar":
        TDEE *= 1.15
    elif objetivo == "perder":
        TDEE *= 0.8
    
    # 4️⃣ Distribuição de macros (30% proteína / 40% hidratos / 30% gorduras)
    proteina = round((TDEE * 0.3) / 4)
    hidratos = round((TDEE * 0.4) / 4)
    gordura = round((TDEE * 0.3) / 9)
    
    # 5️⃣ Exemplo de refeições
    refeicoes = [
        {"nome": "Panquecas de Aveia", "kcal": 400},
        {"nome": "Bowl de Frango e Arroz", "kcal": 650},
        {"nome": "Wrap de Atum", "kcal": 380},
    ]
    
    return {
        "TMB": round(TMB),
        "TDEE": round(TDEE),
        "CaloriasTotais": round(TDEE),
        "Macros": {"proteina": proteina, "hidratos": hidratos, "gordura": gordura},
        "Refeicoes": refeicoes,
    }

# Exemplo de uso
resultado = calcular_calorias(
    sexo="homem",
    idade=28,
    peso=70,
    altura=172,
    atividade="medio",
    objetivo="ganhar"
)

print("=== CALCULADORA DE CALORIAS ===")
print(f"TMB (Taxa Metabólica Basal): {resultado['TMB']} calorias")
print(f"TDEE (Total de Energia Diária): {resultado['TDEE']} calorias")
print(f"Calorias Totais Recomendadas: {resultado['CaloriasTotais']} calorias")
print()
print("=== MACRONUTRIENTES ===")
print(f"Proteína: {resultado['Macros']['proteina']}g")
print(f"Hidratos de Carbono: {resultado['Macros']['hidratos']}g")
print(f"Gordura: {resultado['Macros']['gordura']}g")
print()
print("=== EXEMPLO DE REFEIÇÕES ===")
for refeicao in resultado['Refeicoes']:
    print(f"- {refeicao['nome']}: {refeicao['kcal']} calorias")
