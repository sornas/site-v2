import requests
data = { "session": "ENTER COOKIE!"}
result = requests.get("https://adventofcode.com/2019/leaderboard/private/view/637041.json", cookies=data)
with open("aoc_standings.json", "w") as f:
    f.write(result.text)
