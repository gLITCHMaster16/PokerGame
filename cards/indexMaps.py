import collections, types, math

class IndexTree:
	def __init__(self, indexMapping):
		self._indexMapping = indexMapping
		self._a = None
		self._b = None
		self._c = None

	def put(self, index: int):
		if not self._b:
			self._b = [ index ]
			self._a = IndexTree(self._indexMapping)
			self._c = IndexTree(self._indexMapping)
		else:
			if self._indexMapping.getRank(index)[0][0] == self._indexMapping.getRank(self._b)[0][0]:
				if self._indexMapping.getRank(index)[0][1] >= self._indexMapping.getRank(self._b)[0][1]:
					self._a.put(index)
				else:
					self._c.put(index)
			elif self._indexMapping.getRank(index)[0][0] >= self._indexMapping.getRank(self._b)[0][0]:
				self._a.put(index)
			else:
				self._c.put(index)

	def get(self) -> []:
		if not self._b:
			return []
		else:
			if self._a and self._c:
				return self._a.get() + self._b + self._c.get()
			elif self._a:
				return self._a.get() + self._b
			elif self._c:
				return				   self._b + self._c.get()
			else:
				return 				   self._b



class IndexMap:
	"""
	Must implement _define_text_map(), _define_save_map(), and _define_rank_map()
	See IndexMaps.md
	"""

	def __iterProof(self, val):
		"""Make sure that value is safe to be iterated over, and if not put it into an array"""
		if (isinstance(val, str) or not isinstance(val, collections.Iterable)):
			return [ val ]
		return val

	def getText(self, indices:"Set of card indexes") -> [str]:
		v = self.__iterProof(indices)
		val = []
		for i in v:
			val.append(self._text_mapping[i])
		return (val)

	def getSave(self, indices:"Set of card indexes") -> [str]:
		"""Get a set save values based on this IndexMap"""
		v = self.__iterProof(indices)
		val = []
		for i in v:
			val.append(self._save_mapping[i])
		return(val)

	def getFromSave(self, saveValue) -> [int]:
		"""Get indices from a set of save values based on this IndexMap"""
		v = self.__iterProof(saveValue)
		val = []
		for i in v:
			index = 0
			for j in self._save_mapping:
				if i == j:
					val.append(index)
					continue
				index += 1
		return val

	def getRank(self, indices:"Set of card indexes") -> []:
		"""Get the Rank of a set of cards based on this IndexMap implememntation."""
		v = self.__iterProof(indices)
		val = []
		for i in v:
			val.append(self._rank_mapping[i])
		return val

	def getFromRank(self, ranks:"Set of ranks") -> []:
		v = self.__iterProof(ranks)
		val = []
		for i in v:
			index = 0
			for j in self._rank_mapping:
				if i == j:
					val.append(index)
					continue
				index += 1
		return val


	def sortByRank(self, indices):
		indices = self.__iterProof(indices)
		tree = IndexTree(self)
		for i in indices:
			tree.put(i)
		return tree.get()


	def __init__(self):
		self._text_mapping = []
		self._save_mapping = []
		self._rank_mapping = []

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

	def __init__(self):
		self.card_count = 52 # Set card count, not currently used
		super(AlphaMap, self).__init__()

	def _define_text_map(self): # Define display name for each card index
		for i in [ "Spades", "Hearts", "Diamonds", "Clubs" ]:
			for j in [ "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2, "Ace" ]:
				self._text_mapping.append(str(j) + " of " + i)

	def _define_save_map(self): # Define save name for each card index
		for i in [ "S", "H", "D", "C" ]:
			for j in range(13):
				self._save_mapping.append(i + str(12 - j))

	def _define_rank_map(self): # Define rank for each card index
		for i in range(4):
			for j in [ 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 12 ]:
				self._rank_mapping.append([ j, 3 - i ])
