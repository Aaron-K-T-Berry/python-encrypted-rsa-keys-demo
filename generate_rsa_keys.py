from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

private_key_pass = b"your-password"

encrypted_pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(private_key_pass)
)

print(encrypted_pem_private_key.splitlines()[0])
# b'-----BEGIN ENCRYPTED PRIVATE KEY-----'

unencrypted_pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

print(unencrypted_pem_private_key.splitlines()[0])
# b'-----BEGIN RSA PRIVATE KEY-----'

pem_public_key = private_key.public_key().public_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pem_public_key.splitlines()[0])
# b'-----BEGIN PUBLIC KEY-----'

private_key_file = open("example-rsa.pem", "w")
private_key_file.write(encrypted_pem_private_key.decode())
private_key_file.close()

public_key_file = open("example-rsa.pub", "w")
public_key_file.write(pem_public_key.decode())
public_key_file.close()
