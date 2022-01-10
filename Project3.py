
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

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
print(sort_dict_by_value(most_frequent(here.lower()),True))
