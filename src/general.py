def is_not_none_or_empty(list_object):
    #if isinstance(value, NoneType) or value is None:
    if list_object is None:
        return False
    else:
        return len(list_object) > 0

def is_not_none_or_empty_lists(list_objects, is_conjuction = True):
    results = []
    for list_object in list_objects:
        results.append(is_not_none_or_empty(list_object))
    # conjuction = Logical AND
    if is_conjuction:
        if results.count(True) == len(list_objects):
            return True
        else:
            return False
    else:   # disjunction = Logical OR
        if results.count(True) > 0:
            return True
        else:
            return False