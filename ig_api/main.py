import os
from pathlib import Path
from json import dump
import argparse
from dotenv import load_dotenv
from instagrapi import Client
from get_medias_with_comments import get_medias_with_comments


def main(user_names=[""]):

    load_dotenv()

    cl = Client()
    setting_file_path = "./ig_api/settings.json"
    if Path(setting_file_path).is_file():
        cl.load_settings(setting_file_path)
    else:
        cl.login(os.getenv("IG_ACCOUNT"), os.getenv("IG_PASSWORD"))
        cl.dump_settings(setting_file_path)

    for user_name in user_names:
        user_id = cl.user_id_from_username(user_name)
        medias = get_medias_with_comments(cl, user_id, 3)

        output_result_file = "./results/{user}.json".format(
            user=user_name)
        os.makedirs(os.path.dirname(output_result_file), exist_ok=True)
        with open(output_result_file, "w", encoding='utf8') as f:
            dump(medias, f, indent=4, sort_keys=True,
                 default=str, ensure_ascii=False)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-us", "--users", type=str, required=True, help="User names of IG e.g., rimazeidan51,its_yiling"
    )
    args = arg_parser.parse_args()

    users = str(args.users).split(",")
    main(users)
