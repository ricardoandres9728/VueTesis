from flask import Blueprint, session, make_response, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from usuario.models import Usuario

login_app = Blueprint("login", __name__)

@login_app.route('/login', methods=["POST"])
def login():
    import pdb; pdb.set_trace()
    form = request.json
    print(form)
    if Usuario.query.filter_by(correo=form["correo"]).first():
        usuario = Usuario.query.filter_by(correo=form["correo"]).first()
        if check_password_hash(usuario.password, form["password"]):
            if usuario.id_tipo_usuario == 2:
                session["id"] = usuario.id
                session["apirante"] = True
                return make_response(jsonify({
                    "tipo_usuario": usuario.id_tipo_usuario,
                }), 201)
            if usuario.id_tipo_usuario == 3:
                session["id"] = usuario.id
                session["colegio"] = True
                return make_response(jsonify({
                    "tipo_usuario": usuario.id_tipo_usuario,
                }), 201)
            if usuario.id_tipo_usuario == 1:
                session["id"] = usuario.id
                session["administrador"] = True
                return make_response(jsonify({
                    "tipo_usuario": usuario.id_tipo_usuario,
                }), 201)
        else:
            return make_response(jsonify({
                "error": "Correo y/o contraseña incorrectos",
            }), 400)
    else:
        return make_response(jsonify({
            "error": "Correo y/o contraseña incorrectos",
        }), 400)
