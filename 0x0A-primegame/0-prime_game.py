#!/usr/bin/python3
""" Prime Game """


def isprime(n):
    """ Return True if n is a prime number, else False """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def delete_numbers(n, nums):
    """ Remove numbers divisible by n from nums, set to zero """
    nums[:] = [0 if x % n == 0 else x for x in nums]


def isWinner(x, nums):
    """ Return the name of the player that won the most rounds """
    Maria, Ben = 0, 0

    for game in range(x):
        nums2 = list(range(1, nums[game] + 1))
        turn = 0
        
        while True:
            change = False
            for n in nums2:
                if n > 1 and isprime(n):
                    delete_numbers(n, nums2)
                    change = True
                    turn += 1
                    break

            if not change:
                break
        
        if turn % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
