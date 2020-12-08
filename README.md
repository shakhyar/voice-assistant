<h1>Warning! Unstable release, and still under progress. Donot use without proper documentation</h1>
<h2>Voice Assistant</h2>
<h3>A server client virtual assistant approach.<br>
We need to install dependencies before using it.
<br> I have not provided any requirements.txt because it is still in progress, and is just a prototype. However a sketcy detais of the dependies are:
</h3>
<h4>Python 3.6 (must to have)
<br>
Tensorflow 1.4.0 (must to have, read the "readme" of client_chat_driver to know the reason)
<br>
nltk any version
<br>
numpy any version
<br>
Tflearn any version(all distributions after 2018)
<br>
NVIDIA NeMo(<br>
apt-get install sox libsndfile1 ffmpeg
<br>
pip install wget unidecode
 <br>
BRANCH = 'v1.0.0b2'
  <br>
python -m pip install git+https://github.com/NVIDIA/NeMo.git@$v1.0.0b2#egg=nemo_toolkit[tts]
<br>
)
<br>
Pytorch(server only)
</h4>
