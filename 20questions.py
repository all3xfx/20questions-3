from random import randint
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
				print "Yes, it is a %s" % word
				exit("you win")
			else:
				wrong.add_answer(word)
				fdbk.reply(wrong) # calculates some cool, dynamic feedback
				wrong.show()
				thing.play()
		elif type == "verb":
			verbs = []
			verbs = (thing.verbs)
			if word in verbs:
				print "Yes, it does %s" % word
				thing.play()
			else:
				print "It may or may not %s" % word
				wrong.add_answer(word)
				fdbk.reply(wrong) # calculates some cool, dynamic feedback
				wrong.show()
				thing.play()
		elif type == "adjective":
			adjectives = []
			adjectives = (thing.adjectives)
			if word in adjectives:
				print "Yes, it is %s" % word
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
		elif "does it" in guess:
			guess = guess.split(" ")
			word = guess[-1]
			thing.user_guess(word, "verb")
		elif guess == "#hint":
			fdbk.hint()
		else:
			print "I don't recognize your question"
			thing.play()
class Feedback(object):
	def __init__(self):
		pass
	def reply(self, wrong):  #pass it the list of wrong answers, it will determine how to reply
		print "nope"
		if len(wrong.answers) in [8, 10, 12]:
			help = raw_input("Want a hint? (Y/N)")
			print "----------------" 
			if help == "Y" or "y":
				self.hint()
			else:
				thing.play()
		elif len(wrong.answers) == 14:
			print "OKAY, I'LL STOP ASKING.  TYPE #HINT IF YOU WANT HELP"
		elif len(wrong.answers) == 3:
			self.suggestions('adj')
		elif len(wrong.answers) ==6:
			self.suggestions('verbs')
		else:
			thing.play()
	def suggestions(self, type):
		random_adjectives = []
		for i in range(0,4):
			random_adjectives.append(mystery_list[randint(0,8)][type][0])
		print "here are a few adjectives you might inquire about: %s" % random_adjectives
		
	def hint(self):
		i = randint(0,3)
		j = randint(0,2)
		if i == 0:
			print "it is %s" % thing.adjectives[j]
			thing.play()
		elif i == 1:
			print "it can %s" % thing.verbs[j]
			thing.play()
		elif i == 2:
			print "it is %d letters long" % len(thing.nouns)
		else:
			print "it starts with a %s" % thing.nouns[0]	
			thing.play()
	
		
		
class Answers(object):
	def __init__(self):
		self.answers = []
	def add_answer(self, x):
		self.answers.append(x)
	def show(self):
		print "Things it is not: %s" % self.answers #for a in self.answers:
		#	print "%s it is not\n" % a
	
mystery_list = [
{"name":"frog","adj":["green", "soft", "slimy"], "verbs":["jump", "grow", "swim"]},
{"name":"cat", "adj":["soft", "furry", "quiet"], "verbs":["jump", "grow", "fall"]},
{"name":"plane", "adj":["loud", "fast", "big"], "verbs":["fly", "run", "land"]},
{"name":"bird", "adj":["soft", "fast", "small"], "verbs":["fly", "land", "grow"]},
{"name":"tree", "adj":["green", "big", "brown"], "verbs":["grow", "sway", "fall"]},
{"name":"building", "adj":["big", "hard", "square"], "verbs":["open", "close", "fall"]},
{"name":"cup", "adj":["round", "square", "small"], "verbs":["holds", "hangs", "contains"]},
{"name":"book", "adj":["flat", "square", "long"], "verbs":["sits", "contains", "burns"]},
{"name":"tire", "adj":["round", "hard", "black"], "verbs":["rolls", "turns", "sits"]},]	

adjectives = ["green", "soft", "slimy","soft", "furry", "quiet", "loud", "fast", "big"]

an_object_index = randint(0, len(mystery_list[-1]))
an_object = Mystery(mystery_list[an_object_index]["name"], mystery_list[an_object_index]["adj"], mystery_list[an_object_index]["verbs"])
right = Answers()
wrong = Answers()
fdbk = Feedback()
thing = an_object
thing.play()
