
# https://help.smarkets.com/hc/en-gb/articles/214058369-How-to-calculate-implied-probability-in-betting
def american_to_prob(odds):

    if odds < 0:
        return (-odds) / (-odds + 100)

    return 100 / (odds + 100)

def get_true_prob(american_for, american_against):
    real_for = american_to_prob(american_for)
    real_against = 1 - american_to_prob(american_against)

    print(real_for, real_against)
    print((real_for + real_against) / 2, 1 - real_for - real_against)

    return (real_for + real_against) / 2

def american_to_mult(odds):

    if odds < 0:
        return 100 / -odds
    
    return odds / 100

# https://en.wikipedia.org/wiki/Kelly_criterion
def kelly(mult, prob):
    return (prob * (mult + 1) - 1) / mult

def run_odds(american_for, american_against, boost):
    prob = get_true_prob(american_for, american_against)
    mult = american_to_mult(american_for + boost)
    mult_orig = american_to_mult(american_for)
    print(kelly(mult_orig, prob))

    return kelly(mult, prob)

if __name__ == "__main__":
    print(run_odds(-114, -112, 0))
