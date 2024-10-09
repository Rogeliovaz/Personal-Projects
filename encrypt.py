class Salting:
    """
    A class that applies salting to a given text.

    Attributes:
        salt (str): The salt string to be appended to the original text.
        cipher_text (str): The result of the original text concatenated with the salt.
    """

    def __init__(self, text: str, salt: str) -> None:
        """
        Initializes the Salting class with the provided text and salt.

        Args:
            text (str): The original text that will be salted.
            salt (str): The salt string to append to the text.

        Raises:
            TypeError: If the provided text or salt is not a string.
        """
        if not isinstance(text, str):
            raise TypeError
        if not isinstance(salt, str):
            raise TypeError

        self.salt = salt
        self.cipher_text = text + self.salt

    def __str__(self) -> str:
        """
        Returns the original text by removing the salt.

        Returns:
            str: The original text before salting.
        """
        return self.cipher_text[:-len(self.salt)]

    
class ReverseCipher1:
    """
    A class that encrypts a given text by reversing its characters.

    Attributes:
        cipher_text (str): The encrypted (reversed) version of the provided text.
    """

    def __init__(self, text: str) -> None:
        """
        Initializes the ReverseCipher1 class and encrypts the provided text by reversing it.

        Args:
            text (str): The original text to be encrypted.

        Raises:
            TypeError: If the provided text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError

        self.cipher_text = self.encrypt(text)

    def encrypt(self, text: str) -> str:
        """
        Reverses the characters of the provided text.

        Args:
            text (str): The original text to be reversed.

        Returns:
            str: The reversed text.
        """
        result = ''  # Initialize an empty string to store the reversed text
        for letter in range(len(text) - 1, -1, -1):
            result += text[letter]

        return result

    def __str__(self) -> str:
        """
        Returns the encrypted (reversed) text as a string.

        Returns:
            str: The encrypted (reversed) version of the text.
        """
        result = self.encrypt(self.cipher_text)
        return f"{result}"


class ReverseCipher2:
    """
    A class that reverses the letters of each word in the provided text.
    
    Attributes:
        cipher_text (str): The reversed version of the input text.
    """

    def __init__(self, text: str) -> None:
        """
        Initializes the ReverseCipher2 class and encrypts the provided text by reversing each word.

        Args:
            text (str): The text to be encrypted.

        Raises:
            TypeError: If the provided text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError

        self.cipher_text = self.encrypt(text)

    def encrypt(self, text: str) -> str:
        """
        Reverses each word in the provided text while keeping the word order intact.

        Args:
            text (str): The text to be reversed word by word.

        Returns:
            str: The text with reversed words.
        """
        list_text = text.split(' ')
        reversed_words = []

        for word in list_text:
            temp = ''
            for i in range(len(word) - 1, -1, -1):
                temp += word[i]
            reversed_words.append(temp)

        result = ' '.join(reversed_words)
        return result

    def __str__(self) -> str:
        """
        Returns the encrypted (reversed words) version of the text.

        Returns:
            str: The encrypted text with reversed words.
        """
        result = self.encrypt(self.cipher_text)
        return f"{result}"

    
class XORCipher:
    """
    A class that applies XOR encryption using a key.

    Attributes:
        key (str): The key used for XOR encryption.
        cipher_text (str): The encrypted text.
    """

    def __init__(self, text: str, key: str) -> None:
        """
        Initializes the XORCipher class with the provided text and key.

        Args:
            text (str): The original text to be encrypted.
            key (str): The key used for the XOR operation.

        Raises:
            TypeError: If the provided text or key is not a string.
        """
        if not isinstance(text, str):
            raise TypeError
        if not isinstance(key, str):
            raise TypeError
        
        self.key = key
        self.cipher_text = self.cipher(text)

    def cipher(self, text: str) -> str:
        """
        Encrypts the provided text using the XOR operation and the key.

        Args:
            text (str): The original text to be encrypted.

        Returns:
            str: The XOR encrypted text.
        """
        encryption_lst = []

        for i, char in enumerate(text):
            key = self.key[i % len(self.key)]  # Match the length of the key with the text
            xor = ord(char) ^ ord(key)
            result = chr(xor)
            encryption_lst.append(result)

        encryption_str = ''.join(encryption_lst)
        return encryption_str

    def __str__(self) -> str:
        """
        Returns the decrypted text by applying XOR encryption again on the encrypted text.

        Returns:
            str: The decrypted text.
        """
        return self.cipher(self.cipher_text)


