
# https://help.smarkets.com/hc/en-gb/articles/214058369-How-to-calculate-implied-probability-in-betting
def american_to_prob(odds):

    if odds < 0:
        return odds / (odds + 100)

    return 100 / (odds + 100)

def american_to_mult(odds):

    if odds < 0:
        return 100 / odds
    
    return odds / 100

# https://en.wikipedia.org/wiki/Kelly_criterion
def kelly(mult, prob):
    return (prob * (mult + 1) - 1) / mult

def run_odds(american_for, american_against, boost):
    pass

if __name__ == "__main__":
    pass
