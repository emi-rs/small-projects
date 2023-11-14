from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
BASE_PATH = os.getenv("BASE_PATH")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")
PAGES = int(os.getenv("PAGES"))
SPLITS = int(os.getenv("SPLITS"))

# # these are how much to move the slices up to align the images
# offset_1 = 0
# offset_2 = 0
# offsets = [offset_1, offset_2]


# Flag for bulk editing or page by page editing
# 0 = page by page
# 1 = bulk
def main(is_bulk=False, page=0):
    image_paths = []
    iter_pages = PAGES if is_bulk else 1

    for p in range(iter_pages):
        if iter_pages == 1:
            p = page - 1
        image_paths = get_image_paths(p + 1, SPLITS)
        print(image_paths)


def get_image_paths(page, SPLITS):
    image_paths = []
    for s in range(SPLITS):
        image_paths.append(f"{page}-{s+1}.jpg")
    return image_paths


def concat_vertical(im1, im2, offset):
    w = max(im1.size[0], im2.size[0])
    h = im1.size[1] + im2.size[1]
    im = Image.new("RGBA", (w, h))

    im.paste(im1, (0, 0))
    im.paste(im2, (im1.size[0], 0))

    return im


if __name__ == "__main__":
    main(is_bulk=False, page=1)
