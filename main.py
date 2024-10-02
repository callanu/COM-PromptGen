import numpy as np
import csv

def modifyExisting():

    print("Which prompt would you like to change?")
    for x in range(len(promptList)):
        print (str(x+1) + " : " + promptList[x])
    
    sel1 = int(input(""))
    newPrompt = input("What would you like the prompt changed to?\n")

    promptList[sel1-1] = newPrompt

    with open('promptArray.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

with open('promptArray.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

flatData = [item for sublist in data for item in sublist]
promptList = np.array(flatData)

stayInLoop = True

while(stayInLoop):
    selection = input("M : Modify Existing Prompt.\nV : View Existing Prompts.\n")

    match selection:
        case "M":
            modifyExisting()
        case "V":
            for x in range(len(promptList)):
                print (str(x+1) + " : " + promptList[x])
        case _:
            print("Your selection doesn't match any of the above options. Try again.")