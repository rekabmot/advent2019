start = 146810
end = 612564

matches = 0

def check(i):
  digits = list(str(i))
  
  digit_counts = {
    digits[0]: 1
  }

  for x in range(1, len(digits)):
    if digits[x] in digit_counts:
      digit_counts[digits[x]] += 1
    else:
      digit_counts[digits[x]] = 1

    if digits[x] < digits[x - 1]:
      return False

  for x in digit_counts.values():
    if x == 2:
      return True
  
  return False

for i in range(start, end):
  if check(i):
    matches += 1

print(matches)