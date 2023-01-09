def shorten(suffixes, base):
    def transform(num):
        if type(num) is not str or not num.isdigit():
            return str(num)
        num = int(num)
        for suffix in suffixes:
            if num < base:
                return f"{int(round(num, 0))} {suffix}"
            num /= base

    return transform

print(shorten(['', 'K', 'M'], 1000)('12456789'))
