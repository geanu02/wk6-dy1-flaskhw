from flask import render_template, flash
from flask_login import current_user
from . import bp, lp
from datetime import date

from app.models import FavePokemon
from app.forms import FavePokemonForm


@bp.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    form = FavePokemonForm()
    if form.validate_on_submit():
        poke_num = form.poke_num.data
        fave = FavePokemon(poke_num=poke_num)
        if poke_num in lp.keys():
            fave.poke_name = lp[poke_num][0]
            fave.user_id = current_user.user_id
            fave.commit()
            flash(
                f"{lp[poke_num][0]} successfully added to your party!", "success")
            
        else:
            flash(
                f"{poke_num} isn't one of the six chosen Pokemon for you today. Try again.", "warning")
    return render_template(
        'pokemon.jinja',
        title="PokeFavorites: Pokemon",
        _date=date.today(),
        _dict=lp,
        form=form
    )
