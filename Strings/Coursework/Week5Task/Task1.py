def even_sum(n):
    total_sum = 0

    for i in range(0, n+1, 2):
        if i == 0:
            continue
        else:
            total_sum += i

n = int(input("Enter a number: "))

result = even_sum(n)
print(f'The sum of all the even numbers from 1 to {n} is {result}')

if __name__ == '__main__':
    even_sum(20)

    wrong