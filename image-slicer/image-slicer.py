from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
BASE_PATH = os.getenv("BASE_PATH")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")
PAGES = int(os.getenv("PAGES"))
SPLITS = int(os.getenv("SPLITS"))
OFFSET = int(os.getenv("OFFSET"))


def main(is_bulk=False, page=1):
    image_paths = []
    iter_pages = PAGES if is_bulk else 1
    # The iteration is starting at 0
    # Pages are starting at 1
    for p in range(iter_pages):
        if iter_pages == 1:
            p = page - 1
        image_paths = get_image_paths(p + 1, SPLITS)
        images = []
        for path in image_paths:
            images.append(Image.open(path))

        multi_concat_vertical(images, OFFSET).save(f"{OUTPUT_PATH}0{p+1}.jpg")


def get_image_paths(page, splits):
    image_paths = []
    for s in range(splits):
        image_paths.append(f"{BASE_PATH}{page}-{s+1}.jpg")
    return image_paths


def concat_vertical(im1, im2, offset=0):
    w = max(im1.width, im2.width)
    h = im1.height + im2.height - offset
    im = Image.new("RGB", (w, h))

    im.paste(im1, (0, 0))
    im.paste(im2, (0, im1.height - offset))

    return im


# source: https://note.nkmk.me/en/python-pillow-concat-images/
def multi_concat_vertical(im_list, offset=0):
    _im = im_list.pop(0)
    for im in im_list:
        _im = concat_vertical(_im, im, offset)
    return _im


if __name__ == "__main__":
    main(is_bulk=True, page=1)
