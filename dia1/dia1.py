#Open input
filename = 'input.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]
#Just test the input
#for line in lines:
#  print(line) 

#Make things
result = 0
for line in lines:
  partial_result = 0 
  for i in range(0, len(line), 1):
    try:
      string_int = int(line[i])
      result += string_int * 10
      partial_result += string_int * 10
      break
    except ValueError:
      continue
      
  for j in range (len(line)-1, -1, -1):
    try:
      string_int = int(line[j])
      result += string_int 
      partial_result += string_int
      break
    except ValueError:
      continue
  print(line + " " + str(j) + " " + str(partial_result))
#Print result         
print(result)