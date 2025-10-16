"""
Script final para criar um MEALS_DATABASE híbrido
Mantém receitas originais de qualidade + adiciona melhores da API
"""

import json


def get_best_api_recipes():
    """
    Seleciona apenas as melhores receitas da API
    Traduzidas e otimizadas para português
    """
    
    api_recipes = {
        "lose": [
            {
                "name": "Sopa Mediterrânica de Vegetais Assados",
                "calories": 174,
                "protein": 4,
                "carbs": 18,
                "fat": 10,
                "time": "45 min",
                "category": "Almoço/Jantar",
                "ingredients": [
                    "2 tomates grandes",
                    "1 pimento vermelho",
                    "1 cebola roxa",
                    "2 dentes de alho",
                    "1 abobrinha",
                    "2 colheres de sopa de azeite",
                    "Manjericão fresco",
                    "Sal e pimenta a gosto"
                ],
                "recipe": [
                    "Pré-aqueça o forno a 200°C.",
                    "Corte todos os vegetais em cubos médios.",
                    "Coloque os vegetais num tabuleiro e regue com azeite.",
                    "Tempere com sal, pimenta e alho.",
                    "Asse no forno por 30 minutos até dourar.",
                    "Transfira para uma panela e adicione 500ml de água.",
                    "Triture com varinha mágica até obter consistência cremosa.",
                    "Sirva quente com manjericão fresco."
                ]
            },
            {
                "name": "Camarão com Espargos e Molho de Limão",
                "calories": 327,
                "protein": 37,
                "carbs": 3,
                "fat": 18,
                "time": "25 min",
                "category": "Almoço/Jantar",
                "ingredients": [
                    "300g de camarões limpos",
                    "200g de espargos verdes",
                    "2 dentes de alho picados",
                    "Sumo de 1 limão",
                    "2 colheres de sopa de azeite",
                    "1 colher de chá de manteiga",
                    "Salsa fresca",
                    "Sal e pimenta a gosto"
                ],
                "recipe": [
                    "Lave e corte os espargos em pedaços de 3cm.",
                    "Numa frigideira grande, aqueça o azeite.",
                    "Adicione o alho e salteie por 1 minuto.",
                    "Junte os espargos e cozinhe por 5 minutos.",
                    "Adicione os camarões e cozinhe por 3-4 minutos.",
                    "Tempere com sal, pimenta e sumo de limão.",
                    "Finalize com manteiga e salsa fresca.",
                    "Sirva imediatamente."
                ]
            },
            {
                "name": "Peixe Assado ao Estilo Grego",
                "calories": 344,
                "protein": 28,
                "carbs": 26,
                "fat": 12,
                "time": "30 min",
                "category": "Almoço/Jantar",
                "ingredients": [
                    "400g de filetes de peixe branco",
                    "2 tomates em rodelas",
                    "1 cebola em rodelas",
                    "1 limão em rodelas",
                    "2 dentes de alho picados",
                    "Oregãos secos",
                    "Azeite virgem extra",
                    "Sal e pimenta a gosto"
                ],
                "recipe": [
                    "Pré-aqueça o forno a 180°C.",
                    "Numa assadeira, coloque os filetes de peixe.",
                    "Cubra com rodelas de tomate, cebola e limão.",
                    "Polvilhe o alho picado e oregãos.",
                    "Regue com azeite e tempere com sal e pimenta.",
                    "Asse no forno por 20-25 minutos.",
                    "O peixe está pronto quando se desfaz facilmente.",
                    "Sirva com salada verde."
                ]
            }
        ],
        "maintain": [
            {
                "name": "Jambalaya de Frango",
                "calories": 450,
                "protein": 26,
                "carbs": 35,
                "fat": 21,
                "time": "55 min",
                "category": "Almoço/Jantar",
                "ingredients": [
                    "300g de peito de frango em cubos",
                    "1 xícara de arroz integral",
                    "1 pimento vermelho",
                    "1 cebola picada",
                    "2 tomates picados",
                    "2 dentes de alho",
                    "Colorau doce",
                    "Sal e pimenta a gosto"
                ],
                "recipe": [
                    "Numa panela, refogue o frango até dourar.",
                    "Retire o frango e reserve.",
                    "Na mesma panela, refogue cebola e alho.",
                    "Adicione o pimento e tomate, cozinhe por 5 min.",
                    "Junte o arroz e mexa bem.",
                    "Adicione 2 xícaras de água e o frango.",
                    "Tempere com colorau, sal e pimenta.",
                    "Cozinhe em lume brando por 35 min até o arroz estar cozido."
                ]
            },
            {
                "name": "Risotto de Quinoa com Salmão",
                "calories": 405,
                "protein": 22,
                "carbs": 33,
                "fat": 18,
                "time": "35 min",
                "category": "Almoço/Jantar",
                "ingredients": [
                    "1 xícara de quinoa",
                    "200g de salmão fresco",
                    "1 cebola pequena picada",
                    "2 dentes de alho",
                    "100ml de vinho branco",
                    "500ml de caldo de legumes",
                    "Queijo parmesão ralado",
                    "Azeite e salsa"
                ],
                "recipe": [
                    "Cozinhe a quinoa em água com sal.",
                    "Numa frigideira, grelhe o salmão e reserve.",
                    "Refogue a cebola e alho em azeite.",
                    "Adicione o vinho branco e deixe evaporar.",
                    "Junte a quinoa cozida e mexa bem.",
                    "Adicione caldo aos poucos, mexendo sempre.",
                    "Desfie o salmão e misture à quinoa.",
                    "Finalize com parmesão e salsa fresca."
                ]
            },
            {
                "name": "Smoothie Proteico de Amêndoa e Matcha",
                "calories": 281,
                "protein": 10,
                "carbs": 27,
                "fat": 13,
                "time": "10 min",
                "category": "Snack",
                "ingredients": [
                    "1 xícara de leite de amêndoa",
                    "1 banana congelada",
                    "1 colher de chá de matcha",
                    "1 colher de sopa de manteiga de amêndoa",
                    "1 colher de sopa de mel",
                    "1/2 xícara de espinafres",
                    "Gelo a gosto"
                ],
                "recipe": [
                    "Adicione todos os ingredientes no liquidificador.",
                    "Bata por 2-3 minutos até ficar cremoso.",
                    "Prove e ajuste a doçura se necessário.",
                    "Sirva imediatamente num copo alto.",
                    "Decore com amêndoas laminadas (opcional)."
                ]
            }
        ],
        "gain": [
            {
                "name": "Rolo de Frango com Batata-Doce e Queijo",
                "calories": 550,
                "protein": 45,
                "carbs": 42,
                "fat": 18,
                "time": "50 min",
                "category": "Almoço/Jantar",
                "ingredients": [
                    "2 peitos de frango grandes",
                    "200g de batata-doce cozida",
                    "100g de queijo de cabra",
                    "Espinafres frescos",
                    "2 dentes de alho",
                    "Azeite e tomilho",
                    "Sal e pimenta a gosto"
                ],
                "recipe": [
                    "Pré-aqueça o forno a 180°C.",
                    "Abra os peitos de frango como um livro.",
                    "Tempere com sal, pimenta e alho.",
                    "Espalhe a batata-doce amassada sobre o frango.",
                    "Adicione espinafres e queijo de cabra.",
                    "Enrole o frango e prenda com palitos ou cordel.",
                    "Pincele com azeite e polvilhe tomilho.",
                    "Asse por 35-40 minutos até dourar."
                ]
            },
            {
                "name": "Pimentos Recheados com Peru e Arroz",
                "calories": 520,
                "protein": 38,
                "carbs": 48,
                "fat": 18,
                "time": "55 min",
                "category": "Almoço/Jantar",
                "ingredients": [
                    "4 pimentos grandes",
                    "300g de carne de peru picada",
                    "1 xícara de arroz cozido",
                    "1 cebola picada",
                    "2 tomates picados",
                    "100g de queijo ralado",
                    "Manjericão fresco",
                    "Sal e pimenta"
                ],
                "recipe": [
                    "Pré-aqueça o forno a 180°C.",
                    "Corte a tampa dos pimentos e retire as sementes.",
                    "Refogue a carne de peru com cebola até dourar.",
                    "Adicione o tomate e cozinhe por 5 minutos.",
                    "Misture o arroz cozido e tempere.",
                    "Recheie os pimentos com a mistura.",
                    "Cubra com queijo ralado.",
                    "Asse por 35-40 minutos até os pimentos estarem macios."
                ]
            },
            {
                "name": "Almôndegas Turcas com Arroz de Lentilhas",
                "calories": 580,
                "protein": 32,
                "carbs": 52,
                "fat": 24,
                "time": "50 min",
                "category": "Almoço/Jantar",
                "ingredients": [
                    "400g de carne picada",
                    "1 xícara de lentilhas",
                    "1/2 xícara de arroz",
                    "1 cebola picada",
                    "2 dentes de alho",
                    "Cominho e colorau",
                    "Hortelã fresca",
                    "Sal e pimenta"
                ],
                "recipe": [
                    "Misture a carne com especiarias e forme almôndegas.",
                    "Frite as almôndegas até dourarem e reserve.",
                    "Cozinhe as lentilhas em água com sal.",
                    "Refogue cebola e alho, adicione o arroz.",
                    "Junte as lentilhas e água, cozinhe por 20 min.",
                    "Tempere com cominho e colorau.",
                    "Sirva o arroz de lentilhas com as almôndegas.",
                    "Decore com hortelã fresca."
                ]
            }
        ]
    }
    
    return api_recipes


