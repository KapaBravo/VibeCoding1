"""
Script para atualizar receitas usando a Spoonacular API
Este script busca receitas reais e formata para o MEALS_DATABASE
"""

import os
import json
import requests
from dotenv import load_dotenv
from typing import List, Dict

# Carregar variáveis de ambiente
load_dotenv()

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"


def search_recipes(query: str, diet: str = None, max_calories: int = None, number: int = 10) -> List[Dict]:
    """
    Busca receitas na Spoonacular API
    
    Args:
        query: Termo de busca
        diet: Tipo de dieta (ex: "low calorie", "high protein")
        max_calories: Calorias máximas
        number: Número de receitas a retornar
    
    Returns:
        Lista de receitas encontradas
    """
    if not SPOONACULAR_API_KEY:
        print("❌ ERRO: API Key não configurada!")
        return []
    
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "query": query,
        "number": number,
        "addRecipeInformation": True,
        "fillIngredients": True,
        "instructionsRequired": True,
        "sort": "popularity",
        "sortDirection": "desc"
    }
    
    if diet:
        params["diet"] = diet
    
    if max_calories:
        params["maxCalories"] = max_calories
    
    try:
        print(f"🔍 Buscando receitas: {query}...")
        response = requests.get(f"{BASE_URL}/recipes/complexSearch", params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        results = data.get("results", [])
        print(f"   ✅ Encontradas {len(results)} receitas")
        return results
        
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Erro ao buscar receitas: {e}")
        return []


def get_recipe_details(recipe_id: int) -> Dict:
    """
    Obtém detalhes completos de uma receita
    
    Args:
        recipe_id: ID da receita na Spoonacular
    
    Returns:
        Dicionário com detalhes da receita
    """
    if not SPOONACULAR_API_KEY:
        return {}
    
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "includeNutrition": True
    }
    
    try:
        response = requests.get(f"{BASE_URL}/recipes/{recipe_id}/information", params=params, timeout=15)
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Erro ao obter detalhes da receita {recipe_id}: {e}")
        return {}


def extract_nutrients(nutrition_data: Dict) -> Dict:
    """
    Extrai macronutrientes dos dados nutricionais
    
    Args:
        nutrition_data: Dados nutricionais da API
    
    Returns:
        Dicionário com calorias, proteínas, carbos e gorduras
    """
    nutrients = nutrition_data.get("nutrients", [])
    
    macros = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }
    
    for nutrient in nutrients:
        name = nutrient.get("name", "").lower()
        amount = round(nutrient.get("amount", 0))
        
        if "calorie" in name:
            macros["calories"] = amount
        elif "protein" in name:
            macros["protein"] = amount
        elif "carbohydrate" in name:
            macros["carbs"] = amount
        elif "fat" in name and "saturated" not in name:
            macros["fat"] = amount
    
    return macros


def format_recipe_for_app(recipe_data: Dict) -> Dict:
    """
    Formata dados da Spoonacular para o formato do MEALS_DATABASE
    
    Args:
        recipe_data: Dados da receita da API
    
    Returns:
        Receita formatada para a app
    """
    # Extrair macros
    nutrition = recipe_data.get("nutrition", {})
    macros = extract_nutrients(nutrition)
    
    # Extrair ingredientes
    ingredients = []
    for ingredient in recipe_data.get("extendedIngredients", []):
        original = ingredient.get("original", "")
        if original:
            ingredients.append(original)
    
    # Extrair instruções
    recipe_steps = []
    instructions = recipe_data.get("analyzedInstructions", [])
    
    if instructions:
        steps = instructions[0].get("steps", [])
        for step in steps:
            recipe_steps.append(step.get("step", ""))
    
    # Determinar categoria
    dish_types = recipe_data.get("dishTypes", [])
    category = "Almoço/Jantar"  # Default
    
    if any(t in dish_types for t in ["breakfast", "brunch", "morning meal"]):
        category = "Café da Manhã"
    elif any(t in dish_types for t in ["snack", "appetizer"]):
        category = "Snack"
    elif any(t in dish_types for t in ["dessert"]):
        category = "Sobremesa"
    
    # Tempo de preparação
    ready_time = recipe_data.get("readyInMinutes", 30)
    
    # Imagem
    image_url = recipe_data.get("image", "")
    
    # Formatar para o app
    formatted_recipe = {
        "name": recipe_data.get("title", "Receita"),
        "calories": macros["calories"],
        "protein": macros["protein"],
        "carbs": macros["carbs"],
        "fat": macros["fat"],
        "time": f"{ready_time} min",
        "category": category,
        "ingredients": ingredients[:10],  # Limitar a 10 ingredientes
        "recipe": recipe_steps[:10],  # Limitar a 10 passos
        "image": image_url,
        "source": "Spoonacular",
        "recipe_id": recipe_data.get("id")
    }
    
    return formatted_recipe