class CaesarCipher:
    """
    A class that applies Caesar Cipher encryption to a text.

    Attributes:
        key (int): The shift key used for the Caesar cipher.
        cipher_text (str): The encrypted text.
    """

    def __init__(self, text: str, key: int) -> None:
        """
        Initializes the CaesarCipher class with the text and key.

        Args:
            text (str): The original text to be encrypted.
            key (int): The shift key for the cipher.

        Raises:
            TypeError: If the provided text is not a string or the key is not an integer.
        """
        if not isinstance(text, str):
            raise TypeError
        
        if not isinstance(key, int):
            raise TypeError
        
        if key > 26:
            key = key % 26
        
        if key < -26:
            key = key % -26

        self.key = key
        self.cipher_text = self.cipher(text, self.key)
    
    def cipher(self, text: str, key: int) -> str:
        """
        Applies Caesar Cipher encryption to the provided text.

        Args:
            text (str): The text to be encrypted.
            key (int): The shift key for the cipher.

        Returns:
            str: The encrypted text.
        """
        lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        special_char = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', ':', ';', '<', ',', '>', '.', '/']

        encryption = ''

        for i in text:
            if i == ' ' or i in special_char:
                encryption += i

            if i in lower_case:
                index_lc = lower_case.index(i)
                if index_lc + key > 25:
                    index_lc -= 26
                    encryption += lower_case[index_lc + key]
                else:
                    encryption += lower_case[index_lc + key]

            if i in upper_case:
                index_uc = upper_case.index(i)
                if index_uc + key > 25:
                    index_uc -= 26
                    encryption += upper_case[index_uc + key]
                else:
                    encryption += upper_case[index_uc + key]

        return encryption
    
    def __str__(self) -> str:
        """
        Decrypts the text by reversing the Caesar cipher with the negative key.

        Returns:
            str: The decrypted text.
        """
        return self.cipher(self.cipher_text, -(self.key))


