from orientedpy.utils import to_id, to_rid, valid_rid
from orientedpy.property import Property, String
from pyorient.types import OrientRecord
import copy



class ModelMeta(type):

	def __init__(cls, name, base, namespace):
		cls._register_properties(namespace)

	def _register_properties(cls, namespace):
		properties = {}
		db_names = {}
		for key in namespace:
			if not isinstance(namespace[key], Property):
				continue
			instance = copy.copy(namespace[key])
			properties[key] = instance
			if instance.name is None:
				instance.name = key

			setattr(cls, key, instance.default)
		cls._properties = properties

class BaseModel(object, metaclass = ModelMeta):
	"""docstring for BaseModel"""

	_oRecord = None

	_oClass = None
	_rid = None
	_id = None	
	_properties = None 

	@property
	def id(self):
	    return self._id

	@classmethod
	def oClass(cls):
		return cls._oClass

	def _set_rid(self, rid):
		if valid_rid(rid):
			self._rid = rid
			self._id = to_id(self._rid)
			return True
		else:
			return False

	
	@classmethod
	def _new_from_db(cls, record):
		instance = cls()
		instance._o_record = record
		instance._init_from_record()		
		return instance

	def _init_from_record(self):
		if not self._oRecord:
			return
		self._set_rid(self._oRecord._rid)
		self._set_db_properties(self._oRecord.oRecordData)

	def _set_db_properties(self, properties = None):
		if not properties:
			properties = {}
		for key, prop_instance in self._properties.items():
			if prop_instance.name in properties:
				db_value =  properties[prop_instance.name]
				value = prop_instance.convert_to_python(key, db_value)
				object.__setattr__(self, key, value)
				del properties[key]

		if properties:
			self._set_undefined_db_properties(properties)



	def _set_undefined_db_properties(self, properties):
		for key, value in properties.items():
			if not hasattr(self, key):
				key = '_' + str(key)
			object.__setattr__(self, key, value)

	def _get_property_value(self, key):
        # Notice that __getattr__ is overloaded in Element.
		value = object.__getattribute__(self, key)
		if isinstance(value, Callable):
			return value()
		return value


	def _get_oRecord(self):
		return OrientRecord(self._get_record_data())


	def _get_record_data(self):
		data = {}
		data['__rid'] = self._rid
		data['__version'] = self._oRecord._version if  self._oRecord else None
		data['__o_class'] = self._oClass
		data['__o_storage'] = self._get_db_properties()
		return data


	def _get_db_properties(self):
		properties = {}
		for key in self._properties:  # Python 3
			prop_instance = self._properties[key]
			value = self._get_property_value(key)
			db_value = prop_instance.convert_to_db(key, value)
			properties[prop_instance.name] = db_value

		return properties



class Model(BaseModel):
	"""General Purpose Model"""
	pass

	
class Vertex(Model):	
	pass

class Edge(Model):
	pass
		
		