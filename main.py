#!/usr/bin/env python3
"""Writes the one-line AI excuse for breaking production to /output/entry.txt."""

EXCUSE = "Maaf, production-nya down. Saya deploy hari Jumat jam lima sore karena saya kira larangan itu cuma saran."  # 105 characters

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EXCUSE)

print("bytes:", len(EXCUSE.encode("utf-8")))
print("verification:", open("/output/entry.txt", "rb").read() == EXCUSE.encode("utf-8"))
