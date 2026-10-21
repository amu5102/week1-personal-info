# Name: Amruta Jadhav
# Project: Week 1 - Personal Information Manager
# Description: Collects and displays personal information with basic input validation.

def get_non_empty_input(prompt, field_name):
    """Ask until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            # Limit very long entries to keep the display readable.
            if len(value) > 100:
                print(f"{field_name} is too long. Please use 100 characters or fewer.")
                continue
            return value
        print(f"{field_name} cannot be empty. Please try again.")


def get_valid_age():
    """Ask for an age that is a positive whole number."""
    while True:
        age_text = input("Enter your age in years: ").strip()
        try:
            age = int(age_text)
            if 0 < age <= 120:
                return age
            print("Please enter an age between 1 and 120.")
        except ValueError:
            print("Invalid age. Please enter a whole number, such as 24.")


def main():
    # Welcome message.
    print("=" * 44)
    print("       PERSONAL INFORMATION MANAGER")
    print("=" * 44)
    print("Let's create your personal information profile.\\n")

    # Static information stored in variables.
    name = "Amruta Jadhav"
    city = "Pune"
    hobby = "Learning Python"

    # Dynamic information collected and validated.
    age = get_valid_age()
    favorite_food = get_non_empty_input("What's your favorite food? ", "Favorite food")
    favorite_color = get_non_empty_input("What's your favorite color? ", "Favorite color")

    # Calculate age in months.
    age_in_months = age * 12

    # Display information using f-strings and string methods.
    print("\\n" + "=" * 44)
    print("             YOUR INFORMATION")
    print("=" * 44)
    print(f"Name:           {name.strip().title()}")
    print(f"Age:            {age} years ({age_in_months} months)")
    print(f"City:           {city.strip().title()}")
    print(f"Hobby:          {hobby.strip().title()}")
    print(f"Favorite Food:  {favorite_food.strip().title()}")
    print(f"Favorite Color: {favorite_color.strip().title()}")
    print("-" * 44)
    print("Thank you for using the Personal Information Manager!")
    print("Goodbye!")
    print("=" * 44)


if __name__ == "__main__":
    main()
