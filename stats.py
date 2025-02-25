def get_text_count(c):
    return len(c.split())

def unique_char_count(u):
    char_count = {}
    for char in u.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    items = list(d.items())
    items.sort(reverse=True, key=lambda x: x[1])
    return items
