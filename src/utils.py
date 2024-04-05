import matplotlib.pyplot as plt

def plot_accuracy(results):
    """
    Plots bar chart for model accuracies.
    Input: results dict {model_name: accuracy}
    """
    names = list(results.keys())
    scores = list(results.values())

    plt.figure(figsize=(10,6))
    bars = plt.bar(names, scores, color='skyblue')
    plt.ylim(0, 1)
    plt.ylabel("Accuracy")
    plt.title("Model Accuracy Comparison")
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    for bar, score in zip(bars, scores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 0.05,
                 f"{score:.2f}", ha='center', color='black', fontsize=11)
    plt.tight_layout()
    plt.show()
# Update utilities and data loader with improvements
