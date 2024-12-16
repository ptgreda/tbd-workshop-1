import matplotlib.pyplot as plt
import numpy as np


def get_tests_times(file_name):
    with open(f'dbt_run/{file_name}') as file:
        important_lines = [
            line.strip() for line in file
            if "[OK in" in line
        ]

    times = [
        float(line.split()[-1].replace("s]", ""))
        for line in important_lines
    ]

    return times


if __name__ == "__main__":

    dict = {
        '1': get_tests_times("output_1.txt"),
        '2': get_tests_times("output_2.txt"),
        '4': get_tests_times("output_4.txt"),
    }

    # print sums
    for key in dict:
        print(key, "-", round(sum(dict[key])/60))

    first_key = list(dict.keys())[0]
    x = np.arange(len(dict[first_key]))
    width = 0.25
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in dict.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        multiplier += 1

    ax.set_ylabel('Time (s)')
    ax.set_title('Tests times')
    plt.xticks([])
    ax.legend(loc='upper left', ncols=3)
    plt.yscale("log")
    plt.show()
