from functions import printMatrix, finalFunction, clearScreen

def hamming(seqA, seqB):
    if( len(seqA) != len(seqB)):
        print("Sequence length is different")
        return 

    dif = 0

    for i in range(0, len(seqA)):
        if( seqA[i] != seqB[i] ):
            dif += 1
    
    print("Difference = ", dif)
    
    finalFunction()
    clearScreen()
    
    return 