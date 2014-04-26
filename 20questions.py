class Mystery(object):
	
	def __init__(self, noun, adjective, verb):
		self.nouns = noun
		self.adjective = adjective
		self.verb = verb
	def act(self, what):
		print "bring me a %s %s and %s" % (self.adjective, what, self.verb)

tree = Mystery("apple", ["green", "shiny"], "eat")
descriptor = "shiny apple"
tree.act(descriptor) 
print tree.nouns
print "you have 20 questions, go!"
guess = raw_input(" >")
if tree.nouns in guess:
	print "success"
else:
	print "fail"
