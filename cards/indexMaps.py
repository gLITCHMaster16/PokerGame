class IndexMap:
	"""Must Define _define_text_map and _define_save_map"""
	def getText(self, indices):
		val = []
		for i in indices.split():
			val.append(self._text_mapping[i])
		return (val)

	def getSave(self, indices):
		val = []
		for i in indices.split():
			val.append(self._save_mapping[i])
		return(val)

	def getFromSave(self, indices):
		val = []
		for i in indices.split():
			index = 0
			for j in self._save_mapping:
				if i == j:
					val.append(index)
					continue
				index += 1
		return val

	def __init__(self):
		self._text_mapping = []
		self._save_mapping = []
		self._define_save_map()
		self._define_text_map()

	def _define_text_map(self):
		pass

	def _define_save_map(self):
		pass

class AlphaMap( IndexMap ):
	def _define_text_map(self):
		for i in [ "Ace", "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2 ]:
			for j in [ "Spades", "Hearts", "Diamonds", "Clubs" ]:
				self._text_mapping.append(str(i) + " of " + j)

	def _define_save_map(self):
		for i in [ 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 ]:
			for j in [ "S", "H", "D", "C" ]:
				self._save_mapping.append(j + str(i))
