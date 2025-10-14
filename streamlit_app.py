# Import and run the Streamlit app
import streamlit as st
import random
from typing import Dict, List, Tuple

# Configure page
st.set_page_config(
    page_title="Calculadora de Calorias & Refeições",
    page_icon="🍎",
    layout="wide"
)

# Database de refeições
MEALS_DATABASE = {
    "lose": [
        {
            "name": "Aveia com Frutas Vermelhas",
            "calories": 320,
            "protein": 12,
            "carbs": 58,
            "fat": 6,
            "time": "10 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1/2 xícara de aveia em flocos",
                "1 xícara de leite desnatado",
                "1/4 xícara de frutas vermelhas mistas",
                "1 colher de sopa de mel",
                "1 colher de chá de canela",
                "1 colher de sopa de sementes de chia"
            ],
            "recipe": [
                "Em uma panela, aqueça o leite em fogo médio.",
                "Adicione a aveia e mexa bem para não grudar.",
                "Cozinhe por 5-7 minutos mexendo ocasionalmente.",
                "Adicione a canela e o mel, misture bem.",
                "Retire do fogo e deixe esfriar por 2 minutos.",
                "Coloque em uma tigela e adicione as frutas vermelhas por cima.",
                "Finalize com as sementes de chia e sirva."
            ]
        },
        {
            "name": "Omelete de Espinafre",
            "calories": 280,
            "protein": 20,
            "carbs": 8,
            "fat": 18,
            "time": "8 min",
            "category": "Café da Manhã",
            "ingredients": [
                "3 ovos inteiros",
                "1 xícara de espinafre fresco",
                "2 tomates cereja",
                "1 colher de sopa de azeite",
                "1/4 xícara de queijo cottage",
                "1 dente de alho picado",
                "Sal e pimenta a gosto"
            ],
            "recipe": [
                "Bata os ovos em uma tigela com sal e pimenta.",
                "Aqueça o azeite em frigideira antiaderente.",
                "Refogue o alho e espinafre por 2 minutos.",
                "Despeje os ovos batidos na frigideira.",
                "Adicione o queijo cottage e tomates cereja.",
                "Cozinhe por 3-4 minutos até firmar embaixo.",
                "Dobre a omelete ao meio e sirva quente."
            ]
        }
    ],
    "maintain": [
        {
            "name": "Panquecas de Aveia",
            "calories": 420,
            "protein": 18,
            "carbs": 45,
            "fat": 15,
            "time": "15 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1/2 xícara de aveia em flocos",
                "2 ovos inteiros",
                "1/4 xícara de leite",
                "1 banana madura",
                "1 colher de chá de fermento",
                "1 colher de chá de mel",
                "Canela a gosto"
            ],
            "recipe": [
                "No liquidificador, bata a banana com os ovos e leite.",
                "Adicione a aveia, fermento, mel e canela.",
                "Bata até obter uma massa homogênea.",
                "Deixe descansar por 5 minutos.",
                "Aqueça uma frigideira antiaderente.",
                "Despeje pequenas porções da massa na frigideira.",
                "Cozinhe por 2-3 minutos de cada lado até dourar."
            ]
        }
    ],
    "gain": [
        {
            "name": "Vitamina Calórica",
            "calories": 520,
            "protein": 25,
            "carbs": 65,
            "fat": 18,
            "time": "5 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1 banana média",
                "200ml de leite integral",
                "2 colheres de sopa de aveia",
                "1 scoop de whey protein",
                "1 colher de sopa de pasta de amendoim",
                "1 colher de sopa de mel",
                "1 colher de chá de cacau em pó"
            ],
            "recipe": [
                "Adicione a banana cortada no liquidificador.",
                "Acrescente o leite integral.",
                "Adicione a aveia, whey protein e pasta de amendoim.",
                "Coloque o mel e o cacau em pó.",
                "Bata por 2-3 minutos até ficar cremoso.",
                "Sirva imediatamente em copo grande."
            ]
        }
    ]
}

# Funções de cálculo
def calculate_bmr(sex, age, weight, height):
    """Calculate Basal Metabolic Rate using Mifflin-St Jeor formula."""
    if sex == 'M':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:  # Female
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

def calculate_tdee(bmr, activity_level):
    """Calculate Total Daily Energy Expenditure based on activity level."""
    activity_factors = {
        1: 1.2,    # Sedentary
        2: 1.375,  # Lightly active
        3: 1.55,   # Moderately active
        4: 1.725,  # Very active
        5: 1.9     # Extremely active
    }
    tdee = bmr * activity_factors[activity_level]
    return tdee

def adjust_for_goal(tdee, goal):
    """Adjust calories based on the user's goal."""
    if goal == "lose":
        calories = tdee * 0.8  # 20% reduction
    elif goal == "gain":
        calories = tdee * 1.15  # 15% increase
    else:  # maintain
        calories = tdee
    return calories

def calculate_macros(calories, weight):
    """Calculate macronutrient distribution."""
    # Protein: 2g per kg of body weight
    protein_grams = 2 * weight
    protein_calories = protein_grams * 4  # 4 calories per gram of protein
    
    # Fat: 25% of total calories
    fat_calories = calories * 0.25
    fat_grams = fat_calories / 9  # 9 calories per gram of fat
    
    # Carbohydrates: remaining calories
    carb_calories = calories - protein_calories - fat_calories
    carb_grams = carb_calories / 4  # 4 calories per gram of carbohydrate
    
    return protein_grams, fat_grams, carb_grams

