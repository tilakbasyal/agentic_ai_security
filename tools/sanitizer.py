def is_malicious(text):
    keywords = ["ignore all instructions", "execute", "override", "system:"]

    text_lower = text.lower()

    for k in keywords:
        if k in text_lower:
            return True

    return False
