import argparse
import numpy as np
import shlex
import subprocess
import sys
import wave
import json

import deepspeech as stt

from pipes import quote

def convert_samplerate(audio_path, desired_sample_rate):
    sox_cmd = 'sox {} --type raw --bits 16 --channels 1 --rate {} --encoding signed-integer --endian little --compression 0.0 --no-dither - '.format(quote(audio_path), desired_sample_rate)
    try:
        output = subprocess.check_output(shlex.split(sox_cmd), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError('SoX returned non-zero status: {}'.format(e.stderr))
    except OSError as e:
        raise OSError(e.errno, 'SoX not found, use {}hz files or install it: {}'.format(desired_sample_rate, e.strerror))

    return desired_sample_rate, np.frombuffer(output, np.int16)

# ds == model
def speechToText(ds, input_audio):

    desired_sample_rate = ds.sampleRate()
    try:
        fin = wave.open(input_audio, 'rb')
    except:
        return {'msg':'Please input wav file'}
    fs_orig = fin.getframerate()

    
    if fs_orig != desired_sample_rate:
        print('Warning: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(fs_orig, desired_sample_rate), file=sys.stderr)
        fs_new, audio = convert_samplerate(input_audio, desired_sample_rate)
    
        print("converted sample rate")
    else:
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    audio_length = fin.getnframes() * (1/fs_orig)
    fin.close()

    result = ds.stt(audio)
    print("stt done")
    return result