class Mystery(object):
	
	def __init__(self, noun, adjective, verb):
		self.nouns = noun
		self.adjectives = adjective
		self.verbs = verb
		self.remaining = 21
	def user_guess(self, word, type):
		if type == "noun":
			nouns = []
			nouns = (thing.nouns)  #should this be self.nouns??
			if word in nouns:
				print "____;-)____;-)____;-)____\nYes, it is a %s" % word
				exit("you win")
			else:
				print "No, it is not a %s" % word
				wrong.add_answer(word)
				fdbk.reply(wrong) # calculates some cool, dynamic feedback
				wrong.show()
				thing.play()	
		elif type == "adjective":
			adjectives = []
			adjectives = (thing.adjectives)
			if word in adjectives:
				print "____;-)____;-)____;-)____\nYes, it is %s" % word
				thing.play()
			else:
				wrong.add_answer(word)  #adds wrong answer to list
				fdbk.reply(wrong) # calculates some cool, dynamic feedback
				wrong.show()
				thing.play()	
		else:
			pass
				
			
	def play(self):
		self.remaining += -1
		if self.remaining <= 0:
			exit("sorry, you ran out of guesses, you lose")
		else:
			pass  #what?
		print "you have %s questions, go!" % self.remaining
		print "------------------------"		
		guess = raw_input(" >")
		guess = guess.split("?")
		guess = guess[0]
		print "------------------------"		
		if "is it a" in guess:
			guess = guess.split(" ")
			word = guess[-1]
			thing.user_guess(word, "noun")
		elif "is it" in guess:
			guess = guess.split(" ")
			word = guess[-1]
			thing.user_guess(word, "adjective")
		elif guess == "#hint":
			fdbk.hint()
		else:
			print "I'm not saying it is, but I'm not saying it isn't"
			thing.play()
class Feedback(object):
	def __init__(self):
		pass
	def reply(self, wrong):  #pass it the list of wrong answers, it will determine how to reply
		print "nope %d" % len(wrong.answers)
		if len(wrong.answers) in [2, 4, 6]:
			help = raw_input("Want a hint? (Y/N)")
			if help == "Y" or "y":
				self.hint()
			else:
				pass
		elif len(wrong.answers) == 8:
			print "OKAY, I'LL STOP ASKING.  TYPE #HINT IF YOU WANT HELP"
		else:
			pass
			
	def hint(self):
		pass
	
		
		
class Answers(object):
	def __init__(self):
		self.answers = []
	def add_answer(self, x):
		self.answers.append(x)
	def show(self):
		print "Things it is not: %s" % self.answers #for a in self.answers:
		#	print "%s it is not\n" % a
	
	
		
frog = Mystery("frog","green","jump")
right = Answers()
wrong = Answers()
fdbk = Feedback()
thing = frog
thing.play()
