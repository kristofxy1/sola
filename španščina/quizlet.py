import sys

def parse_csv(csv_file):
    terms = []
    with open(csv_file, 'r') as file:
        for line in file:
            word, definition = line.strip().split(' - ')
            terms.append((word, definition))
    return terms

def quizlet(csv_file):
    terms = parse_csv(csv_file)
    while True:
        for word, definition in terms:
            answer = input(f"{definition}: ")
            if answer == word:
                print("Pravilno!")
            else:
                print(f"Napačno. Pravilen odgovor je {word}.")
        again = input("Želiš ponoviti quiz? (da/ne) ")
        if again.lower() == "ne":
            break

if len(sys.argv) != 2:
    print("Prosim, vnesi ime datoteke.")
    sys.exit(1)

quizlet(sys.argv[1])

