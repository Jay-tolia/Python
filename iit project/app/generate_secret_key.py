import secrets

# Generate a random secret key of 16 bytes, represented as a hexadecimal string
secret_key = secrets.token_hex(16)
print(secret_key)
