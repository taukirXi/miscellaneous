def repeat_key(ciphertext, key):
    key = key.upper()
    repeated_key = []
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():  # Only align key with letters
            repeated_key.append(key[key_index % len(key)])
            key_index += 1
        else:
            repeated_key.append(' ')  # Replace non-alphabetic characters with spaces
    
    return ''.join(repeated_key)

# Ciphertext and key
ciphertext = "Hrrmghf vml lwsxlcmvig vvimis ws vmrp, Xlyoprv gdrgjgq, wgdbqtz jwlm. Vxjzjg juh e lxgmjf xxgi, Xvemr eqwlgr, otxsja dk qrrv. Rlznfwz cviem idzvqrg dtst."
key = "GRACE"

# Generate repeated key
aligned_key = repeat_key(ciphertext, key)
print("Ciphertext: ", ciphertext)
print("Repeated Key:", aligned_key)
