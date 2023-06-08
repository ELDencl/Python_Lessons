data = open("text.txt", encoding='utf-8')
print(data)

print(data.readlines())

data.close



data = open("text.txt",mode='r', encoding='utf-8')
data.write('Третья запись \n')
data.close