def print_summary():
    """Mostra resumo das receitas selecionadas"""
    recipes = get_best_api_recipes()
    
    print("\n" + "="*70)
    print("🌟 RECEITAS SELECIONADAS DA SPOONACULAR API")
    print("="*70 + "\n")
    
    for goal in ["lose", "maintain", "gain"]:
        goal_pt = {"lose": "PERDER PESO", "maintain": "MANTER PESO", "gain": "GANHAR PESO"}[goal]
        
        print(f"\n🎯 {goal_pt}:")
        print("-" * 70)
        
        for i, recipe in enumerate(recipes[goal], 1):
            print(f"{i}. {recipe['name']}")
            print(f"   📊 {recipe['calories']}kcal | "
                  f"P:{recipe['protein']}g | "
                  f"C:{recipe['carbs']}g | "
                  f"G:{recipe['fat']}g")
            print(f"   ⏱️  {recipe['time']} | 🍽️  {recipe['category']}\n")
    
    print("="*70)
    print("\n✅ Estas receitas serão ADICIONADAS às tuas receitas existentes!")
    print("📝 O teu MEALS_DATABASE terá:")
    print("   - Receitas originais (mantidas)")
    print("   - + 9 receitas novas da Spoonacular")
    print("   - TOTAL: ~60+ receitas variadas\n")


def create_integration_instructions():
    """Cria instruções para integração manual"""
    recipes = get_best_api_recipes()
    
    with open('receitas_para_adicionar.json', 'w', encoding='utf-8') as f:
        json.dump(recipes, f, ensure_ascii=False, indent=2)
    
    print("💾 Receitas salvas em: receitas_para_adicionar.json")
    print("\n" + "="*70)
    print("📋 INSTRUÇÕES DE INTEGRAÇÃO")
    print("="*70)
    print("\n1. Abre o ficheiro streamlit_app.py")
    print("2. Encontra o MEALS_DATABASE")
    print("3. Adiciona as novas receitas de 'receitas_para_adicionar.json'")
    print("4. Ou deixa-me fazer isso automaticamente!\n")
    print("="*70 + "\n")


def main():
    """Função principal"""
    print_summary()
    create_integration_instructions()
    
    print("❓ Queres que eu adicione estas receitas automaticamente ao streamlit_app.py?")
    print("   (Vou manter todas as tuas receitas existentes + adicionar estas)\n")


if __name__ == "__main__":
    main()

