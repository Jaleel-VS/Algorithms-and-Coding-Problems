def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text.lower():
        if char in seen:
            dupes.add(char) # add duplicate letter to set if already in seen
        seen.add(char)
    return len(dupes)