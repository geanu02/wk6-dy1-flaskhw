from flask import render_template

import pokebase as pb

from . import bp 

@bp.route('/')
def home():

    s1 = pb.SpriteResource('pokemon', 17)

    return render_template(
        'index.jinja',
        title="PokeFavorites: Welcome!",
        sprite1=s1.url
    )

@bp.route('/about')
def about():
    return render_template(
        'about.jinja',
        title="PokeFavorites: About Page"
    )

@bp.route('/access')
def access():
    return render_template(
        'access.jinja',
        title="PokeFavorites: Access Page"
    )