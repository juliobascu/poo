from PIL import Image

ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

lista=[]
def main(img):
    image = Image.open(img)
    # you can first resize the image if needed
    # image = image.resize((width, height))
    ascii_art = convert_to_ascii_art(image)
    # save_as_text(ascii_art)
    z=" ".join(ascii_art)
    x='"""'+z+'"""'
    lista.append(x)


def convert_to_ascii_art(image):
    ascii_art = []
    (width, height) = 80,80
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convert_pixel_to_character(px)
        ascii_art.append(line)
    return ascii_art


def convert_pixel_to_character(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return ascii_characters_by_surface[index]


def save_as_text(ascii_art):
    with open("image.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
        file.close()


# if __name__ == '__main__':
cont=18
ext=".png"
for i in range(38):
    ruta="C:/Users/Jawy/Desktop/poke video/"+str(cont)+ext
    main(ruta)
    cont=int(cont)
    cont+=1

for i in lista:
    print(i)