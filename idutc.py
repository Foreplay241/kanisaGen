import datetime
import json
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from settings import *
import sourceOSRS
import sourceMTG
import sourceREDDIT


class IDUTC(tk.LabelFrame):
    def __init__(self, master=None, TEXIOTY=None):
        """
        This is the frame for inputting the ID and UTC.

        :param master: Toolbox frame that contains each Tul.
        :param TEXIOTY: Texioty frame, for textual input and output.
        """
        super().__init__(master)
        self.configure(text="idutc")
        self.TEXIOTY = TEXIOTY
        self.entry_ID_string_var = StringVar()
        self.entry_UTC_string_var = StringVar()
        self.id_entry = Entry(self, textvariable=self.entry_ID_string_var, bg='light yellow')
        # IT'S NOT PINK,
        self.utc_entry = Entry(self, textvariable=self.entry_UTC_string_var, bg='pink')
        # IT'S LIGHT-ISH RED
        self.id_entry.grid(column=1, row=0, columnspan=2)
        self.utc_entry.grid(column=1, row=1, columnspan=2)

        # INITIATE THE BUTTONS TO CONTROL USE_ID AND USE_UTC
        self.new_button = Button(self, text="New ID/UTC", command=self.generate_new_IDUTC, width=10)
        self.set_button = Button(self, text="Set ID/UTC", command=self.setUseIDUTC, width=10)
        self.save_button = Button(self, text="Save Metadata", command=self.saveJSON, width=10)
        self.load_button = Button(self, text="Load Metadata", command=self.loadJSON, width=10)
        self.new_button.grid(column=3, row=0)
        self.set_button.grid(column=3, row=1)
        self.save_button.grid(column=4, row=0)
        self.load_button.grid(column=4, row=1)

        data_source_options = [
            "Random", "Reddit", "OSRS",
            "Human", "MTG"]

        self.artyle_artributes_dict = {
            "Transparency": ["Door", "Window"],
            "Coloration": ["Rainbow", "Cloud"],
            "Animation Speed": ["Ice", "Fire"],
            "Size": ["Chicken", "Dog", "Camel"],
            "Motion Range": ["Sock", "Rock"],
            "Accuracy": ["Pen", "Crayon"]
        }
        ki = 0
        self.attributeMenus = {}
        for key in list(self.artyle_artributes_dict.keys()):
            attribute_str_var = StringVar()
            attribute_str_var.set(random.choice(self.artyle_artributes_dict[key]))
            if key == "Size":
                attribute_str_var.set("Dog")
            self.attributeMenus[key] = [attribute_str_var,
                                        OptionMenu(self, attribute_str_var, *self.artyle_artributes_dict[key])]
            row = ki % 2
            col = ki % 3
            self.attributeMenus[key][1].grid(column=col + 5, row=row)
            ki += 1

        self.data_source_var = StringVar()
        self.data_source_var.set("Random")
        dropmenu = OptionMenu(self, self.data_source_var, *data_source_options)
        dropmenu.grid(column=0, row=0, rowspan=2)
        self.use_data_dict = {}
        self.generate_new_IDUTC()
        self.setUseIDUTC()
        self.kre8dict = self.setupKRE8dict(self.entry_ID_string_var.get(),
                                           self.entry_UTC_string_var.get(),
                                           self.data_source_var.get())

    def gather_attributes(self) -> list:
        attribs_list = []
        for key in self.attributeMenus:
            attribs_list.append(self.attributeMenus[key][0].get())
        return attribs_list

    def saveJSON(self):
        """
        Saves the Meta dictionary as a JSON file in the folder of data_source.
        :return:
        """
        use_id = self.kre8dict["use_id"]
        use_utc = self.kre8dict["use_utc"]
        file_name = f'{use_id}_{use_utc}'
        sorted_number_list = new_number_list(use_utc)
        sorted_number_list.sort()
        save_folder = self.kre8dict["data_source"]
        dumpDict = self.kre8dict
        print(dumpDict)
        dumpDict["royalty_percentage"] = 3
        dumpDict["image"] = "ipfs://"
        dumpDict["animation_url"] = "ipfs://"
        with open(f'JSONs/{save_folder}/{file_name}.json', 'w') as f:
            json.dump(dumpDict, f, indent=4)

    def generate_new_IDUTC(self):
        """
        Generate a new IDUTC based on the data_source
        """
        use_id, use_utc = create_id_utc(self.data_source_var.get())
        if self.data_source_var.get() == "Reddit":
            use_id, use_utc = sourceREDDIT.create_IDUTC()
        elif self.data_source_var.get() == "MTG":
            use_id, use_utc = sourceMTG.create_idutc()
        elif self.data_source_var.get() == "OSRS":
            use_id, use_utc = sourceOSRS.create_IDUTC()
        self.id_entry.delete(0, END)
        self.utc_entry.delete(0, END)
        self.id_entry.insert(0, use_id)
        self.utc_entry.insert(0, use_utc)

    def setUseIDUTC(self):
        """
        Sets up the initial "use_data_dict" to generate the final Meta dictionary.
        :return:
        """
        self.kre8dict = self.setupKRE8dict(self.entry_ID_string_var.get(),
                                           self.entry_UTC_string_var.get(),
                                           self.data_source_var.get())

    def loadJSON(self):
        """Loads an idutc from a json file."""
        loaded_file = askopenfilename(initialdir='/home/trevor/PythonProjects/KanisaRedditGen/JSONs/')
        loaded_file = loaded_file.replace("/", " ")
        loaded_file = loaded_file.split()
        loaded_file = loaded_file[len(loaded_file) - 1][:-5].split('_')
        self.entry_ID_string_var.set(loaded_file[0])
        self.entry_UTC_string_var.set(loaded_file[1])

    def add_random_dict(self):
        """Add a dictionary of random data."""
        pass

    def add_reddit_dict(self):
        """Add a dictionary of reddit data."""
        pass

    def add_mtg_dict(self):
        """Add a dictionary of MTG data."""
        self.use_data_dict['MTG_dict'] = sourceMTG.new_chosen_card(
            sourceMTG.get_new_card(self.TEXIOTY.input_text_entry.get()))

    def setupKRE8dict(self, use_id: str, use_utc: str, data_source: str) -> dict:
        """
        Sets up the initial KRE8shun dictionary.
        """
        number_list = new_number_list(use_utc)
        number_list.sort()
        desc = ""
        for c in use_id:
            if c.lower() in ALPHANUMERIC_WORD_LISTS:
                desc += random.choice(ALPHANUMERIC_WORD_LISTS[c.lower()]) + " "
            else:
                desc += random.choice(PUNCTUATION_WORD_LISTS[c.lower()]) + " "
        filename = random.choice(desc.split()[0:2]).title() + "_" + random.choice(desc.split()[2:4]).title() + "_" + random.choice(desc.split()[4:6]).title()
        KRE8dict = {
            "use_id": use_id,
            "use_utc": use_utc,
            "color_list": new_color_list(use_id, is_float=False),
            "number_list": number_list,
            "data_source": data_source,
            "name": filename,
            "file_path": f"GLYTH/{self.gather_attributes()[3]}/{filename}.png",
            "artributes": self.gather_attributes(),
            "description": desc
        }
        return KRE8dict


