from PIL import Image
import numpy as np

image_name = input("nome da imagem: ")
img1 = Image.open(image_name).convert('L')


width, height = img1.size
proportion = height / width
if height > 1000:
    img1 = img1.resize((int(height / 5), int(width / 2.5  * proportion)))
    width, height = img1.size
print(img1.size)
img1.save('greyscale.png')
img = Image.open("greyscale.png").convert("L")
val_data = list(img.getdata())
arr = np.array(val_data).reshape(height, width)
arr = arr.tolist()

lighting = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|?-_+~<>i!lI;:,"^`'.  """
lighting_dark = lighting[::-1]
arr = [[int(i / 4) for i in j]for j in arr]
arr = list(arr)

ascii_text = ""
for i in arr:
    for j in i:
        ascii_text += lighting_dark[j] + lighting_dark[j]
    ascii_text += "\n"

with open("ascii_dark.txt", 'w') as file:
    file.write(ascii_text)
ascii_text = ""
for i in arr:
    for j in i:
        ascii_text += lighting[j] + lighting[j]
    ascii_text += "\n"

with open("ascii_light.txt", 'w') as file:
    file.write(ascii_text)
