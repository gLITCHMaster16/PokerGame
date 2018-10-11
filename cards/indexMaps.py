import collections, types
class IndexMap:
	"""Must Define _define_text_map and _define_save_map"""
	def getText(self, indices):
		if (isinstance(indices, str) or not isinstance(indices, collections.Iterable)):
			v = [ indices ]
		else:
			v = indices

		val = []
		for i in v:
			val.append(self._text_mapping[i])
		return (val)

	def getSave(self, indices):
		if (isinstance(indices, str) or not isinstance(indices, collections.Iterable)):
			v = [ indices ]
		else:
			v = indices

		val = []
		for i in v:
			val.append(self._save_mapping[i])
		return(val)

	def getFromSave(self, saveValue):
		if (isinstance(saveValue, str) or not isinstance(saveValue, collections.Iterable)):
			v = [ saveValue ]
		else:
			v = saveValue

		val = []
		#print(v)
		for i in v:
			#print (i)
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
		self._rank_mapping = []
		self._card_count = 52

		self._define_save_map()
		self._define_text_map()
		self._define_rank_map()

	def _define_text_map(self):
		pass

	def _define_save_map(self):
		pass

	def _define_rank_map(self):
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

	def _define_rank_map(self):
		for i in range(self._card_count):
			self._rank_mapping.append([ i % 4, i % 13 ])
