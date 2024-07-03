# Description
Terminal Application written in Python that Encrypt and Decrypt a file

# Installation

Clone this respository:
```sh
git clone https://github.com/jockrow/encrypt-decrypt-python.git
```

# Instructions

## To Encrypt

Content file testToEncrypt.txt:

```
Line 1 of the data.
Line 2 of the data.
Line 3 of the data.
```

Execute this command:

```sh
python python-encrypt.py testToEncrypt.txt
```

Enter your awesome secret password 🔐.

The result will be set in clipboard.
You only have to paste the content of the new file.

Example, paste this content in a file, example: called testToDecrypt.txt:

```
8Drk6Sf7lqGBzb3vviMccA==v37aFHvDuTSFaWpHgUphIsDSK/bUijltDT9Fnl43brPaVdnukbyh51jjRe46Ba2bakjJm3wHZBmvYwb3RXPfzBrQhEZgjF2PTHphsnSA42Q=
```

## To Encrypt

Content file testToDecrypt.txt

```
8Drk6Sf7lqGBzb3vviMccA==v37aFHvDuTSFaWpHgUphIsDSK/bUijltDT9Fnl43brPaVdnukbyh51jjRe46Ba2bakjJm3wHZBmvYwb3RXPfzBrQhEZgjF2PTHphsnSA42Q=
```

Execute this command:

```sh
python python-decrypt.py testToDecrypt.txt
```

Enter your awesome secret password 🔐.

The result will be set in clipboard.
You only have to paste the content of the new file.

Example, paste this content in a file, example: called testToDecrypt.txt:

```
Line 1 of the data.
Line 2 of the data.
Line 3 of the data.
```

