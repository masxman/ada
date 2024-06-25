def computeLPSArray(pat, M, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    computeLPSArray(pat, M, lps)
    i = j = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
            if j == M:
                print(f"Found pattern at index {i - j}")
                j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

txt = input("Enter the text: ")
pat = input("Enter the pattern: ")
KMPSearch(pat, txt)
