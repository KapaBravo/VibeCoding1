"""
Daily Calorie Calculator
A simple calculator to determine daily calorie needs based on the Mifflin-St Jeor formula.
"""

def get_user_info():
    """Ask the user for their personal information and goals."""
    print("=== Daily Calorie Calculator ===")
    print("Let's calculate your daily calorie needs!\n")
    
    # Get user information
    sex = input("Enter your sex (M for male, F for female): ").upper()
    while sex not in ['M', 'F']:
        print("Please enter M for male or F for female.")
        sex = input("Enter your sex (M for male, F for female): ").upper()
    
    age = int(input("Enter your age in years: "))
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    
    print("\nActivity levels:")
    print("1 = Sedentary (little to no exercise)")
    print("2 = Lightly active (light exercise 1-3 days/week)")
    print("3 = Moderately active (moderate exercise 3-5 days/week)")
    print("4 = Very active (hard exercise 6-7 days/week)")
    print("5 = Extremely active (very hard exercise, physical job)")
    
    activity_level = int(input("Enter your activity level (1-5): "))
    while activity_level not in [1, 2, 3, 4, 5]:
        print("Please enter a number between 1 and 5.")
        activity_level = int(input("Enter your activity level (1-5): "))
    
    print("\nGoals:")
    print("1 = Lose weight")
    print("2 = Maintain weight")
    print("3 = Gain weight")
    
    goal_choice = int(input("Enter your goal (1-3): "))
    while goal_choice not in [1, 2, 3]:
        print("Please enter 1, 2, or 3.")
        goal_choice = int(input("Enter your goal (1-3): "))
    
    goals = {1: "lose", 2: "maintain", 3: "gain"}
    goal = goals[goal_choice]
    
    return sex, age, weight, height, activity_level, goal

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

def display_results(calories, protein_grams, fat_grams, carb_grams, goal):
    """Display the calculated results to the user."""
    print("\n" + "="*50)
    print("YOUR DAILY CALORIE RECOMMENDATIONS")
    print("="*50)
    
    print(f"Goal: {goal.title()} weight")
    print(f"Recommended daily calories: {calories:.0f}")
    print()
    print("Macronutrient breakdown:")
    print(f"• Protein: {protein_grams:.1f} grams")
    print(f"• Fat: {fat_grams:.1f} grams")
    print(f"• Carbohydrates: {carb_grams:.1f} grams")
    print()
    print("Remember: These are estimates. Consult a healthcare")
    print("professional for personalized nutrition advice.")

def main():
    """Main function that runs the calorie calculator."""
    try:
        # Get user information
        sex, age, weight, height, activity_level, goal = get_user_info()
        
        # Calculate BMR
        bmr = calculate_bmr(sex, age, weight, height)
        print(f"\nYour BMR (Basal Metabolic Rate): {bmr:.0f} calories")
        
        # Calculate TDEE
        tdee = calculate_tdee(bmr, activity_level)
        print(f"Your TDEE (Total Daily Energy Expenditure): {tdee:.0f} calories")
        
        # Adjust for goal
        daily_calories = adjust_for_goal(tdee, goal)
        
        # Calculate macronutrients
        protein_grams, fat_grams, carb_grams = calculate_macros(daily_calories, weight)
        
        # Display results
        display_results(daily_calories, protein_grams, fat_grams, carb_grams, goal)
        
    except ValueError:
        print("Error: Please enter valid numbers for age, weight, and height.")
    except KeyboardInterrupt:
        print("\nCalculator stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
