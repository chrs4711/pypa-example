import requests

def say_hello():
    print('hello from my_function')


def another_function():
    print('hello from another_function')


def cat_fact() -> str:
    r = requests.get('https://cat-fact.herokuapp.com/facts/random')
    
    result = r.json()
    print(result['text'])


if __name__ == "__main__":
    """Say Hello"""
    say_hello()
