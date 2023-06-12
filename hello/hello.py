import requests


def say_hello():
    print('hello from my_function')


def hello_function() -> str:
    """ Returns the string `hello` """
    return "hello"


def cat_fact() -> str:

    hello_function()

    r = requests.get('https://cat-fact.herokuapp.com/facts/random')
    
    result = r.json()
    fact = result['text']
    print(fact)

    return fact


if __name__ == "__main__":
    """Say Hello"""
    cat_fact()
