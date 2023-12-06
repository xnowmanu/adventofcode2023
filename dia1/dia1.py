#Open input
filename = 'input_test.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]
#Just test the input
for line in lines:
  print(line) 

#Make things
result = 0
for line in lines:
  for i in range(0, len(line)-1, 1):
    if int(line[i]) != 0: 
      result += int(line[i]) * 10
      break
  for j in range (len(line)-1, 0, -1):
    
    if int(line[j]) != 0:
      result += int(line[j])
      break
  
#Print result         
print(result)