"""
Name: Ahmed Amro Abd-Elmoneim Kandil
ID: 4211133
Group: A1
Lec: 1

This file contains a class called VigeneReCipher which can be
used to encrypt and decrypt messages using the vigene're cipher.
"""

import os
import subprocess


class VigeneReCipher:
    """
    A class to encrypt and decrypt messages using the Vigenere cipher.

    Attributes:
        key: The key to use for encryption or decryption.

    Methods:
        encrypt: Encrypts the plain text message.
        decrypt: Decrypts the cipher text message.
    """

    def __init__(self, key: str) -> None:
        """
        Initializes a new VigenereCipher object.

        Args:
            key (str): The key to use for encryption or decryption.

        Raises:
            ValueError: if the `key` argument is empty or contains non-alphabetic characters.
        """

        if not key.isalpha():
            raise ValueError("The key must contain only alphabetic characters.")

        self.__key = key.lower()

    @property
    def key(self) -> str:
        """
        Gets the key used for encryption and decryption.

        Returns:
            str: The key.
        """

        return self.__key

    @key.setter
    def key(self, key: str) -> None:
        """
        Sets the key used for encryption and decryption.

        Args:
            key (str): The new key.

        Raises:
            ValueError: if the `key` argument is empty or contains non-alphabetic characters.
        """

        if not key.isalpha():
            raise ValueError("The key must contain only alphabetic characters.")

        self.__key = key.lower()

    def extend_key(self, text: str) -> str:
        """
        Extends the key to match the length of the text.

        Args:
            text (str): The text for which to extend the key.

        Returns:
            str: The extended key.
        """

        extended_key = self.__key

        while len(extended_key) < len(text):
            extended_key += self.__key

        return extended_key[: len(text)]

    def encrypt(self, plain_text: str) -> str:
        """
        Encrypts the plain text message.

        Args:
            plain_text (str): The plain text message to encrypt.

        Returns:
            str: The encrypted message.
        """

        def encrypt_char(char: str, key_char: str) -> str:
            if not char.isalpha():
                return char

            return chr((ord(char) + ord(key_char) - 2 * ord("a")) % 26 + ord("a"))

        plain_text = plain_text.lower()
        extended_key = self.extend_key(plain_text)

        encrypted_text = [
            encrypt_char(char, key_char)
            for char, key_char in zip(plain_text, extended_key)
        ]

        return "".join(encrypted_text)

    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the cipher text message.

        Args:
            cipher_text (str): The cipher text message to decrypt.

        Returns:
            str: The decrypted message.
        """

        def decrypt_char(char: str, key_char: str) -> str:
            if not char.isalpha():
                return char

            return chr((ord(char) - ord(key_char) + 26) % 26 + ord("a"))

        cipher_text = cipher_text.lower()
        extended_key = self.extend_key(cipher_text)

        decrypted_text = [
            decrypt_char(char, key_char)
            for char, key_char in zip(cipher_text, extended_key)
        ]

        return "".join(decrypted_text)


def clear_terminal() -> None:
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run([command])


def main() -> None:
    key = input("Enter the secret key: ")
    encrypter = VigeneReCipher(key=key)

    OPTIONS = (
        "Encrypt",
        "Decrypt",
        "Change Key",
    )

    FUNCTIONS = {
        1: encrypter.encrypt,
        2: encrypter.decrypt,
    }

    while True:
        clear_terminal()

        for i, option in enumerate(OPTIONS, start=1):
            print(f"{i}. {option}")

        text = input("Enter the message: ")
        option_num = int(input("Enter option num or 0 for quit: "))

        if option_num == 3:
            new_key = input("Enter the secret key: ")
            encrypter.key = new_key
            continue

        result = FUNCTIONS.get(option_num, quit)(text)
        print(result)

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
