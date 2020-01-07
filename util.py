import hashlib
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


# generate image from hash
def generate_image_from_hash(hex_hash: str, size: int, row: int):
    print("An {}x{} sized image with {} rows will be generated.".format(size, size, row))
    color = get_color_from_hash(hex_hash)

    piece_capacity = len(hex_hash) // (row ** 2)

    # create Image
    image = Image.new(mode="RGB", size=(row, row), color=(128, 128, 128))

    for row_ctr in range(row):
        for col_ctr in range(row):
            piece_idx = row_ctr * piece_capacity + col_ctr
            piece = hex_hash[piece_idx:piece_idx + piece_capacity]
            if sum(map(ord, piece)) % 2 == 1:
                image.putpixel((row_ctr, col_ctr), color)
    return image.resize(size=(size, size), resample=Image.NEAREST)
