from memory_profiler import profile


def mergeAlternately(word1: str, word2: str) -> str:
        from itertools import zip_longest
        output_str = ""
        for c1, c2 in zip_longest(word1, word2, fillvalue=None):
                if c1:
                        output_str += str(c1)
                if c2:
                        output_str += str(c2)
        
        return output_str




print(mergeAlternately("ab","pqrs"))




# Method 2

@profile
def mergeAlternately_2(word1: str, word2: str) -> str:
    max_len = max(len(word1), len(word2))
    output_str = ""

    for i in range(max_len):
            if len(word1) > i:
                  output_str += str(word1[i])
            if len(word2) > i:
                  output_str += str(word2[i])

    return output_str

# print(mergeAlternately_2("ab","pqrs"))
