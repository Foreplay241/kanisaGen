import json
import random
import uu
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

from settings import *

HANGMAN_PHRASES = ["The quick brown fox jumps over the lazy dog.",
                   f"If you guess the letter {random.choice(['Q', 'J', 'X', 'Z'])}, I win.",
                   "Why did the chicken cross the playground? To get to the other slide!",
                   "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?",
                   "A woodchuck would chuck as much wood as a woodchuck could chuck wood."
                   ]

HANGMAN_TEXTMAN_LIST = ["  ╔═════╕   \n"
                        "  ║     ┇   \n"
                        "  ║         \n"
                        "  ║         \n"
                        "  ║         \n"
                        "  ║         \n"
                        "  ║         \n"
                        "══╩═════════\n",

                        "  ╔═════╕   \n"
                        "  ║     ┇   \n"
                        "  ║     ◯   \n"
                        "  ║         \n"
                        "  ║         \n"
                        "  ║         \n"
                        "  ║         \n"
                        "══╩═════════\n",

                        "  ╔═════╕   \n"
                        "  ║     ┇   \n"
                        "  ║     ◯   \n"
                        "  ║     ‡   \n"
                        "  ║     ‡   \n"
                        "  ║         \n"
                        "  ║         \n"
                        "══╩═════════\n",

                        "  ╔═════╕   \n"
                        "  ║     ┇   \n"
                        "  ║     ◯   \n"
                        "  ║    /‡   \n"
                        "  ║     ‡   \n"
                        "  ║         \n"
                        "  ║         \n"
                        "══╩═════════\n",

                        "  ╔═════╕   \n"
                        "  ║     ┇   \n"
                        "  ║     ◯   \n"
                        "  ║    /‡\\ \n"
                        "  ║     ‡   \n"
                        "  ║         \n"
                        "  ║         \n"
                        "══╩═════════\n",

                        "  ╔═════╕   \n"
                        "  ║     ┇   \n"
                        "  ║     ◯   \n"
                        "  ║    /‡\\ \n"
                        "  ║     ‡   \n"
                        "  ║    /    \n"
                        "  ║         \n"
                        "══╩═════════\n",

                        "  ╔═════╕   \n"
                        "  ║     ┇   \n"
                        "  ║     ◯   \n"
                        "  ║    /‡\\ \n"
                        "  ║     ‡   \n"
                        "  ║    / \\ \n"
                        "  ║         \n"
                        "══╩═════════\n"
                        ]


def prompto(img: Image, kre8dict: dict) -> Image:
    """
    Creates a writing prompt from
    @param img:
    @param kre8dict:
    @return:
    """
    pass


def generate_madlib_sentence(action: str, kre8dict: dict) -> str:
    number = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][0]
    pet_name = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][1]
    furniture = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][2]
    adjective = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][3]
    location = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][4]
    noun = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][5]
    pronoun = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][6]
    animal = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][7]
    food = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][8]
    vehicle = ANOTHER_WORD_LISTS[random.choice(kre8dict['use_id'])][9]
    time_prepword = random.choice(["before", "while", "after", "since"])
    space_prepword = random.choice(["between", "above", "underneath", "beside"])
    determiner = random.choice(['a', 'some', 'the', 'that'])
    send_sent = f"{pronoun.title()} {action} {determiner} {adjective} {noun}"
    send_sent += random.choice([".", ", ", "!"])
    print(send_sent[-2:])
    if send_sent[-2:] == ", ":
        send_sent += f"{time_prepword} {pet_name.title()} the {animal} ate {food}s in {location}{random.choice(['.', '!'])}"
    send_sent += f" The {noun} landed {space_prepword} the {furniture}."
    return send_sent


def dict_to_str(hidden_phrase_dict: dict) -> str:
    hidden_word_str = ""
    for c in hidden_phrase_dict:
        hidden_word_str += hidden_phrase_dict[c]
    return hidden_word_str


def check_hangman_letter(letter_to_check: str, chosen_phrase: str, hidden_phrase: dict, missed_letters: list) -> (dict, list):
    if letter_to_check in chosen_phrase:
        for i in range(len(chosen_phrase)):
            if letter_to_check*(i+1) in hidden_phrase:
                if hidden_phrase[letter_to_check*(i+1)] == "◙":
                    hidden_phrase[letter_to_check*(i+1)] = f'{letter_to_check}'
    else:
        if letter_to_check in missed_letters:
            pass
        else:
            missed_letters.append(letter_to_check)

    return hidden_phrase, missed_letters


