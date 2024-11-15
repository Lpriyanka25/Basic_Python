def fibonacci_sequence(n):
    """
    Calculate the Fibonacci sequence up to the nth term.

    Args:
        n (int): Number of terms in the sequence.

    Returns:
        list: Fibonacci sequence up to the nth term.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the first two terms
    fib_sequence = [0, 1]
    
    # Generate the sequence
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence
