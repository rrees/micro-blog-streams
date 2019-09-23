
def read(query, mapper):

	def delayed_read():
		for item in query:
			yield mapper(item)

	return delayed_read()