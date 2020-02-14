# Speech generation from text file 

---

**Synthesizing text with Google Cloud Text-to-Speech API**

In this Python project the [Google Cloud Text-to-Speech API](https://cloud.google.com/text-to-speech) is used to synthesize text from a text file. The Google Cloud Text-to-Speech API uses DeepMind's deep neural network [WaveNet](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio) to synthesize text.

Link to a video with a voice-over generated from a textfile and the resources of this project: https://www.youtube.com/watch?v=HLywAP-tRTU&t=1s
For more examples, see folder 'audio_files' (related text file in folder 'text_files').

---
### Files inculded

My project includes the following files:
* <code>tts_main_gh.py</code> - main script
* <code>text_synthesizer.py</code> - class for text synthesizer

### Requirements

Python-Version: 3.7.2

Packeges:
* Google Cloud          - google.cloud

### Usage

1. Set location for your [Google credentials](https://cloud.google.com/docs/authentication/getting-started) JSON-file in <code>tts_main_gh.py</code> (line 21)
2. Set parameters in <code>tts_main_gh.py</code> (line 4 to 18)
3. Run <code>tts_main_gh.py</code>



