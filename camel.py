camel_cased=input("camelcase: ")
snake_cased=""
for char in camel_cased:
   if char.isupper():
      snake_cased=snake_cased+"_"+char.lower()
   else:
    snake_cased=snake_cased+char
print("snake_case:",snake_cased)
