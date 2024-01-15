from dataclasses import dataclass
import random

import mtgsdk

info_list = ["name", "type", "rarity", "artist",  "number", "color_identity"]
spell_info_list = ["mana_cost", "cmc"]
creature_info_list = ["power", "toughness"]
listed_card_names = ["ultimatum", "lightning", "boots", "explore", "demon", "angel"]
keyword_abilities = ["first strike", "deathtouch", "haste"]


def new_chosen_card(kard: mtgsdk.Card) -> dict:
    """Return an info dictionary based on the kard being used."""
    card_info_dict = {
        'name': kard.name,
        'type': kard.type,
        'rarity': kard.rarity,
        'artist': kard.artist,
        'number': kard.number,
        'color_identity': kard.color_identity,
    }
    if 'Land' not in kard.type:
        info_list.append('mana_cost')
        info_list.append('cmc')
        card_info_dict['mana_cost'] = kard.mana_cost
        card_info_dict['cmc'] = kard.cmc
    if kard.text:
        info_list.append('text')
        card_info_dict['text'] = kard.text
    
    if "Creature" in kard.type:
        info_list.append('power')
        info_list.append('toughness')
        card_info_dict['power'] = kard.power
        card_info_dict['toughness'] = kard.toughness
    return card_info_dict


def get_new_card(partial_name: str) -> mtgsdk.Card:
    """Get a random new card based on the partial name."""
    named_cards = mtgsdk.Card.where(name=partial_name).all()
    chosen_card = random.choice(named_cards)
    while chosen_card.multiverse_id is None:
        chosen_card = random.choice(named_cards)
    return chosen_card


def create_idutc() -> (str, str):
    """Create an idutc with MTG being the data source."""
    card_name = random.choice(listed_card_names)
    named_cards = mtgsdk.Card.where(name=card_name).all()
    chosen_card = random.choice(named_cards)
    use_id = chosen_card.name
    lz = '0'
    # ENSURE THERE IS A 10-DIGIT MULTIVERSE ID FOR THE CHOSEN CARD
    while chosen_card.multiverse_id is None:
        chosen_card = random.choice(named_cards)
    if len(str(chosen_card.multiverse_id)) < 10:
        lz *= 10 - len(str(chosen_card.multiverse_id))
    use_utc = lz + str(chosen_card.multiverse_id)
    return use_id, use_utc
