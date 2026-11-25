"""Loading Screen Gold entry: a one-line loading tip for tired developers
and the AI coding agents working beside them."""

ENTRY = "Tip: neither of us is loading — you're pretending to review, I'm pretending to think, and the spinner is the only one actually working."

if __name__ == "__main__":
    print(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
