import json
import os
import random
from datetime import time, datetime
from os.path import exists
from tkinter import *
import requests
import idutc
import wordie
# from manfried import TalkingPinata
from settings import *

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BASE_URL = "https://discord.com/api/v9"
headers = {
    "Authorization": f"Bot {TOKEN}"
}
textbox_width = 88


class TEXIOTY(LabelFrame):
    def __init__(self, master=None, IDUTC=None):
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
        self.configure(text=f'Texioty:')
        self.IDUTC_frame: idutc.IDUTC = IDUTC
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
        # DIFFERENT MODES TO BE ENABLED AND DISABLED
        self.isTestingKeys = False
        self.isDiary = False

        self.isHiLo = False
        self.hilo_number = 12
        self.hilo_guesses = 0

        self.diary_line_length = 75
        self.diarySentenceList = []
        self.prev_kommand_list = []

        self.isHangman = False
        self.missed_hangman_letters = []
        self.hangman_phrase = random.choice(wordie.HANGMAN_PHRASES)
        self.hidden_hangman_phrase = {}

        # KOMMAND CYCLING
        self.kom_index = 0
        self.texity.bind('<Up>', lambda e: self.previous_kommand())
        self.texity.bind('<Down>', lambda e: self.next_kommand())
        self.texity.focus_set()

        self.base_loopring_api_url = "https://api3.loopring.io"

        self.commands_dict = {"'disp'": ["Display the current kre8dict."],
                              "'dear_sys,'": ["Enters into diary mode.",
                                              "Anything typed will be added to a diary entry."],
                              "'/until_next_time'": ["Exits diary mode.", "Saves the entry into the .diary folder."],
                              "'help'": ["Displays some help about the program itself."],
                              "'kommands'": ["Displays this."],
                              "'start (hangman, hilo)'": ["Start a hangman or a hilo game."]}

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
        texioty_help_list_strings = ["                    ╪Texioty╪",
                                     "                    └┴┴┴┴┴┴┴┘",
                                     "Texioty is all about processing commands and displaying information.", ""]
        idutc_help_list_strings = ["                    ╪idutc╪",
                                   "                    └┴┴┴┴┴┘",
                                   "The idutc is a combination of an id and a utc.", ""]
        welcoming_help_strings = {
            "opening": help_list_strings,
            "Texioty": texioty_help_list_strings,
            "idutc": idutc_help_list_strings
        }
        print(tul_section)
        tul_help_dict = {
            "Texioty": ["Bottom tul, derives from 'text' and 'IO'",
                        "The green box is used for textual input.",
                        "The blue box is used for textual output.",
                        "For a list of commands, use the 'kommands' command."],
            "idutc": ["Top tul, derives from 'id' and 'utc'",
                      "Source and keywords dictate creation and whatnot.",
                      "You can type many letters and numbers in the yellow box.",
                      "In the red box you can type a 10-digit number."]
        }
        texioty_help_dict = {
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
        help_dict = {
            "opening": tul_help_dict,
            "Texioty": texioty_help_dict,
            "idutc": idutc_help_dict
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

        if self.isHangman:
            if self.input_list[0] == "guess" and len(self.missed_hangman_letters) < 6:
                self.hidden_hangman_phrase, self.missed_hangman_letters = wordie.check_hangman_letter(self.input_list[1],
                                                                                                      self.hangman_phrase,
                                                                                                      self.hidden_hangman_phrase,
                                                                                                      self.missed_hangman_letters)
                self.clear_texoty()
                self.priont_string(wordie.HANGMAN_TEXTMAN_LIST[len(self.missed_hangman_letters)])
                self.priont_string(wordie.dict_to_str(self.hidden_hangman_phrase))
                self.priont_string("Missed letters┐")
                self.priont_list("Missed letters", self.missed_hangman_letters)

            elif len(self.input_list[1]) > 1 and self.input_list[0] == "guess":
                self.priont_string("Too many letters, only one at a time, please.")

            else:
                self.priont_string("No more guesses!")
                self.end_hangman_mode()

        if self.isHiLo:
            if self.input_list[0] == "guess":
                guess_num = int(self.input_list[1])
                self.hilo_guesses += 1
                if guess_num > self.hilo_number:
                    self.priont_string("too big")
                elif guess_num < self.hilo_number:
                    self.priont_string("too small")
                elif guess_num == self.hilo_number:
                    self.priont_string("just right")
                    self.priont_string(f"You guessed correctly with {self.hilo_guesses} attempts.")
                    self.end_hilo_mode()

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
            self.priont_string(wordie.generate_madlib_sentence(random.choice(["kicked", "threw up on", "jumped over",
                                                                              "can deliver", "shot guns at", "tackled",
                                                                              "stole", "built"]), self.IDUTC_frame.kre8dict))

        if self.input_list[0] == "madlib":
            self.clear_texoty()
            self.start_madlib_story()

        if self.input_list[0] == "start":
            self.clear_texoty()
            if self.input_list[1] == "hangman":
                self.hidden_hangman_phrase = self.start_hangman_mode()
                self.priont_string(wordie.HANGMAN_TEXTMAN_LIST[0])
                self.priont_string(wordie.dict_to_str(self.hidden_hangman_phrase))
                self.priont_string("Missed letters┐")
            elif self.input_list[1] == "hilo":
                self.hilo_number = self.start_hilo_mode()
                self.priont_string("Guess a number between: 0 and 99")

        if self.input_list[0] == "end":
            if self.input_list[1] == "hangman":
                self.priont_string(wordie.dict_to_str(self.hidden_hangman_phrase))
                self.priont_string(self.hangman_phrase)
                self.priont_string("Thank you for playing!")
                self.isHangman = False

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
        if self.isHangman or self.isHiLo:
            self.input_str_var.set("guess ")
            self.texity.icursor(END)

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

    def start_hangman_mode(self) -> dict:
        self.isHangman = True
        self.configure(text=f'Texioty: Hangman')
        return self.reset_hidden_phrase()

    def reset_hidden_phrase(self):
        self.missed_hangman_letters = []
        self.hangman_phrase = random.choice(wordie.HANGMAN_PHRASES)
        self.hidden_hangman_phrase = {}
        hidden_c = "-"
        for c in self.hangman_phrase:
            for i in range(len(self.hangman_phrase)):
                if c in self.hidden_hangman_phrase:
                    c += c[0]
            self.hidden_hangman_phrase[c] = "◙"
            if c[0] in " ,.?!":
                self.hidden_hangman_phrase[c] = c[0]
            else:
                self.hidden_hangman_phrase[c] = "◙"
        for key in self.hidden_hangman_phrase:
            print(f"{key}: {self.hidden_hangman_phrase[key]}")
        return self.hidden_hangman_phrase

    def end_hangman_mode(self):
        self.clear_texoty()
        self.isHangman = False
        self.configure(text=f'Texioty:')

    def start_hilo_mode(self) -> int:
        self.isHiLo = True
        random_number = random.randint(0, 99)
        self.configure(text=f'Texioty: HiLo')
        return random_number

    def end_hilo_mode(self):
        self.isHiLo = False
        self.configure(text=f'Texioty:')

    def start_diary_mode(self) -> datetime:
        """Start a diary entry."""
        start_now = datetime.now()
        self.isDiary = True
        self.priont_string(f"-Entering diary mode-   {start_now}")
        self.diarySentenceList = []
        self.configure(text=f'Texioty: Digiary')
        return start_now

    def stop_diary_mode(self) -> datetime:
        """Stop a diary entry."""
        end_now = datetime.now()
        self.isDiary = False
        self.priont_string(f"-Exiting diary mode-   {end_now}")
        self.configure(text=f'Texioty:')
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
        subject = random.choice(["A fully grown adult clown", "A scary robot", "Superman", "My 9th grade English teacher",
                                 "The local veterinary", "The next door neighbor", "The slowest firefighter", "Jeremy"])
        action = random.choice(["kicked", "jumped over", "stole", "made a sandwich with", "smoked something with",
                                "got too drunk with", "couldn't find", "made the dumbest face at"])
        objekt = random.choice([f"a {random.choice(['soccer ', 'foot', 'basket', 'base'])}ball", "my brand new lego set", "my first dog", "the tall shady tree",
                                "some dirty underwear", "a dead skunk"])
        aftermath = random.choice(["then did a cartwheel", "after beating cheeks with grandpa", "and obviously died",
                                   "and decided to rob a liquer store", "but couldn't plant a potato",
                                   "mission accomplished"])
        self.priont_string(f"{subject} {action} {objekt}, {aftermath}{random.choice(['.', '!', '?'])}")

    def start_madlib_story(self, ):
        pass


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


def save_json(kre8dict: dict):
    """
    Saves the Meta dictionary as a JSON file in the folder of data_source.
    :return:
    """
    dumpDict = kre8dict
    with open(f'JSONs/{kre8dict["name"]}.json', 'w') as f:
        json.dump(dumpDict, f, indent=4)
