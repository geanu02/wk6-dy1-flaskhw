from flask import Blueprint

import random
import pokebase as pb

bp = Blueprint('pokemon', __name__, url_prefix='/pokemon')

def load_pokemon():
    _dict = {}
    rand_list = random.sample(range(1, 890), 6)
    for num in rand_list:
        p_info = pb.pokemon(num)
        p_sprite = pb.SpriteResource(
            'pokemon', num, other=True, official_artwork=True)
        _dict[num] = [p_info.name.title(), p_sprite.url]
    return _dict

lp = load_pokemon()

def lookup_pokemon(num):
    return pb.pokemon(num).name.title()

from app.blueprints.pokemon import routes