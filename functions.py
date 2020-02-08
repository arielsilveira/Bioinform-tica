import subprocess, platform

def clearScreen():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
    else: #Linux and Mac
        print("\033c", end="")

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], " ", end="")
            
        print()

def finalFunction():
    print("Press Enter for exit!")
    enter = input()

    if(enter == ''):
        return
    
    while(enter != ''):
        print("Press Enter for exit!")
        enter = input()
    
    return