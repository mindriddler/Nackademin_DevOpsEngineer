from PIL import Image
from io import BytesIO

# BytesIO is a in-memory buffer that could be useful

with open('lesson_12/examples/cat.jpg', 'rb') as f, BytesIO() as p:
    p.write(f.read())
    print(p)
    # pip install pillow
    # https://pillow.readthedocs.io/en/stable/reference/Image.html
    img = Image.open(p)
    img.show()
