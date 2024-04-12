import argparse
import random
import time
from typing import List

from PIL import Image, ImageDraw


def load_phrases(phrase_file: str) -> List[str]:
    with open(phrase_file, mode="r", encoding="utf8") as phrases:
        processed = phrases.read().splitlines()
        if len(processed) < 1:
            raise ValueError("File needs to have at least one line")
        return processed


def paint_image(words: List[str], width: int = 1000, height: int = 1000, steps: int = 5,
                bonus: bool = True) -> Image.Image:
    # Create image
    image = Image.new(mode='RGB', size=(height, width), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    cell_size = int(image.width / steps)

    # Draw vertical lines
    for x in range(0, image.width, cell_size):
        line = ((x, 0), (x, image.height))
        draw.line(line, fill=0, width=2)

    # Draw horizontal lines
    for y in range(0, image.height, cell_size):
        line = ((0, y), (image.width, y))
        draw.line(line, fill=0, width=2)

    # Draw text boxes
    for i, x in enumerate(range(0, width, cell_size)):
        for j, y in enumerate(range(0, height, cell_size)):
            # Check for bonus field
            is_bonus = i == steps // 2 and j == steps // 2 and bonus

            color = (255, 0, 0) if is_bonus else 0
            text = "Bonus" if is_bonus else random.choice(words)

            # Draw text
            draw.multiline_text((x + cell_size // 2, y + cell_size // 2),
                                text=text,
                                align="center",
                                anchor="ms",
                                font_size=cell_size // 10, fill=color)

    return image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-width", default=1000, help="width of image in pixels", type=int)
    parser.add_argument("-height", default=1000, help="height of image in pixels", type=int)
    parser.add_argument("-steps", default=5, help="grid side length", type=int)
    parser.add_argument("-words", required=True, help="words text file", type=str)
    parser.add_argument("-seed", default=time.time_ns(), help="seed for the bingo", type=int)
    parser.add_argument("-bonus", default=False, help="adds bonus field if side length is odd", type=bool)

    args = parser.parse_args()

    try:
        bingo_phrases = load_phrases(args.words)
    except FileNotFoundError:
        parser.error(f"File {args.words} does not exist")
    except ValueError:
        parser.error(f"File {args.words} needs to have at least one line")
    else:
        random.seed(args.seed)
        bingo_image = paint_image(bingo_phrases, args.width, args.height, args.steps, bonus=args.bonus)

        bingo_image.save(f"bingo_{args.words.split('.')[0]}_{args.steps}x{args.steps}.png", format="PNG")
