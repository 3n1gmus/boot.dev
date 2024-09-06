def fizzbuzz(start, end):
    for i in range(start, end + 1):
        output = ""
        if i % 3 == 0:
            output += "fizz"
        if i % 5 == 0:
            output += "buzz"
        elif output == "":
            output = i
        print(output)


# Don't Touch Below This Line


def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()