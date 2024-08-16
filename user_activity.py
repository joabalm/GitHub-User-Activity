import requests
import argparse

api_url = "https://api.github.com/users/{}/events"

def user_activity(name_user):
    request = requests.get(api_url.format(name_user))
    if request.status_code == 200:
        data = request.json()
    print(data)

def main():
    parser = argparse.ArgumentParser(
        prog="GitHub user activity",
        description="Github-user-activity-CLI"
    )

    subparser = parser.add_subparsers(dest="command", help="Availabre commands")

    subparser_user_activity = subparser.add_parser("user.activity", help="User for fetches events")
    subparser_user_activity.add_argument("user", type=str, help="User for fetches events")

    args = parser.parse_args()

    if args.command == "user.activity":
        user_activity(args.user)
    else:
        print("user not found")

if __name__ == "__main__":
    main()

