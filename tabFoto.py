import random

from PIL.ImageFont import ImageFont
# from memory_profiler import profile
from tkinter import *
from os import *
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import glob
from tkinter import ttk

import fotoes
from settings import *

import artstyle


class Fotoes(artstyle.Artyle):
    def __init__(self, master=None, idutc=None):
        """
            A collection of options to create a new and exciting Foto.
        """
        super(Fotoes, self).__init__(master, idutc=idutc)
        self.tab_name = "Foto"
        self.home_folder_path = 'C:\\Users\\thisr\\PycharmProjects\\KanisaRedditGen\\'
        r1 = random.randint(0, 69)
        r2 = random.randint(0, 69)
        self.setup_button_choices(["Change Foto 1",
                                   "Change Foto 2"
                                   ])
        self.button_dict["Change Foto 1"][1].configure(command=self.update_foto_button)
        self.button_dict["Change Foto 2"][1].configure(command=self.update_foto2_button)
        self.checkbutton_choice_list = ["HSB filter", "RGB filter", "Blur", "Contour", "Detail",
                                        "Edge Enhance", "Emboss", "Find Edges", "Smooth", "Shuffled"]
        self.slider_choice_list = ["Hue", "Saturation", "Brightness",
                                   "Red", "Green", "Blue", "Blend"]
        self.slider_limit_dict = {
            "Hue": [0, 360],
            "Saturation": [0, 100],
            "Brightness": [0, 100],
            "Blend": [0, 100],
            "Red": [0, 255],
            "Green": [0, 255],
            "Blue": [0, 255]
        }
        self.setup_slider_bars(self.slider_choice_list)
        self.setup_checkbutton_choices(self.checkbutton_choice_list)
        self.setup_text_boxes(1)

    def gather_foto_options(self) -> dict:
        """Gather and return the options Foto will use to make."""
        sd = self.slider_dict
        if self.IDUTC_frame.data_source_var.get() == "Random":
            for slider in self.slider_choice_list:
                rn = random.randint(6, 94)
                sd[slider][0].set(rn)
        chosen_foto_options = {"IMG": self.button_dict["Change Foto 1"][0].get(),
                               "IMG2": self.button_dict["Change Foto 2"][0].get(),
                               "AB": sd["Blend"][0].get(),
                               "HSB": [sd["Hue"][0].get(), sd["Saturation"][0].get(), sd["Brightness"][0].get()],
                               "RGB": [sd["Red"][0].get(), sd["Green"][0].get(), sd["Blue"][0].get()],
                               "Filters": []}
        for option in self.checkbutton_choice_list:
            if self.checkbutton_dict[option][0].get() == 1:
                chosen_foto_options["Filters"].append(option)
                if option == "Shuffled":
                    chosen_foto_options["Shuffle Size"] = self.textbox_dict["0"][0].get()
        return chosen_foto_options

    def setup_slider_bars(self, slider_name_list: list):
        super().setup_slider_bars(slider_name_list)

    def update_foto_button(self):
        """Add a single foto"""
        self.use_data_dict = self.IDUTC_frame.kre8dict
        x = ""
        rn = random.randint(0, 69)
        lp = random.choice(["landscape", "landscape"])
        if self.use_data_dict["data_source"] == "Random":
            x = f'/assets/Fotoes/OG/{lp}{rn}.jpg'
        elif self.use_data_dict["data_source"] == "Human":
            x = openfilename_str()
            x = x[len(self.home_folder_path):]
        self.button_dict["Change Foto 1"][0].set(x)

    def update_foto2_button(self):
        """Add a second foto"""
        self.use_data_dict = self.IDUTC_frame.kre8dict
        x = ""
        rn = random.randint(0, 69)
        lp = random.choice(["landscape", "landscape"])
        if self.use_data_dict["data_source"] == "Random":
            x = f'/assets/Fotoes/OG/{lp}{rn}.jpg'
        elif self.use_data_dict["data_source"] == "Human":
            x = openfilename_str()
            x = x[len(self.home_folder_path):]
        self.button_dict["Change Foto 2"][0].set(x)

    def add_foto(self, img: Image, kre8dict: dict) -> Image:
        """
        Add foto to the img masterpiece.

        :param img: Masterpiece Image
        :param kre8dict: Dictionary of kre8shun.
        :return:
        """
        print(kre8dict)
        imaj1 = Image.open(self.home_folder_path + kre8dict["Masterpiece"]["Foto"]["IMG"])
        imaj2 = Image.open(self.home_folder_path + kre8dict["Masterpiece"]["Foto"]["IMG2"])
        bimg = fotoes.blend_foto(imaj1, imaj2, kre8dict["Masterpiece"]["Foto"]["AB"]/100)
        rimg = fotoes.resize_foto(bimg, img.size)
        for chosen in kre8dict["Masterpiece"]["Foto"]["Filters"]:
            if chosen == "HSB filter":
                rimg = fotoes.hsb_filter_foto(rimg, kre8dict)
            if chosen == "RGB filter":
                rimg = fotoes.rgb_filter_foto(rimg, kre8dict)
            if chosen == "Blur":
                rimg = rimg.filter(ImageFilter.BLUR)
            if chosen == "Contour":
                rimg = rimg.filter(ImageFilter.CONTOUR)
            if chosen == "Detail":
                rimg = rimg.filter(ImageFilter.DETAIL)
            if chosen == "Edge Enhance":
                rimg = rimg.filter(ImageFilter.EDGE_ENHANCE)
            if chosen == "Emboss":
                rimg = rimg.filter(ImageFilter.EMBOSS)
            if chosen == "Find Edges":
                rimg = rimg.filter(ImageFilter.FIND_EDGES)
            if chosen == "Smooth":
                rimg = rimg.filter(ImageFilter.SMOOTH)
            if chosen == "Shuffled":
                rimg = fotoes.shuffle_foto(rimg, kre8dict)
        img.paste(rimg, (0, 0))
        return img
