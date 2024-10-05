import logging
import os
import re
import sys
from unidecode import unidecode
from yt_dlp import YoutubeDL
import whisper
import torch


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("transcriber.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def parameterize_filename(filename):
    """I miss you Ruby parameterize

    Ensures file names are OS safe.
    """

    ascii_filename = unidecode(filename)
    
    # Step 2: Replace spaces with dashes
    ascii_filename = ascii_filename.replace(" ", "-")
    
    # Step 3: Remove all non-alphanumeric characters except dashes and underscores
    sanitized = re.sub(r'[^a-zA-Z0-9\-_]', '', ascii_filename)
    
    return sanitized

def get_device():
    if torch.backends.mps.is_available():
        device = "mps"
        logging.info("MPS device detected. Using GPU (MPS).")
    elif torch.cuda.is_available():
        device = "cuda"
        logging.info("CUDA device detected. Using GPU (CUDA).")
    else:
        device = "cpu"
        logging.info("No GPU detected. Using CPU.")
    return device


def download_youtube_video(url, output_path='downloads'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(id)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            video_id = info_dict.get('id', None)
            ext = 'mp3'

            # Construct paths: original and final
            temp_filename = f"{video_id}.{ext}"
            temp_file = os.path.join(output_path, temp_filename)

            # Sanitize the title and create the final filename
            sanitized_title = parameterize_filename(title)
            final_filename = f"{sanitized_title}.{ext}"
            final_file = os.path.join(output_path, final_filename)

            # Rename the temporary file to the final filename
            os.rename(temp_file, final_file)

            logging.info(f"Audio downloaded and converted to: {final_file}")
            return final_file
    except Exception as e:
        logging.error(f"Error downloading video: {e}")
        sys.exit(1)


def transcribe_audio(audio_path, device, model_size="base"):
    try:
        logging.info(f"Loading Whisper model ({model_size})...")
        model = whisper.load_model(model_size).to(device)
        logging.info(f"Transcribing audio: {audio_path} on device: {device}")
        result = model.transcribe(audio_path, fp16=(device != "cpu"))
        transcription = result['text']
        return transcription
    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
        sys.exit(1)


def save_transcription(transcription, audio_path, output_path='transcriptions'):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        base = os.path.splitext(os.path.basename(audio_path))[0]
        txt_file = os.path.join(output_path, f"{base}.txt")
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(transcription)
        logging.info(f"Transcription saved to: {txt_file}")
    except Exception as e:
        logging.error(f"Error saving transcription: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        logging.error("Usage: python main.py <YouTube_URL>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    device = get_device()
    audio_path = download_youtube_video(youtube_url)
    transcription = transcribe_audio(audio_path, device)
    save_transcription(transcription, audio_path)


if __name__ == "__main__":
    main()
