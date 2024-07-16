def make_snippet(string):
    if len(string) > 5:
        return string[:5]+"..."
    else:
        return string