The eSpeak command-line interface (CLI) offers a wide range of settings to customize speech synthesis. Here are the most useful and commonly-used options:

### Core Options

- **-h, --help**
  - Display all available options and exit.

- **-v, --voice=**
  - Select a specific voice or language (e.g., 'en', 'en-gb', 'en/f3'). Variants and accents are also supported[1][2].

- **-s, --speed=**
  - Set the speaking speed in words per minute. Range: 80–450 (default: 175)[1][2][3].

- **-p, --pitch=**
  - Adjust the base pitch. Range: 0 (low) to 99 (high), default 50[1][2][3].

- **-a, --amplitude=**
  - Set the amplitude (volume). Range: 0–200, default 100[1][2].

- **-g, --gap=**
  - Pause (in units of 10ms) between words (e.g., 10 = 100ms gap)[1][2][4][5].

- **-f, --file=**
  - Read input text from a specified text file instead of the command line[1][2][4][3].

- **--stdin**
  - Read input text from standard input until EOF[1][2][4].

### Output and Audio Control

- **-w, --wav=**
  - Write synthesized speech to a WAV audio file (instead of playing it)[1][2][3][4].

- **-z, --stdout**
  - Write the synthesized audio to standard output (handy for piping)[1].

- **-d**
  - Specify an audio device for playback[1][2].

- **-q, --quiet**
  - Suppress audio output (useful for phoneme/IPA output only)[1][2].

### Phonetic and Linguistic Features

- **--ipa**
  - Output the phonetic transcription as IPA[1].

- **--pho**
  - Output phonetic transcription in eSpeak’s internal phoneme notation[1].

- **-x**
  - Write phoneme mnemonics to stdout for each word[1][2].

- **-X**
  - Write phoneme mnemonics and translation trace (for debugging)[1][2].

- **-m**
  - Treat input text as SSML (Speech Synthesis Markup Language), supporting some SSML tags for detailed control[1][2].

### Advanced and Miscellaneous

- **-k, --capitals=**
  - Handle capital letters:
    - 1 = speak “capitals”
    - 2 = spell individually
    - Higher values = pitch increase (e.g., -k20)[1][2].

- **-l**
  - Specify language for text processing[1].

- **--voices[=LANG|mb]**
  - List all available voices, optionally filter by language or MBROLA voices[1][3].

- **--version**
  - Show version and voice data location[1][2].

### Usage Tips

- Combine multiple options: For example, `espeak -v en-gb -s 150 -p 60 "Text"` uses a British voice, slows down speed, and raises pitch[3][5].
- Find voices: `espeak --voices` to see all options available[3][1].
- Save to file: Combine `-f` and `-w` to convert text files into WAV audio.

These settings enable detailed customization for a wide range of uses—from screen readers to audio file generation or linguistic analysis[1][2][3].

[1] https://linuxcommandlibrary.com/man/espeak
[2] https://man.archlinux.org/man/espeak-ng.1
[3] https://www.howtogeek.com/have-your-linux-terminal-read-to-you-with-the-espeak-command/
[4] https://www.baeldung.com/linux/command-line-text-to-speech
[5] https://wiki.freepascal.org/espeak
[6] https://espeak.sourceforge.net/commands.html
[7] https://github.com/espeak-ng/espeak-ng
[8] https://wiki.call-cc.org/eggref/5/espeak
[9] https://greenwebpage.com/community/how-to-text-to-speech-output-using-command-line/
[10] https://espeak.sourceforge.net/docindex.html
[11] https://www.youtube.com/watch?v=493xbPIQBSU
[12] https://www.fon.hum.uva.nl/sgc/ManPages/Speech_Synthesis_in_SpeakGoodChinese.html
[13] https://askubuntu.com/questions/468723/how-to-use-espeak-command-in-ubuntu