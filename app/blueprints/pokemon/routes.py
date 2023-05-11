from flask import render_template, flash
from flask_login import current_user
from . import bp, lp, lookup_pokemon
from datetime import date

from app.models import FavePokemon
from app.forms import FavePokemonForm


@bp.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    form = FavePokemonForm()
    if form.validate_on_submit():
        poke_num = form.poke_num.data
        pokenum_check = FavePokemon.query.filter_by(poke_num=poke_num).first()
        if not pokenum_check:
            poke_name = lp[poke_num][0]
        else:
            poke_name = lookup_pokemon(poke_num)
        if not pokenum_check and poke_num in lp.keys():
            fave = FavePokemon(poke_num=poke_num)
            fave.poke_name = poke_name
            fave.user_id = current_user.user_id
            fave.commit()
            flash(f"{poke_name} successfully added to your party!", "success")
        elif pokenum_check and poke_num not in lp.keys():
            flash(f"{poke_name} isn't one of today's six favorites, but it's part of your team!", "warning")
        elif pokenum_check and poke_num in lp.keys():
            flash(f"{poke_name} is already in your party!", "warning")
        else:
            flash(f"Pokemon # {poke_name} isn't one of today's six chosen Pokemon. Try again?", "warning")
    return render_template(
        'pokemon.jinja',
        title="PokeFavorites: Pokemon",
        _date=date.today(),
        _dict=lp,
        form=form
    )
