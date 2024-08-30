Hash Hunter

Hash Hunter is a versatile hash-cracking tool that supports a wide range of hash types. It uses a wordlist to test potential passwords against hashes and reports any matches found.
Features

    Supports Multiple Hash Types: MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, Blake2s, Blake2b, SHA3 variants, and more.

Installation
Prerequisites

Ensure you have Python 3 installed on your system. You can download Python from python.org.
Setting Up the Project

    Clone the Repository:

    bash

git clone https://github.com/sagar-sehrawat/Hash-Hunter.git
cd HashHunter

Create a Virtual Environment:

bash

python3 -m venv venv

Activate the Virtual Environment:

    On macOS/Linux:

    bash

source venv/bin/activate

On Windows:

bash

    venv\Scripts\activate

Install Required Packages:

bash

    pip install -r requirements.txt

Usage

    Prepare Your Wordlist (recom:rockyou.txt) and Hash File: Each hash should be on a new line.

 
    Run the Tool:

    bash

    python cracker.py -w /path/to/wordlist -f /path/to/hashfile [-v]

        -w, --wordlist: Path to the wordlist file.
        -f, --hashfile: Path to the file containing the target hashes.
        -v, --verbose: Enable verbose output to see which passwords are being tested.

Example

bash

python cracker.py -w ./pass.txt -f ./hash.txt -v


Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub if you have suggestions or improvements.