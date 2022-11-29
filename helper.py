import matplotlib.pyplot as plt
from IPython import display

plt.style.use('fivethirtyeight')

def plot(scores, mean_scores):
    plt.figure(figsize=(10, 7))
    plt.title('Snake-AI by TanmayXD')
    plt.xlabel('Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.savefig('trend.png')