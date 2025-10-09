# Wave Height Checker for Nazaré
# This program shows wave height information for Nazaré

import random
import time

def get_wave_height():
    """Get wave height information for Nazaré"""
    
    print("Getting wave data for Nazaré...")
    
    # For learning purposes, we'll simulate realistic wave data
    # In a real program, you would get this from a weather API
    
    # Nazaré is famous for huge waves, so let's simulate realistic conditions
    wave_height = round(random.uniform(0.5, 8.0), 1)  # Random height between 0.5-8 meters
    wave_direction = random.randint(200, 280)  # Typical direction for Nazaré
    wave_period = round(random.uniform(8, 20), 1)  # Wave period in seconds
    
    # Display the wave information
    print("\n" + "="*50)
    print("🌊 NAZARÉ WAVE REPORT 🌊")
    print("="*50)
    print(f"Wave Height: {wave_height} meters")
    print(f"Wave Direction: {wave_direction}°")
    print(f"Wave Period: {wave_period} seconds")
    print("="*50)
    
    # Give a simple interpretation
    if wave_height < 1.0:
        print("🌊 Small waves - Good for beginners!")
    elif wave_height < 2.0:
        print("🌊 Medium waves - Fun surfing conditions!")
    elif wave_height < 4.0:
        print("🌊 Big waves - Experienced surfers only!")
    else:
        print("🌊 HUGE waves - Nazaré giants! 🏄‍♂️")
        print("   These are the legendary waves that Nazaré is famous for!")
    
    print(f"\nNote: This is simulated data for learning purposes.")
    print(f"Real wave data would come from weather services or surf reports.")

if __name__ == "__main__":
    print("Welcome to the Nazaré Wave Height Checker!")
    print("This program shows you the current wave conditions in Nazaré, Portugal.")
    print()
    
    get_wave_height()
    
    print("\nWould you like to check again? Just run this program again!")
