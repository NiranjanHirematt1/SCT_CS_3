# Password Strength Checker 🔐

A simple Python script that checks the strength of a password based on various security factors, including length, character variety, and presence of special characters. This project helps users assess and improve the security of their passwords.

## Features
- **Password Analysis**: Evaluates password length and types of characters used (uppercase, lowercase, digits, and special characters).
- **Strength Scoring**: Rates the password as "Weak," "Moderate," or "Strong" based on its composition.

## How It Works
1. **Length Check**: Longer passwords generally improve strength; this checker awards points for passwords 8 characters and above.
2. **Character Diversity**:
   - Checks for uppercase letters, lowercase letters, digits, and special characters.
   - Points are added to the strength score based on the presence of these different types.
3. **Final Rating**: A cumulative score translates into a "Weak," "Moderate," or "Strong" rating, guiding users to create more secure passwords.

## Requirements
- Python 3.x

## Installation
Clone this repository and navigate to the project folder:
```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker


Enter your password: Password123!
Password strength: Strong


License
This project is open-source and available under the MIT License.