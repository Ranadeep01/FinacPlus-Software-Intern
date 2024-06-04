def caesar_cipher(s, r):
    result = []
    for char in s:
        if char.isalpha():
            sft = r % 26
            if char.isupper():
                result.append(chr((ord(char) - ord('A') + sft) % 26 + ord('A')))
            else:
                result.append(chr((ord(char) - ord('a') + sft) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    lst = s[0]
    cnt = 1

    for char in s[1:]:
        if char == lst:
            cnt += 1
        else:
            if cnt > 1:
                encoded.append(f"{lst}{cnt}")
            else:
                encoded.append(lst)
            lst = char
            cnt = 1
    
    if cnt > 1:
        encoded.append(f"{lst}{cnt}")
    else:
        encoded.append(lst)
    
    return ''.join(encoded)

def special_cipher(input_s, rotation_number):
    caesar_shifted = caesar_cipher(input_s, rotation_number)
    encoded_result = run_length_encode(caesar_shifted)
    
    return encoded_result

red = special_cipher('AABCCC', 3)
print(red)
