import streamlit as st

# Set the page title
st.title("Hello World!")

# Display a simple message
st.write("Welcome to your first Streamlit app!")

# Add a friendly greeting
st.write("This is a simple web page created with by KapaBravo.")

# Add a separator
st.divider()

# Calorie Calculator Functions
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

# Calorie Calculator section
st.subheader("🍎 Calorie Calculator")
st.write("Calculate your daily calorie needs based on your goals!")

# Create a form for the calorie calculator
with st.form("calorie_calculator"):
    st.write("**Personal Information:**")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        sex = st.selectbox("Sex", ["M", "F"], help="M for Male, F for Female")
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=25)
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.1)
    
    with col2:
        height = st.number_input("Height (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)
        activity_level = st.selectbox(
            "Activity Level",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "Sedentary (little to no exercise)",
                2: "Lightly active (light exercise 1-3 days/week)",
                3: "Moderately active (moderate exercise 3-5 days/week)",
                4: "Very active (hard exercise 6-7 days/week)",
                5: "Extremely active (very hard exercise, physical job)"
            }[x]
        )
        goal = st.selectbox("Goal", ["lose", "maintain", "gain"], 
                          format_func=lambda x: {
                              "lose": "Lose weight",
                              "maintain": "Maintain weight", 
                              "gain": "Gain weight"
                          }[x])
    
    # Calculate button
    calculate_button = st.form_submit_button("Calculate My Calories")
    
    if calculate_button:
        # Calculate BMR
        bmr = calculate_bmr(sex, age, weight, height)
        
        # Calculate TDEE
        tdee = calculate_tdee(bmr, activity_level)
        
        # Adjust for goal
        daily_calories = adjust_for_goal(tdee, goal)
        
        # Calculate macronutrients
        protein_grams, fat_grams, carb_grams = calculate_macros(daily_calories, weight)
        
        # Display results
        st.success("🎯 Your Daily Calorie Recommendations")
        
        # Create columns for results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Daily Calories", f"{daily_calories:.0f}")
            st.metric("BMR", f"{bmr:.0f}")
            st.metric("TDEE", f"{tdee:.0f}")
        
        with col2:
            st.metric("Protein", f"{protein_grams:.1f} g")
            st.metric("Fat", f"{fat_grams:.1f} g")
        
        with col3:
            st.metric("Carbs", f"{carb_grams:.1f} g")
        
        # Additional info
        st.info("💡 **Remember:** These are estimates. Consult a healthcare professional for personalized nutrition advice.")


