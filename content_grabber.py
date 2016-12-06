import re
import matlab.engine
from bs4 import BeautifulSoup
from urllib.request import urlopen

#search terms:
query_vector = []
query_vector.append('Barack')
query_vector.append('Obama')

print("SEARCH QUERY TERMS:", end="")
for term in query_vector:
	print(" {0}".format(term), end="")
print('', end="\n")

print('\n#############################')
print('####BEGINNING COMPUTATION####')

#matlab engine
eng = matlab.engine.start_matlab()
print("Engine started")

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
print("Stopwords gathered")

#define pages and urls
page_dict = {}

#google
page_dict["google_0"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["google_1"] = "https://www.barackobama.com/"
page_dict["google_2"] = "https://www.whitehouse.gov/administration/president-obama"
page_dict["google_3"] = "https://plus.google.com/+BarackObama"
page_dict["google_4"] = "https://www.wired.com/2016/10/president-obama-mit-joi-ito-interview/"

#bing
page_dict["bing_0"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["bing_1"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["bing_2"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["bing_3"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["bing_4"] = "https://en.wikipedia.org/wiki/Barack_Obama"

#yahoo
page_dict["yahoo_0"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["yahoo_1"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["yahoo_2"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["yahoo_3"] = "https://en.wikipedia.org/wiki/Barack_Obama"
page_dict["yahoo_4"] = "https://en.wikipedia.org/wiki/Barack_Obama"

#for each file in the pages
doc_terms_dict = {}
for file in page_dict:
	#grab the content
	response = urlopen(page_dict[file])
	the_page = response.read()
	soup = BeautifulSoup(the_page, "html.parser")
	soup = soup.get_text().encode('utf-8')
	soup = soup.split()

	#cleanse of non alphanumeric characters
	curr_term_count = {}
	for word in soup:
		word = word.decode('utf-8')

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
print("Document terms gathered")

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
print("Term dictionary created")

#generate the document term matrix
f = open('document_term_matrix.txt', 'w')
q = open('query_vector.txt', 'w')
i = 0
for term in final_dict:
	i += 1
	curr_dict = final_dict[term]
	#google documents
	google = 'google_'
	for x in range(0, 5):
		curr_google = google + str(x)
		if curr_google in curr_dict:
			f.write("{0}\t".format(curr_dict[curr_google]))
		else:
			f.write("0\t")

	#bing documents
	bing = 'bing_'
	for x in range(0, 5):
		curr_bing = bing + str(x)
		if curr_bing in curr_dict:
			f.write("{0}\t".format(curr_dict[curr_bing]))
		else:
			f.write("0\t")

	#yahoo documents
	yahoo = 'yahoo_'
	for x in range(0, 5):
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

#call the matlab script to get the ranks
ranks = eng.latent_semantic()
print("Gathering results from Matlab")

print('######COMPUTATIONS DONE######')
print('#############################\n')

#google ranks
for x in range(0, 5):
	test = ranks[x]
	print("Google {0} rank: {1}".format(x, test))

#bing ranks
for x in range(0, 5):
	test = ranks[x + 5]
	print("Bing {0} rank: {1}".format(x, test))

#yahoo ranks
for x in range(0, 5):
	test = ranks[x + 10]
	print("Yahoo {0} rank: {1}".format(x, test))