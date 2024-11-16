def modular_exponentiation(A, B, M):
    result = 1  # Initialize result
    A = A % M   # Update A to be A % M

    while B > 0:
        # If B is odd, multiply A with the result
        if B % 2 == 1:
            result = (result * A) % M
        
        # Now B must be even, so we divide it by 2
        B = B // 2
        A = (A * A) % M  # Square A and reduce it modulo M

    return result

# Input
A, B, M = map(int, input("Enter A, B, M separated by spaces: ").split())

# Output
print(modular_exponentiation(A, B, M))
