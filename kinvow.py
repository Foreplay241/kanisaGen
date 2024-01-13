import datetime
import random
from tkinter import *
from tkinter import ttk
# from memory_profiler import profile
import profile
# import pyscreenshot as ImageGrab
from PIL import Image, ImageDraw, ImageGrab

import artay
import idutc
import settings
import tabGlyth
import texioty
from settings import *


class KINVOW(ttk.LabelFrame):
    def __init__(self, master=None, IDUTC=None, ARTAY=None, TEXIOTY=None):
        """
        Frame that holds the canvas/window.
        
        :param master: Toolbox frame that contains each Tul.
        :param IDUTC: idutc frame that the user can place input.
        :param ARTAY: Array of art. Tul for selecting basic options.
        :param TEXIOTY: Texioty frame, for textual input and output.
        """
        super(KINVOW, self).__init__(master=master)
        self.configure(text="Kinvow")
        # self.IDUTC_frame: idutc.IDUTC = IDUTC
        # self.TEXIOTY_frame: texioty.TEXIOTY = TEXIOTY
        self.ARTAY_frame: artay.ARTAY = ARTAY
        
        self.use_canvas = Canvas(self, bg=random.choice(RANDOM_COLOR_STR_LIST), width=640, height=640)
        self.use_canvas.grid(column=0, row=0, columnspan=3)

    def generate_glyth(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a glyth to the img.
        :param img: img to add a glyth to.
        :param kre8dict: Instructions on how to add the glyth.
        :param abt: Is it an avatar, banner, or tile? Masterpiece? Wallpaper?
        :return:
        """
        kre8dict[abt]["Glyth"] = self.ARTAY_frame.glythTab.gather_glyth_options()
        self.ARTAY_frame.glythTab.add_glyth(img, kre8dict, abt)

    def generate_glyph(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a glyph to the img.
        :param abt: Avatar, Banner or Tile or Masterpiece.
        :param img: img to add a glyph to.
        :param kre8dict: Instructions on how to add the glyph.
        :return:
        """
        kre8dict[abt]["Glyph"] = self.ARTAY_frame.glyphTab.gather_glyph_options()
        self.ARTAY_frame.glyphTab.add_glyph(img, kre8dict, abt)

    def generate_wordie(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a wordie to the img.
        :param abt:
        :param img: img to add a wordie to.
        :param kre8dict: Instructions on how to add the wordie.
        :return:
        """
        kre8dict["Word Dict"] = {}
        for c in kre8dict["use_id"]:
            word = ALPHANUMERIC_WORD_LISTS[c[:1].lower()][0]
            kre8dict["Word Dict"][word.upper()] = []
            for c2 in word.lower():
                kre8dict["Word Dict"][word.upper()].append(random.choice(ALPHANUMERIC_WORD_LISTS[c2]).upper())
        kre8dict[abt]["Wordie"] = self.ARTAY_frame.wordieTab.gather_wordie_options()
        self.ARTAY_frame.wordieTab.add_wordie(img, kre8dict, abt)

    def generate_spirite(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a spirite to the img.
        :param abt:
        :param img: img to add a spirite to.
        :param kre8dict: Instructions on how to add the spirite.
        :return:
        """
        kre8dict[abt]["Spirite"] = self.ARTAY_frame.spiriteTab.gather_spirite_options()
        self.ARTAY_frame.spiriteTab.add_spirite(img, kre8dict)

    def generate_recipe(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a recipe to the img.
        :param abt:
        :param img: img to add a recipe to.
        :param kre8dict: Instructions on how to add the recipe.
        :return:
        """
        kre8dict[abt]["Recipe"] = self.ARTAY_frame.recipeTab.gather_recipe_options()
        print("Kre8dict", kre8dict)
        self.ARTAY_frame.recipeTab.add_recipe(img, kre8dict)

    def generate_foto(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a foto to the img.
        :param abt:
        :param img: img to add a foto to.
        :param kre8dict: Instructions on how to add the foto.
        :return:
        """
        kre8dict[abt]["Foto"] = self.ARTAY_frame.fotoTab.gather_foto_options()
        self.ARTAY_frame.fotoTab.add_foto(img, kre8dict)

    def generate_mujic(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a mujic to the img.
        :param abt:
        :param img: img to add a mujic to.
        :param kre8dict: Instructions on how to add the mujic.
        :return:
        """
        kre8dict[abt]["Mujic"] = self.ARTAY_frame.mujicTab.gather_mujic_options()
        self.ARTAY_frame.mujicTab.add_mujic(img, kre8dict)

    def generate_gaym(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a gaym to the img.
        :param abt:
        :param img: img to add a gaym to.
        :param kre8dict: Instructions on how to add the gaym.
        :return:
        """
        kre8dict[abt]["Gaym"] = self.ARTAY_frame.gaymTab.gather_gaym_options()
        self.ARTAY_frame.gaymTab.add_gaym(img, kre8dict)
