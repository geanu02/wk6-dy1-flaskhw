from flask import render_template 

from . import bp 

@bp.route('/pokemon')
def pokemon():
    return render_template(
        'pokemon.jinja',
        title="PokeFavorites: Pokemon"
    )