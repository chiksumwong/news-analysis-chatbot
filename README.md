[![CircleCI](https://circleci.com/gh/chiksumwong/news_analysis_chatbot.svg?style=svg)](https://circleci.com/gh/chiksumwong/news_analysis_chatbot)
# News Analysis Chatbot

## Start the local mongodb
```sh
$ "C:\Program Files\MongoDB\Server\4.0\bin\mongod.exe" --dbpath="c:\data\db"
```

## Start Server
```sh
$ python manage.py runserver
```

## URL
### Chatbot
| Method | Urls                                   |
| ------ | -------------------------------------- |
| POST   | http://127.0.0.1:8000/chatbot/webhook/ |

### News
| Method | Urls                                      |
| ------ | ----------------------------------------- |
| GET    | http://127.0.0.1:8000/api/news/           |
| POST   | http://127.0.0.1:8000/api/news/           |
| POST   | http://127.0.0.1:8000/api/info/           |
| POST   | http://127.0.0.1:8000/api/checknews/      |
| POST   | http://127.0.0.1:8000/api/checknewsbyurl/ |


## Model training
```sh
$ python model_training/TrainModel.py

```

## Model testing
```sh
$ python model_training/TestModel.py

```

## Release python environment
```sh
$ pip freeze > requirements.txt
```