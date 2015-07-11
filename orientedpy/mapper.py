
def get_model_map():
    from orientedpy.core import OrientDB
    return OrientDB.get_model_map()

def cast_record(record):
    model = get_model(record._class)
    model_instance = model._new_from_db(record)
    return model_instance

    

def get_model(oclass):
    model_map = get_model_map()
    model = model_map.get(oclass, model_map.get('DEFAULT'))
    return model
  


class RecordMeta(type):
    
    def __call__(cls,*args,**kwargs):
       
        record = super(RecordMeta, cls).__call__(*args, **kwargs)
        model_instance = cast_record(record)
       
        return model_instance
        