def fetch_recipes_by_goal(goal: str, count: int = 15) -> List[Dict]:
    """
    Busca receitas específicas para cada objetivo
    
    Args:
        goal: Objetivo ("lose", "maintain", "gain")
        count: Número de receitas a buscar
    
    Returns:
        Lista de receitas formatadas
    """
    print(f"\n{'='*60}")
    print(f"🎯 Buscando receitas para: {goal.upper()}")
    print(f"{'='*60}\n")
    
    all_recipes = []
    
    # Configurações por objetivo
    if goal == "lose":
        queries = [
            ("healthy breakfast low calorie", None, 400),
            ("grilled chicken salad", "low calorie", 450),
            ("vegetable soup", "low calorie", 300),
            ("fish with vegetables", "low calorie", 400),
            ("greek yogurt snack", None, 200)
        ]
    elif goal == "maintain":
        queries = [
            ("balanced breakfast", None, 500),
            ("chicken with rice", None, 600),
            ("pasta with vegetables", None, 550),
            ("salmon with quinoa", None, 600),
            ("protein smoothie", None, 350)
        ]
    else:  # gain
        queries = [
            ("high protein breakfast", "high protein", 600),
            ("chicken breast with sweet potato", "high protein", 700),
            ("beef with rice", "high protein", 750),
            ("protein pasta", "high protein", 650),
            ("peanut butter smoothie", "high protein", 500)
        ]
    
    # Buscar receitas para cada query
    for query, diet, max_cal in queries:
        recipes = search_recipes(query, diet=diet, max_calories=max_cal, number=3)
        
        for recipe in recipes[:2]:  # Pegar só 2 por query
            # Obter detalhes completos
            recipe_id = recipe.get("id")
            if recipe_id:
                print(f"   📥 Obtendo detalhes: {recipe.get('title', 'N/A')}")
                full_recipe = get_recipe_details(recipe_id)
                
                if full_recipe:
                    formatted = format_recipe_for_app(full_recipe)
                    all_recipes.append(formatted)
                    
                    if len(all_recipes) >= count:
                        break
        
        if len(all_recipes) >= count:
            break
    
    print(f"\n✅ Total de receitas obtidas para '{goal}': {len(all_recipes)}\n")
    return all_recipes[:count]


def save_recipes_to_json(recipes_by_goal: Dict, filename: str = "spoonacular_recipes.json"):
    """
    Salva as receitas em um arquivo JSON
    
    Args:
        recipes_by_goal: Dicionário com receitas por objetivo
        filename: Nome do arquivo
    """
    filepath = f"/Users/luisferreira/Downloads/vibecoding-cursor-template/{filename}"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(recipes_by_goal, f, ensure_ascii=False, indent=2)
    
    print(f"💾 Receitas salvas em: {filename}")


def main():
    """
    Função principal
    """
    print("\n" + "="*60)
    print("🍽️  ATUALIZAÇÃO DE RECEITAS - SPOONACULAR API")
    print("="*60 + "\n")
    
    if not SPOONACULAR_API_KEY:
        print("❌ ERRO: Configure a SPOONACULAR_API_KEY no ficheiro .env")
        return
    
    # Buscar receitas para cada objetivo
    all_recipes = {
        "lose": fetch_recipes_by_goal("lose", count=15),
        "maintain": fetch_recipes_by_goal("maintain", count=15),
        "gain": fetch_recipes_by_goal("gain", count=15)
    }
    
    # Salvar em JSON
    save_recipes_to_json(all_recipes)
    
    # Estatísticas
    print("\n" + "="*60)
    print("📊 RESUMO")
    print("="*60)
    print(f"Receitas para PERDER PESO: {len(all_recipes['lose'])}")
    print(f"Receitas para MANTER PESO: {len(all_recipes['maintain'])}")
    print(f"Receitas para GANHAR PESO: {len(all_recipes['gain'])}")
    print(f"TOTAL: {sum(len(r) for r in all_recipes.values())}")
    print("="*60 + "\n")
    
    print("✅ Processo concluído!")
    print("📄 Próximo passo: Revê o ficheiro 'spoonacular_recipes.json'")
    print("🔄 Depois, vamos integrar no streamlit_app.py\n")


if __name__ == "__main__":
    main()

