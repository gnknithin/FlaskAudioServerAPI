try:
    from flask import Blueprint
except ModuleNotFoundError:
    print("\nFlask must be Installed\n")
    sys.exit(0)

api = Blueprint('api',__name__)

from . import views, errors