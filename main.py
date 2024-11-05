import sympy as sp
import time
import regex as re


def main():
    """
    Main function that displays the menu, gets the user's tool choice, and calls the
    appropriate function based on the selected tool. Also displays a thank-you message.
    """
    print("-" * 50)
    if not main_welcome():
        return
    print("-" * 50)
    main_menu()
    tool = input("Enter your choice: ")
    main_menu_logic(tool)
    print("-" * 50)
    print("Thank you for using Discrete Math Solutions!")
    print("-" * 50)


def combinatorics():
    """
    Combinatorics tool that calculates permutations and combinations of 'n' items taken 'r' at a time.
    Prompts the user to enter values for 'n' and 'r', validates the input, and displays results based on
    the user's choice. Allows users to exit by typing 'exit'.
    """
    data = {"n": 0, "r": 0}
    choice = ""

    combinatorics_intro()

    n = get_valid_int("Enter the value of n: ")
    if n == False:
        return

    r = get_valid_int("Enter the value of r: ")
    if r == False:
        return

    data["n"] = int(n)
    data["r"] = int(r)

    permutations = "[Result of Permutations]"
    combinations = "[Result of Combinations]"

    # Loop twice to allow the user to calculate both permutations and combinations
    for i in range(3):
        if i == 2:
            print("NOTE: You get one more chance to calculate the other operation.")
        combinatorics_menu(n, r)
        # Loop until the user selects a valid option
        while choice not in ["1", "2"]:
            choice = input("Enter your choice: ")
            start = time.time()
            if choice == "1":
                print(f"Permutations of {n} and {r} is {permutations}\n")
                responsiveness(start, time.time())
            elif choice == "2":
                print(f"Combinations of {n} and {r} is {combinations}\n")
                responsiveness(start, time.time())
            elif choice.lower() == "exit":
                return
            else:
                print("Invalid choice. Please select a valid option.")
        choice = ""

    more_details("Combinatorics")


def truth_table():
    """
    Truth Table tool that generates a truth table for logical propositions.
    Prompts the user to enter a logic statement, validates the format, and displays
    the truth table for valid statements. Allows users to exit by typing 'exit'.
    """
    logic = ""
    valid = False

    # Define valid propositions pattern
    valid_propositions = re.compile(
        r"^(¬)?[a-zA-Z] (∧|∨) (¬)?[a-zA-Z]|"
        r"(¬)?[a-zA-Z] → (¬)?[a-zA-Z]|"
        r"(¬)?[a-zA-Z] ↔ (¬)?[a-zA-Z]|"
        r"(¬)?[a-zA-Z]$"
    )

    # Define symbols
    and_symbol = "\u2227"  # ∧
    or_symbol = "\u2228"  # ∨
    not_symbol = "\u00AC"  # ¬
    if_then_symbol = "\u2192"  # →
    iff_symbol = "\u2194"  # ↔

    # Define valid logic operators
    valid_operators = {
        "and": and_symbol,
        "AND": and_symbol,
        "And": and_symbol,
        "^": and_symbol,
        "&": and_symbol,
        "+": and_symbol,
        "or": or_symbol,
        "OR": or_symbol,
        "Or": or_symbol,
        "v": or_symbol,
        "V": or_symbol,
        "|": or_symbol,
        "<->": iff_symbol,
        "iff": iff_symbol,
        "IFF": iff_symbol,
        "Iff": iff_symbol,
        "then": if_then_symbol,
        "THEN": if_then_symbol,
        "Then": if_then_symbol,
        "->": if_then_symbol,
        "not ": not_symbol,
        "NOT ": not_symbol,
        "Not ": not_symbol,
        "!": not_symbol,
        "~": not_symbol,
        "-": not_symbol,
        "if ": "",
        "IF ": "",
        "If ": "",
    }

    truth_table_intro()

    # Loop until a valid logic statement is entered or the user types 'exit'
    while not valid:
        logic = input("\nLogic Statement: ")
        start_time = time.time()  # Start the timer

        # Exit the function if the user types 'exit'
        if logic.lower() == "exit":
            return

        # Replace all valid operators with their symbols
        for key, symbol in valid_operators.items():
            logic = logic.replace(key, symbol)

        # Check if the entire modified logic statement is valid
        if valid_propositions.match(logic):
            valid = True  # Valid input; exit the loop
        else:
            print("Invalid operator or proposition. Please enter a valid statement.")

    print(f"\nTruth table for {logic}:")
    responsiveness(start_time, time.time())  # Calculate responsiveness

    more_details("Truth Tables")


