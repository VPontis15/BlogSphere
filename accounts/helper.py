from datetime import date


import random

def displayGreeting(user):

    greetings = [f"Welcome back {user}", f"Good to see you {user}", f"Whats on your mind {user}?", f"Always happy to see you {user}", f"Hello again {user}! Your presence brightens our day.", f"Back for more awesomeness? Let's dive in {user}!",f"Welcome back, avid reader! Ready to explore new insights? {user}",f"Hi there! Your return sparks the journey through intriguing articles {user}.",f"Great to see you again! Dive into captivating articles waiting for you {user}.",f"Back for more inspiration {user}? Let's embark on a new reading adventure!",f"Welcome back, fellow explorer! Uncover fresh perspectives with us.",f"Hello, dear reader! Your return signals a wonderful journey ahead.",f"Welcome back {user} to our blog world! Ready to explore,",f"Hi there {user}! Dive into intriguing articles,"]
    number = random.randint(0, len(greetings)-1)
    return greetings[number]

def default_date():
    return date.today()