import sys

input = sys.stdin.readline

song = """
baby sukhwan tururu turu
very cute tururu turu
in bed tururu turu
baby sukhwan
""".split()
len_of_song = len(song)

n = int(input())
result = song[n % len_of_song - 1]
if "turu" in result:
    count = (n // len_of_song) + result.count("ru")
    if count > 4:
        result = f"tu+ru*{count}"
    else:
        result = "tu" + "ru" * count
print(result)
