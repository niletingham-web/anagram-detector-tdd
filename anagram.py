def are_anagrams(first: str, second: str) ->bool:
    return sorted(first) == sorted(second)