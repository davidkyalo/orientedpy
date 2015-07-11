
def to_id(rid):
	if not valid_rid(rid):
		return None	
	#print(type(ri))
	return rid.replace('#','').strip() if rid[0:1] == '#' else rid


def to_rid(id):
	if not valid_rid(id):
		return None
	return id if id[0] == '#' else '#' + id

def valid_rid(rid):
	if rid == None or not len(rid) or rid.find(':') == -1:
		return False
	rid = rid.replace('#', '').strip()
	lst = rid.split(':')
	if len(lst) != 2:
		return False

	try:
		int(lst[0])
		int(lst[1])
		return True
	except ValueError:
  		return False 