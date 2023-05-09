from flask import Blueprint

import random
import pokebase as pb

bp = Blueprint('pokemon', __name__, url_prefix='/pokemon')


def load_pokemon():
    _dict = {}
    rand_list = random.sample(range(1, 890), 6)
    for i, _n in enumerate(rand_list):
        p_num = _n
        p_info = pb.pokemon(_n)
        p_sprite = pb.SpriteResource(
            'pokemon', _n, other=True, official_artwork=True)
        _dict[i] = [p_num, p_info.name.title(), p_sprite.url]
    return _dict


lp = load_pokemon()

from app.blueprints.pokemon import routes