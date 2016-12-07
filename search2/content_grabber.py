import re
from bs4 import BeautifulSoup

#search terms:
query_vector = []

query_vector.append('fly')
query_vector.append('car')
query_vector.append('bird')
query_vector.append('speed')
query_vector.append('motorcycle')

#fly car bird speed motorcycle


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
page_dict["google_0"] = "google_0.htm" #http://www.samsonmotorworks.com/switchblade
page_dict["google_1"] = "google_1.htm" #https://en.wikipedia.org/wiki/Land_speed_record
page_dict["google_2"] = "google_2.htm" #https://en.wikipedia.org/wiki/British_land_speed_record
page_dict["google_3"] = "google_3.htm" #http://pal-v.com/
page_dict["google_4"] = "google_4.htm" #http://www.dailymail.co.uk/sciencetech/article-3170252/Is-bird-plane-No-s-TF-X-Amazing-new-flying-car-concept-fit-normal-garage-revealed.html
page_dict["google_5"] = "google_5.htm" #http://www.dailymail.co.uk/sciencetech/article-3753369/Could-real-flying-car-600-000-flying-motorbike-hit-112mph-land-air.html
page_dict["google_6"] = "google_6.htm" #https://books.google.com/books?id=Ji_ty9AEz58C&pg=PA334&lpg=PA334&dq=fly+car+bird+speed+motorcycle&source=bl&ots=fR1slkLOJW&sig=H9kjzrI5xodA4qCS57SocDyKvWM&hl=en&sa=X&ved=0ahUKEwjgruvb_uDQAhUF1xQKHcFSAMQQ6AEIQTAH#v=onepage&q=fly%20car%20bird%20speed%20motorcycle&f=false
page_dict["google_7"] = "google_7.htm" #https://books.google.com/books?id=sNgDAAAAMBAJ&pg=RA1-PA70&lpg=RA1-PA70&dq=fly+car+bird+speed+motorcycle&source=bl&ots=0_i5U8GKQO&sig=KlJrwkflPGMh9TYVEUyLaeJqgv0&hl=en&sa=X&ved=0ahUKEwjgruvb_uDQAhUF1xQKHcFSAMQQ6AEIQzAI#v=onepage&q=fly%20car%20bird%20speed%20motorcycle&f=false
page_dict["google_8"] = "google_8.htm" #http://www.dailymail.co.uk/sciencetech/article-2690468/That-motorbike-FLYING-Gyrocopter-hit-112mph-land-air-goes-sale.html
page_dict["google_9"] = "google_9.htm" #http://www.revzilla.com/common-tread/polaris-slingshot

#bing
page_dict["bing_0"] = "bing_0.htm" #https://en.wikipedia.org/wiki/British_land_speed_record
page_dict["bing_1"] = "bing_1.htm" #http://www.fastestbird.com/
page_dict["bing_2"] = "bing_2.htm" #https://en.wikipedia.org/wiki/List_of_birds_by_flight_speed
page_dict["bing_3"] = "bing_3.htm" #hhttp://www.cnn.com/2015/03/10/travel/sr71-blackbird-worlds-fastest-plane/index.html
page_dict["bing_4"] = "bing_4.htm" #http://pal-v.com/
page_dict["bing_5"] = "bing_5.htm" #http://www.fia.com/sports/fia-world-land-speed-records
page_dict["bing_6"] = "bing_6.htm" #http://speedofanimals.com/animals/roadrunner
page_dict["bing_7"] = "bing_7.htm" #http://www.airhogs.com/
page_dict["bing_8"] = "bing_8.htm" #http://www.popsci.com/technology/article/2010-01/forget-flying-car-flying-motorcycle-coming
page_dict["bing_9"] = "bing_9.htm" #http://wonderopolis.org/wonder/which-bird-flies-the-fastest/

#yahoo
page_dict["yahoo_0"] = "yahoo_0.htm" #http://www.samsonmotorworks.com/switchblade
page_dict["yahoo_1"] = "yahoo_1.htm" #https://en.wikipedia.org/wiki/Land_speed_record
page_dict["yahoo_2"] = "yahoo_2.htm" #https://en.wikipedia.org/wiki/British_land_speed_record
page_dict["yahoo_3"] = "yahoo_3.htm" #http://pal-v.com/
page_dict["yahoo_4"] = "yahoo_4.htm" #https://www.youtube.com/watch?v=QOftJT17AO0
page_dict["yahoo_5"] = "yahoo_5.htm" #http://www.dailymail.co.uk/sciencetech/article-3170252/Is-bird-plane-No-s-TF-X-Amazing-new-flying-car-concept-fit-normal-garage-revealed.html
page_dict["yahoo_6"] = "yahoo_6.htm" #http://www.dailymail.co.uk/sciencetech/article-3753369/Could-real-flying-car-600-000-flying-motorbike-hit-112mph-land-air.html
page_dict["yahoo_7"] = "yahoo_7.htm" #http://www.dailymail.co.uk/sciencetech/article-2690468/That-motorbike-FLYING-Gyrocopter-hit-112mph-land-air-goes-sale.html
page_dict["yahoo_8"] = "yahoo_8.htm" #http://www.revzilla.com/common-tread/polaris-slingshot
page_dict["yahoo_9"] = "yahoo_9.htm" #http://newatlas.com/bird-of-prey-bike/39930/
									 #https://www.pinterest.com/pin/463518986619187113/ was the next link if we want to skip yt

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