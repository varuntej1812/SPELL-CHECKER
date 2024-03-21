import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('Review.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Filter out empty lines and convert non-empty lines to integers
values = [int(line.strip()) for line in lines if line.strip()]

if values:  # Check if the values list is not empty
    df = pd.DataFrame({'Values': values})

    value_counts = df['Values'].value_counts().sort_index()

    colors = ['red', 'orange', 'yellow', 'blue', 'green']

    plt.bar(value_counts.index, value_counts.values, color=colors)

    plt.xlabel('Reviews')
    plt.ylabel('Number of Occurrences')
    plt.title('Bar Graph with Reviews')
    plt.show()

    average_value = np.mean(values)
    print(f'The average of all values is: {average_value:.2f}/5')
else:
    print("No valid values found in the file.")
