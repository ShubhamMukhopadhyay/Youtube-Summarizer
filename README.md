# YouTube Video Summarizer with Gemini AI
This project provides a simple FastAPI application to summarize YouTube video transcripts using Google's Gemini 1.5 Flash generative AI model. It extracts video transcripts and then uses Gemini to provide a concise summary in a structured JSON format.

Features: 
Extracts transcripts from YouTube videos using the youtube_transcript_api library.

Utilizes Google's Gemini 1.5 Flash model for generating summaries.

Exposes a /summarize endpoint via FastAPI to easily get summaries by providing a YouTube URL.

Prerequisites :
Before you begin, ensure you have the following installed:

Python 3.8+

Google Gemini API Key: You'll need to obtain an API key from Google AI Studio.

uvicorn: For running the FastAPI application.

Installation:
Clone the repository:

Bash

    git clone <your-repository-url>
    cd <your-repository-name>
    Create a virtual environment (recommended):

Bash

    python -m venv venv
    On Windows:

Bash

    .\venv\Scripts\activate
    On macOS/Linux:

Bash
    
    source venv/bin/activate
    Install the required packages:

Bash

    pip install -r requirements.txt
    (If you don't have a requirements.txt yet, create one with the following content and then run pip install -r requirements.txt):
    requirements.txt content:

google-generativeai
youtube-transcript-api
fastapi
uvicorn
Configuration
Get your Gemini API Key:

Go to Google AI Studio.

Create a new API key.

Update GEMINI_API_KEY in the code:
Open the main.py (or whatever you named your Python file) and replace "AIzaSyDqLhg9XbdAJlGA4N8Z6Yrb00j7yr9W64M" with your actual Gemini API Key:

Python

# main.py
GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
Note on extract_youtube_id:
Your current extract_youtube_id function has specific logic for youtube.com/watch?v= and youtu.be/. If your YouTube URLs are in the standard format (e.g., https://www.youtube.com/watch?v=VIDEO_ID or https://youtu.be/VIDEO_ID), you might need to adjust this function. For the FastAPI endpoint, you will pass the full URL directly.

The hardcoded VIDEO_ID variable in the if __name__ == "__main__": block is for direct script execution testing. When running with FastAPI/Uvicorn, the get_summary endpoint handles the URL dynamically.

How to Run
This program has two ways to run:

1. Running as a Standalone Script (for testing fetch_transcript and summarize_with_gemini)
You can run the script directly from your command prompt to test the summary generation for a specific hardcoded video ID (as defined by VIDEO_ID in the if __name__ == "__main__": block).

Open your Command Prompt (Windows) or Terminal (macOS/Linux).

Navigate to your project directory:

Bash

        cd path/to/your/project
        Activate your virtual environment (if you created one):
        
        On Windows: .\venv\Scripts\activate
        
        On macOS/Linux: source venv/bin/activate

Run the Python script:

Bash

        python main.py
        (Replace main.py with the actual name of your Python file).

This will execute the code within the if __name__ == "__main__": block, fetch the transcript for the hardcoded VIDEO_ID, and print the summary to your console.

2. Hosting the API with FastAPI and Uvicorn (for accessing via Postman/Browser)
This is how you run the web service to provide the summary functionality via an API endpoint.

Open your Command Prompt (Windows) or Terminal (macOS/Linux).

Navigate to your project directory:

Bash

        cd path/to/your/project
        Activate your virtual environment:
        
        On Windows: .\venv\Scripts\activate
        
        On macOS/Linux: source venv/bin/activate

Start the Uvicorn server:

Bash

        uvicorn main:app --reload
        (Replace main with the name of your Python file without .py extension).

main:app means "look for the app object in main.py".

--reload is useful during development, as it automatically reloads the server when you make code changes.

You will see output indicating that the FastAPI application is running, typically on http://127.0.0.1:8000.

How to Use the API (with Postman)
Once the Uvicorn server is running, you can interact with your API using a tool like Postman, Insomnia, or even your web browser.

Using Postman:
Open Postman.

Create a new Request.

Set the HTTP Method: Choose GET.

Enter the Request URL:

        http://127.0.0.1:8000/summarize?url=YOUR_YOUTUBE_URL
Example:
If you want to summarize a video with the URL https://www.youtube.com/watch?v=dQw4w9WgXcQ, your Postman URL would be:

http://127.0.0.1:8000/summarize?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
Note: Ensure the url parameter in your request is correctly URL-encoded if it contains special characters, though standard YouTube URLs usually don't require much encoding beyond what Postman handles automatically.

Send the Request: Click the "Send" button.

Expected Response:
The API will return a JSON object containing the summary of the video transcript:

JSON

{
  "summary": "{\n  \"topic_name\": \"[Name of the main topic in the video]\",\n  \"topic_summary\": \"[A short, concise summary of the video's content]\"\n}"
}
Note: The summary value is a string containing another JSON-formatted string, as per your summarize_with_gemini function's prompt. You might want to parse this inner JSON in your client application.
