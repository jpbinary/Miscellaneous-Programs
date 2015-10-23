from passlib.hash import pbkdf2_sha512
# Grubs pbkdf2-hmac-sha512

'''
    default_salt_size = 64
    min_salt_size = 0
    max_salt_size = 1024

    default_rounds = pbkdf2_sha512.default_rounds
    min_rounds = 1
    max_rounds = 0xffffffff # setting at 32-bit limit for now
    rounds_cost = "linear"
'''

# Note: The salt is included in the returned hash.

# strong hash example
hash1 = pbkdf2_sha512.encrypt("password", rounds=250000, salt_size=1024)

# default hash example
hash2 = pbkdf2_sha512.encrypt("password")

print hash1
print '--------------------------------'
print hash2

# returns true if hash matches password
print '--------------------------------'
print 'hash1 Password matches: ', pbkdf2_sha512.verify("wrong password", hash1)
print 'hash2 Password matches: ', pbkdf2_sha512.verify("password", hash2)
