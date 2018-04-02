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

## Database Configuration

Open prototype\prototype\settings.py and set your database parameters

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prototype',
        'USER': '<USER_USER>',
        'PASSWORD': '<USER_PASS>',
        'HOST': '<USER_HOST>',
        'PORT': '<USER_PORT>',
    }
}
```

## Running the Server

Activate Virtual Environment

```
virtualenv -p <python 3.5 32-bit exe file path> env
.\env\Scripts\activate
```
Install packages
```
pip install -r requirements.txt 
```
Build database and run the server
```
cd prototype
python manage.py migrate
python manage.py runserver
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
