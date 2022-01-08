
def most_frequent(here):
    dictionary = dict()
    for key in here:
        if key not in dictionary:
            if key == ' ':
                continue
            dictionary[key] = 1
        else:
            dictionary[key] += 1
    return dictionary


here = input("Enter a String: ")
print(most_frequent(here.lower()))
