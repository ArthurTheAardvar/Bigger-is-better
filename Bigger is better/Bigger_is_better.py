cases = int(input()) 

for i in range(cases): #go through the other lines
    line = input()
    
    line = line.split(" ") #split up the line by spaces
    
    line = [int(num) for num in line]
    print(max(line))

   
