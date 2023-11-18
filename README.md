# Python ASCII Encryption

This Python script demonstrates a simple ASCII-based encryption algorithm. It converts alphabetic characters to their ASCII numerical values, applies a secret number for encryption, and allows decryption using the same secret number.

## Getting Started

To get started, clone or download the repository:

```bash
git clone https://github.com/KalyanMurapaka45/Python-ASCII-Encryption
cd Python-ASCII-Encryption
```

## Basics

ASCII encryption involves converting alphabetic characters to ASCII numerical values and using a secret number for encryption and decryption.

- Encrypting:
  ```
  a -> 97 -> 97 (+|-) secret_number -> new character
  ```
  Let's say our secret number is 5:
  ```
  a -> 97 -> 97 + 5 -> f
  ```

- Decrypting:
  ```
  f -> 102 -> 102 (+|-) secret_number -> decrypted character
  ```
  Since we know the secret number is 5:
  ```
  f -> 102 -> 102 - 5 > a
  ```

## Implementation

The repository includes two functions, `encrypt` and `decrypt`, which perform ASCII-based encryption and decryption. They take a text input and a secret number for encryption and return the encrypted text. Decryption requires specifying the secret number and the encrypted text.

## Demo

```python
from algorithms import encrypt, decrypt

army_text = "Throw the missiles at 9pm"
print(encrypt(army_text, key=10))
# Output: '^r|y\x81*~ro*ws}}svo}*k~*Czw'

print(decrypt('^r|y\x81*~ro*ws}}svo}*k~*Czw', key=10))
# Output: 'Throw the missiles at 9pm'
```

## Explore

Explore the script's functionality by testing it with various input texts to understand how it can be adapted to different use cases.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to contributors and developers who have contributed to this project.
