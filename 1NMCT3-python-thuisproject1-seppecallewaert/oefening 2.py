import random
def swap_lower_upper(string):
    return string.swapcase()

def shuffle(string):
    words = string.split(" ")
    random.shuffle(words)
    return words

zin = "Dit is EEN test"
print("de doorgegeven string is {0}".format(zin))
print("het resultaat van de eerste functie is:{0}".format(swap_lower_upper(zin)))
print("het resultaat van de tweede functie is: {0}".format(shuffle(zin)))





