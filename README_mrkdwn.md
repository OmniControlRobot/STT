[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/woomurf/STT)

You can test on open api or web site demo.

[Demo](https://master-stt-woomurf.endpoint.ainize.ai/)


Mozilla Voice STT
---

[![Documentation](https://readthedocs.org/projects/deepspeech/badge/?version=latest)](http://mozilla-voice-stt.readthedocs.io/?badge=latest) [![Task Status](https://community-tc.services.mozilla.com/api/github/v1/repository/mozilla/STT/master/badge.svg)](https://community-tc.services.mozilla.com/api/github/v1/repository/mozilla/STT/master/latest) 

Mozilla Voice STT is an open source Speech-To-Text engine, using a model trained by machine learning techniques based on [Baidu's Deep Speech research paper](https://arxiv.org/abs/1412.5567). 

Mozilla Voice STT uses Google's [TensorFlow](https://www.tensorflow.org/) to make the implementation easier.

Documentation for installation, usage, and training models are available on [mozilla-voice-stt.readthedocs.io](http://mozilla-voice-stt.readthedocs.io/?badge=latest>).

For the latest release, including pre-trained models and checkpoints, [see the latest release on GitHub](https://github.com/mozilla/DeepSpeech/releases/latest).

For contribution guidelines, see [CONTRIBUTING.rst](https://github.com/mozilla/DeepSpeech/blob/master/CONTRIBUTING.rst).

For contact and support information, see [SUPPORT.rst](https://github.com/mozilla/DeepSpeech/blob/master/SUPPORT.rst).

### Docker build & Run

You can try running STT API server using docker. 

`docker build -t stt . `

`docker run ${HostPort}:80 --gpus all stt` 
