import numpy as np
from PIL import Image

def load_matrix_from_image(_path: str, _width: int, _height: int) -> np.matrix:
    img = Image.open(_path).convert('L')
    arr = np.array(img.getdata())
    mat = []
    for i in range(_height):
        mat.append(arr[i * _width : (i + 1) * _width])
    return np.matrix(mat)

genuine_watermark_matrix = load_matrix_from_image(".\data\genuine-watermark.png", 192, 192)
print(genuine_watermark_matrix)

pirate_watermark_matrix = load_matrix_from_image(".\data\pirate-watermark.png", 192, 192)
print(pirate_watermark_matrix)
