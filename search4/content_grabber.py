import re
from bs4 import BeautifulSoup

#search terms:
query_vector = []
query_vector.append('compassionate')
query_vector.append('one')
query_vector.append('lightning')
query_vector.append('excessive')
query_vector.append('serenity')
#compassionate one lightning excessive serenity

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
page_dict["google_0"] = "google_0.htm" #http://www.dalailama.com/messages/compassion
page_dict["google_1"] = "google_1.htm" #http://www.thepublicdiscourse.com/2016/09/17348/
page_dict["google_2"] = "google_2.htm" #http://compassionatecivilization.blogspot.com/2015/05/change-courage-serenity-and-wisdom.html
page_dict["google_3"] = "google_3.htm" #http://www.serenityhospice.com/caregivers-families/why-serenity/
page_dict["google_4"] = "google_4.htm" #https://www.ccel.org/ccel/kronstadt/christlife.iii.html
page_dict["google_5"] = "google_5.htm" #http://inspiritcrystals.com/crystals/
page_dict["google_6"] = "google_6.htm" #http://www.vnews.com/Archives/2015/12/e4-US-Fashion-Colorofth-ls-vn-xxxxxx
page_dict["google_7"] = "google_7.htm" #http://clodagh.com/newsletters_archive/spring-2016/
page_dict["google_8"] = "google_8.htm" #https://en.wikiquote.org/wiki/Hermann_Hesse
page_dict["google_9"] = "google_9.htm" #http://clodagh.com/newsletters_archive/spring-2016/

#bing
page_dict["bing_0"] = "bing_0.htm" #http://www.compassionatexpression.com/healing_sanctuary_&_inn.htm
page_dict["bing_1"] = "bing_1.htm" #http://www.imore.com/iphone-7-review-one-month-later
page_dict["bing_2"] = "bing_2.htm" #https://trinitystjohn.com/2016/08/01/compassionate-lightning/
page_dict["bing_3"] = "bing_3.htm" #https://www.vrbo.com/77937#!
page_dict["bing_4"] = "bing_4.htm" #http://nws.noaa.gov/com/weatherreadynation/news/011112_lightning.html
page_dict["bing_5"] = "bing_5.htm" #http://www.thepublicdiscourse.com/2016/09/17348/
page_dict["bing_6"] = "bing_6.htm" #https://www.psychologytoday.com/blog/changepower/201402/what-is-the-opposite-worry
page_dict["bing_7"] = "bing_7.htm" #http://alwayswellwithin.com/2010/05/11/retraining-the-brain-for-cfs-fms-mcs-ptsd-gws/
page_dict["bing_8"] = "bing_8.htm" #http://www.sleeprestlive.com/
page_dict["bing_9"] = "bing_9.htm" #http://www.sandiegouniontribune.com/

#yahoo
page_dict["yahoo_0"] = "yahoo_0.htm" #http://www.compassionatexpression.com/healing_sanctuary_&_inn.htm
page_dict["yahoo_1"] = "yahoo_1.htm" #http://www.imore.com/iphone-7-review-one-month-later
page_dict["yahoo_2"] = "yahoo_2.htm" #https://trinitystjohn.com/2016/08/01/compassionate-lightning/
page_dict["yahoo_3"] = "yahoo_3.htm" #http://alwayswellwithin.com/2010/05/11/retraining-the-brain-for-cfs-fms-mcs-ptsd-gws/
page_dict["yahoo_4"] = "yahoo_4.htm" #http://www.thepublicdiscourse.com/2016/09/17348/
page_dict["yahoo_5"] = "yahoo_5.htm" #http://www.huffingtonpost.com/genevieve-lill/relationships-6-ways-to-b_b_596478.html
page_dict["yahoo_6"] = "yahoo_6.htm" #https://www.vrbo.com/77937#!
page_dict["yahoo_7"] = "yahoo_7.htm" #http://www.lionsroar.com/living-the-compassionate-life/
page_dict["yahoo_8"] = "yahoo_8.htm" #https://www.psychologytoday.com/blog/changepower/201402/what-is-the-opposite-worry
page_dict["yahoo_9"] = "yahoo_9.htm" #http://www.universeofsymbolism.com/symbolic-meaning-of-fireflies.html

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