def add_data_source_dict(use_data: dict):
    """
    Adds data_source dictionary keys and values for the data source info.
    :param use_data: dictionary to add data source infor to.
    :return:
    """
    if use_data["data_source"] == "Reddit":
        submission = reddit.submission(use_data["use_ID"])
        use_data["link"] = f'https://www.reddit.com/{use_data["use_ID"]}'
        use_data["submission"] = submission
    elif use_data["data_source"] == "OSRS":
        use_data["OSRS Player"] = "OSRSSTUFF"
        use_data["Player Skills"] = ["Attack", "Defence", "Prayer"]
    elif use_data["data_source"] == "MTG":
        card_name = use_data["use_id"]
        named_cards = Card.where(name="Boros").all()
        if len(named_cards) == 0:
            named_cards = Card.where(name="King").all()
        chosen_card = random.choice(named_cards)
        flavor_list = []
        lz = '0'
        if len(str(chosen_card.multiverse_id)) < 10:
            lz *= 10 - len(str(chosen_card.multiverse_id))
        for card in named_cards:
            if card.flavor not in flavor_list:
                flavor_list.append(card.flavor)

    elif use_data["data_source"] == "Human":
        # use_data["name"] = ""
        pass
    elif use_data["data_source"] == "Barcode":
        use_data["item_name"] = ""
        use_data["item_info"] = []


# def setupKRE8dict(use_id: str, use_utc: str, data_source: str) -> dict:
#     """
#     Sets up the initial KRE8shun dictionary.
#     """
#     number_list = new_number_list(use_utc)
#     number_list.sort()
#     filename = f"{use_id}_{use_utc}_{datetime.datetime.now().microsecond}"
#     KRE8dict = {
#         "use_id": use_id,
#         "use_utc": use_utc,
#         "color_list": new_color_list(use_id),
#         "number_list": number_list,
#         "data_source": data_source,
#         "name": filename,
#         "artributes": ["Window", "Rainbow", "Fire", "Dog", "Sock", "Pen"]
#     }
#     return KRE8dict
