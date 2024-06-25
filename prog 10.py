MAX_CHARS = 256

def max(a, b):
    return a if a > b else b

def badCharHeuristic(pat, size, badchar):
    for i in range(MAX_CHARS):
        badchar[i] = -1
    for i in range(size):
        badchar[ord(pat[i])] = i

def patternsearch(text, pat):
    m = len(pat)
    n = len(text)
    badchar = [-1] * MAX_CHARS
    badCharHeuristic(pat, m, badchar)
    s = 0  # Initialize shift

    while s <= (n - m):
        j = m - 1
        while j >= 0 and pat[j] == text[s + j]:
            j -= 1
        if j < 0:
            print("\nPattern occurs at position =", s)
            s += m
        else:
            s += max(1, j - badchar[ord(text[s + j])])

# Main Code
text = input("Enter the text: ").rstrip('\n')
pat = input("Enter the pattern: ").rstrip('\n')
patternsearch(text, pat)
