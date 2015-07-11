import pyorient
from orientedpy.config import MODEL_MAP
#from orientedpy import Model as DefaultModel
class OrientDB(pyorient.OrientDB):
	"""
	Sub Class of OrientDB
	"""
	_model_map_ = MODEL_MAP

	def __new__(cls, host = 'localhost', port = 2424, model_map = None):
		cls.set_model_map(model_map)
		return object.__new__(cls)

	def __init__(self, host='localhost', port=2424, model_map = None):
		super(OrientDB, self).__init__(host, port)

	@classmethod
	def get_model_map(cls):
		return cls._model_map_

	@classmethod
	def set_model_map(cls, model_map):
		if isinstance(model_map, dict):
			for key, value in cls._model_map_.items():
				if not key in model_map:
					model_map[key] = value
			cls._model_map_ = model_map


"""
class DB(object):
	
	model_map = {}
	def __init__(self, client, db_name, model_map, default_model = None):
		self.client = client
		self.db_name = db_name
		self.__is_open = False
		self.username = None
		self.password = None
		self._classes_map = {}
		self.model_map = model_map
		self.default_model = default_model
	
	@classmethod
	def get_mapper(self):
		from orientedpy import Model

		return RecordMapper(self.model_map, Model)

	def open(self, username, password):
		self.username = username
		self.password = password
		try:
			self.client.db_open(self.db_name, username, password)
		except:
			self.__is_open = False
			return False
		else:
			self.__is_open = True
			return True

	def set_classes_map(self, classes_map):
		self._classes_map = classes_map

	@property
	def classes_map(self):
	    return self._classes_map
	

	@property
	def _is_open(self):
	    return self.__is_open
	

	def close(self):
		if self._is_open:
			self.client.db_close()
		return 


	def load_record(self, rid):
		if not valid_rid(rid):
			return False
		#return self.client.query("select from Parent where @rid ="+rid)
		return self.client.record_load(rid)

	def execute(self, *args):
		return self.client.command(*args)

	def query(self, *args):
		return self.client.query(*args)
"""
