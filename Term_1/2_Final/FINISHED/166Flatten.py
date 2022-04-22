"""Flatten"""
import json
def main(var: list):
    """Flatten"""
    my_list = []
    for i in var:
        if isinstance(i, list):
            my_list += main(i)
        else:
            my_list.append(i)
    return my_list
print(sorted(main(json.loads(input())))[::-1])
