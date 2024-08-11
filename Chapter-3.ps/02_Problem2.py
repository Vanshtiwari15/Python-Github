letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Vansh").replace("<|Date|>", "24 Jan,2027"))