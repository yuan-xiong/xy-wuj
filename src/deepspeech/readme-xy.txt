#!/bin/bash

# https://deepspeech.readthedocs.io/en/r0.9/?badge=latest
	apt install -y vim wget curl git

# docker
	docker pull ubuntu:18.04
	docker run -dit -v /home/xy18/yuan:/home/xy18/yuan ubuntu:18.04 /bin/bash

# python3
	apt update
	apt install -y python3.6 python3-pip
	python3.6 -m pip install --upgrade pip

# deepspeech
	# binary
		# deepspeech-0.9.3 numpy-1.19.5
		python3.6 -m pip install deepspeech
		python3.6 -m pip install --upgrade deepspeech
	# source
		git clone https://github.com/mozilla/DeepSpeech.git

	# models
		wget -c https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
		wget -c https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

	# audio
		wget -c https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/audio-0.9.3.tar.gz

	# run
		#deepspeech --model deepspeech-0.9.3-models.pbmm --scorer deepspeech-0.9.3-models.scorer --audio audio/2830-3980-0043.wav
		deepspeech --model models/deepspeech-0.9.3-models.pbmm --scorer models/deepspeech-0.9.3-models.scorer --audio data/audio/2830-3980-0043.wav

	# autosub
		#https://github.com/mozilla/DeepSpeech-examples/tree/r0.9/autosub
		git clone https://github.com/abhirooptalasila/AutoSub
		python3.6 -m pip install -r requirements.txt

		# ffmpeg
		sudo apt-get install -y ffmpeg
		python3.6 -m pip install deepspeech-gpu
		python3 autosub/main.py --model /home/AutoSub/deepspeech-0.9.3-models.pbmm --scorer /home/AutoSub/deepspeech-0.9.3-models.scorer --file ~/movie.mp4

