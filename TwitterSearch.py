#add search function

import tweepy

auth = tweepy.OAuthHandler('WzyxRNEEOfuzMJuXJsRiKwkTu', 'U18LqVCGXOvtV9y5KNWIcTg0E93Y5uxvZeer6VTe1gV3yaIpIz')
auth.set_access_token('551032669-W6xZcJDSFIUq8uWPBp5y6ssFtpikVYQ3vTB6mpTu', 'qycG3wuqxQvsFVV17hu9G8awhBkFWEsY8CDLVyOjK4o50')

api = tweepy.API(auth)

#public_tweets = api.home_timeline()

keywords = []


public_tweets  = api.user_timeline(id = 'IrishRail')
#public_tweets = API.user_timeline(['15115986')
for tweet in public_tweets:
	repr(print(tweet.text))
	if(tweet.text[0] != '@'):
		if 'delay' or 'signal' or  'fault' or 'delays' or 'mechanical' in tweet.text:
			keywords.append(tweet.text)
		
print('!!!!!!!!!!!!!!KEYWORDS!!!!!!!!!!!!!!')
print(keywords);
	
	