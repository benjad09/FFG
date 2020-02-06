


class Random:
	def __init__(self, seed): # Initalizes Random object
		self.seed = seed
	def next(self, limit): # Use the formula to generate the random number
		self.seed = ((16807 * self.seed) % 2147483647)
		nSeed = self.seed % limit
		return nSeed
	def choose(self, characters): # call next and choose a character from the string characters
		i = self.next(len(characters))
		c = characters[i]
		return c

class Words:
	def __init__(self, seed): # Initalizes Words object
		self.first = ''
		self.follow = {} # Dictionary
		self.random = Random(seed)
	def add(self, word): # define add function here.
		self.first = self.first + word[0]
		for i in range(0, len(word) - 1):
			if word[i] in self.follow:
				self.follow[word[i]] = self.follow[word[i]] + word[i+1]
			else:
				self.follow[word[i]] = word[i+1]
		return None
	def make(self, size): # define make function here
		i = 0
		fLetter = self.random.choose(self.first)
		word1 = fLetter
		nLetter = fLetter
		while nLetter in self.follow and i < size:
			nLetter = self.random.choose(self.follow[nLetter])
			word1 = word1 + nLetter
			i = i + 1
		return word1

