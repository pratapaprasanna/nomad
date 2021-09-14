import json
import time
import pandas as pd


def get_current_time():
    return int(time.time()) * 1000


def get_state_information(state):
    df = pd.read_csv("state_codes.csv")
    try:
        min_df = df[df["state"] == state].reset_index()
        return min_df["tin"][0], min_df["state-code"][0]
    except:
        return None


def read_config():
    with open("config.json") as fp:
        data = json.load(fp)
    return data


def tailor_strings(input):
    input = input.lower().strip()
    input = " ".join(input.split()).replace(" ", "-")
    return input
