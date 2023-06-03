from flask import request, jsonify

from . import bp
from app.models import User, FavePokemon
from app.blueprints.api.helpers import token_required

# Receive All Pokemon Favorites
@bp.get('/pokeall')
@token_required
# def poke_all():
def poke_all(user):
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
@token_required
# def trainer_pokemon(username):
def trainer_pokemon(user, username):
    trainer = User.query.filter_by(username=username).first()
    if trainer:
        return jsonify([{
            'fave_id': poke.fave_id,
            'id': poke.poke_num,
            'pokeName': poke.poke_name,
            'pokeImg': poke.poke_art,
            'date_added': poke.date_added,
            'pokemon_trainer': poke.user_id
        } for poke in trainer.fave_pokemon]), 200
    return jsonify([{'message':'Invalid username.'}]), 404

# Receive Favorite Pokemon by Pokemon Number
@bp.get('/pokemon/<poke_num>')
@token_required
# def get_Pokemon(poke_num):
def get_Pokemon(user, poke_num):
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

# Add Pokemon to Favorites
@bp.route('/add/<poke_num>', methods=['POST'])
@token_required
def add_Pokemon(user, poke_num):
    content = request.json
    username = content['username']
    poke_num = content['id']
    poke_name = content['pokeName']
    poke_art = content['pokeImg']

    userByName = User.query.filter_by(username=username).first()
    if user.user_id != userByName.user_id:
        return jsonify([{
            "message": "Token and User not in same account",
            "status": "error",
            "success": False
        }])
    pokenum_check = poke_num in [num.poke_num for num in user.fave_pokemon]
    if not pokenum_check:
    # If Pokemon is not in the FavePokemon table:
        fave = FavePokemon(poke_num=poke_num)
        fave.poke_name = poke_name
        fave.poke_art = poke_art
        fave.user_id = user.user_id
        fave.commit()
        return jsonify([{
            "message": f"{poke_name} successfully added to favorites!",
            "status": "added",
            "success": True
        }])
    elif pokenum_check:
        return jsonify([{
            "message": f"{poke_name} is already in favorites!",
            "status": "favorites",
            "success": False
        }])
    else:
        return jsonify([{
            "message": f"{poke_name} is not added to favorites!",
            "status": "error",
            "success": False
        }])