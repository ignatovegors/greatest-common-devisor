def gcd_euclid(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd_euclid(a % b, b)
    else:
        return gcd_euclid(a, b % a)


def main():
    a, b = map(int, input().split())
    print(gcd_euclid(a, b))


if __name__ == "__main__":
    main()
