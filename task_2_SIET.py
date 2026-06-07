from PIL import Image
def encrypt_image(input_file, output_file, key):
    img = Image.open(input_file)
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256  )
    img.save(output_file)
def decrypt_image(input_file, output_file, key):
    img = Image.open(input_file)
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256 )
    img.save(output_file)
choice = input("Encrypt or Decrypt (E/D): ").upper()
key = int(input("Enter key value: "))

if choice == "E":
    encrypt_image("input.jpg", "encrypted.png", key)
    print("Image encrypted successfully.")
elif choice == "D":
    decrypt_image("encrypted.png", "decrypted.png", key)
    print("Image decrypted successfully.")
else:
    print("Invalid choice.")