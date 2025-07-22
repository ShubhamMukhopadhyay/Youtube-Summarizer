import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi import FastAPI

app=FastAPI()

# ✅ Replace with your actual API key
GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API"

# 🔧 Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


def extract_youtube_id(url):
    if "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")
    

# 🎥 Set your video ID
VIDEO_ID = extract_youtube_id(url="https://www.youtube.com/watch?v=R8OZY3isCLs") # type: ignore


def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        print("❌ Transcript fetch error:", e)
        return None

def summarize_with_gemini(transcript_text):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    prompt = f"""
Summarize the following transcript in the format:

{{
  "topic_name": "Name of the topic",
  "topic_summary": "Short summary"
}}

Transcript:
{transcript_text}
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Gemini error:", e)
        return None
    
@app.get("/summarize")
def get_summary(url:str):
    video_id=extract_youtube_id(url)
    transcript=fetch_transcript(video_id)

    if transcript:
        summary = summarize_with_gemini(transcript)
        return {"summary":summary}

    else:
        return{"error": "Transcript not found"}


if __name__ == "__main__":
    transcript = fetch_transcript(VIDEO_ID)
    if transcript:
        result = summarize_with_gemini(transcript)
        if result:
            print("\n✅ Final Output JSON:\n")
            print(result)
