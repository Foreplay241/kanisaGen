import random
from PIL import Image, ImageDraw, ImageFont
from settings import *

emonob16 = ImageFont.truetype("emonob.ttf", 16)
emonob32 = ImageFont.truetype("emonob.ttf", 32)


def add_ingredients(img: Image, kre8dict: dict) -> Image:
    ing_dict = kre8dict["Masterpiece"]["Recipe"]["Ingredients"]
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for i, (key, value) in enumerate(ing_dict.items()):
        x_position = 64 if i < 5 else 224 if i < 10 else 384
        y_position = (height * .1) + 5 * ((i % 5) * 3) if i < 10 else (height * .1) + 5 * (((i - 10) % 5) * 3)
        draw.text((x_position, y_position), text=f'{value[0]} {key}', font=emonob16)
    return img


def add_directions(img: Image, kre8dict: dict) -> Image:
    dir_dict = kre8dict["Masterpiece"]["Recipe"]["Directions"]
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for i, (key, value) in enumerate(dir_dict.items()):
        draw.text((147, height * .5 + (10 * ((i * 2) + 2))),
                  text=f'{key}: {value}', font=emonob16)
    return img


def add_labels(img: Image, kre8dict: dict) -> Image:
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for _ in range(5):
        draw.text((32 + random.randint(-2, 2), 16 + random.randint(-2, 2)),
                  text="  ".join("Ingredients"), font=emonob16,
                  fill=random.choice(RANDOM_COLOR_STR_LIST))
        draw.multiline_text((32 + random.randint(-2, 2), height // 2 + random.randint(-2, 2)),
                            text="\n".join("Directions"), font=emonob16,
                            fill=random.choice(RANDOM_COLOR_STR_LIST))
        draw.text((width * .8 + random.randint(-2, 2), height * .8 + random.randint(-2, 2)),
                  text="created by: \n    -" + kre8dict["Masterpiece"]["Recipe"]["recipe_info"][0], font=emonob16,
                  fill=random.choice(RANDOM_COLOR_STR_LIST))
        draw.text((4 + random.randint(-2, 2), height * .3 + random.randint(-2, 2)),
                  text=kre8dict["Masterpiece"]["Recipe"]["recipe_info"][1], font=emonob32,
                  fill=random.choice(RANDOM_COLOR_STR_LIST))
    return img
