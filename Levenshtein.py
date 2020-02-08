from numpy import array,zeros
import functions as func

def levenshtein(seqA, seqB):
    
    if(len(seqA) != len(seqB)):
        print("Tamanho da sequência diferente!")
        return

    result = zeros(( len(seqA) + 1, len(seqB) +1))

    for i in range(0, len(seqA) + 1):
        result[i][0] = i

    for i in range(0, len(seqB) + 1):
        result[0][i] = i

    sum = 0
    
    for i in range(1, len(seqA) + 1):
        for j in range(1, len(seqB) + 1):

            if seqA[i - 1] == seqB[j - 1]:
                sum = 0
            else:
                sum = 1
            
            result[i][j] = min(result[i-1][j] + 1, 
                                min(result[i][j-1] + 1, 
                                result[i-1][j-1] + sum))
    
    print("Matrix:")
    func.printMatrix(result)
    
    print("\nResult = ", result[len(seqA)][len(seqB)])
    func.finalFunction()
    func.clearScreen()