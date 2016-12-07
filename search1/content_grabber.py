import re
from bs4 import BeautifulSoup

#search terms:
query_vector = []
query_vector.append('free')
query_vector.append('movies')
query_vector.append('cage')
query_vector.append('pizza')
query_vector.append('calories')
#free movies cage pizza calories

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
page_dict["google_0"] = "google_0.htm" #http://www.everydayhealth.com/diet-and-nutrition-pictures/best-and-worst-movie-food-picks.aspx
page_dict["google_1"] = "google_1.htm" #http://www.health.com/health/gallery/0,,20658048,00.html
page_dict["google_2"] = "google_2.htm" #https://www.washingtonpost.com/news/to-your-health/wp/2015/07/09/want-to-know-how-many-calories-are-in-that-burger-sit-tight-the-fda-has-delayed-menu-calorie-count-rules/?utm_term=.5b4cbd75843a
page_dict["google_3"] = "google_3.htm" #https://www.washingtonpost.com/news/wonk/wp/2015/01/20/your-kids-are-getting-way-too-many-calories-from-pizza/?utm_term=.3873e53e46fb
page_dict["google_4"] = "google_4.htm" #https://www.tacobell.com/food/nutrition
page_dict["google_5"] = "google_5.htm" #http://twoboots.com/our-pizzas/
page_dict["google_6"] = "google_6.htm" #http://civileats.com/2015/05/01/all-the-news-thats-fit-to-eat-big-pizza-teams-up-with-grocery-stores-and-movie-theaters-to-fight-calorie-labeling/
page_dict["google_7"] = "google_7.htm" #http://www.cancerdietitian.com/2014/05/healthy-pizza-my-thoughts-from-a-papa-murphys-kitchen-tour.html
page_dict["google_8"] = "google_8.htm" #http://www.dailymail.co.uk/femail/article-3255405/The-napkin-diet-Infographic-reveals-dabbing-grease-pizza-slice-takes-away-calories-removes-nearly-FIVE-GRAMS-fat.html
page_dict["google_9"] = "google_9.htm" #http://www.dailymail.co.uk/femail/article-2908812/Is-2-000-calories-really-looks-like-favorite-food-chains.html

#bing
page_dict["bing_0"] = "bing_0.htm" #http://calorielab.com/restaurants/pizza-pizza-ca/2090
page_dict["bing_1"] = "bing_1.htm" #http://www.pizzapizza.ca/nutrition/
page_dict["bing_2"] = "bing_2.htm" #http://cinemacafe.com/
page_dict["bing_3"] = "bing_3.htm" #http://www.calorieking.com/calories-in-pizza.html?page=2
page_dict["bing_4"] = "bing_4.htm" #https://www.pizzaexpress.com/our-food/restaurant-menu
page_dict["bing_5"] = "bing_5.htm" #http://www.sparkpeople.com/calories-in.asp?food=gluten+free+pizza
page_dict["bing_6"] = "bing_6.htm" #https://www.washingtonpost.com/news/wonk/wp/2015/01/20/your-kids-are-getting-way-too-many-calories-from-pizza/?utm_term=.9e6e87d48c29
page_dict["bing_7"] = "bing_7.htm" #https://www.washingtonpost.com/politics/fda-proposal-would-require-chain-restaurants-to-display-calorie-information/2011/04/01/AFOxCkHC_story.html?utm_term=.b29e6eda11ec
page_dict["bing_8"] = "bing_8.htm" #https://www.caloriecount.com/calories-pizza-calzones-ic2101
page_dict["bing_9"] = "bing_9.htm" #http://www.calorieking.com/calories-in-pizza.html

#yahoo
page_dict["yahoo_0"] = "yahoo_0.htm" #http://calorielab.com/restaurants/pizza-pizza-ca/2090
page_dict["yahoo_1"] = "yahoo_1.htm" #http://www.pizzapizza.ca/nutrition/
page_dict["yahoo_2"] = "yahoo_2.htm" #https://www.washingtonpost.com/news/wonk/wp/2015/01/20/your-kids-are-getting-way-too-many-calories-from-pizza/?utm_term=.749e43acd48a
page_dict["yahoo_3"] = "yahoo_3.htm" #http://www.sparkpeople.com/calories-in.asp?food=gluten+free+pizza
page_dict["yahoo_4"] = "yahoo_4.htm" #http://www.calorieking.com/calories-in-pizza.html
page_dict["yahoo_5"] = "yahoo_5.htm" #https://www.caloriecount.com/calories-pizza-calzones-ic2101
page_dict["yahoo_6"] = "yahoo_6.htm" #http://www.sparkpeople.com/calories-in.asp?food=nachos+with+cheese
page_dict["yahoo_7"] = "yahoo_7.htm" #https://www.washingtonpost.com/politics/fda-proposal-would-require-chain-restaurants-to-display-calorie-information/2011/04/01/AFOxCkHC_story.html?utm_term=.9e1c1fb91095
page_dict["yahoo_8"] = "yahoo_8.htm" #https://www.caloriecount.com/calories-pizza-i21049
page_dict["yahoo_9"] = "yahoo_9.htm" #

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