import tempfile
from typing import Optional
import argparse
from pytube import YouTube
import whisper


def download_audio(url: str, output_path: str) -> str:
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    if stream is None:
        raise RuntimeError("No audio stream found for given URL")
    downloaded_file = stream.download(output_path=output_path)
    return downloaded_file


def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    return result.get("text", "")


def main(url: str, model_size: str = "base", output: Optional[str] = None) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_file = download_audio(url, tmpdir)
        text = transcribe_audio(audio_file, model_size)
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(text)
        else:
            print(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe a YouTube video using OpenAI's Whisper")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-m", "--model", default="base", help="Whisper model size (tiny, base, small, medium, large)")
    parser.add_argument("-o", "--output", help="Path to save the transcription")

    args = parser.parse_args()
    main(args.url, args.model, args.output)

