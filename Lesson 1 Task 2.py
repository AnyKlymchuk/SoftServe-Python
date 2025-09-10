def get_numbers():
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    return a, b

def main():
    a, b = get_numbers()

    # Perform calculations
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    division_result = a / b
    exponentiation_result = a ** b
    floor_division_result = a // b
    modulo_result = a % b

    # Output results
    print("A + B =", sum_result)
    print("A - B =", difference_result)
    print("A * B =", product_result)
    print("A / B =", division_result)
    print("A ** B =", exponentiation_result)
    print("A // B =", floor_division_result)
    print("A % B =", modulo_result)

if __name__ == "__main__":
    main()
