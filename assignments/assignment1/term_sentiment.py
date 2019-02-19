import sys
import re

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
    
    counter = {}
    with open(tweets_file) as f:
        tweets = list(f)
    
    od = sorted(sent_scores.keys(),key=len,reverse = True)
    for tweet in tweets:
        score = 0
        for k in od:
            match = re.search(r'\b'+k+r'\b',tweet)
            if match:
                score += sent_scores[k]
                str_text = '\\b' + k+ '\\b'
                tweet = tweet.replace(match[0],'');
        for term in tweet.split():
            if term in new_term_sent.keys():
                new_term_sent[term] = (new_term_sent[term] * counter[term] + score)/(counter[term]+1)
                counter[term] += 1
            else:
                new_term_sent[term] = score
                counter[term] = 1

    
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