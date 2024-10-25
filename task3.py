import re

def check_password_strength(password):
    strength_score = 0
    

    if len(password) >= 8:
        strength_score += 1
    if len(password) >= 12:
        strength_score += 1
    
    
    if re.search(r'[a-z]', password): 
        strength_score += 1
    if re.search(r'[A-Z]', password): 
        strength_score += 1
    if re.search(r'[0-9]', password):  
        strength_score += 1
    if re.search(r'[@$!%*?&#]', password):  
        strength_score += 1
    
   
    if strength_score <= 2:
        return "Weak"
    elif strength_score <= 4:
        return "Moderate"
    else:
        return "Strong"

# Test the function
password = input("Enter your password: ")
print(f"Password strength: {check_password_strength(password)}")
