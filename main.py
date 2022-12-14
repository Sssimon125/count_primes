"""This is a simple program to count the number of primes"""


def filter_prime(divisor, number):
    """Return true if number is a potential prime"""
    if number == divisor:
        return True
    if not number % divisor:
        return False
    return True


class Solution:

    def countPrimes(self, n: int) -> int:
        """Return a list of primes >= n"""

        working_list = [i for i in range(2, n)]
        divisor = 2
        while divisor**2 <= n:
            working_list = list(filter(
                lambda x: filter_prime(divisor, x), working_list))
            divisor += 1
        return len(working_list)

    def find_primes(self, n: int) -> int:
        """Return a list of primes >= n"""

        working_list = [i for i in range(2, n)]
        divisor = 2
        for i in working_list:
            if divisor**2 <= n:
                working_list = list(filter(
                    lambda x: filter_prime(divisor, x), working_list))
                if i/divisor != 1:
                    divisor = i
        return len(working_list)


solution = Solution()
print('output', (solution.find_primes(300)))
print('output', (solution.countPrimes(300)))


# print(filter_prime(2, 2))
# print(filter_prime(2, 3))
# print(filter_prime(2, 4))
# print(filter_prime(3, 9))
