from score import *
from filter import Filter, punctuations
import threading

# Set initial value to 0; each thread adds its value to get final sentiment
global sentiment
sentiment = 0.0

# Create class for thread; each thread performs independent analysis
class sentimentThread(threading.Thread):
	def __init__(self, text):
		threading.Thread.__init__(self)
		self.text = text

	def __str__(self):
		return ''.join(self.text)

	def run(self):
		global sentiment
		for line in self.text:
			# Get scores for each word
			for word in line:
				# Get sentiment of each word
				sentiment += getScore(word).score


def Sentiment(text):
	global sentiment
	threads = []
	# Split dataset into 5 parts
	text = text.split(" ")
	temp = int(len(text)/5)

	# Initialize 5 threads to handle each part
	for i in range(5):
		for word in text[(0+i*temp):(temp+i*temp)]:
			snippet = ''.join([char for char in word if char not in punctuations])
			threads.append(sentimentThread(snippet))

	# Append remaining words to the last thread
	for word in text[(5*temp):]:
		snippet = ''.join([char for char in word if char not in punctuations])
		threads.append(sentimentThread(snippet))

	# Call run() method of thread
	for thread in threads:
		thread.start()


	# Combine resuts of the threads
	for thread in threads:
		thread.join()

	# Return the total value; combination of all threads
	return sentiment