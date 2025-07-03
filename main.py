from mean_var_std import calculate

# Sample test input for development
if _name_ == '_main_':
    test_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    try:
        result = calculate(test_input)
        print("Calculation successful:\n")
        for key, value in result.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
