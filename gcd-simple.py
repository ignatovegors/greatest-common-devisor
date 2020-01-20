def gcd_simple(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a,b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d


def main():
    a, b = map(int, input().split())
    print(gcd_simple(a, b))


if __name__ == "__main__":
    main()
