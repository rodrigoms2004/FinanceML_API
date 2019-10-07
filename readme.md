# Python Sentiment Analysis API

This application provides sentiment analysis to the Midterm app from Siraj Raval course.

[Midterm](https://github.com/rodrigoms2004/FinanceMidTermSiraj2019)


### Requirements


Install textblob and flask

```
pip install Flask textblob
```

### Running

Command line

```
python src/app.py
```

### Running in background


Use nohup 
```
nohup python src/app.py > output.log &
```


Check logs
```
tail -f output.log 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [07/Oct/2019 12:19:12] "POST /api/sentiment HTTP/1.1" 200 -
127.0.0.1 - - [07/Oct/2019 12:19:14] "POST /api/sentiment HTTP/1.1" 200 -
```

Killing process *kill PID*
```
ps ax | grep app.py
27036 pts/24   S      0:01 python src/app.py
27154 pts/24   S+     0:00 grep --color=auto app.py

kill 27036
```

### Heroku commands


* login in Heroku
```
$ heroku login
```

* Define heroku repo
```
$ heroku git:remote -a YOUR_HEROKU_APP_NAME_HERE
```

* Deploy the app
```
$ git push heroku master
```

#### More commands

Create a *dyno* runinng (Linux Container)
```
$ heroku ps:scale web=1
```

Check app logs
```
$ heroku logs --tail
```

## Useful links

[Python in Background](https://janakiev.com/blog/python-background/)

[How to Install Python 3.6.1 in Ubuntu 16.04 LTS](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/)

[How to install Pip3 & Django on Ubuntu 18.04 / Ubuntu 16.04 LTS](https://computingforgeeks.com/how-to-install-pip3-django-on-ubuntu-18-04-ubuntu-16-04-lts/)


[pip install - locale.Error: unsupported locale setting](https://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting)

[Install Flask and create your first web application](https://dev.to/sahilrajput/install-flask-and-create-your-first-web-application-2dba)

[Heroku Deploy PORTUGUESE CONTENT](https://jtemporal.com/deploy-flask-heroku/)

[Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

[Heroku dashboard](https://dashboard.heroku.com)


## Authors

* **Rodrigo Moraes Silveira**
*Git hub* - (https://github.com/rodrigoms2004)
*E-mail*  - rodrigoms2004@gmail.com
*Discord* - rodrigo.silveira#4776

* **Marco Alessandro de Campos**
*Git hub* - (https://github.com/titocampos)
*E-mail*  - titocampos@gmail.com
*Discord* - titocampos

* **Craig Austin**
*Git hub* - (https://github.com/WannaBreakout)
*E-mail*  - craig07may@gmail.com
*Discord* - cabin

* **Stefan Fricke**
*Git hub* - (https://github.com/Stefan566)
*E-mail*  - 
*Discord* - Stefan999


 