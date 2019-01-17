[![CircleCI](https://circleci.com/gh/chiksumwong/news_analysis_chatbot.svg?style=svg)](https://circleci.com/gh/chiksumwong/news_analysis_chatbot)
# news-analysis-chatbot
News Analysis Chatbot

# Database
$ python manage.py migrate

# Create Admin
$ python manage.py createsuperuser --email admin@example.com --username admin
(password: admin)

# Start Server:
$ python manage.py runserver

# url
## Chatbot
[POST] http://127.0.0.1:8000/chatbot/webhook/

## News
[GET] http://127.0.0.1:8000/api/news/
[POST] http://127.0.0.1:8000/api/news/