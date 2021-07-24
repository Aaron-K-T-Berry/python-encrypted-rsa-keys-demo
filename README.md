# python-encrypted-rsa-keys-demo

This repo will show you how you can easily use the python crypto library to generate encrypted rsa key pairs.

## Running the demo

1. Install python venv and requirements

   ```shell
   python3 -m venv venv
   source venv/bin/active
   pip3 install -r ./requirements.txt
   ```

2. Run the demo python script

   ```shell
   python3 ./generate_rsa_keys.py
   ```

3. There will be 2 generated key pair files generated in the root of the repo. Take a look at [generate_rsa_keys.py](./generate_rsa_keys.py) for more details on implementation.
