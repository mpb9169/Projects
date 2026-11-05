sample_list = [1, 7, 8, -6, 8, 5, -6, 2, 2, 9, 7, 9, 0, 0, -11, -19, 12]

def print_list(lst):
    print(sorted(lst))

def remove_recursive(lst):
    if not lst:
        return []
    head, *tail = lst
    return [head] + remove_recursive([x for x in tail if x != head])

def remove_reduce(lst):
    from functools import reduce
    return reduce(lambda acc, x: acc if x in acc else acc + [x], lst, [])

def remove_filter(lst):
    seen = set()
    def is_new(x):
        if x in seen:
            return False
        seen.add(x)
        return True
    return list(filter(is_new, lst))

print_list(remove_recursive(sample_list))
print_list(remove_reduce(sample_list))
print_list(remove_filter(sample_list))