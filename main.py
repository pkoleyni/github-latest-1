import sys
import json
import requests

def find_user():
    response = requests.get(
        "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=django&site=stackoverflow")
    question = response.json()['items'][0]
    user_id = question['owner']['user_id']
    display_name = question['owner']['display_name']
    return user_id


def get_question(user_id):
    question = 'https://api.stackexchange.com/2.2/users/{}/questions?order=desc&sort=activity&site=stackoverflow'.format(
        user_id)
    response = requests.get(question)
    a = response.json()
    return a


if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(response.content)

    print(events[0]['created_at'])




