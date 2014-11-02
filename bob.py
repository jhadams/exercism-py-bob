class bob:
	def hey(sentence):
		if (sentence == ""):
			return "Fine, be that way."
		elif (sentence.endswith("?")):
			return "Sure."
		elif (sentence == sentence.upper()):
			return "Whoa, chill out!"
		return "Whatever."
