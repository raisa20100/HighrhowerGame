# from  game_data import data
# import random

# def get_random_account():
#     """Get data from random account"""
#     return random.choice(data)

# def format_data(account):
#     """Format account into printable format: name, description and country"""
#     name = account["name"] 
#     description = account["description"]
#     country = account["country"]
#     # print(f'{name}: {account["follower_count"]}')
#     return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#     """Checks followers againts user's guess
#      and returns True  if they got it right.
#     Or False if they  got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
    
# def game():
#     scores = 0
#     game_should_countine = True
#     account_a = get_random_account()
#     account_b = get_random_account()

#     while game_should_contiune:
#         account_a = account_b
#         account_b = get_random_account()

#         while account_a == account_b:
#             account_b = get_random_account()

#         print(f"Comare A: {format_data(account_a)}")
        

