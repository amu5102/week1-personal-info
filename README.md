# Personal Information Manager

## Project Description

This is my first Python project! It's a program that stores and displays personal information. It demonstrates Python variables, input/output, string formatting, and basic validation.

## Project Overview and Objectives

The goal is to create a beginner-friendly command-line application that stores profile information, asks the user for additional details, validates input, calculates age in months, and prints a neatly formatted profile.

## What I Learned

1. **Variables**: How to store different types of data.
2. **Input/Output**: Getting user input and displaying results.
3. **String Formatting**: Using f-strings to create nice output.
4. **Error Handling**: Basic validation for user input.

## How to Run This Program

1. Make sure Python 3.10 or newer is installed.
2. Open terminal/command prompt.
3. Navigate to the project folder.
4. Run: `python personal_info.py`
5. Follow the prompts to enter your information.

On Windows, if `python` is not recognized, try `py personal_info.py`.

## Features

- Stores static information (name, city, and hobby) and collects age.
- Gets dynamic information from the user (favorite food and color).
- Displays all information in a formatted way.
- Validates empty and overly long text input.
- Checks that age is a whole number between 1 and 120.
- Calculates age in months.
- Uses comments, functions, f-strings, and string methods.

## Code Structure

```text
week1-personal-info/
├── personal_info.py
└── README.md
```

- `personal_info.py`: contains input validation functions and the main program.
- `README.md`: explains the project, setup, features, testing, and learning outcomes.

## Sample Output

The example below illustrates the expected output. Your actual age and answers will depend on the values you enter.

```text
============================================
       PERSONAL INFORMATION MANAGER
============================================
Let's create your personal information profile.

Enter your age in years: 25
What's your favorite food? Pizza
What's your favorite color? Blue

============================================
             YOUR INFORMATION
============================================
Name:           Amruta Jadhav
Age:            25 years (300 months)
City:           Pune
Hobby:          Learning Python
Favorite Food:  Pizza
Favorite Color: Blue
--------------------------------------------
Thank you for using the Personal Information Manager!
Goodbye!
============================================
```

## Testing and Validation

| Test case | Expected result |
|---|---|
| Valid age, food, and color | Profile is displayed; age is multiplied by 12 |
| Empty favorite food or color | Program displays a message and asks again |
| Non-numeric age such as `abc` | Program asks for a whole number |
| Age `0` or greater than `120` | Program asks for an age from 1 to 120 |
| Whitespace-only response | Treated as empty |
| More than 100 characters for food or color | Program rejects the entry and asks again |

## Challenges & Solutions

**Challenge**: User might enter empty input.  
**Solution**: The program uses `.strip()` and repeats the prompt when the value is empty.

**Challenge**: Formatting the output nicely.  
**Solution**: Used f-strings, string methods, and separators for readable output.

**Challenge**: The age might not be a valid number.  
**Solution**: Used `try/except` and range validation to handle invalid age input.

## Screenshots of Working Application

**Before submission:** Run `personal_info.py` in VS Code or Command Prompt and insert a real screenshot showing the entered values and formatted output here. A second screenshot showing an invalid or empty input being rejected is recommended. The sample output above is illustrative and is not a screenshot of a live run.

## Technical Requirements Checklist

- [x] At least four pieces of personal information are stored or displayed.
- [x] At least two pieces of information are requested from the user.
- [x] Information is displayed in a readable format.
- [x] Comments explain the code.
- [x] Basic input validation is implemented.
- [x] String methods and f-strings are used.
- [x] Age in months is calculated.
- [x] Setup instructions and test cases are documented.

## Learning Outcomes

This project practices variables, strings, integers, input/output, arithmetic, comments, functions, loops, exception handling, input validation, and formatted output.
