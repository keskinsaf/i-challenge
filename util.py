import hashlib, math
from PIL import Image


# generate hash
def create_hex_hash(username: str):
    encoded = username.encode("utf-8")
    hashed = hashlib.sha256(encoded)
    return hashed.hexdigest()


# impressed by https://stackoverflow.com/a/312464/6013366
def chunks(lst, n, limit=None):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, limit if limit is not None else len(lst), n):
        yield lst[i:i + n]


def get_color_from_hash(hex_hash: str):
    limit = 63
    c_parts = list(chunks(hex_hash, limit // 3, limit))
    ls = [sum(list(map(ord, c_part))) for c_part in c_parts]
    return tuple([clr % 256 for clr in ls])


def put_pixel(image: Image, top_left_coord: (int, int), color: (int, int, int), scale: int = 3):
    y, x = top_left_coord
    # for each row
    for i in range(scale):
        # for each col
        for j in range(scale):
            image.putpixel((x + j, y + i), color)


# generate image from hash
def generate_image_from_hash(hex_hash: str, size: int, row: int):
    print("An {}x{} sized image with {} rows will be generated.".format(size, size, row))
    color = get_color_from_hash(hex_hash)

    piece_capacity = len(hex_hash) // (row ** 2)

    img_res = 2 + row * 3
    # create Image
    image = Image.new(mode="RGB", size=(img_res, img_res), color=(255, 255, 255))

    for row_idx in range(1, 1 + (row * 3), 3):
        row_ctr = (row_idx - 1) // 3
        for col_idx in range(1, math.ceil(1 + (row * 3)/2), 3):
            col_ctr = (col_idx - 1) // 3
            piece_idx = piece_capacity * (row_ctr * row + col_ctr)
            piece = hex_hash[piece_idx:piece_idx + piece_capacity]
            if sum(map(ord, piece)) % 2 == 1:
                put_pixel(image, (row_idx, col_idx), color)

    for row_idx in range(1, 1 + (row * 3)):
        for col_idx in range(math.ceil(1 + (row * 3)/2), img_res):
            image.putpixel((col_idx, row_idx), image.getpixel((img_res - 1 - col_idx, row_idx)))

    return image.resize(size=(size, size), resample=Image.NEAREST)
