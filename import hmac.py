import hmac
import hashlib

message = b"Siyon kalpund"
key = b"super_secret_key"

md5 = hashlib.md5(message).hexdigest()

print("MD5 Digest 1:", md5)
print("MD5 Digest 2:", md5)

sha1 = hashlib.sha1(message).hexdigest()

print("SHA-1 Digest:", sha1)


def hmac_gen(key, msg):
    return hmac.new(
        key,
        msg,
        hashlib.sha256
    ).hexdigest()


def verify(key, msg, mac):
    return hmac.compare_digest(
        hmac_gen(key, msg),
        mac
    )


mac = hmac_gen(key, message)

print("Message:", message.decode())
print("HMAC-SHA256 Tag:", mac)

print(
    "Original Message Verification:",
    verify(key, message, mac)
)

print(
    "Tampered Message Verification:",
    verify(key, b"Aditya Batule.", mac)
)