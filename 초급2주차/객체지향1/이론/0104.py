import string

def encode_char(char):
    if char in string.ascii_lowercase:
        return chr(ord('z') - ord(char) + ord('a'))
    if char in string.ascii_uppercase:
        return chr(ord('Z') - ord(char) + ord('A'))
    return char

def decode_char(char):
    if char in string.ascii_lowercase:
        return chr(ord('z') - ord(char) + ord('a'))
    if char in string.ascii_uppercase:
        return chr(ord('Z') - ord(char) + ord('A'))
    return char


def reverse_string(string):
    return ''.join(reversed(string))


def encode(password):

    reversed_password = reverse_string(password)

    encoded = ""
    for i in range(len(reversed_password)):
        encoded += encode_char(reversed_password[i])

    result = encoded + str(len(encoded))[-1]
    
    return result


def decode(encoded_password):

    number_stripped = encoded_password[:-1]

    decoded = ""
    for i in range(len(number_stripped)):
        decoded += decode_char(number_stripped[i])
    
    result = reverse_string(decoded)
    
    return result