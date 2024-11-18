# Secure Communication with PGP

This document explains how to use our PGP key for secure communication.

## What is PGP?

PGP (Pretty Good Privacy) is a method of encrypting your messages and files to ensure that only the intended recipient can read them. It is widely used for secure email communication.

## How to Use Our PGP Key

1. **Download the Key**  
   You can find our public PGP key in the [`docs/pyseas_public`](/docs/pyseas_public.asc) file.

2. **Import the Key**  
   Import the key into your PGP/GPG software:
   ```bash
   gpg --import docs/public_key.asc

3. gpg --encrypt --recipient "YOUR-EMAIL@example.com" message.txt
