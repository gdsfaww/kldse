# YouTube Video Transcriber

This repository now includes a simple script to transcribe audio from a YouTube video using [pytube](https://github.com/pytube/pytube) and [OpenAI's Whisper](https://github.com/openai/whisper).

## Requirements

Install the required packages:

```bash
pip install pytube whisper
```

## Usage

Run the script and provide a YouTube URL:

```bash
python scripts/youtube_transcriber.py "https://www.youtube.com/watch?v=<video_id>" -o output.txt
```

The transcription will be printed to the console unless `-o` is given to save it to a file.
