import os

ENTRY = "Dad died during the meeting that should've been an email, and I spent his last breath on mute."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY)
