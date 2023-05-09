from flask import render_template

from . import bp, lp
from datetime import date


@bp.route('/pokemon')
def pokemon():
    return render_template(
        'pokemon.jinja',
        title="PokeFavorites: Pokemon",
        _date=date.today(),
        _dict=lp
    )
