from flask import Blueprint
from .models import Usuario, TipoUsuario


usuario_app = Blueprint("usuario", __name__, url_prefix="/usuario")