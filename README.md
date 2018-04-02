# Prototype Segmenter and Labeler


## Requirements

```
Python 3.5 32-bit
pip
virtualenv
```

## Features

* Basic file upload.
* File upload to Google Cloud Storage
* Asynchronous Speech Recognition by Google Speech API (output will be located in /temp/transcript.txt)

## Notes

Make sure to upload .flac files.

## Running the Server

Open command prompt and run:

```
>virtualenv -p <python 3.5 32-bit exe file path> env
>.\env\Scripts\activate
>pip install -r requirements.txt 
>cd prototype
\prototype>python manage.py migrate
\prototype>python manage.py runserver
```
## Setup

Open command prompt and run:

```
>virtualenv -p <python 3.5 32-bit exe file path> env
>.\env\Scripts\activate
>pip install -r requirements.txt 
>cd prototype
\prototype>python manage.py migrate
\prototype>python manage.py runserver
```



## Database Configuration

Open prototype\prototype\settings.py and set you database ROOT, PASSWORD, HOST and PORT

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prototype',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

