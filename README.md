# Multi-Provider Chatbot

This is a Python chatbot that can use OpenAI, Perplexity AI, or Gemini (Google) APIs to generate responses. It automatically tries each provider in order and returns the first successful response.

## Features

- Supports OpenAI (GPT-3.5), Perplexity AI, and Gemini (Gemini 1.5 Flash)
- Automatically falls back to the next provider if one fails
- API keys are securely loaded from a `.env` file

## Setup

1. **Clone the repository** (if not already):

   ```sh
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

   Or manually:

   ```sh
   pip install openai google-generativeai python-dotenv requests
   ```

3. **Create a `.env` file** in the project root with your API keys:

   ```env
   PERPLEXITY_API_KEY=your_perplexity_api_key
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. **Run the chatbot:**
   ```sh
   python chatbot.py
   ```

## Usage

- Type your prompt and press Enter.
- To exit, type `quit`, `exit`, or `bye`.

## Security

- The `.env` file is included in `.gitignore` and will not be tracked by git.
- **Never share your API keys publicly.**

## Requirements

- Python 3.8+
- Internet connection

## License

MIT
