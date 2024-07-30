from PIL import Image

def image_to_rgb565(image_path):
    with Image.open(image_path).convert('RGB') as img:
        width, height = img.size
        rgb565_data = []

        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                rgb565 = ((r & 0xf8) << 8) | ((g & 0xfc) << 3) | (b >> 3)
                rgb565_high = (rgb565 >> 8) & 0xFF
                rgb565_low = rgb565 & 0xFF
                rgb565_data.append(rgb565_high)
                rgb565_data.append(rgb565_low)

        return bytes(rgb565_data)