import json
import os
from datetime import time, datetime
from os.path import exists
from tkinter import *
import requests
import idutc
# import kinvow
# from dotenv import load_dotenv
from PIL import Image, ImageDraw
# import mujic
# import wordie
# from manfried import TalkingPinata
from settings import *

from pytube import YouTube, Playlist

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BASE_URL = "https://discord.com/api/v9"
headers = {
    "Authorization": f"Bot {TOKEN}"
}


class TEXIOTY(LabelFrame):
    def __init__(self, master=None, IDUTC=None, ARTAY=None, KINVOW=None):
        """
        An array of art. A few styles turns into alot of styles. Maybe too many styles, possibly not enough.
        The world may never know.
        
        :param master: aRtay frame, housing all the other artyles.
        :param IDUTC: idutc frame, user input frame.
        :param ARTAY: Array of art. Tul for selecting basic options.
        :param KINVOW: Canvas Window, for visual input(eventually) and output.
        """
        super(TEXIOTY, self).__init__(master)
        self.input_list = []
        self.crimg = None
        self.tongue_list = ["English", "Filipino", "French", "Spanish", "German"]
        self.chosen_tongue = "English"
        # self.chosen_tongue = random.choice(self.tongue_list)
        self.configure(text=f'Texioty:')
        self.IDUTC_frame: idutc.IDUTC = IDUTC
        # import artay
        # self.ARTAY_frame: artay.ARTAY = ARTAY
        # self.KINVOW_frame: kinvow.KINVOW = KINVOW
        # self.manny = TalkingPinata()
        self.texoty = Text(self, height=26, width=69, bg="light blue", relief=SUNKEN)
        self.texoty.grid(column=0, row=0, rowspan=28)
        self.input_str_var = StringVar()
        self.texity = Entry(self, width=69, bg="light green", textvariable=self.input_str_var)
        self.texity.grid(column=0, row=29)
        # CONFIG LANGUAGE TAGS FOR LATER USE
        self.texoty.tag_config("English", background="light blue", foreground="blue")
        self.texoty.tag_config("French", background="blue", foreground="red")
        self.texoty.tag_config("Filipino", background="gold", foreground="blue")
        self.texoty.tag_config("Spanish", background="red", foreground="gold")
        self.texoty.tag_config("German", background="black", foreground="yellow")

        self.texity.bind('<Return>', lambda e: self.input_from_texity())
        self.texity.bind('<KP_Enter>', lambda e: self.input_from_texity())
        self.texity.bind('<Key>', self.key_test)
        self.isTestingKeys = False
        # DIARY SETUP
        self.isDiary = False
        self.diary_line_length = 75
        self.diarySentenceList = []
        self.prev_kommand_list = []

        # KOMMAND CYCLING
        self.kom_index = 0
        self.texity.bind('<Up>', lambda e: self.previous_kommand())
        self.texity.bind('<Down>', lambda e: self.next_kommand())
        self.texity.focus_set()

        self.base_loopring_api_url = "https://api3.loopring.io"

        self.commands_dict = {"'kre8 [art-style]'": ["Creates a masterpiece with the given art style."],
                              "'discord [art-style]'": ["Currently disabled",
                                                        "Create a masterpiece and send to discord."],
                              "'disp'": ["Display the current kre8dict."],
                              "'dear_sys,'": ["Enters into diary mode.",
                                              "Anything typed will be added to a diary entry."],
                              "'/until_next_time'": ["Exits diary mode.", "Saves the entry into the .diary folder."],
                              "'help'": ["Displays some help about the program itself."],
                              "'kommands'": ["Displays this."],
                              "'dl [video link]'": ["Currently disabled", "Download the audio of a youtube video."]}

    def key_test(self, event):
        """Test some key presses from the board of keys."""
        if self.isTestingKeys:
            self.print_to_texoty(f'char:{event.char}, keysym:{event.keysym}, keycode:{event.keycode}')

    def priont_help(self, tul_section="opening"):
        """
        Shows a type of tutorial in the Texoty window.
        :return:
        """
        help_list_strings = ["                       ╪Hello! Welcome to KanisaGen╪",
                             "                       └┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┘",
                             "One of the first things you should notice are the four sections of \n"
                             "the window, these are the tuls you can use to make masterpieces.", ""]
        artay_help_list_strings = ["                    ╪aRtay╪",
                                   "                    └┴┴┴┴┴┘",
                                   "A tray of art contains an array of art styles.", ""]
        texioty_help_list_strings = ["                    ╪Texioty╪",
                                     "                    └┴┴┴┴┴┴┴┘",
                                     "Texioty is all about processing commands and displaying information.", ""]
        idutc_help_list_strings = ["                    ╪idutc╪",
                                   "                    └┴┴┴┴┴┘",
                                   "The idutc is a combination of an id and a utc.", ""]
        kinvow_help_list_strings = ["                    ╪Kinvow╪",
                                    "                    └┴┴┴┴┴┴┘",
                                    "A window can be a canvas, too much use and it'll be a door.", ""]
        welcoming_help_strings = {
            "opening": help_list_strings,
            "aRtay": artay_help_list_strings,
            "Texioty": texioty_help_list_strings,
            "idutc": idutc_help_list_strings,
            "Kinvow": kinvow_help_list_strings
        }
        print(tul_section)
        tul_help_dict = {
            "aRtay": ["Top-left tul, derives from 'art' and 'tray'",
                      "It contains tabs labeled 'Glyth', 'Glyph', 'Wordie' and so on.",
                      "These tabs are art-styles and each have different options.",
                      "Different outcomes will occur, based on your choices."],
            "Texioty": ["Bottom-left tul, derives from 'text' and 'IO'",
                        "The green box is used for textual input.",
                        "The blue box is used for textual output.",
                        "For a list of commands, use the 'kommands' command."],
            "idutc": ["Top-right tul, derives from 'id' and 'utc'",
                      "Source and keywords dictate creation and whatnot.",
                      "You can type many letters and numbers in the yellow box.",
                      "In the red box you can type a 10-digit number."],
            "Kinvow": ["Bottom-right tul, derives from 'canvas' and 'window'",
                       "Creates an image based on the Texioty command used.",
                       "The command decides which art-styles to use.",
                       "The art-styles decide how to use the idutc."],
        }
        artay_help_dict = {
            "Art Styles": ["Glyth - Lines, points and shapes of colors and stuff.",
                           "Glyph - Basically the same as a Glyth, just in a grid.",
                           "Wordie - Word gayms of puzzles with stories with words.",
                           "Spirite - A sprite with spirit for gayms to use as assets.",
                           "Recipe - Recipes help you cook good food, better.",
                           "Foto - Make a foto out of photos and maths.",
                           "Mujic - Music with a pinch of magic.",
                           "Gaym - Games with mixed up logic and spirites.",
                           "Meem - Memes of originality mixed with reposts."]

        }
        texioty_help_dict = {
            "kre8": ["You can use multiple art styles in the same kre8 kommand.",
                     "Separate which art styles to use with a space.",
                     "First style typed will be first created on the kinvow.",
                     "kre8 glyph glyth", "kre8 glyth mujic", "kre8 foto recipe", "kre8 glyph spirite"],
            "dear_sys,": ["This will start diary mode, anything typed will be saved.",
                          "It will still accept kommands while in diary mode.",
                          "Entries will be jumbled in Texioty for some privacy.",
                          "/until_next_time will exit diary mode and save the entry.",
                          "'.diary' is a hidden folder containing diary entries."]
        }
        idutc_help_dict = {
            "Source": ["Random - idutc with random letters and numbers.",
                       "Human - idutc with human name and birthdate."],
            "Keywords": ["Door/Window - Determines the amount of transparency.",
                         "Sock/Rock - Determines how many parts are animated.",
                         "Fire/Ice - Determines speed of animation.",
                         "Camel/Dog/Chicken - Determines size of Masterpiece.",
                         "Rainbow/Cloud - Determines colors of Masterpiece.",
                         "Crayon/Pen - Determines accuracy of colors and lines."]

        }
        kinvow_help_dict = {

        }
        help_dict = {
            "opening": tul_help_dict,
            "aRtay": artay_help_dict,
            "Texioty": texioty_help_dict,
            "idutc": idutc_help_dict,
            "Kinvow": kinvow_help_dict
        }
        for help_str in welcoming_help_strings[tul_section]:
            self.priont_string(help_str)
        self.priont_dict(help_dict[tul_section])

    def wait_for_response(self, response_to_wait_for='') -> str:
        self.priont_string('Saywhatnow?')
        response = self.texity.get()
        self.texity.setvar(value='')
        return response

    def previous_kommand(self):
        """Changes the input box to the previous kommand in the list."""
        if self.input_str_var.get() == '':
            self.kom_index = 0
        if self.kom_index <= len(self.prev_kommand_list) - 1:
            self.kom_index += 1
            final_kom = clamp(len(self.prev_kommand_list) - self.kom_index, 0, len(self.prev_kommand_list) - 1)
            self.input_str_var.set(self.prev_kommand_list[final_kom])

    def next_kommand(self):
        """Changes the input box to the next kommand in the list."""
        if self.kom_index >= 1:
            self.kom_index -= 1
            final_kom = clamp(len(self.prev_kommand_list) - self.kom_index, 0, len(self.prev_kommand_list) - 1)
            self.input_str_var.set(self.prev_kommand_list[final_kom])
        if self.kom_index == 0:
            self.input_str_var.set('')

    def input_from_texity(self):
        """
        Gets the input from texity and determines if it is a kommand.
        :return:
        """
        # GET INPUT AND SPLIT IT INTO A LIST
        text_input = self.input_str_var.get()
        self.input_list = text_input.split()

        if self.isDiary:
            self.diarySentenceList.append(timestamp_line_entry(datetime.now(), text_input,
                                                               lead_line='  ',
                                                               follow_line='_' * (self.diary_line_length - len(
                                                                   text_input) - 2)))
            if self.input_list[0] == "ts":
                self.diarySentenceList.pop()
                tim_samp = datetime.now()
                line_entry = text_input[3:]
                print(f'{tim_samp}  {line_entry}')
                self.diarySentenceList.append(timestamp_line_entry(tim_samp, line_entry,
                                                                   lead_line='ts',
                                                                   follow_line='_' * (self.diary_line_length - len(
                                                                       line_entry) - 2)))

            self.priont_string(f'  [+{"".join(random.sample(text_input, len(text_input)))}')
            if text_input == "/until_next_time":
                et = self.stop_diary_mode()
                self.diarySentenceList.append(timestamp_line_entry(et, text_input,
                                                                   lead_line='ts',
                                                                   follow_line=' ' * (self.diary_line_length - len(
                                                                       text_input))))
                create_date_entry(et, self.diarySentenceList)
                self.clear_texoty()

        if self.input_list:
            self.prev_kommand_list.append(text_input)

        # PRINT THE KOMMAND DICT TO TEXOTY
        if self.input_list[0] == "help" or self.input_list[0] == "?":
            self.clear_texoty()
            if len(self.input_list) > 1:
                self.priont_help(self.input_list[1])
            else:
                self.priont_help()
        if self.input_list[0] == "kommands":
            self.clear_texoty()
            self.priont_commands()

        if self.input_list[0] == "RSG":
            self.clear_texoty()
            self.make_random_sentence()

        # ENTER DIARY MODE
        if self.input_list[0] == "dear_sys,":
            st = self.start_diary_mode()
            self.diarySentenceList.append(timestamp_line_entry(st, self.input_list[0],
                                                               lead_line='ts', follow_line=' ' * (
                        self.diary_line_length - len(self.input_list[0]))))
        # SET THE LANGUAGE OF TEXOTY
        if self.input_list[0] == "set":
            self.chosen_tongue = self.input_list[1]
            self.texoty.tag_add(self.chosen_tongue, "0.0", END)
            self.configure(text=f'Texioty: {self.chosen_tongue}')

        if self.input_list[0] == "dl":
            yt = YouTube(self.input_list[1], on_complete_callback=self.priont_string('Completed'))
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path="YOUTUBE/")
            self.priont_string(f"Downloading {yt.title}")

        if self.input_list[0] == "disp":
            self.clear_texoty()
            kre8dict = self.IDUTC_frame.kre8dict
            self.priont_dict(kre8dict)

        if self.input_list[0] == "addrecipe":
            self.ARTAY_frame.add_osrs_recipes()

        if self.input_list[0] == "check":
            self.clear_texoty()
            # address = self.IDUTC_frame.kre8dict['use_id']
            mm_address = '0xb1A955A7Aa511a7EAA8215b8e086ed2C5d5fE916'
            gs_address = '0xEFc9Fe27d230f89D605d1b59d0BE62fe4da93659'
            lr_address = '0x7d8e7c819e8a1d5e918d81a7d2d00959e85e3404'
            my_addresses = [mm_address, gs_address, lr_address]
            for adrs in my_addresses:
                loopringAccountDict = self.find_loopring_account(adrs)
                nftDict = self.check_nfts(loopringAccountDict['accountId'])
                self.filter_nfts(nftDict, [self.input_list[1]])

        if self.input_list[0] == "kre8":
            print(self.input_list)
            self.create_masterpiece()

        if self.input_list[0] == "avatar":
            self.create_avatar("MOLOKAI", {})

        if self.input_list[0] == "pin":
            self.pin_masterpiece()

        if self.input_list[0] == "batch":
            kre8dict = self.IDUTC_frame.kre8dict
            if not os.path.isdir(kre8dict['name']):
                os.mkdir(kre8dict['name'])
            for abt in ["Avatar", "Banner", "Tile"]:
                self.create_abt(kre8dict, abt)
            self.create_batch(kre8dict)

        # if self.input_list[0] == "discord":
        #
        #     # channel_id_list = [1078081276378087454, 1078370849427562568, 1078371706999148624,
        #     #                    1078371850754740278, 1078371864684019802, 1078372206029066341]
        #     channel_id_list = [1078371850754740278]
        #     for ch_id in channel_id_list:
        #         messages_path = f'{BASE_URL}/channels/{ch_id}/messages'
        #         channel_path = f'{BASE_URL}/channels/{ch_id}'
        #         respo = requests.get(channel_path, headers=headers)
        #         kre8dict = self.IDUTC_frame.setupKRE8dict(f"r4nd0m", f"4206942069", "Random")
        #         # kre8dict = self.IDUTC_frame.setupKRE8dict(f"{respo.json()['name']}", f"{ch_id}"[9:], "Random")
        #         size = set_masterpiece_size(kre8dict['artributes'][3])
        #         nim = Image.new("RGBA", size, BLUE_VIOLET)
        #         self.generate_artyles(nim, kre8dict, self.input_list)
        #         fileName = f"KINVOW/{kre8dict['name']}.png"
        #         nim.save(fileName)
        #         files = {
        #             'file': (f'{fileName}', open(f'{fileName}', 'rb'))
        #         }
        #         paylow = {
        #             "content": fileName
        #         }
        #         if "Mujic" in kre8dict:
        #             mujicFileName = f"MUJIC/{kre8dict['name']}.wav"
        #             files['file'] = (f'{mujicFileName}', open(f'{mujicFileName}', 'rb'))
        #             paylow['content'] = mujicFileName
        #         respo = requests.post(messages_path, json=paylow, headers=headers, files=files)
        #         print(respo)
        self.input_str_var.set("")

        # if len(text_input) == 1:
        #     kre8dict = self.IDUTC_frame.kre8dict
        #     size = set_masterpiece_size(kre8dict['artributes'][3])
        #     nim = Image.new("RGBA", size, DRS_PURPLE)
        #     wordie.check_hangman_letter(text_input, kre8dict)
        #     wordie.update_hangman(nim, kre8dict)
        #     self.priont_dict(kre8dict)
        #     save_name = f"Wordie/{kre8dict['artributes'][3]}/{kre8dict['name']}.png"
        #     nim.save(save_name)
        #     self.crimg = PhotoImage(file=save_name)
        #     self.KINVOW_frame.use_canvas.create_image(320, 320, image=self.crimg)

    def upload_discord(self):
        pass

    def generate_artyles(self, nim: Image, kre8dict: dict, artyle_list: list, abt="Masterpiece"):
        kre8dict[abt] = {}
        for artyle in artyle_list:
            print(f"artyle: {artyle}")
            if artyle.lower() == "glyth":
                self.generate_glyth(nim, kre8dict, abt)
            if artyle.lower() == "glyph":
                self.generate_glyph(nim, kre8dict, abt)
            if artyle.lower() == "wordie":
                self.generate_wordie(nim, kre8dict, abt)
            if artyle.lower() == "spirite":
                self.generate_spirite(nim, kre8dict)
            if artyle.lower() == "foto":
                self.generate_foto(nim, kre8dict)
            if artyle.lower() == "recipe":
                self.generate_recipe(nim, kre8dict)
            if artyle.lower() == "mujic":
                self.generate_mujic(nim, kre8dict)
            if artyle.lower() == "gaym":
                self.generate_gaym(nim, kre8dict)

    def generate_glyth(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a glyth to the img.
        :param img: img to add a glyth to.
        :param abt: Type of image to generate.
        :param kre8dict: Instructions on how to add the glyth.
        :return:
        """
        self.KINVOW_frame.generate_glyth(img, kre8dict, abt)

    def generate_glyph(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a glyph to the img.
        :param abt: Avatar, Banner or Tile or Masterpiece.
        :param img: img to add a glyph to.
        :param kre8dict: Instructions on how to add the glyph.
        :return:
        """
        self.KINVOW_frame.generate_glyph(img, kre8dict, abt)

    def generate_wordie(self, img: Image, kre8dict: dict, abt="Masterpiece"):
        """
        Using the kre8dict, add a wordie to the img.
        :param abt:
        :param img: img to add a wordie to.
        :param kre8dict: Instructions on how to add the wordie.
        :return:
        """
        self.KINVOW_frame.generate_wordie(img, kre8dict, abt)

    def generate_spirite(self, img: Image, kre8dict: dict):
        """
        Using the kre8dict, add a spirite to the img.
        :param img: img to add a spirite to.
        :param kre8dict: Instructions on how to add the spirite.
        :return:
        """
        self.KINVOW_frame.generate_spirite(img, kre8dict)

    def generate_recipe(self, img: Image, kre8dict: dict):
        """
        Using the kre8dict, add a recipe to the img.
        :param img: img to add a recipe to.
        :param kre8dict: Instructions on how to add the recipe.
        :return:
        """
        self.KINVOW_frame.generate_recipe(img, kre8dict)

    def generate_foto(self, img: Image, kre8dict: dict):
        """
        Using the kre8dict, add a foto to the img.
        :param img: img to add a foto to.
        :param kre8dict: Instructions on how to add the foto.
        :return:
        """
        self.KINVOW_frame.generate_foto(img, kre8dict)

    def generate_mujic(self, img: Image, kre8dict: dict):
        """
        Using the kre8dict, add a mujic to the img.
        :param img: img to add a mujic to.
        :param kre8dict: Instructions on how to add the mujic.
        :return:
        """
        self.KINVOW_frame.generate_mujic(img, kre8dict)

    def generate_gaym(self, img: Image, kre8dict: dict):
        """
        Using the kre8dict, add a gaym to the img.
        :param img: img to add a gaym to.
        :param kre8dict: Instructions on how to add the gaym.
        :return:
        """
        self.KINVOW_frame.generate_gaym(img, kre8dict)

    def print_to_texoty(self, string_to_display: str, font_color='blue'):
        self.texoty.configure(fg=font_color)
        self.texoty.insert(END, string_to_display + "\n")
        self.texoty.yview(END)

    def clear_texoty(self):
        """Clear all the text from texoty."""
        self.texoty.delete("0.0", END)

    def priont_dict(self, dioct: dict, dioct_name=None, dioct2_name=None):
        """
        Iterate through dioct and display each key/value pair.

        :param dioct_name:
        :param dioct:
        :param dioct2_name:
        """
        for key in dioct:
            # If there is a dioct_name, there is an inner dictionary.
            if dioct_name:
                lead_space = " " * (len(dioct_name) - 1)
                self.priont_string(f'{lead_space}└{key}┐')
            else:
                self.priont_string(f'{key}┐')
            if type(dioct[key]) == str:
                self.priont_string(f'{" " * (len(key) - 1)} └{dioct[key]}')
            elif type(dioct[key]) == list:
                self.priont_list(key, dioct[key], dioct_name)
            elif type(dioct[key]) == dict:
                self.priont_dict(dioct[key], dioct_name=key)
            elif type(dioct[key]) == int:
                self.priont_int(key, dioct[key])

    def priont_string(self, striong: str, font_color='blue', dioct_name=None):
        """
        Display a striong on texoty in the color of font_color.

        :return:
        @param font_color:
        @param striong:
        @param dioct_name:
        """
        self.texoty.configure(fg=font_color)
        self.texoty.tag_add(self.chosen_tongue, "1.0", END)
        self.texoty.insert(END, striong + "\n")
        self.texoty.yview(END)

    def priont_list(self, key_of_list: str, liost: list, dioct_name=None):
        """
        Display a list on texoty, each item in the list on its own line.

        @param liost:
        @param key_of_list:
        @param dioct_name:
        """
        leading_spaces = " " * len(key_of_list)
        if key_of_list == "number_list":
            self.priont_string(str(f'{leading_spaces}└{liost}'))
        elif dioct_name:
            extra_spaces = " " * (len(dioct_name) + 2)
            for io in liost:
                self.priont_string(f'{leading_spaces}{extra_spaces}└{io}')
        else:
            for io in liost:
                if liost.index(io) == len(liost) - 1:
                    self.priont_string(f'{leading_spaces}└{io}')
                else:
                    self.priont_string(f'{leading_spaces}├{io}')

    def priont_int(self, key_of_int: str, iont: int):
        """Display an integer on texoty."""
        leading_spaces = " " * len(key_of_int)
        self.priont_string(f'{leading_spaces}└{iont}')

    def start_diary_mode(self) -> datetime:
        """Start a diary entry."""
        start_now = datetime.now()
        self.isDiary = True
        self.priont_string(f"-Entering diary mode-   {start_now}")
        self.diarySentenceList = []
        return start_now

    def stop_diary_mode(self) -> datetime:
        """Stop a diary entry."""
        end_now = datetime.now()
        self.isDiary = False
        self.priont_string(f"-Exiting diary mode-   {end_now}")
        return end_now

    def create_avatar(self, img: Image, kre8dict: dict) -> Image:
        # size = set_masterpiece_size("Avatar")
        self.generate_artyles(img, kre8dict, self.input_list, "Avatar")

    def create_banner(self, img: Image, kre8dict: dict) -> Image:
        # size = set_masterpiece_size("Banner")
        self.generate_artyles(img, kre8dict, self.input_list, "Banner")

    def create_tile(self, img: Image, kre8dict: dict) -> Image:
        # size = set_masterpiece_size("Tile")
        self.generate_artyles(img, kre8dict, self.input_list, "Tile")

    def create_abt(self, kre8dict: dict, abt="Avatar"):
        """
        Create an avatar, banner and tile with the given kre8dict.

        :param abt: Which part of the abt?
        :param kre8dict: Instructions to build avatar/banner/tile.
        :return:
        """
        size = set_masterpiece_size(abt)
        nim = Image.new("RGBA", size, SUMMER_SKY)
        if abt == "Avatar":
            self.create_avatar(nim, kre8dict)
        if abt == "Banner":
            self.create_banner(nim, kre8dict)
        if abt == "Tile":
            self.create_tile(nim, kre8dict)
        save_name = f"{kre8dict['name']}/{abt}.png"
        nim.save(save_name)
        self.priont_dict(kre8dict)

    def create_masterpiece(self):
        """
        Create a masterpiece with the selected artyles from the kommand.

        :return:
        """
        kre8dict = self.IDUTC_frame.kre8dict
        size = set_masterpiece_size(kre8dict["artributes"][3])
        nim = Image.new("RGBA", size, DRS_PURPLE)
        if len(self.input_list) > 1:
            self.generate_artyles(nim, kre8dict, self.input_list)
            save_name = f"{self.input_list[1].upper()}/{kre8dict['artributes'][3]}/{kre8dict['name']}.png"
            for c in save_name:
                if c in "?!&":
                    save_name = save_name.replace(c, "")
            nim.save(save_name)
            self.crimg = PhotoImage(file=save_name)
            self.KINVOW_frame.use_canvas.create_image(320, 320, image=self.crimg)
        self.priont_dict(kre8dict)

    def pin_masterpiece(self):
        kre8dict = self.IDUTC_frame.kre8dict
        pin_resp = self.manny.pin_masterpiece_pinata(kre8dict["name"], kre8dict["file_path"])
        kre8dict["image"] += pin_resp["IpfsHash"]
        kre8dict["animation_url"] += pin_resp["IpfsHash"]
        self.priont_dict(pin_resp)
        save_json(kre8dict)
        self.IDUTC_frame.setUseIDUTC()

    def create_batch(self, kre8dict: dict):
        batch_size = self.input_list[1]
        for i in range(int(batch_size)):
            size = set_masterpiece_size("Dog")
            nim = Image.new("RGBA", size, DRS_PURPLE)
            self.generate_artyles(nim, kre8dict, self.input_list)
            save_name = f"{kre8dict['name']}/{i}_{kre8dict['name']}.png"
            nim.save(save_name)

    def find_loopring_account(self, address: str) -> dict:
        endpoint = self.base_loopring_api_url + "/api/v3/account"
        endpoint += f"?owner={address}"
        response: requests.Response = requests.get(url=endpoint)
        return response.json()

    def check_nfts(self, lr_account_id: int) -> dict:
        endpoint = self.base_loopring_api_url + f"/api/v3/user/nft/balances"
        endpoint += f"?accountId={lr_account_id}"
        lr_headers = {
            'X-API-KEY': "j0Uvr4vGb4cLZr6TUfnMfW1krU3CaPil10cJPiNCumZCwfUGgZiQQHcVHsvYLGOS"
        }
        response: requests.Response = requests.get(url=endpoint, headers=lr_headers)
        return response.json()

    def filter_nfts(self, nft_dict: dict, white_list: list):
        for nft in nft_dict['data']:
            if nft['nftId'] == white_list[0].lower():
                self.priont_dict(nft)

    def generate_avatar(self, nim, kre8dict):
        pass

    def priont_commands(self):
        self.priont_dict(self.commands_dict)

    def make_random_sentence(self):
        subject = random.choice(["A full grown clown-adult", "A scary robot", "Superman", "My 9th grade English teacher",
                                 "The local veterinary", "The next door neighbor", "The slowest firefighter", "Jeremy"])
        action = random.choice(["kicked", "jumped over", "stole", "made a sandwich with", "smoked something with",
                                "got too drunk with", "couldn't find", "made the dumbest face at"])
        objekt = random.choice(["a soccer ball", "my brand new lego set", "my first dog", "the tall shady tree",
                                "some dirty underwear", "a dead skunk"])
        aftermath = random.choice(["then did a cartwheel", "after beating cheeks with grandpa", "and obviously died",
                                   "and decided to rob a liquer store", "but couldn't plant a potato",
                                   "mission accomplished"])
        self.priont_string(f"{subject} {action} {objekt}, {aftermath}{random.choice(['.', '!', '?'])}")


def create_date_entry(entry_time: datetime, entry_list: list):
    """
    Create a date entry for today.
    :param entry_time: Exact time the entry was created.
    :param entry_list: List of entry lines.
    :return:
    """
    entry_date_name = f'{entry_time.year}_{entry_time.month}_{entry_time.day}'
    entry_list.pop(len(entry_list) - 2)
    if exists(f'.diary/{entry_date_name}.txt'):
        with open(f'.diary/{entry_date_name}.txt', 'a') as f:
            for ent in entry_list:
                f.write(ent + "\n")
            f.write("\n")
    else:
        with open(f'.diary/{entry_date_name}.txt', 'w') as f:
            for ent in entry_list:
                f.write(ent + "\n")
            f.write("\n")


def timestamp_line_entry(entry_time: datetime, entry_line: str, lead_line=" ", follow_line=" ") -> str:
    """
    Take an entry line and add a time stamp with a lead and follow string.
    
    :param entry_time: Hour:Minute:Seconds
    :param entry_line: Text to be timestamped
    :param lead_line: Text to the left of the entry_line
    :param follow_line: Text to the right of the entry_line
    :return:
    """
    time_stamp = f'{entry_time.hour:02d}:{entry_time.minute:02d}:{entry_time.second:02d}'
    ret_str = lead_line + entry_line + follow_line
    if lead_line == "ts":
        ret_str = '  ' + entry_line + follow_line + time_stamp
        if entry_line == "dear_sys," or entry_line == "/until_next_time":
            ret_str = entry_line + follow_line + time_stamp + f':{entry_time.microsecond:2d}'

    return ret_str


def set_masterpiece_size(image_size: str) -> (int, int):
    """
    Set the size of the masterpiece from animal to pixels.
    @param image_size:
    @return:
    """
    size = (0, 0)
    if image_size == "Chicken":
        size = (320, 320)
    elif image_size == "Dog":
        size = (640, 640)
    elif image_size == "Camel":
        size = (960, 960)
    elif image_size == "Avatar":
        size = (500, 500)
    elif image_size == "Tile":
        size = (500, 700)
    elif image_size == "Banner":
        size = (1500, 500)
    return size


def save_json(kre8dict: dict):
    """
    Saves the Meta dictionary as a JSON file in the folder of data_source.
    :return:
    """
    dumpDict = kre8dict
    with open(f'JSONs/{kre8dict["name"]}.json', 'w') as f:
        json.dump(dumpDict, f, indent=4)
