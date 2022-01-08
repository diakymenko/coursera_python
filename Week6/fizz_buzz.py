def fizz_buzz(n):
    if 0 < n < 2 * 10 ** 5:
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    else:
        print("NONE")

n = int(input())
fizz_buzz(n)

