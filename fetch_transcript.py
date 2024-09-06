from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(video_id, languages=['en', 'de']):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def main():
    video_id = 'n7Spn1KUC38'  # Example video ID
    transcript = fetch_transcript(video_id)
    if transcript:
        for entry in transcript:
            print(f"{entry['start']:.2f} - {entry['start'] + entry['duration']:.2f}: {entry['text']}")

if __name__ == '__main__':
    main()
