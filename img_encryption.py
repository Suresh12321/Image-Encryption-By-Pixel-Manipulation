from PIL import Image

def encrypt_image(image_path, key, shift_x, shift_y):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_img = Image.new(img.mode, (width, height))
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            new_x = (x + shift_x) % width
            new_y = (y + shift_y) % height
            encrypted_img.putpixel((new_x, new_y), (r, g, b))
    encrypted_img.save("encrypted_image.png")

def decrypt_image(image_path, key, shift_x, shift_y):
    img = Image.open(image_path)
    width, height = img.size
    decrypted_img = Image.new(img.mode, (width, height))
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            new_x = (x - shift_x) % width
            new_y = (y - shift_y) % height
            decrypted_img.putpixel((new_x, new_y), (r, g, b))
    decrypted_img.save("decrypted_image.png")

image_path = "a.jpeg"
key = 115
shift_x = 160
shift_y = 550

encrypt_image(image_path, key, shift_x, shift_y)
decrypt_image("encrypted_image.png", key, shift_x, shift_y)

#By Sureshkumar
