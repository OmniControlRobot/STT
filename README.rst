.. image:: https://ainize.ai/images/run_on_ainize_button.svg 
   :target: https://ainize.web.app/redirect?git_repo=https://github.com/woomurf/STT
   :alt: Run on Ainize


`Demo <https://master-stt-woomurf.endpoint.ainize.ai/>`_


Project DeepSpeech
==================


.. image:: https://readthedocs.org/projects/deepspeech/badge/?version=latest
   :target: https://deepspeech.readthedocs.io/?badge=latest
   :alt: Documentation


.. image:: https://community-tc.services.mozilla.com/api/github/v1/repository/mozilla/DeepSpeech/master/badge.svg
   :target: https://community-tc.services.mozilla.com/api/github/v1/repository/mozilla/DeepSpeech/master/latest
   :alt: Task Status


DeepSpeech is an open-source Speech-To-Text engine, using a model trained by machine learning techniques based on `Baidu's Deep Speech research paper <https://arxiv.org/abs/1412.5567>`_. Project DeepSpeech uses Google's `TensorFlow <https://www.tensorflow.org/>`_ to make the implementation easier.

Documentation for installation, usage, and training models are available on `deepspeech.readthedocs.io <https://deepspeech.readthedocs.io/?badge=latest>`_.

For the latest release, including pre-trained models and checkpoints, `see the latest release on GitHub <https://github.com/mozilla/DeepSpeech/releases/latest>`_.

For contribution guidelines, see `CONTRIBUTING.rst <CONTRIBUTING.rst>`_.

For contact and support information, see `SUPPORT.rst <SUPPORT.rst>`_.

Docker build and Run 
--------------------

You can try running STT API server using docker. 

.. code::

   docker build -t stt .

.. code::

   docker run -p ${HostPort}:80 --gpus all stt 
