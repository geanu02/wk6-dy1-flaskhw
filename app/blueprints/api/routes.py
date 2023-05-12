from flask import jsonify

from . import bp
from app.models import User, FavePokemon

# Receive All Pokemon Favorites
@bp.get('/pokeall')
def poke_all():
    pokemon = FavePokemon.query.all()
    if pokemon:
        return jsonify([{
            'fave_id': poke.fave_id,
            'poke_num': poke.poke_num,
            'poke_name': poke.poke_name,
            'poke_art': poke.poke_art,
            'date_added': poke.date_added,
            'pokemon_trainer': poke.user_id
        } for poke in pokemon]), 200
    return jsonify([{'message':'No posts available to view.'}]), 404

# Receive Favorite Pokemon from Single Pokemon Trainer
@bp.get('/<username>/pokemon')
def trainer_pokemon(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify([{
            'fave_id': poke.fave_id,
            'poke_num': poke.poke_num,
            'poke_name': poke.poke_name,
            'poke_art': poke.poke_art,
            'date_added': poke.date_added,
            'pokemon_trainer': poke.user_id
        } for poke in user.fave_pokemon]), 200
    return jsonify([{'message':'Invalid username.'}]), 404

# Receive Favorite Pokemon by Pokemon Number
@bp.get('/pokemon/<poke_num>')
def get_Pokemon(poke_num):
    try:
        poke = FavePokemon.query.filter_by(poke_num=poke_num).first()
        return jsonify([{
            'poke_num': poke.poke_num,
            'poke_name': poke.poke_name,
            'poke_art': poke.poke_art,
            'date_added': poke.date_added,
            'pokemon_trainer': poke.user_id
        }])
    except:
        jsonify([{'message':'Pokemon not registered.'}]), 404

