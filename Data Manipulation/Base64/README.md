## Current Scripts

1. Base64Encode.py - Encodes images to Base64 string

# Base64Encode.py

Prereqs:
pyperclip - For copying to clipboard

This script takes in a file path as a script parameter, after which the script
then attempts to encode the file's contents into base64. The result is then
copied to the clipboard.

Example of running the script:
```
python Base64Encode.py [file path]
```
where '[file path]' is the path to the file. So if the file is in the current
directory called 'test.png' then running the script will look like:
```
python Base64Encode.py 'test.png'
```