class VigenereCipher:
    """
    A class that applies Vigenere Cipher encryption to a text.

    Attributes:
        key (str): The encryption key used.
        cipher_text (str): The encrypted text.
    """

    def __init__(self, text: str, key: str) -> None:
        """
        Initializes the VigenereCipher class with the text and key.

        Args:
            text (str): The original text to be encrypted.
            key (str): The key for the Vigenere cipher.

        Raises:
            TypeError: If the provided text or key is not a string.
        """
        if not isinstance(text, str):
            raise TypeError
        
        if not isinstance(key, str):
            raise TypeError
        
        self.key = key
        self.cipher_text = self.cipher(text)
    
    def cipher(self, text: str) -> str:
        """
        Applies Vigenere Cipher encryption to the provided text.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        special_char = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', ':', ';', '<', ',', '>', '.', '/']
        key_len = len(self.key)
        encryption = ''

        for i, char in enumerate(text):
            key_char = self.key[i % key_len]

            if char == ' ' or char in special_char:
                encryption += char
            # These two elifs handfle the main logic     
            elif char in lower_case:
                index_text_lc = lower_case.index(char)
                if key_char.isnumeric():
                    index_key_lc = int(key_char)
                elif key_char in upper_case:
                    index_key_uc = upper_case.index(key_char)
                else:
                    index_key_lc = lower_case.index(key_char)

                index_result = (index_key_lc + index_text_lc) % 26
                encryption += lower_case[index_result]

            elif char in upper_case:
                index_text_uc = upper_case.index(char)
                if key_char.isnumeric(): 
                    index_key_uc = int(key_char)
                elif key_char in lower_case:
                    index_key_uc = lower_case.index(key_char)
                else:
                    index_key_uc = upper_case.index(key_char)

                index_result = (index_key_uc + index_text_uc) % 26
                encryption += upper_case[index_result]

        return encryption

    def decrypt(self, text: str, key: str) -> str:
        """
        Decrypts the Vigenere Cipher encrypted text.

        Args:
            text (str): The encrypted text.
            key (str): The encryption key.

        Returns:
            str: The decrypted text.
        """
        key_len = len(key)
        decryption = ''
        lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        special_char = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', ':', ';', '<', ',', '>', '.', '/']

        for i, char in enumerate(text):
            key_char = key[i % key_len]

            if char == ' ' or char in special_char:
                decryption += char

            elif char in lower_case:
                index_text_lc = lower_case.index(char)
                if key_char.isnumeric():
                    index_key_lc = int(key_char)
                elif key_char.islower():
                    index_key_lc = lower_case.index(key_char)
                else:
                    index_key_lc = upper_case.index(key_char)

                index_result = (index_text_lc - index_key_lc) % 26
                decryption += lower_case[index_result]

            elif char in upper_case:
                index_text_uc = upper_case.index(char)
                if key_char.isnumeric():
                    index_key_uc = int(key_char)
                elif key_char.isupper():
                    index_key_uc = upper_case.index(key_char)
                else:
                    index_key_uc = lower_case.index(key_char)

                index_result = (index_text_uc - index_key_uc) % 26
                decryption += upper_case[index_result]

        return decryption
    
    def __str__(self) -> str:
        """
        Decrypts the text using the Vigenere cipher.

        Returns:
            str: The decrypted text.
        """
        return self.decrypt(self.cipher_text, self.key)

class CustomMappingCipher:
    """
    A class that implements a custom character mapping cipher for encryption and decryption.

    Attributes:
        character_map (dict): A dictionary that maps characters to their encrypted equivalents.
        cipher_text (str): The encrypted text after applying the custom mapping cipher.
    """

    def __init__(self, text: str) -> None:
        """
        Initializes the CustomMappingCipher class with a text and applies the cipher to encrypt it.

        Args:
            text (str): The original text to be encrypted.

        Raises:
            TypeError: If the provided text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError
        
        self.character_map = {
            # Mapping of characters to their corresponding encrypted values
            'a': ',', 'b': 'c', 'c': '/', 'd': '&', 'e': 'k', 'f': '}', 'g': '4', 'h': 'w',
            'i': '>', 'j': 'b', 'k': 'W', 'l': 'P', 'm': 'V', 'n': '$', 'o': '"', 'p': '`',
            'q': 'U', 'r': 'x', 's': '~', 't': 'o', 'u': 'K', 'v': 'B', 'w': ']', 'x': 'e',
            'y': '[', 'z': '7', 'A': 'H', 'B': 'i', 'C': 'G', 'D': 's', 'E': ';', 'F': 'A',
            'G': 'y', 'H': 'g', 'I': 'r', 'J': '%', 'K': 'p', 'L': '^', 'M': 'C', 'N': '6',
            'O': 'O', 'P': '8', 'Q': '3', 'R': '\\', 'S': '5', 'T': '0', 'U': 'Y', 'V': '1',
            'W': '+', 'X': '{', 'Y': '2', 'Z': 'D', '0': '(', '1': '=', '2': '?', '3': 'q',
            '4': '<', '5': 't', '6': 'f', '7': 'L', '8': '|', '9': 'l', '!': 'Q', '"': 'F',
            '#': 'h', '$': ')', '%': 'X', '&': 'd', "'": 'j', '(': '.', ')': 'v', '*': 'E',
            '+': "'", ',': '#', '-': '@', '.': '*', '/': 'z', ':': 'S', ';': ':', '<': 'N',
            '=': 'Z', '>': ' ', '?': 'T', '@': '-', '[': 'R', '\\': 'u', ']': 'M', '^': '9',
            '_': '_', '`': 'a', '{': 'n', '|': 'I', '}': 'J', '~': '!', ' ': 'm'
        }
        self.cipher_text = self.cipher(text)

    def cipher(self, text: str) -> str:
        """
        Encrypts the provided text using the custom character mapping.

        Args:
            text (str): The original text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        encryption = ''

        for letter in text:
            for k, v in self.character_map.items():
                if letter == k:
                    encryption += v
            
        return encryption

    def decrypt(self, text: str) -> str:
        """
        Decrypts the provided encrypted text by reversing the character mapping.

        Args:
            text (str): The encrypted text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        decrypted = ''
        new_dict = dict()

        
        for k, v in self.character_map.items():
            new_dict[v] = k
        
        for letter in text:
            for k, v in new_dict.items():
                if letter == k:
                    decrypted += v
        return decrypted

    def __str__(self) -> str:
        """
        Returns the decrypted version of the ciphered text.

        Returns:
            str: The decrypted text.
        """
        return self.decrypt(self.cipher_text)


