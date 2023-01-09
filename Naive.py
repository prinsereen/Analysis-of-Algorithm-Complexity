# Python3 program for Naive Pattern
# Searching algorithm


def search(pat, txt):
	M = len(pat)
	N = len(txt)

	for i in range(N - M + 1):
		j = 0

		while(j < M):
			if (txt[i + j] != pat[j]):
				break
			j += 1

		if (j == M):
			print("Pattern found at index ", i)


# Driver's Code
if __name__ == '__main__':
	txt = "AABAACAADAABAAABAA"
	pat = "AABA"
	
	# Function call
	search(pat, txt)

# This code is contributed
# by PrinciRaj1992