def word_search(img: Image, kre8dict: dict) -> Image:
    """
    Create a 2d-array of letters with words in order.

    :param img:
    :param kre8dict:
    :return:
    """
    nl = kre8dict["number_list"]
    cl = kre8dict["color_list"]
    draw = ImageDraw.Draw(img)
    w, h = img.size
    letters_array = []
    word_list = ["KANISA", "BLUE"]
    font = ImageFont.truetype('trebucbd.ttf', 16)
    for i in range(nl[5]):
        word_picked = random.choice(list(kre8dict["Word Dict"].keys()))
        word_list.append(word_picked.upper())
    for word in kre8dict["Masterpiece"]["Wordie"]:
        if word != "Type" and word != "Word Search":
            word_list.append(word.upper())
    kre8dict["Masterpiece"]["Wordie"]["Word Search"]["Word List"] = word_list
    for x in range(0, w, 16):
        letters_array.append([])
        for y in range(0, h, 16):
            letters_array[x//16].append("")
    cx, cy = 0, 0
    for word in word_list:
        print(word)
        cx = random.randint(0, 16)
        orientation = random.choice(["Vertical", "Horizontal", "Diagonal"])
        if orientation == "Vertical":
            for c in word:
                print(cx, cy)
                letters_array[cx][cy] = c.upper()
                draw.text((cx*16+4, cy*16-2), font=font, text=c.upper(), fill=cl[1], align='right')
                cy += 1
        elif orientation == "Horizontal":
            for c in word:
                print(cx, cy)
                letters_array[cx][cy] = c.upper()
                draw.text((cx*16+4, cy*16-2), font=font, text=c.upper(), fill=cl[1], align='right')
                cx += 1
        elif orientation == "Diagonal":
            for c in word:
                print(cx, cy)
                letters_array[cx][cy] = c.upper()
                draw.text((cx*16+4, cy*16-2), font=font, text=c.upper(), fill=cl[1], align='right')
                cx += 1
                cy += 1
        # cy += 1

    # FILL IN THE REST OF SLOTS WITH RANDOM LETTERS.
    for cx in range(len(letters_array)):
        for cy in range(len(letters_array[cx])):
            if len(letters_array[cx][cy]) == 0:
                c = random.choice("abcdefghijklmnopqrstuvwxyz")
                letters_array[cx][cy] = c.upper()
                draw.text((cx*16+4, cy*16-2), font=font, text=c.upper(), fill=WHITE, align='right')
    # werd_serch_dict = {
    #     'letter_array': letters_array,
    #     'find_list': word_list
    # }
    kre8dict["Masterpiece"]["Wordie"]["Word Search"]["Letter Array"] = letters_array
    # with open(f'WORDIE/werd_serch_array.txt', 'w') as f:
    #     json.dump(werd_serch_dict, f, separators=(',', ': '))
    return img


def kollage(img: Image, kre8dict: dict) -> Image:
    """
    Create a collage of words on the img provided.
    """
    nl = kre8dict["number_list"]
    cl = kre8dict["color_list"]
    draw = ImageDraw.Draw(img)
    use_cl = []
    w, h = img.size
    for colo in cl:
        co0 = int(colo[0] * 255)
        co1 = int(colo[1] * 255)
        co2 = int(colo[2] * 255)
        use_cl.append((co0, co1, co2))
    for x in range(0, w, 64):
        for y in range(0, h, 32):
            rand_c = random.choice(kre8dict["use_id"])
            word = random.choice(ALPHANUMERIC_WORD_LISTS[rand_c])
            draw.text((x, y), text=word, fill=random.choice(use_cl), angle=random.randint(-nl[8], nl[8])*36)
    return img


def poetree(img: Image, kre8dict: dict) -> Image:
    """
    Creates a poem that rhymes and stuff.
    @param img:
    @param kre8dict:
    @return:
    """
    pass


def lyrix(img: Image, kre8dict: dict) -> Image:
    """
    Gather lyrics from the internets.
    """
    pass


def digiary(img: Image, kre8dict: dict) -> Image:
    """
    Create a masterpiece from a digiary entry. Or create a digiary entry.
    """
    pass
