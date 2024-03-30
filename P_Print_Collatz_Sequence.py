def collatz_conjecture(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

def print_collatz_sequence(m):
    for i in range(1, m + 1):
        print(*collatz_conjecture(i), sep=', ')

m = int(input("Nhập vào số nguyên dương m: "))
print_collatz_sequence(m)

