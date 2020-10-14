print("THIS PROGRAM ISN'T BULLETPROOF AND WILL BREAK IF THE INPUT ISN'T AS INTENDED. THIS WAS WRITTEN IN 10 MINUTES WITH THE PURPOSE OF.... I DON'T KNOW \n")
print("also pls use python3 or else pins starting with the number 0 won't work ehehehe not my fault tho\n\n")

print("please insert your 4 digit PIN. The program will only store your PIN for validation purposes\n")

answ = list(str(input()))
sol = list('0000')

while (sol != answ):
    if(sol[3] == '9'):
        sol[3] = '0'
        if(sol[2] == '9'):
            sol[2] = '0'
            if(sol[1] == '9'):
                sol[1] = '0'
                if(sol[0] == '9'):
                    print("sorry :(")
                    exit()
                else:
                    sol[0] = str(int(sol[0])+1)
            else:
                sol[1] = str(int(sol[1])+1)
        else:
            sol[2] = str(int(sol[2])+1)
    else:
        sol[3] = str(int(sol[3])+1)
    print("\n TRYING "+ str(sol[0])+ str(sol[1])+ str(sol[2])+ str(sol[3]) + "...")


print("\n\n\nPIN CRACKED!!!!!!! SOLUTION: " + str(sol) + "\n\n\nPIN (from original input): " + str(answ))