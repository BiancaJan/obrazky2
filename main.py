from PIL import Image

v = int(input("Vyska pyramidy"))

pic = Image.new("RGB",(2*v-1,v),(255,255,255))
pixels = pic.load()
for i in range(1,v+1):
    px = v-i
    py = i-1
    for j in range(0,2*i-1):
        pixels[px+j,py] = (0,0,0)
#pic.show()

from PIL import Image

v = int(input("Vyska pyramidy"))

image = Image.new("RGB",(v,v),(255,255,255))
pixels = image.load()
for i in range(1,v+1):
    px = v-i
    py = i-1
    for j in range(0, i):
        pixels[px+j,py] = (0,0,0)
#image.show()

from PIL import Image

v = int(input("Vyska pyramidy"))

image1 = Image.new("RGB",(2*v+1,v),(255,255,255))
pixels = image1.load()
for i in range(1,v+1):
    px = v- i
    py = i-1
    for j in range(0,2*i-1):
        pixels[px+j,py]=(0,0,0)
    for y in range(v):
        for x in range(v-1,2*v-1):
            pixels[x,y] = (255,255,255)

#image1.show()

from PIL import Image, ImageDraw
width, height = 300, 300
diamond = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(diamond)
points_triangle1 = [(width // 2, 0), (width - 1, height // 2), (0, height // 2)]
points_triangle2 = [(width // 2, height), (width - 1, height // 2), (0, height // 2)]
draw.polygon(points_triangle1, fill='black')
draw.polygon(points_triangle2, fill='black')
#diamond.show()

from PIL import Image

width = 300
height = 200

white = Image.new('RGB', (width, height // 3), 'white')

# Vytvoriť modrý obdĺžnik
blue = Image.new('RGB', (width, height // 3), '#0052A5')

# Vytvoriť červený obdĺžnik
red = Image.new('RGB', (width, height // 3), '#D52B1E')

# Spojiť obdĺžniky do jedného obrázka
russian_flag = Image.new('RGB', (width, height))
russian_flag.paste(white, (0, 0))
russian_flag.paste(blue, (0, height // 3))
russian_flag.paste(red, (0, 2 * (height // 3)))

# Uložiť obrázok
russian_flag.save('russian_flag.png')

#russian_flag.show()

from PIL import Image

v = int(input("výška vlajky: "))

image = Image.new("RGB", (3*v, 2*v), "white")
pixels = image.load()
for i in range(2*v):
    for j in range(3*v):
        if j < v:  # Červená časť vlajky
            pixels[j, i] = (255, 0, 0)
        elif j >= v and j < 2*v:  # Biela časť vlajky
            pixels[j, i] = (255, 255, 255)
        else:  # Modrá čiara vlajky
            pixels[j, i] = (0, 0, 255)

#image.show()

from PIL import Image, ImageDraw

# Veľkosť obrázka
width, height = 300, 300

# Vytvoriť biely obrázok
image = Image.new('RGB', (width, height), 'white')

# Vytvoriť objekt ImageDraw
draw = ImageDraw.Draw(image)

# Uhlopriečka
draw.line((0, 0, width, height), fill='black')

# Uložiť obrázok
image.save('half_black_diagonal.png')

# Zobraziť obrázok
image.show()

from PIL import Image, ImageDraw

# Veľkosť obrázka
width, height = 300, 300

# Vytvoriť biely obrázok
image = Image.new('RGB', (width, height), 'white')

# Vytvoriť objekt ImageDraw
draw = ImageDraw.Draw(image)

# Uhlopriečka
draw.line((0, 0, width, height), fill='black')

# Vyfarbenie jednej časti
draw.polygon([(0, 0), (width, 0), (0, height)], fill='blue')

# Uložiť obrázok
image.save('half_colored_diagonal.png')

# Zobraziť obrázok
image.show()

from PIL import Image, ImageDraw

# Veľkosť obrázka
width, height = 300, 300

# Vytvoriť biely obrázok
image = Image.new('RGB', (width, height), 'white')

# Vytvoriť objekt ImageDraw
draw = ImageDraw.Draw(image)

# Nakresliť horizontálnu čiaru
draw.line([(0, height // 2), (width, height // 2)], fill='black', width=5)

# Nakresliť vertikálnu čiaru
draw.line([(width // 2, 0), (width // 2, height)], fill='black', width=5)

# Uložiť obrázok
image.save('plus.png')

# Zobraziť obrázok
image.show()
