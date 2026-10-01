from PIL import Image

src = 'imgs/me1.jpg'
out = 'public/images/portrait.png'

img = Image.open(src).convert('RGBA')
background = (252, 253, 248, 255)

pixels = img.load()
width, height = img.size

for y in range(height):
    for x in range(width):
        r, g, b, a = img.getpixel((x, y))
        dist = ((r - background[0]) ** 2 + (g - background[1]) ** 2 + (b - background[2]) ** 2) ** 0.5
        if dist < 35:
            pixels[x, y] = (255, 255, 255, 0)

img.save(out)
print(f'Created {out} ({width}x{height})')
