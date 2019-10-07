# Python Sentiment Analysis API

### Requirements


Install textblob and flask

```
pip install Flask TextBlob
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

## Useful links

[Python in Background](https://janakiev.com/blog/python-background/)

[How to Install Python 3.6.1 in Ubuntu 16.04 LTS](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/)

[How to install Pip3 & Django on Ubuntu 18.04 / Ubuntu 16.04 LTS](https://computingforgeeks.com/how-to-install-pip3-django-on-ubuntu-18-04-ubuntu-16-04-lts/)


[pip install - locale.Error: unsupported locale setting](https://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting)

[Install Flask and create your first web application](https://dev.to/sahilrajput/install-flask-and-create-your-first-web-application-2dba)




sudo apt-get install python3.6-gdbm



sudo apt-get install python3-pip

 locale
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
LANG=en_US.UTF-8
LANGUAGE=
LC_CTYPE=pt_BR.UTF-8
LC_NUMERIC=pt_BR.UTF-8
LC_TIME=pt_BR.UTF-8
LC_COLLATE="en_US.UTF-8"
LC_MONETARY=pt_BR.UTF-8
LC_MESSAGES="en_US.UTF-8"
LC_PAPER=pt_BR.UTF-8
LC_NAME=pt_BR.UTF-8
LC_ADDRESS=pt_BR.UTF-8
LC_TELEPHONE=pt_BR.UTF-8
LC_MEASUREMENT=pt_BR.UTF-8
LC_IDENTIFICATION=pt_BR.UTF-8
LC_ALL=


$ export LC_ALL=C
$ locale
LANG=en_US.UTF-8
LANGUAGE=
LC_CTYPE="C"
LC_NUMERIC="C"
LC_TIME="C"
LC_COLLATE="C"
LC_MONETARY="C"
LC_MESSAGES="C"
LC_PAPER="C"
LC_NAME="C"
LC_ADDRESS="C"
LC_TELEPHONE="C"
LC_MEASUREMENT="C"
LC_IDENTIFICATION="C"
LC_ALL=C
