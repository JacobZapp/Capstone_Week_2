import requests

question = input('Ask the 8 ball a question: ')

magic_8_ball_api_url = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}' # Im unsure if this url works

try:
    response = requests.get(magic_8_ball_api_url).json()
    print(response)
    answer = response['magic']['answer']
    print(f'The magic 8 Ball says..... {answer}')
except Exception as e:
    print('Sorry, something went wrong with the 8 ball. Please try again later.')
    print(f'Error details: {e}')