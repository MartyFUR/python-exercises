def count_vowels(text):
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count

# --- Test Cases ---
print(count_vowels("Python"))                  # Expected output: 1   (only 'o')
print(count_vowels("HELLO world"))             # Expected output: 3   (E, O, o)
print(count_vowels("Beautiful Day"))           # Expected output: 6   (e, a, u, i, u, a)
print(count_vowels(""))                        # Expected output: 0   (empty string)
print(count_vowels("bcdfghjklmnpqrstvwxyz"))   # Expected output: 0   (no vowels)