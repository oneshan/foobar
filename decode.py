import base64

# google account
key = 'seudotw'

# encypted string
string = """
KEIGEQw3MiAWUkRVdHA0FxAFG3N7c0IWCwM4MjICAAFIdG1zQhAXGzEyPgARQ0N0cDYDEwsdICR0 RU9ESD05MBcQAAY2OzZCWURINTQ7DBASCjkyPRFSRFV0cCYLGQsMPzI3QllESCY2MQccEBxzd2lF UhcOMjJ0SVVDCTs4dEVPREgjPj1EUhk=
"""


def decode():
    result = [chr(ord(char) ^ ord(key[idx % len(key)]))
              for idx, char in enumerate(base64.b64decode(string))]
    return ''.join(result)

if __name__ == "__main__":
    print(decode())
