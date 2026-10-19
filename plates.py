def main():
  plate=input("plate: ")
  if is_valid(plate):
    print("valid")
  else:
    print("invalid")
def is_valid(s):
  if not(2<=len(s)<=6 and s[0:2].isalpha()):
    return false
  for char in s:
    if not char.isalnum():
      return false 
  for i in range (len(s)):
    if s[i].isdigit():
      if s[i]=='0':
        return false
      for j in range (i,len(s)):
         if not s[j].isdigit():
            return false
      break
  return True
             
main()
