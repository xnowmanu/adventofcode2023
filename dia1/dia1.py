#Open input
filename = 'input.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]
#Just test the input
#for line in lines:
#  print(line) 

#Make things

digits = {
"one" : 1,
"two" : 2,
"three" : 3,
"four" : 4,
"five" : 5,
"six" : 6,
"seven" : 7,
"eight" : 8,
"nine" : 9,
"0" : 0,
"1" : 1,
"2" : 2,
"3" : 3,
"4" : 4,
"5" : 5,
"6" : 6,
"7" : 7,
"8" : 8,
"9" : 9
}

result = 0

for line in lines:
  found = 0
  partial_result = ""
  miniresult = 0
  print(line)
  for i in range(0, len(line), 1):
    try:
      string_int = int(line[i])
      result += string_int * 10
      break
    except ValueError:
      partial_result = partial_result + line[i]
      for key in digits:
        if partial_result.__contains__(key) :
          string_int = digits[key]
          found = 1
          break
      if found == 1 :
        result += string_int * 10
        found = 0
        miniresult += string_int * 10
        break

      continue

  found = 0
  partial_result = ""
  for j in range (len(line)-1, -1, -1):
    try:
      string_int = int(line[j])
      result += string_int 
      break
    except ValueError:
      partial_result = line[j] + partial_result
      for key in digits:
        if partial_result.__contains__(key) :
          string_int = digits[key]
          found = 1
          break
      if found == 1 :
        result += string_int
        found = 0
        miniresult += string_int
        break
      
      continue
  print(miniresult)
#Print result         
print(result)