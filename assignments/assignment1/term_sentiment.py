import sys

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    scores = {}
    
    afinnfile = open(sentiment_file, 'r')
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t") # The file is tab-delimited and "\t" means tab character
        scores[term] = int(score) # Conver the score to an integer. It was parsed as a string.
    afinnfile.close()
    
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0
    for w in tweet.split():
        if w in sent_scores.keys():
            score += sent_scores[w]
    
    return score

def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    new_term_sent = {}
    
    words = {}
    with open(tweets_file) as f:
        tweets = list(f)
#    sent_scores.sort(key=len, reverse = True)
    sortedList = sorted(sent_scores.keys(),key=len,reverse = True)
    print (sortedList)
    for line in tweets:
        if len(line) is 1: #empty line
            continue
#        wordArr = line.split()
#        for k in sortedList:
#            if k in wordArr:
#                score = sent_scores[k]
##                line.replace(k,"") # remove that term from line
#                for i in [x for x in range(-3,3) if x != 0] : # i should not be 0
#                    if wordArr.index(k) + i >= 0 and wordArr.index(k) + i < len(wordArr) :
#                        index = wordArr.index(k) + i
#                        word = wordArr[index]
#                        if word not in sortedList:
#                            if word not in words:
#                                words[word] = (3-abs(i)) * score
#                            else:
#                                words[word] = (3-abs(i)) * score + words[word] # update from the old score
#            print(words)
        
        
        
#    for k,v in words.items():
#        print(k + ":" +str(v))
                        
                    
                

                
                

#            if k in line:
#                print(k)

#        words = line.split()
#        for w in words:
#            if w in sent_scores.keys():  
#                new_term_sent[w] = sent_scores[w]
#            else:
#                score = 0
#                for i in range (-3,3):
#                    if words.index(w) + i >= 0 and words.index(w) + i < len(words):
#                        index = words.index(w) + i
#                        if words[index] in sent_scores.keys():
#                            score += sent_scores[index]
                    
                    
#            new_term_sent[w] = score
            
    for k,v in new_term_sent.items():
        print(k + " " + str(v))
    
    return new_term_sent


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    for term in new_term_sent:        
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()