__version__ = "0.0.1"

def analyse_data(list):
    sum = 0
    count = 0
    while (count < len(list)):
        sum = sum + list[count]
        count = count + 1
    average = sum / len(list)
    return (sum, average)
