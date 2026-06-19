import os
from PIL import Image

def remove_black_background(input_path, output_path, threshold=50):
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # item is (R, G, B, A)
            # If the pixel is dark (black background), make it transparent
            if item[0] < threshold and item[1] < threshold and item[2] < threshold:
                newData.append((item[0], item[1], item[2], 0))  # Transparent
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Successfully processed {input_path} and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    assets_dir = os.path.join(os.getcwd(), "assets")
    logo_path = os.path.join(assets_dir, "logo.png")
    out_path = os.path.join(assets_dir, "logo_transparent.png")
    
    if os.path.exists(logo_path):
        remove_black_background(logo_path, out_path, threshold=30)
    else:
        print(f"Could not find {logo_path}")
