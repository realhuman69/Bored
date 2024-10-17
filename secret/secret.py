def encode_message(image_path, message):
    img = Image.open(image_path)

    # Convert image to RGB if not already in that mode
    if img.mode != 'RGB':
        img = img.convert('RGB')

    encoded_image = img.copy()
    
    message += chr(0)  # Null character to indicate the end of the message
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    data_index = 0
    for x in range(img.width):
        for y in range(img.height):
            pixel = list(encoded_image.getpixel((x, y)))
            for i in range(3):  # For RGB channels
                if data_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                    data_index += 1
            encoded_image.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image.save('encoded_image.png')
    messagebox.showinfo("Success", "Message encoded and saved as 'encoded_image.png'.")

def decode_message(image_path):
    img = Image.open(image_path)

    # Convert image to RGB if not already in that mode
    if img.mode != 'RGB':
        img = img.convert('RGB')

    binary_message = ""
    
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            for i in range(3):  # For RGB channels
                binary_message += str(pixel[i] & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == '00000000':
            break  # End of message
        message += chr(int(byte, 2))
        
    messagebox.showinfo("Decoded Message", message)
