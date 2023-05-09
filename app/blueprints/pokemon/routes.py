from flask import render_template 

from . import bp, lp

@bp.route('/pokemon')
def pokemon():
    return render_template(
        'pokemon.jinja',
        title="PokeFavorites: Pokemon",
        _dict=lp
    )