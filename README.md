# Typograf Service

The typograf prepares the entered Russian text for publication.
* remove extra space and tabs
* remove extra linebreak
* replace " and ' to « »
* replacement hyphen on dash in the phone number
* connect number with word by non-breaking spaces
* replacing dash on hyphen
* replacing hyphens on dashes
* connect conjunctions and any words by non-breaking space

# How to use

For use typograf, you need to install the static module using the command
```Bash
pip install -r requirements.txt
```
To use the generation script, you need to type in the console

```Bash
python3 sever.py
```
The result of the script can be seen [here](http://127.0.0.1:5000/)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)