hours = int(input())
minutes = int(input()) + 51


print(f"{(hours + 6 + int(minutes > 60)) % 24:02d}:{(minutes) % 60:02d}")

