# Question 3
def print_odd_triangular_patterns():
    
    try:
        n = int(input("Enter a natural number (n) to generate patterns up to: "))
        if n < 1:
            print("Please enter a positive natural number.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    for current_row_limit in range(1, n + 1):
        if current_row_limit % 2 == 0:
            continue

        current_pattern_elements = []
        for num in range(1, current_row_limit + 1):
            current_pattern_elements.append(str(num))

        print(" ".join(current_pattern_elements))

print_odd_triangular_patterns()