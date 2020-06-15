import random
import httplib2
import ch_sets

print('Парсер imgur 1.0')
count = int(input('Количество картинок: '))
for image in range(0, count):
    address_list = random.choices(ch_sets.symbols, k=5)
    address = ''
    for symbol in address_list:
        address += symbol

    img = 'https://i.imgur.com/' + address + '.jpg'
    p = httplib2.Http('.cache')
    response, content = p.request(img)
    name = 'out/' + address + '.jpg'
    if response['content-length'] == '503':
        print(image + 1, address, '- провал')
    else:
        print(image + 1, address, '- успех')
        out = open(name, "wb")
        out.write(content)
        out.close()
