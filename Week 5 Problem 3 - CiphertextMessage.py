class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        count_of_valid_words = 0
        max_count = 0
        ans = ()

        for s in range(0, 27):
            message_text_decrypted = super().apply_shift(s)
            words_in_ciphertext = message_text_decrypted.split(' ')

            for word in words_in_ciphertext:
                if is_word(WORDLIST_FILENAME, word):
                    count_of_valid_words += 1

            if count_of_valid_words > max_count:
                max_count = count_of_valid_words
                ans = (max_count, message_text_decrypted)

        return ans
