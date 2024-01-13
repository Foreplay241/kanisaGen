import os
import random
from tkinter import *
import artstyle
import wordie
from settings import *


class Wordie(artstyle.Artyle):
    def __init__(self, master=None, idutc=None):
        """
        A tab that has options for putting words on the kinvow.

        :param master: aRtay frame, housing all the other artyles.
        :param idutc: idutc frame, user input frame.
        """
        super(Wordie, self).__init__(master=master, idutc=idutc)
        self.tab_name = "Wordie"
        self.wordie_choices = ["Hangman", "Word search", "Collage"]
        self.setup_radiobutton_choices(self.wordie_choices)

    def destroy_word_optionmenus(self):
        """Destroy each of the optionmenus that contain wordlists"""
        for c in self.optionmenu_dict:
            self.optionmenu_dict[c][1].destroy()

    def gather_wordie_options(self) -> dict:
        """Gather and return a dictionary of wordie options."""
        chosen_wordie_options = {
            "Type": self.radiobutton_dict["Word search"][0].get()
        }
        return chosen_wordie_options

    def add_wordie(self, img: Image, kre8dict: dict, abt="Masterpiece") -> Image:
        """
        Adds the wordie type of wordie on the img provided.
        """
        selected_colors = []
        if kre8dict["artributes"][1] == "Rainbow":
            for ltr in kre8dict["use_id"]:
                selected_colors.append(ALPHANUMERIC_COLORS[ltr])
        elif kre8dict["artributes"][1] == "Cloud":
            shadelvl = 255 // len(kre8dict["use_id"])
            for i in range(len(kre8dict["use_id"])):
                selected_colors.append(((i + 1) * shadelvl, (i + 1) * shadelvl, (i + 1) * shadelvl))
        print(kre8dict)
        if kre8dict["Masterpiece"]["Wordie"]["Type"] == 0:
            kre8dict["Masterpiece"]["Wordie"]["Type"] = "Hangman"
            kre8dict["Masterpiece"]["Wordie"]["Hangman"] = {
                "Chosen": random.choice(list(kre8dict["Word Dict"].keys())),
                "Hidden": {},
                "Missed Letters": []
            }
            for c in kre8dict["Masterpiece"]["Wordie"]["Hangman"]["Chosen"]:
                if c in kre8dict["Masterpiece"]["Wordie"]["Hangman"]["Hidden"]:
                    c += c
                kre8dict["Masterpiece"]["Wordie"]["Hangman"]["Hidden"][c] = " ◙ "
            wordie.hangman(img, kre8dict)
        if kre8dict["Masterpiece"]["Wordie"]["Type"] == 1:
            kre8dict["Masterpiece"]["Wordie"]["Type"] = "Word Search"
            kre8dict["Masterpiece"]["Wordie"]["Word Search"] = {
                "Letter Array": [],
                "Word List": [],
                'Found Words': []
            }
            wordie.word_search(img, kre8dict)
        if kre8dict["Masterpiece"]["Wordie"]["Type"] == 2:
            kre8dict["Masterpiece"]["Wordie"]["Type"] = "Collage"
            wordie.kollage(img, kre8dict)
        print(kre8dict)
        # self.create_werd_serch(kre8dict)
        return img

    # def create_werd_serch(self, kre8dict: dict):
    #     for filename in os.listdir(f"WORDIE/"):
    #         if filename.startswith("index"):
    #             print(filename)
    #             line_list = []
    #             with open(f"WORDIE/{filename}", "r") as file:
    #                 for line in file.readlines():
    #                     line_list.append(line)
    #             with open(f"WORDIE/{kre8dict['use_id']}{filename}", "w") as file:
    #                 for line in line_list:
    #                     if line.find("letters_grid = ~~[]~~") >= 0:
    #                         print(kre8dict["Masterpiece"]["Wordie"])
    #                         line = line.replace("letters_grid = ~~[]~~", f"letters_grid = {kre8dict['Wordie']['Word Search']['Letter Array']}")
                        # if line.find("word_array = ~~[]~~") >= 0:
                        #     print("THIS")
                        #     line = line.replace("word_array = ~~[]~~", f"word_array = {kre8dict['Wordie']['Word Search']['Word List']}")
                        # file.write(line)
