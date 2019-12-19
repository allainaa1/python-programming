from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import json
from unidecode import unidecode

# client.players_advanced_season_totals(season_end_year=2020, output_type=OutputType.JSON, output_file_path="AdvplayersStats2020.json")

# client.season_schedule(season_end_year=2020, output_type=OutputType.JSON, output_file_path="2020Schedule.json")

with open("playersSeason2020.json", "r") as playersTotals_file:
    data = json.load(playersTotals_file)
