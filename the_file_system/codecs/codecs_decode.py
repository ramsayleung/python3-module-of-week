from codecs_to_hex import to_hex

text = 'français'

encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

print('Original: ', repr(text), type(text))
print('Encoded: ', to_hex(encoded, 1), type(encoded))
print('Decoded: ', repr(decoded), type(decoded))
