"""
Name: Ahmed Amro Abd-Elmoneim Kandil
ID: 4211133
Group: A1
Lec: 1

This file contains a class called SimpleSubstitutionCipher
which can be used to encrypt and decrypt messages
using the simple substitution cipher.
"""

import os
import subprocess


class SimpleSubstitution:
    """
    A class to encrypt and decrypt messages using the simple substitution cipher.

    Attributes:
        key: The key to use for encryption or decryption.

    Methods:
        encrypt: Encrypts the plain text message.
        decrypt: Decrypts the cipher text message.
    """

    def __init__(self, key: int = 13) -> None:
        """
        Initializes a new SimpleSubstitution object.

        Args:
            key (int, optional): The key to use for encryption or decryption.

        Raises:
            ValueError: if the `key` argument is lower than 2.
        """

        if key < 2:
            raise ValueError("The key can't be lower than 2.")

        self.__key = key

    @property
    def key(self) -> int:
        """
        Gets the key used for encryption and decryption.

        Returns:
            int: The key.
        """

        return self.__key

    @key.setter
    def key(self, key: int) -> None:
        """
        Sets the key used for encryption and decryption.

        Args:
            key (int): The new key.

        Raises:
            ValueError: if the `key` argument is lower than 2.
        """

        if key < 2:
            raise ValueError("The key can't be lower than 2.")

        self.__key = key

    def encrypt(self, plain_text: str) -> str:
        """
        Encrypts the plain text message.

        Args:
            plain_text (str): The plain text message to encrypt.

        Returns:
            str: The encrypted message.
        """

        return "".join([chr(ord(char) + self.__key) for char in plain_text])

    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the cipher text message.

        Args:
            cipher_text (str): The cipher text message to decrypt.

        Returns:
            str: The decrypted message.
        """

        return "".join([chr(ord(char) - self.__key) for char in cipher_text])


def clear_terminal() -> None:
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run([command])


def main() -> None:
    key = int(input("Enter the secret key: "))
    encrypter = SimpleSubstitution(key=key)

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
            new_key = int(input("Enter the secret key: "))
            encrypter.key = new_key
            continue

        result = FUNCTIONS.get(option_num, quit)(text)
        print(result)

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
