from PIL import Image

def encode_text_in_image(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    message += "$$$"
    binary_message = ''.join(format(ord(i), '08b') for i in message)

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                r, g, b = img.getpixel((col, row))
                r = (r & ~1) | int(binary_message[index])
                encoded.putpixel((col, row), (r, g, b))
                index += 1

    encoded.save(output_path)
    print("✅ Message encoded and saved as:", output_path)



encode_text_in_image("C:/Users/nevin/OneDrive/Desktop/Personal Project/STENOGRAPHY-PROJECT/input.png", "This is a sensitive information.CONFIDENTIAL!!!!", "encoded.png")
