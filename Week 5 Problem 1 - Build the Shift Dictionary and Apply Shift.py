    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        plaintext_list = []
        self.ciphertext_list = []

        for letter in string.ascii_lowercase:
            plaintext_list.append(letter)

        for i in range(0, 26 - shift):
            self.ciphertext_list.append(plaintext_list[i + shift])

        for i in range(-3, 0):
            self.ciphertext_list.append(plaintext_list[i + shift])

        return self.ciphertext_list
        
import string

plaintext_list = []
ciphertext_list = []
shift = 3

for letter in string.ascii_lowercase:
    plaintext_list.append(letter)

for i in range(0, 26 - shift):
     ciphertext_list.append(plaintext_list[i + shift])

for i in range(-3, 0):
    ciphertext_list.append(plaintext_list[i+shift])

print(plaintext_list)
print(ciphertext_list) 
