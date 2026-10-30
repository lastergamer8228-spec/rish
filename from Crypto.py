from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)

Private_key = key
public_key = key.publickey()

message = b"Aditya Batule"

h = SHA256.new(message)

signature = pkcs1_15.new(Private_key).sign(h)

try:
    pkcs1_15.new(public_key).verify(h, signature)
    verification_result = True

except (ValueError, TypeError):
    verification_result = False

print(f"Message: {message.decode()}")

print(
    f"Signature verification result: {verification_result}"
)