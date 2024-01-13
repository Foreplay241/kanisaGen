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
textbox_width = 88


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
        self.texoty = Text(self, height=32, width=textbox_width, bg="light blue", relief=SUNKEN)
        self.texoty.grid(column=0, row=0, rowspan=28)
        self.input_str_var = StringVar()
        self.texity = Entry(self, width=textbox_width, bg="light green", textvariable=self.input_str_var)
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

        # PRINT A LIST OF COMMANDS TO TEXOTY
        if self.input_list[0] == "kommands":
            self.clear_texoty()
            self.priont_commands()

        # PRINT A RANDOMLY GENERATED SENTENCE
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

        if self.input_list[0] == "disp":
            self.clear_texoty()
            kre8dict = self.IDUTC_frame.kre8dict
            self.priont_dict(kre8dict)

        self.input_str_var.set("")

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

    def find_loopring_account(self, address: str) -> dict:
        endpoint = self.base_loopring_api_url + "/api/v3/account"
        endpoint += f"?owner={address}"
        response: requests.Response = requests.get(url=endpoint)
        return response.json()

    def filter_nfts(self, nft_dict: dict, white_list: list):
        for nft in nft_dict['data']:
            if nft['nftId'] == white_list[0].lower():
                self.priont_dict(nft)

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
