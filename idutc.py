# import datetime
import json
# import random
import tkinter as tk
from tkinter import *
# from tkinter import ttk
# from tkinter.filedialog import askopenfilename
from settings import *
import sourceOSRS
import sourceMTG
import sourceREDDIT


class IDUTC(tk.LabelFrame):
    def __init__(self, master=None, texioty=None):
        """
        This is the frame for inputting the ID and UTC.

        :param master: Toolbox frame that contains each Tul.
        :param texioty: Texioty frame, for textual input and output.
        """
        super().__init__(master)
        self.configure(text="idutc")
        self.TEXIOTY = texioty
        self.entry_ID_string_var = StringVar()
        self.entry_UTC_string_var = StringVar()
        self.id_entry = Entry(self, textvariable=self.entry_ID_string_var, bg='light yellow')
        # IT'S NOT PINK,
        self.utc_entry = Entry(self, textvariable=self.entry_UTC_string_var, bg='pink')
        # IT'S LIGHT-ISH RED
        self.id_entry.grid(column=1, row=0, columnspan=2)
        self.utc_entry.grid(column=1, row=1, columnspan=2)

        # INITIATE THE BUTTONS TO CONTROL USE_ID AND USE_UTC
        self.new_button = Button(self, text="New ID/UTC", command=self.generate_new_idutc, width=10)
        self.set_button = Button(self, text="Set ID/UTC", command=self.set_use_idutc, width=10)
        self.save_button = Button(self, text="Save Metadata", command=self.save_json, width=12)
        self.new_button.grid(column=3, row=0)
        self.set_button.grid(column=3, row=1)
        self.save_button.grid(column=4, row=0, rowspan=2)

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
        self.generate_new_idutc()
        self.set_use_idutc()
        self.kre8dict = self.setup_kre8dict(self.entry_ID_string_var.get(),
                                            self.entry_UTC_string_var.get(),
                                            self.data_source_var.get())

    def gather_attributes(self) -> list:
        attribs_list = []
        for key in self.attributeMenus:
            attribs_list.append(self.attributeMenus[key][0].get())
        return attribs_list

    def save_json(self):
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

    def generate_new_idutc(self):
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

    def set_use_idutc(self):
        """
        Sets up the initial "use_data_dict" to generate the final Meta dictionary.
        :return:
        """
        self.kre8dict = self.setup_kre8dict(self.entry_ID_string_var.get(),
                                            self.entry_UTC_string_var.get(),
                                            self.data_source_var.get())

    def add_random_dict(self):
        """Add a dictionary of random data."""
        pass

    def add_reddit_dict(self, kre8dict: dict):
        """Add a dictionary of reddit data."""
        kre8dict['Reddit_dict'] = sourceREDDIT.new_chosen_submission(self.entry_ID_string_var.get())

    def add_mtg_dict(self, kre8dict: dict):
        """Add a dictionary of MTG data."""
        kre8dict['MTG_dict'] = sourceMTG.new_chosen_card(
            sourceMTG.get_new_card(self.entry_ID_string_var.get()))

    def add_osrs_dict(self, kre8dict: dict):
        kre8dict['OSRS_dict'] = sourceOSRS.new_chosen_player(self.entry_ID_string_var.get())

    def setup_kre8dict(self, use_id: str, use_utc: str, data_source: str) -> dict:
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
        filename = random.choice(desc.split()).title() + "_" + random.choice(desc.split()).title()
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
        if data_source == "MTG":
            self.add_mtg_dict(KRE8dict)
        elif data_source == "Reddit":
            self.add_reddit_dict(KRE8dict)
        elif data_source == "OSRS":
            self.add_osrs_dict(KRE8dict)
        return KRE8dict
