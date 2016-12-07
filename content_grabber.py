import re
from bs4 import BeautifulSoup

#search terms:
query_vector = []
query_vector.append('fast')
query_vector.append('plane')
query_vector.append('animal')
query_vector.append('computer')
query_vector.append('scary')
query_vector.append('death')
query_vector.append('fire')
query_vector.append('car')
query_vector.append('truck')
#fast plane animal computer scary death fire car truck

#get the stopwords
stopwords = []
with open('stopwords.txt') as f:
	stopwords = f.readlines()
	stopwords = [x.strip() for x in stopwords]

#cleanse the stopwords of non alphanumeric characters
clean_stopwords = []
for word in stopwords:
	word = re.sub(r'[^a-zA-Z0-9]+', '', word)
	clean_stopwords.append(word)

#define pages and urls
page_dict = {}

#google
page_dict["google_0"] = "google_0.htm" #http://www.dailymail.co.uk/news/article-1248177/Toyota-recall-Last-words-father-family-died-Lexus-crash.html
page_dict["google_1"] = "google_1.htm" #http://www.dailymail.co.uk/news/article-2413231/Roman-Pirozek-Jr-Man-decapitates-remote-control-helicopter.html
page_dict["google_2"] = "google_2.htm" #http://www.inthe80s.com/compgame.shtml
page_dict["google_3"] = "google_3.htm" #https://en.wikipedia.org/wiki/List_of_Super_Bowl_commercials
page_dict["google_4"] = "google_4.htm" #http://filmsound.org/cliche/
page_dict["google_5"] = "google_5.htm" #http://www.chicagotribune.com/news/local/breaking/
page_dict["google_6"] = "google_6.htm" #https://cleantechnica.com/2016/07/02/tesla-model-s-autopilot-crash-gets-bit-scary-negligent/
page_dict["google_7"] = "google_7.htm" #https://books.google.com/books?id=LOsPSCAN29gC&pg=PA2&lpg=PA2&dq=fast+plane+animal+computer+scary+death+fire+car+truck&source=bl&ots=k_7fkoVZVB&sig=ihKTq4J5ZP5QOEmaORcIiJdNf1s&hl=en&sa=X&ved=0ahUKEwjCvOTq6uDQAhUBrhQKHRl4DV8Q6AEIRzAH#v=onepage&q&f=false
page_dict["google_8"] = "google_8.htm" #http://www.cheatcc.com/pc/grandtheftauto5cheatscodes.html
page_dict["google_9"] = "google_9.htm" #https://books.google.com/books?id=2vs-RNjRBFUC&pg=PA20&lpg=PA20&dq=fast+plane+animal+computer+scary+death+fire+car+truck&source=bl&ots=oIfNXLXHKm&sig=TCtfc5vl_4IZ0oYCik9IwRLMGjM&hl=en&sa=X&ved=0ahUKEwjCvOTq6uDQAhUBrhQKHRl4DV8Q6AEITzAJ#v=onepage&q&f=false

#bing
page_dict["bing_0"] = "bing_0.htm" #http://www.steeringgames.com/category/driving
page_dict["bing_1"] = "bing_1.htm" #http://poki.com/en/simulation
page_dict["bing_2"] = "bing_2.htm" #https://en.wikipedia.org/wiki/Richard_Scarry
page_dict["bing_3"] = "bing_3.htm" #https://www.yahoo.com/
page_dict["bing_4"] = "bing_4.htm" #http://www.freegames.net/category/parking-games.html
page_dict["bing_5"] = "bing_5.htm" #http://www.wesh.com/local-news
page_dict["bing_6"] = "bing_6.htm" #http://www.ketv.com/local-news
page_dict["bing_7"] = "bing_7.htm" #http://www.cbsnews.com/live/
page_dict["bing_8"] = "bing_8.htm" #http://www.kcci.com/local-news
page_dict["bing_9"] = "bing_9.htm" #http://poki.com/en/truck

#yahoo
page_dict["yahoo_0"] = "yahoo_0.htm" #http://www.steeringgames.com/category/driving
page_dict["yahoo_1"] = "yahoo_1.htm" #https://www.sounddogs.com/
page_dict["yahoo_2"] = "yahoo_2.htm" #http://auto.howstuffworks.com/car-driving-safety/accidents-hazardous-conditions/10-causes-of-car-fires.htm
page_dict["yahoo_3"] = "yahoo_3.htm" #http://www.gamemeteor.com/
page_dict["yahoo_4"] = "yahoo_4.htm" #http://gahe.com/Truck-games
page_dict["yahoo_5"] = "yahoo_5.htm" #https://www.youtube.com/watch?v=QllQ6TtmXII
page_dict["yahoo_6"] = "yahoo_6.htm" #http://www.freegames.net/category/racing-games.html
page_dict["yahoo_7"] = "yahoo_7.htm" #http://poki.com/en/truck
page_dict["yahoo_8"] = "yahoo_8.htm" #http://urbanlegends.about.com/od/fauxphotos/
page_dict["yahoo_9"] = "yahoo_9.htm" #http://www.dailymail.co.uk/news/article-2359288/Impala-escapes-Cheetahs-jumping-car-tourists-Kruger-National-Park.html

#for each file in the pages
doc_terms_dict = {}
for file in page_dict:
	#grab the content
	with open(page_dict[file], 'rb') as f:
		the_page = f.readlines()

	soup = []
	for content in the_page:
		test = BeautifulSoup(content, "html.parser")
		test = test.get_text().encode('utf-8')
		test = test.split()
		for word in test:
			word = word.decode('utf-8')
			soup.append(word)

	#cleanse of non alphanumeric characters
	curr_term_count = {}
	for word in soup:
		#word = word.decode('utf-8')

		#clean the non alphanumeric words
		clean_word = re.sub(r'[^a-zA-Z0-9]+', '', word)

		#if it is not a stopword and its not empty
		if clean_word not in clean_stopwords and len(clean_word) > 0:

			#create term count dict
			if clean_word in curr_term_count:
				curr_term_count[clean_word] += 1
			else:
				curr_term_count[clean_word] = 1

	doc_terms_dict[file] = curr_term_count

#generate the term dictionary
final_dict = {}
for file in doc_terms_dict:
	curr_term_count = doc_terms_dict[file]
	for word in curr_term_count:
		if word in final_dict:
			final_dict[word][file] = curr_term_count[word]
		else:
			final_dict[word] = {}
			final_dict[word][file] = curr_term_count[word]
#generate the document term matrix
f = open('document_term_matrix.txt', 'w')
q = open('query_vector.txt', 'w')
i = 0
for term in final_dict:
	i += 1
	curr_dict = final_dict[term]
	#google documents
	google = 'google_'
	for x in range(0, 10):
		curr_google = google + str(x)
		if curr_google in curr_dict:
			f.write("{0}\t".format(curr_dict[curr_google]))
		else:
			f.write("0\t")

	#bing documents
	bing = 'bing_'
	for x in range(0, 10):
		curr_bing = bing + str(x)
		if curr_bing in curr_dict:
			f.write("{0}\t".format(curr_dict[curr_bing]))
		else:
			f.write("0\t")

	#yahoo documents
	yahoo = 'yahoo_'
	for x in range(0, 10):
		curr_yahoo = yahoo + str(x)
		if curr_yahoo in curr_dict:
			f.write("{0}\t".format(curr_dict[curr_yahoo]))
		else:
			f.write("0\t")

	#write an endline
	f.write("\n")

	#write the query vector
	if term in query_vector:
		q.write("1\n")
	else:
		q.write("0\n")

f.close()
q.close()