import random
import matplotlib.pyplot as plt

math_prob = 0.5

def coin_toss():
    return random.choice(['h', 't'])

def prob_visual(n):
    heads, tails = 0,0
    heads_prob = []
    tails_prob = []
    toss_counts = []

    for i in range(1, n+1):
        if coin_toss() == 'h':
            heads += 1
        else:
            tails += 1

        heads_prob.append(heads / i)
        tails_prob.append(tails / i)
        toss_counts.append(i)

    plt.figure(figsize=(8, 6))
    plt.plot(toss_counts, heads_prob, label='Tossed Heads Probability', color='blue')
    plt.plot(toss_counts, tails_prob, label='Tossed Tails Probability', color='orange')
    plt.axhline(y=math_prob, color= 'black', linestyle='--', label='Math Probability (0.5)')
    plt.title('Coin Toss Probability Visualization')
    plt.xlabel('number of tosses')
    plt.ylabel('probability')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    try:
        tosses = int(input("Enter the number of coin tosses to simulate the visualization: "))
        prob_visual(tosses)

    except ValueError:
        print("Please enter a valid number above 100 for better visual")