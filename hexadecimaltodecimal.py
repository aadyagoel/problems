#hexadecimal conversion to decimal
def h2d(number):
  answer = []
  dictionary = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15:'F'}
  if number < 16:
    if number <= 9:
      answer[0] = number
    else:
      answer[0] = dictionary[number]
  quotient = number
  while quotient >= 16:
    remainder = quotient%16
    if remainder <= 9:
      answer.append(remainder)
    else:
      answer.append(dictionary[remainder])
    quotient = quotient//16
  
  if quotient <= 9:
    answer.append(quotient)
  else:
    answer.append(dictionary[quotient])
  answer.reverse()
  print(answer)

h2d(204)