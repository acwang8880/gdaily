from tabulate import tabulate
import typer
import genshinstats as gs
import yaml
from pathlib import Path

# for i in gs.get_wish_history():
#     print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")

# show configs
# modify configs (add / delete entry)
#    validation surrounding
# daily login for (all / person)
# see wish counter (calculate percentages / tracker / type of 5050 win)

"""
daily_reward_info = gs.get_daily_reward_info()
claim_daily_result = gs.claim_daily_reward()


# output = tabulate([daily_reward_info, claim_daily_result], headers=["Info", "Result"])
print(daily_reward_info)
print(claim_daily_result)
"""

package_dir = Path(__file__).parent.absolute()
config_path = package_dir.joinpath("credentials.yml")

with open(config_path) as f:
    user_configs = yaml.load(f, Loader=yaml.FullLoader)

print(user_configs)

for user, secrets in user_configs.items():
    print("=======")
    print(user)
    gs.set_cookie(
        ltuid=secrets["ltuid"],
        ltoken=secrets["ltoken"]
    )
    daily_reward_info = gs.get_daily_reward_info()
    claim_daily_result = gs.claim_daily_reward()

    print(daily_reward_info)
    print(claim_daily_result)
