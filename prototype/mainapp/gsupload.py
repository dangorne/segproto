import os, sys, getopt
import django

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'prototype.settings'
django.setup()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + '/mainapp/speech-af1080e33239.json'

from mainapp.models import UploadForm, Upload

def upload_blob(bucket_name, source, target_name):

    from google.cloud import storage
    # storage_client = storage.Client.from_service_account_json(os.getcwd() + '/mainapp/speech-af1080e33239.json')
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(target_name)
    blob.upload_from_filename(source)

    print('File {} uploaded to {}.'.format(
        source,
        target_name))

    #uncomment to speech recognize
    transcribe_gcs("gs://segbuck/" + target_name)

def transcribe_gcs(gcs_uri):

    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    from google.auth.credentials import Credentials

    speech_client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        enable_word_time_offsets = True,
        language_code='en-US')

    operation = speech_client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result()
    print('Operation completed...')

    for result in response.results:
        # The first alternative is the most likely one for this portion.
        with open(os.getcwd() + '/temp/transcript.txt', 'w', encoding='utf-8') as file:
            file.write(format(result.alternatives[0].transcript))

    print('written')

def main(argv):

    try:
        opts, args = getopt.getopt(argv, "k:", ["key"])

    except getopt.GetoptError:
        print('input error')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-k", "--key"):
            pk = arg

    print("uploading...")

    upload_blob('segbuck', os.getcwd() + '/media/' + str(Upload.objects.get(pk=int(pk)).file), pk)
    # transcribe_gcs("gs://segbuck/55")

if __name__ == "__main__":
    main(sys.argv[1:])

# ffmpeg -i in.mp4 out.flac
# ffmpeg -i input.mp3 -ss 10 -t 6 -acodec copy output.mp3
# ffmpeg -i input.mp3 -ss 00:02:54.583 -acodec copy output.mp3
# ffmpeg -ss 10 -to 16 -i input.mp3 output.mp3
