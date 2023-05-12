from flask import render_template, flash
from flask_login import current_user, login_required
from . import bp, lp, lookup_pokemon
from datetime import date

from app.models import User, FavePokemon
from app.forms import FavePokemonForm


@bp.route('/todays_pokemon', methods=['GET', 'POST'])
def todays_pokemon():
    form = FavePokemonForm()
    if form.validate_on_submit():
        poke_num = form.poke_num.data
        poke_name = lookup_pokemon(poke_num)
        logged_in_user = current_user.user_id
        user = User.query.filter_by(user_id=logged_in_user).first()
        pokenum_check = poke_num in [num.poke_num for num in user.fave_pokemon]
        # pokenum_check = FavePokemon.query.filter_by(poke_num=poke_num).first()
        if poke_num in lp.keys():
        # If the Pokemon number one of today's 6
            if not pokenum_check:
            # If Pokemon is not in the FavePokemon table:
                fave = FavePokemon(poke_num=poke_num)
                fave.poke_name = poke_name
                fave.poke_art = lp[poke_num][1]
                fave.user_id = logged_in_user
                fave.commit()
                flash(f"{poke_name} has been successfully added to your party!", "success")
            # If Pokemon is in the FavePokemon table and user:
            else:
                flash(f"{poke_name} is already in your party!", "warning")
        else:
            if pokenum_check:
                flash(
                    f"{poke_name} isn't one of today's six favorites, but it's part of your team!", "warning")
            else:
                flash(
                    f"{poke_name} isn't one of today's chosen six Pokemon. Try again?", "warning")
    return render_template(
        'pokemon.jinja',
        title="PokeFavorites: Pokemon",
        _date=date.today(),
        _dict=lp,
        form=form
    )

@bp.route('/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first()
    return render_template(
        'user_page.jinja',
        title=f"{user.first_name}'s Pokemon Party",
        user=user
    )