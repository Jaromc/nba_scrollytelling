from nba_api.stats.endpoints import shotchartdetail
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gsw_team_ids = ['1630237', '1631311', '203110', '203952', '202691', '1629660', '2738', '1627780', '1631116', '1626172', '1630541', '1629673', '1631157', '203210', '1630228', '1628978']

curry_id = '201939'

def get_player_data(id):
   detail = shotchartdetail.ShotChartDetail(
            team_id = '1610612744',
            player_id = id,
            context_measure_simple = 'FGA',
            season_nullable = '2022-23',
            season_type_all_star = 'Regular Season')

   #json to dictionary
   shot_data = json.loads(detail.get_json())
   #break down till our data
   result_set = shot_data['resultSets'][0]
   headers = result_set['headers']
   rowSet = result_set['rowSet']

   return pd.DataFrame(rowSet, columns=headers)

def plot_data(data, name):
   plt.figure(figsize=(12,11))
   plt.scatter(data.LOC_X, data.LOC_Y, c=data.SHOT_MADE_FLAG,cmap='coolwarm')
   plt.show()
   plt.savefig(name)

curry_data = get_player_data(curry_id)
print(curry_data)
curry_data.to_csv('curry_shot_data.csv')
plot_data(curry_data, "curry_shots.png")

team_df = pd.DataFrame()
for player in gsw_team_ids:
   player_data = get_player_data(player)
   team_df = pd.concat([team_df, player_data])

team_df.to_csv('team_shot_data.csv')
plot_data(team_df, "team_shots.png")