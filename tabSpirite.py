import random
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

import artstyle
import spirite
from settings import *


class Spirite(artstyle.Artyle):
    def __init__(self, master=None, idutc=None):
        """
        A tab with options for loading different spirite layers.

        :param master: aRtay frame, housing all the other artyles.
        """
        super(Spirite, self).__init__(master, idutc=idutc)
        # self.disp_img = None
        self.tab_name = "Spirite"
        self.spirite_optionmenu_choice_list = ["None", "Alien", "Asteroid", "Ball", "Medallion", "Ship", "Sword",
                                               "Tribloc", "RTJ", "Boat", "Platform", "Goal"]
        self.setup_dropdown_menus(word_list=self.spirite_optionmenu_choice_list, dropdown_name="Spirite Type")
        self.spirite_str = self.dropdown_menu_dict["Spirite Type"][0].get()
        self.layer_name_dict = LAYER_DICT[self.spirite_str]
        self.chosen_spirite_layer_dict = {}

    def setup_dropdown_menus(self, word_list=None, word_str=None, dropdown_name=""):
        super().setup_dropdown_menus(word_list=word_list, word_str=word_str, dropdown_name=dropdown_name)
        # self.dropdown_menu_dict["Spirite Type"][1].configure(command=self.update_spirite_str)

    def update_spirite_str(self):
        self.spirite_str = self.dropdown_menu_dict["Spirite Type"][0].get()

    def gather_spirite_options(self) -> dict:
        """Gather Spirite options into a dictionary."""
        chosen_spirite_options = {
            self.dropdown_menu_dict["Spirite Type"][0].get(): LAYER_DICT[self.dropdown_menu_dict["Spirite Type"][0].get()]
        }
        return chosen_spirite_options

    def generate_populate_spirite_choices(self):
        self.destroy_word_optionmenus()
        self.setup_dropdown_menus()

    def destroy_word_optionmenus(self):
        """Destroy each of the optionmenus that contain wordlists"""
        for layer_name in self.layer_name_dict:
            self.chosen_spirite_layer_dict[layer_name][1].destroy()

    def setup_wordlist_optionmenus(self, word_str: str):
        """Create optionmenus for each wordlist."""
        super().setup_dropdown_menus(word_str)

    def add_spirite(self, img: Image, kre8dict: dict) -> Image:
        """
        Add a spirite to the masterpiece.
        :param img:
        :param kre8dict:
        :return:
        """
        w, h = img.size
        spirite_layers = []
        sw, sh = (w // 4, h // 4)
        fraim = spirite.stack_layers(img, kre8dict, (sw, sh))
        spirite_layers.append(fraim)
        for layer in spirite_layers:
            img.paste(layer, ((w // 2) - sw // 2, (h // 2) - sh // 2), mask=layer)
        return img
