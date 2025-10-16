"""
Script helper para trabalhar com a Spoonacular API
Permite buscar receitas, validar macros e obter imagens de refeições
"""

import os
import requests
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class SpoonacularAPI:
    def __init__(self):
        self.api_key = os.getenv('SPOONACULAR_API_KEY')
        if not self.api_key:
            raise ValueError("SPOONACULAR_API_KEY não encontrada no ficheiro .env")
        
        self.base_url = "https://api.spoonacular.com"
    
    def search_recipes(self, query: str, diet: str = None, max_results: int = 5) -> List[Dict]:
        """
        Procura receitas por nome
        
        Args:
            query: Nome da receita (ex: "grilled chicken salad")
            diet: Tipo de dieta (ex: "ketogenic", "vegetarian")
            max_results: Número máximo de resultados
        
        Returns:
            Lista de receitas encontradas
        """
        endpoint = f"{self.base_url}/recipes/complexSearch"
        
        params = {
            'apiKey': self.api_key,
            'query': query,
            'number': max_results,
            'addRecipeInformation': True,
            'fillIngredients': True
        }
        
        if diet:
            params['diet'] = diet
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get('results', [])
        except requests.exceptions.RequestException as e:
            print(f"Erro ao procurar receitas: {e}")
            return []
    
    def get_recipe_nutrition(self, recipe_id: int) -> Optional[Dict]:
        """
        Obtém informação nutricional de uma receita
        
        Args:
            recipe_id: ID da receita na Spoonacular
        
        Returns:
            Dicionário com informação nutricional
        """
        endpoint = f"{self.base_url}/recipes/{recipe_id}/nutritionWidget.json"
        
        params = {
            'apiKey': self.api_key
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter nutrição: {e}")
            return None
    
    def get_recipe_details(self, recipe_id: int) -> Optional[Dict]:
        """
        Obtém detalhes completos de uma receita
        
        Args:
            recipe_id: ID da receita
        
        Returns:
            Dicionário com todos os detalhes da receita
        """
        endpoint = f"{self.base_url}/recipes/{recipe_id}/information"
        
        params = {
            'apiKey': self.api_key,
            'includeNutrition': True
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter detalhes: {e}")
            return None
    
    def format_recipe_for_app(self, recipe_data: Dict) -> Dict:
        """
        Formata os dados da API para o formato usado na app
        
        Args:
            recipe_data: Dados da receita da API
        
        Returns:
            Dicionário no formato da app
        """
        # Extrair nutrição
        nutrition = recipe_data.get('nutrition', {})
        nutrients = {n['name']: n['amount'] for n in nutrition.get('nutrients', [])}
        
        # Extrair ingredientes
        ingredients = [
            f"{ing.get('amount', '')} {ing.get('unit', '')} {ing.get('name', '')}".strip()
            for ing in recipe_data.get('extendedIngredients', [])
        ]
        
        # Extrair instruções
        instructions = []
        analyzed_instructions = recipe_data.get('analyzedInstructions', [])
        if analyzed_instructions:
            steps = analyzed_instructions[0].get('steps', [])
            instructions = [step.get('step', '') for step in steps]
        
        # Formatar no formato da app
        formatted = {
            'name': recipe_data.get('title', 'Receita'),
            'calories': int(nutrients.get('Calories', 0)),
            'protein': int(nutrients.get('Protein', 0)),
            'carbs': int(nutrients.get('Carbohydrates', 0)),
            'fat': int(nutrients.get('Fat', 0)),
            'time': f"{recipe_data.get('readyInMinutes', 30)} min",
            'category': self._determine_category(recipe_data),
            'ingredients': ingredients,
            'recipe': instructions,
            'image_url': recipe_data.get('image', '')
        }
        
        return formatted
    
    def _determine_category(self, recipe_data: Dict) -> str:
        """Determina a categoria da refeição baseado nos dados"""
        dish_types = recipe_data.get('dishTypes', [])
        
        if any(t in dish_types for t in ['breakfast', 'morning meal']):
            return 'Café da Manhã'
        elif any(t in dish_types for t in ['lunch', 'main course', 'main dish']):
            return 'Almoço'
        elif any(t in dish_types for t in ['dinner']):
            return 'Jantar'
        elif any(t in dish_types for t in ['snack', 'appetizer', 'fingerfood']):
            return 'Lanche'
        else:
            return 'Almoço'  # Default


def example_usage():
    """Exemplo de como usar a API"""
    
    # Inicializar API
    api = SpoonacularAPI()
    
    # Exemplo 1: Procurar receitas
    print("🔍 Procurando receitas de salada de frango...")
    recipes = api.search_recipes("grilled chicken salad", max_results=3)
    
    for recipe in recipes:
        print(f"\n📝 {recipe['title']}")
        print(f"   Tempo: {recipe.get('readyInMinutes', 'N/A')} min")
        print(f"   ID: {recipe['id']}")
    
    # Exemplo 2: Obter detalhes e nutrição de uma receita
    if recipes:
        recipe_id = recipes[0]['id']
        print(f"\n📊 Detalhes da receita {recipe_id}...")
        
        details = api.get_recipe_details(recipe_id)
        if details:
            formatted = api.format_recipe_for_app(details)
            
            print(f"\n✅ Receita formatada:")
            print(f"   Nome: {formatted['name']}")
            print(f"   Calorias: {formatted['calories']}")
            print(f"   Proteína: {formatted['protein']}g")
            print(f"   Hidratos: {formatted['carbs']}g")
            print(f"   Gordura: {formatted['fat']}g")
            print(f"   Ingredientes: {len(formatted['ingredients'])} itens")
            print(f"   Passos: {len(formatted['recipe'])} passos")


if __name__ == "__main__":
    example_usage()