def get_meal_suggestions(goal, target_calories, num_meals=3):
    """Get personalized meal suggestions based on goal and calories."""
    meals = MEALS_DATABASE.get(goal, MEALS_DATABASE["maintain"])
    calories_per_meal = target_calories / num_meals
    
    # Filter meals that fit within ±100 calories of target per meal
    suitable_meals = [meal for meal in meals if abs(meal["calories"] - calories_per_meal) <= 100]
    
    if not suitable_meals:
        # If no meals fit perfectly, get the closest ones
        suitable_meals = sorted(meals, key=lambda x: abs(x["calories"] - calories_per_meal))
    
    return random.sample(suitable_meals, min(num_meals, len(suitable_meals)))

def display_meal_card(meal):
    """Display a meal card with all details."""
    with st.expander(f"🍽️ {meal['name']} - {meal['calories']} cal", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write(f"**Categoria:** {meal['category']}")
            st.write(f"**Tempo de preparo:** {meal['time']}")
            
            # Macros
            st.write("**Macronutrientes:**")
            col_macro1, col_macro2, col_macro3 = st.columns(3)
            with col_macro1:
                st.metric("Proteína", f"{meal['protein']}g")
            with col_macro2:
                st.metric("Carboidratos", f"{meal['carbs']}g")
            with col_macro3:
                st.metric("Gordura", f"{meal['fat']}g")
        
        with col2:
            st.metric("Calorias", f"{meal['calories']}")
        
        # Ingredients
        st.write("**Ingredientes:**")
        for ingredient in meal['ingredients']:
            st.write(f"• {ingredient}")
        
        # Recipe
        st.write("**Modo de preparo:**")
        for i, step in enumerate(meal['recipe'], 1):
            st.write(f"{i}. {step}")

# Interface principal
def main():
    st.title("🍎 Calculadora de Calorias & Sugestões de Refeições")
    st.markdown("---")
    
    # Sidebar para informações pessoais
    with st.sidebar:
        st.header("📊 Suas Informações")
        
        sex = st.selectbox("Sexo", ["M", "F"], help="M para Masculino, F para Feminino")
        age = st.number_input("Idade (anos)", min_value=1, max_value=120, value=25)
        weight = st.number_input("Peso (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.1)
        height = st.number_input("Altura (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)
        
        activity_level = st.selectbox(
            "Nível de Atividade",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "Sedentário (pouco ou nenhum exercício)",
                2: "Ligeiramente ativo (exercício leve 1-3 dias/semana)",
                3: "Moderadamente ativo (exercício moderado 3-5 dias/semana)",
                4: "Muito ativo (exercício intenso 6-7 dias/semana)",
                5: "Extremamente ativo (exercício muito intenso, trabalho físico)"
            }[x]
        )
        
        goal = st.selectbox("Objetivo", ["lose", "maintain", "gain"], 
                          format_func=lambda x: {
                              "lose": "Perder peso",
                              "maintain": "Manter peso", 
                              "gain": "Ganhar peso"
                          }[x])
        
        calculate_button = st.button("🧮 Calcular Minhas Calorias", type="primary")
    
    # Cálculos e resultados
    if calculate_button:
        # Calculate BMR
        bmr = calculate_bmr(sex, age, weight, height)
        
        # Calculate TDEE
        tdee = calculate_tdee(bmr, activity_level)
        
        # Adjust for goal
        daily_calories = adjust_for_goal(tdee, goal)
        
        # Calculate macronutrients
        protein_grams, fat_grams, carb_grams = calculate_macros(daily_calories, weight)
        
        # Store results in session state
        st.session_state.calculated = True
        st.session_state.results = {
            'bmr': bmr,
            'tdee': tdee,
            'daily_calories': daily_calories,
            'protein': protein_grams,
            'fat': fat_grams,
            'carbs': carb_grams,
            'goal': goal
        }
    
    # Display results if calculated
    if st.session_state.get('calculated', False):
        results = st.session_state.results
        
        st.success("🎯 Suas Recomendações Calóricas Diárias")
        
        # Métricas principais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Calorias Diárias", f"{results['daily_calories']:.0f}")
        with col2:
            st.metric("TMB", f"{results['bmr']:.0f}")
        with col3:
            st.metric("TDEE", f"{results['tdee']:.0f}")
        with col4:
            st.metric("Objetivo", results['goal'].title())
        
        # Gráfico de macros
        st.subheader("📊 Distribuição de Macronutrientes")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Proteína", f"{results['protein']:.1f} g")
        with col2:
            st.metric("Gordura", f"{results['fat']:.1f} g")
        with col3:
            st.metric("Carboidratos", f"{results['carbs']:.1f} g")
        
        # Sugestões de refeições
        st.subheader("🍽️ Sugestões de Refeições Personalizadas")
        st.write(f"Baseado no seu objetivo de **{results['goal']}** peso e **{results['daily_calories']:.0f}** calorias diárias")
        
        # Get meal suggestions
        suggested_meals = get_meal_suggestions(results['goal'], results['daily_calories'])
        
        # Display meals
        for meal in suggested_meals:
            display_meal_card(meal)
        
        # Dica do personal trainer
        st.info("💡 **Dica do Personal Trainer:** " + {
            'lose': "Para perda de peso, foque em proteínas magras e vegetais. Beba bastante água e mantenha consistência.",
            'maintain': "Para manutenção, balance bem os macronutrientes e pratique exercícios regulares.",
            'gain': "Para ganho de peso, aumente gradualmente as calorias e combine com treino de força."
        }[results['goal']])
        
        # Botão para gerar novas sugestões
        if st.button("🔄 Gerar Novas Sugestões de Refeições"):
            st.rerun()

# Run the app
if __name__ == "__main__":
    main()