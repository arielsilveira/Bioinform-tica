import sys
from Hamming import hamming
from Levenshtein import levenshtein
from SmithWaterman import smithWaterman
from NeedlemanWusch import needlemanWusch
from Blast import blast
import functions as func

def algorithm(option, dna_seq):
    if( option == 1):
        hamming(dna_seq[0], dna_seq[1])
    if( option == 2):
        levenshtein(dna_seq[0], dna_seq[1])
    if( option == 3):
        smithWaterman(dna_seq[0], dna_seq[1])
    if( option == 4):
        needlemanWusch(dna_seq[0], dna_seq[1])
    if( option == 5):
        blast(dna_seq[0], dna_seq[1])

    return 

def main():
    if len(sys.argv) != 2:
        print("python3 main.py file_name")
        EOFError()
        exit()

    dna_seq = []

    with open(sys.argv[1]) as file:
        for line in file:
            seq = line.strip()
            dna_seq.append(seq)

    option = 1

    while(option != 0):
        print("Escolha os diferentes algoritmos abaixo!")
        print("1 - Hamming")
        print("2 - Levenshtein")
        print("3 - Smith-Waterman")
        print("4 - NeedlemanWusch")
        print("5 - Blast")
        print("0 - Exit")

        option = int(input())
        func.clearScreen()

        if(option > 5 or option < 0):
            print("Erro na escolha do algoritmo! Favor tentar novamente.")
            print()
        else:
            algorithm(option, dna_seq)

if __name__ == "__main__":
    main()