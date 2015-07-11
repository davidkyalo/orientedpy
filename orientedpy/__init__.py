import sys
import orientedpy.pyorient_types
sys.modules["pyorient.types"] = pyorient_types

from .core import OrientDB  #Client, DB, to_id, to_rid, valid_rid
from .models import Model, Vertex

