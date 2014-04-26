class Mystery(object):
	
	def __init__(self, noun, adjective, verb):
		self.nouns = noun
		self.adjectives = adjective
		self.verbs = verb
	def user_guess(self, word, type):
		if type == "noun":
			nouns = []
			nouns = (thing.nouns)
			if word in nouns:
				print "Yes, it is a %s" % word
				exit("you win")
			else:
				print "No, it is not a %s" % word
				#remaining += -1
				thing.play(remaining)				
				
		elif type == "adjective":
			adjectives = []
			adjectives = (thing.adjectives)
			if word in adjectives:
				print "yes, it is %s" % word
				exit("good job!)"
			else:
				print "No, it is not %s" % word
				thing.play(remaining)
			
	
	def play(self, remaining):
		print "you have %s questions, go!" % remaining
		guess = raw_input(" >")
		if "is it a" in guess:
			guess = guess.split(" ")
			word = guess[-1]
			thing.user_guess(word, "noun")
		elif "is it" in guess:
			guess = guess.split(" ")
			word = guess[-1]
			thing.user_guess(word, "adjective")
		else:
			print "fail"
			exit(1)

frog = Mystery("frog","green","jump")
thing = frog
remaining = 20

thing.play(20)
