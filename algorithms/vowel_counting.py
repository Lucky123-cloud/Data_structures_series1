def count_vowels_consonants(s):
    vowels = set("aeiou")
    s=s.lower()
    v_count = sum(1 for ch in s if ch in vowels)
    c_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return v_count, c_count

v, c = count_vowels_consonants("Backend Engineer") 
print("Vowels:", v, "Consonants:", c)

