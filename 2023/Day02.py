import re
from collections import ChainMap
import numpy

raw_data = [
    line for line in open("2023/Inputs/Day02Input.txt", "r").read().splitlines()
]
id_pattern = re.compile(r"Game\s(\d+):\s")
bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
games = [
    {
        "id": int(re.search(id_pattern, line).group(1)),
        "reveals": [
            dict(
                ChainMap(
                    *[
                        {pick.split(" ")[1]: int(pick.split(" ")[0])}
                        for pick in reveal.split(", ")
                    ]
                )
            )
            for reveal in line.split(": ")[1].split("; ")
        ],
    }
    for line in raw_data
]

answer_one = sum(
    game["id"]
    for game in games
    if all(
        [
            all([bag[color] >= quantity for color, quantity in reveal.items()])
            for reveal in game["reveals"]
        ]
    )
)

print(f"Answer 1: {answer_one}")

for game in games:
    for reveal in game["reveals"]:
        for color, quantity in reveal.items():
            if "minimum" not in game.keys():
                game["minimum"] = {}
            if color not in game["minimum"].keys():
                game["minimum"][color] = quantity
            else:
                game["minimum"][color] = max(game["minimum"][color], quantity)

answer_two = sum(numpy.prod(list(game["minimum"].values())) for game in games)

print(f"Answer 2: {answer_two}")
