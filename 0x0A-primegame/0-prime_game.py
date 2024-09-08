def sieve_of_eratosthenes(max_n):
    """ Generate a list of primes up to max_n using the Sieve of Eratosthenes """
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if (is_prime[p] == True):
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_n + 1) if is_prime[p]]


def isWinner(x, nums):
    """ Return the name of the player who won the most rounds """
    max_n = max(nums) if nums else 0
    primes = sieve_of_eratosthenes(max_n)
    
    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        if n < 2:
            Ben_wins += 1
            continue
        
        # Initialize game state
        is_prime = [True] * (n + 1)
        turn = 0
        
        while True:
            found_move = False
            for prime in primes:
                if prime > n:
                    break
                if is_prime[prime]:
                    found_move = True
                    for multiple in range(prime, n + 1, prime):
                        is_prime[multiple] = False
                    turn += 1
                    break
            
            if not found_move:
                break
        
        if turn % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1
    
    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