def set_checker():
    """
    Set Checker tool that checks if one set is a subset or superset of another.
    Prompts the user to enter two sets, validates the input, and determines
    subset/superset relationships. Allows users to exit by typing 'exit'.
    """
    valid = False
    data = {"set1": [], "set2": []}

    # Regex pattern for a valid set format (comma-separated list of integers)
    valid_set = re.compile(r"^\d+(,\s*\d+)*$")

    set_checker_intro()

    set1 = get_valid_set("Enter the first set: ", valid_set)
    if set1 == False:
        return
    set2 = get_valid_set("Enter the second set: ", valid_set)
    if set2 == False:
        return

    start_time = time.time()  # Start the timer

    data["set1"] = parse_set(set1)
    data["set2"] = parse_set(set2)

    response = "[Result of Set Checker]"
    print(f"\n{response}\n")
    responsiveness(start_time, time.time())  # Calculate responsiveness

    more_details("Sets")


def main_welcome():
    """
    Displays an introduction to the main menu.
    """
    title = "Discrete Math Solutions"
    print(f"\t  {title}\n")
    print("Welcome to the Discrete Mathematics Solutions Tools!\n")
    print("This program has a Combinatorics Calculator,")
    print("a Truth Table Generator, and a Set Subset")
    print("and Superset Checker tool.\n")
    print("Each tool will guide you through the process and provide")
    print("solutions for valid inputs in less than one second.\n\n")
    print('Enter "+" for more details about Discrete Math.\n')
    print('To get started, press enter or type "exit" to quit.\n\n')

    user_input = "n/a"

    while user_input == "n/a":
        user_input = input()
        if user_input == "":
            print("Great! Let's get started...\n")
            return True
        elif user_input.lower() == "exit":
            return False
        elif user_input == "+":
            more_details("Discrete Math", True)
            print("\nTo get started, press enter or type 'exit' to quit.\n\n")
            user_input = "n/a"
        else:
            return True


def main_menu():
    """
    Displays the main menu for Discrete Math Solutions, allowing the user to
    select a tool: Combinatorics, Truth Table, Set Checker, or Exit.
    """
    title = "Discrete Math Tools\n"
    print(title)
    print("Please select the tool you want to use:\n")
    print("1. Combinatorics  <--- Calculate permutations and combinations")
    print("2. Truth Table    <--- Generate a truth table for logical propositions")
    print("3. Set Checker    <--- Check if one set is a subset or superset of another")
    print("4. Exit\n")
    print('Enter "+" for more details about Discrete Math.\n')


def main_menu_logic(choice):
    """
    Processes the user's choice from the main menu and calls the corresponding function.
    Loops until the user chooses to exit.
    """
    while choice != "4":
        if choice == "1":
            print("-" * 50)
            combinatorics()
            print("-" * 50)
        elif choice == "2":
            print("-" * 50)
            truth_table()
            print("-" * 50)
        elif choice == "3":
            print("-" * 50)
            set_checker()
            print("-" * 50)
        elif choice == "+":
            more_details("Discrete Math", True)
            print("-" * 50)
        elif choice.lower() == "exit":
            return
        else:
            print("\nInvalid choice. Please select a valid option.")
        main_menu()
        choice = input("Enter your choice: ")


def combinatorics_intro():
    """
    Displays an introduction to the Combinatorics tool.
    """
    print("Welcome to the Combinatorics Tool!\n")
    print(
        "This tool will calculate permutations and combinations of n items taken r at a time.\n"
    )
    print('Type "exit" at any time to return to the main menu.\n\n')


def combinatorics_menu(n, r):
    """
    Displays the operation options for the Combinatorics tool.
    """
    print(f"\nOperation options to perform on {n} and {r}:")
    print("1. Permutations")
    print("2. Combinations\n")


def truth_table_intro():
    """
    Displays an introduction to the Truth Table tool.
    """
    print("Welcome to the Truth Table Generator!\n")
    print("Here are some logical operators and their symbols:")
    print(f"{'Logic:':<20}{'Symbol:':<10}{'Example:':<20}")

    options = {
        "Logic": ["AND", "OR", "NOT", "IF THEN", "IF AND ONLY IF"],
        "Symbols": ["∧", "∨", "¬", "→", "↔"],
        "Example": ["P and Q", "P or Q", "not P", "if P then Q", "P iff Q"],
    }

    for i in range(len(options["Logic"])):
        print(
            f"{options['Logic'][i]:<20}{options['Symbols'][i]:<10}{options['Example'][i]:<20}"
        )

    print("\n\nEnter a logic statement as shown in the examples above.\n")
    print('Type "exit" at any time to return to the main menu.\n')


def set_checker_intro():
    """
    Displays an introduction to the Set Checker tool.
    """
    example = '(e.g., "1, 2, 3, 4")'

    print("Welcome to the Set Checker Tool!\n")
    print(
        f"Enter two sets to check if one is a subset or superset of the other {example}.\n"
    )
    print('Type "exit" at any time to return to the main menu.\n\n')


def get_valid_int(prompt):
    """
    Prompts the user to enter a positive integer. If the user inputs 'exit', returns False.
    Ensures valid integer input; otherwise, prompts again.
    """
    var = input(prompt)
    while not var.isdigit():
        if not var.isdigit() and var.lower() != "exit":
            print("Invalid input. Please enter a positive integer.")
            var = input(prompt)
        elif var.lower() == "exit":
            return False
    return var


def get_valid_set(prompt, valid_set):
    """
    Prompts the user to enter a set of integers. If the user inputs 'exit', returns False.
    Ensures valid set input; otherwise, prompts again.
    """
    var = input(prompt)
    while not valid_set.match(var):
        if not valid_set.match(var) and var.lower() != "exit":
            print("Invalid input. Please enter a set of integers separated by commas.")
            var = input(prompt)
        elif var.lower() == "exit":
            return False
    return var


def parse_set(set_str):
    """
    Parses a comma-separated string of integers and converts each element to an integer.
    Returns a list of integers.
    """
    return [int(x.strip()) for x in set_str.split(",")]


def responsiveness(start_time, end_time):
    """
    Calculates and prints the time taken for an operation to complete, showing responsiveness.
    """
    print(f"Time taken: {round(end_time - start_time, 3)} seconds\n")


def more_details(x, flag=False):
    """
    Displays more details about the Combinatorics tool.
    """
    if flag == False:
        choice = input(f"Would you like more details about {x}? (y/n): ")
    elif flag == True:
        choice = "y"

    if choice.lower() == "y":
        if x == "Discrete Math":
            print(
                "\nDiscrete mathematics is the study of mathematical structures that are fundamentally"
            )
            print("discrete rather than continuous.\n")
            print(
                "It includes the study of mathematical objects that can assume only distinct, separated values."
            )
            print(
                "Discrete objects can be characterized by integers, whereas continuous objects require"
            )
            print("real numbers.\n")
            print(
                "Discrete mathematics has applications in computer science, cryptography, and combinatorics.\n"
            )
            print(
                "The tools in this program provide solutions to common problems in discrete mathematics.\n"
            )
        elif x == "Combinatorics":
            print(
                "\nCombinatorics is a branch of mathematics that deals with counting,"
            )
            print(
                "especially when it comes to the number of ways a particular event can occur.\n"
            )
            print(
                "Permutations and combinations are two fundamental concepts in combinatorics.\n"
            )
            print(
                "Permutations refer to the arrangement of objects in a particular order,"
            )
            print(
                "while combinations refer to the selection of objects without considering the order.\n"
            )
            print(
                "For example, the number of ways to arrange 3 different books on a shelf is a permutation,"
            )
            print(
                "while the number of ways to select 2 books from a set of 5 books is a combination.\n"
            )
            print(
                "Combinatorics has applications in various fields, including computer science,"
            )
            print("probability theory, and cryptography.\n")
            print(
                "To calculate permutations and combinations, enter the values of 'n' and 'r'."
            )
            print(
                "The tool will then provide you with the results for both permutations and combinations.\n"
            )
        elif x == "Truth Tables":
            print(
                "\nA truth table is a mathematical table used in logic to determine the truth values of"
            )
            print("a complex statement based on the truth values of its components.\n")
            print(
                "It shows all possible truth values for a given logical expression.\n"
            )
            print(
                "Truth tables are used to evaluate the validity of arguments, to determine the truth values"
            )
            print("of compound statements, and to simplify logical expressions.\n")
            print(
                "To generate a truth table, enter a logical proposition using valid logical operators."
            )
            print(
                "The tool will then display the truth table for the given proposition.\n"
            )
        elif x == "Sets":
            print(
                "\nA set is a collection of distinct objects, considered as an object in its own right.\n"
            )
            print(
                "In set theory, one set is said to be a subset of another if every element of the first set"
            )
            print("is also an element of the second set.\n")
            print(
                "Conversely, one set is said to be a superset of another if every element of the second set"
            )
            print("is also an element of the first set.\n")
            print(
                "To check if one set is a subset or superset of another, enter the two sets."
            )
            print(
                "The tool will then determine the relationship between the two sets.\n"
            )
    elif choice.lower() != "n" or choice.lower() != "exit":
        print("Response not recognized. Returning to the main menu.")


if __name__ == "__main__":
    main()
