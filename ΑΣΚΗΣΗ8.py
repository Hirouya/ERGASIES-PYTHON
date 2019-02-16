import tweepy

#συνάρτηση που παίρνει τα 10 tweets ενος χρήστη
def getTweets(handle):
    tweets=api.user_timeline(screen_name=handle,count=10,tweet_mode='extended')
    tweetlist=[]
    for tweet in tweets:
        tweetlist.append(tweet.full_text)
    return tweetlist

#συνάρτηση που βρίσκει τον αριθμό των follower ενος χρήστη
def getFollowers(handle):
    numfol =api.get_user(screen_name=handle)
    return numfol.followers_count
#συ΄ναρτηση που υπολογίζει πόσες λέξεις εχουν συνολικά τα tweets ενος χρήστη
def findnumwords(orilist):
    lsum=0
    for i in orilist:
        words = (i.split())
        x = len(words)
        lsum = lsum + x
    return lsum
#συνάρτηση που υπολογίζει το γινόμενο του αριθμού των follower με την ποσότητα
#των λέξεων
def calmult(numfol,wordsum):
    ans = numfol * wordsum
    return ans

#συνδεση με twitter
consumer_key = "Wy0JyQqfcM7iwfa7qY44oAePO"
consumer_secret = "KlRHOsByO9pPlUwjcaJpwHQ64vaXrh4nEfEfbXbhgpXsW2MZjj"
access_key = "1096818404214956033-mqFCxpdnuwAGOfpKdyaQcMb0yEm0GR"
access_secret = "NtHdMrzuwhgDtZm7dsOjN96MRaRJq4CCVij2WAEDwv7mb"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
#εισαγωγή από τον χρήστη δύων λογαριασμών
user1= input("give first user's twitter handle ")
user2= input("give second user's twitter handle ")
#κάλεσμα συναρτήσεων
u1t = getTweets(user1)
u2t = getTweets(user2)
u1f = getFollowers(user1)
u2f = getFollowers(user2)
u1sum = findnumwords(u1t)
u2sum = findnumwords(u2t)
ans1 = calmult(u1f,u1sum)
ans2 = calmult(u2f,u2sum)
#έλεγχος τελικού ερωτήματος
if ans1 > ans2:
    print("ο χρήστης " + user1 + " εχει μεγαλύτερο γινόμενο")
elif ans1 < ans2:
    print("ο χρήστης " + user2 + " εχει μεγαλύτερο γινόμενο")
else:
    print("Οι δύο χρήστες έχουν το ίδιο γινόμενο")
