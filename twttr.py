t=input("input: ")
output=""
for char in text:
  if char.lower() not in ["a","e","i","o","u"]:
    output=output + char
print("output",output)
