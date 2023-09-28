def spam_confidence(line):
    i = line.find(":") + 1
    return float(line[i:])


CHECK = "X-DSPAM-Confidence:"

while True:
    try:
        fname = input("Enter file name: ")
        with open(fname) as fh:
            count = 0
            tot = 0.0

            for line in fh:
                if not line.startswith(CHECK):
                    continue
                count += 1
                tot += spam_confidence(line)

        print("Average spam confidence:", tot / count)
        exit(0)

    except FileNotFoundError:
        print("That file does not exist. Try again.")
        continue

    except ValueError:
        print("Cannot convert string to float")
        exit(1)
