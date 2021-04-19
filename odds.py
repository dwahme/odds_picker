import argparse

# https://help.smarkets.com/hc/en-gb/articles/214058369-How-to-calculate-implied-probability-in-betting
def american_to_prob(odds):

    if odds < 0:
        return (-odds) / (-odds + 100)

    return 100 / (odds + 100)

def get_true_prob_single(american_for):
    real_for = american_to_prob(american_for)

    return real_for - .025

def get_true_prob_ave(american_for, american_against):
    real_for = american_to_prob(american_for)
    real_against = 1 - american_to_prob(american_against)

    return (real_for - real_against) / 2

def american_to_mult(odds):

    if odds < 0:
        return 100 / -odds
    
    return odds / 100

# https://en.wikipedia.org/wiki/Kelly_criterion
def kelly(mult, prob):
    return (prob * (mult + 1) - 1) / mult

def run_odds(american_for, boost):
    prob = get_true_prob_single(american_for)
    mult = american_to_mult(boost)

    return kelly(mult, prob)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run odds')
    parser.add_argument('american_for', action='store', type=int,
                        help='The American odds of the bet going in your favor')
    parser.add_argument('-a', action='store', dest='american_against', type=int, default=None,
                        help='The American odds of the bet in the opposite favor')
    parser.add_argument('-b', action='store', dest='boost', type=int, default=None,
                        help='The American odds that the bet gets boosted to')
    parser.add_argument('-f', action='store', dest='frac', type=float, default=0.5,
                        help='The fraction to reduce the kelly bet size by (default: 0.5)')
    parser.add_argument('-m', action='store', dest='money', type=float, default=None,
                        help='The amount of money you have available')

    args = parser.parse_args()

    succ = get_true_prob_single(args.american_for)
    print(f"The single-estimate probability of success is: {100 * succ:.3f}%")

    if args.american_against != None:
        succ = get_true_prob_ave(args.american_for, args.american_against)
        print(f"The averaged probability of success is: {100 * succ:.3f}%")

    if args.boost != None:
        mult = american_to_mult(args.boost)
        print(f"The profit multiplier from this bet is: {mult}x")
        f = kelly(mult, succ)
        print(f"The original kelly fraction of your money that should be bet is: {f * 100:.2f}%")

        if args.frac != None:
            f = f * args.frac
            print(f"The reduced fraction of your money that should be bet is: {f * 100:.2f}%")

        if f <= 0:
            print("\nThis bet is not worth it")
    
        if args.money != None and f > 0:
            tot = args.money * f
            pot = tot * (mult + 1)
            net = pot * succ - tot
            print(f"\nYou should bet: ${tot:.2f}")
            print(f"Potential winnings: ${pot:.2f}")
            print(f"Average net profit: ${pot:.2f} * {succ * 100:.2f}% - ${tot:.2f} = ${net:.2f}")

    # o = run_odds(138, 207)
    # print(o/2)
    # print(62.38 * o, 62.38 * o / 2)
