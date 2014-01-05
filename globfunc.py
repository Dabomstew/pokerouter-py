import re
hashRegex = re.compile(r"\W")

def hashName(string):
    return hashRegex.sub("", string.upper())

if __name__ == "__main__":
    print hashName("Kappa's trol''ling 123 testing Kappa")
    