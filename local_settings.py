'''
Local Settings for a spacer01bot account. 
'''

# Twitter API configuration
MY_CONSUMER_KEY = 'VEKqS1O5PHcVl35JzHevbU2n9'
MY_CONSUMER_SECRET = 'jPUuxuXrSAVIdPeKW6lnlOkHOn9jzmor5yCgKMOgm5JlzAix8x'
MY_ACCESS_TOKEN_KEY = '962822936267776000-0mdXANNuYQmkzuVTHYJuP7GoknaMu7V'
MY_ACCESS_TOKEN_SECRET = 'cj62He01EuNO0r9m42LkVScMM9RgAivJolw1AsuOzG7Is'

# Sources (Twitter, local text file or a web page)
SOURCE_ACCOUNTS = ["spacer01","NASA","Space_Station","NASAVoyager","AFSpace","SETIInstitute","MarsCuriosity","BadAstronomer","NASAKepler","NASA_Hubble","lowflyingrocks","apod","_SpaceWeather_","armysmdc","usnrl","SPAWARHR","US_Stratcom"]  # A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
SOURCE_EXCLUDE = r'^$'  # Source tweets that match this regexp will not be added to the Markov chain. You might want to filter out inappropriate words for example.
STATIC_TEST = False  # Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "testcorpus.txt"  # The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
SCRAPE_URL = False  # Set this to true to scrape a webpage.
SRC_URL = ['http://www.example.com/one', 'https://www.example.com/two']  # A comma-separated list of URLs to scrape
WEB_CONTEXT = ['span', 'h2']  # A comma-separated list of the tag or object to search for in each page above.
WEB_ATTRIBUTES = [{'class': 'example-text'}, {}] # A list of dictionaries containing the attributes for each page.

ODDS = 1  # How often do you want this to run? 1/8 times?
ORDER = 2  # How closely do you want this to hew to sensical? 2 is low and 4 is high.

DEBUG = False  # Set this to False to start Tweeting live
TWEET_ACCOUNT = "spacer01bot"  # The name of the account you're tweeting to.
