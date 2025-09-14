# Content Creator Crew

A CrewAI-powered educational content generation system that researches topics, creates scripts, and generates audio using Google's Gemini AI.

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Clone and navigate to the project
cd content_creator_crew

# Set up your Gemini API key
export GEMINI_API_KEY="your_api_key_here"
# OR for Windows PowerShell:
# $env:GEMINI_API_KEY="your_api_key_here"

# Install dependencies
pip install -e .
```

### 2. Verify Setup
```bash
# Check your environment
python setup_env.py

# Test the voice tool independently
python test_voice_tool.py
```

### 3. Run the Crew
```bash
# Generate educational content about AI LLMs
python -m content_creator.main
```

## 🔧 Troubleshooting WAV File Generation

### Common Issues:

1. **Missing API Key**
   - Error: "GEMINI_API_KEY or GOOGLE_API_KEY environment variable not set"
   - Solution: Set the environment variable as shown above

2. **Dependencies Missing**
   - Error: Import errors for google.genai or wave
   - Solution: Run `pip install -e .` to install all dependencies

3. **Permission Issues**
   - Error: Cannot write to outputs directory
   - Solution: Ensure the outputs directory is writable

4. **Audio Generation Fails**
   - Error: "Gemini did not return inline audio data"
   - Solution: Check your API key validity and quotas

### Debug Steps:

1. **Run the environment check**:
   ```bash
   python setup_env.py
   ```

2. **Test voice tool independently**:
   ```bash
   python test_voice_tool.py
   ```

3. **Check logs**: The enhanced tool now includes comprehensive logging

4. **Verify API key**: Ensure your Gemini API key is valid and has TTS permissions

## 📁 Project Structure

```
content_creator_crew/
├── src/content_creator/
│   ├── main.py              # Main execution script
│   ├── crew.py              # CrewAI crew definition
│   ├── tools/
│   │   └── custom_tool.py   # Voice generation tool
│   └── config/
│       ├── agents.yaml      # Agent configurations
│       └── tasks.yaml       # Task definitions
├── outputs/                 # Generated files (scripts, reports, audio)
├── test_voice_tool.py      # Independent voice tool test
├── setup_env.py            # Environment verification script
└── TROUBLESHOOTING.md      # Detailed troubleshooting guide
```

## 🎯 How It Works

1. **Research Agent**: Gathers information about the specified topic
2. **Reporting Agent**: Creates a detailed report from the research
3. **Scriptwriter Agent**: Writes an educational content script and generates audio using Gemini TTS
4. **Output**: Script, report, and WAV audio file in the outputs directory

## 📋 Requirements

- Python 3.10-3.13
- Valid Gemini API key with TTS permissions
- Internet connection for API calls
- Write permissions for the outputs directory

## 🆘 Getting Help

1. **Check the troubleshooting guide**: `TROUBLESHOOTING.md`
2. **Run environment checks**: `python setup_env.py`
3. **Test voice tool**: `python test_voice_tool.py`
4. **Review logs**: The tool now includes detailed logging for debugging

## 🔑 API Key Setup

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Set the environment variable:
   ```bash
   export GEMINI_API_KEY="your_key_here"
   ```
4. Verify with: `echo $GEMINI_API_KEY`

## 📝 Expected Outputs

When successful, you should see:
- `report-YYYYMMDD-HHMMSS.md` - Research report
- `script-YYYYMMDD-HHMMSS.md` - Content script
- `content-YYYYMMDD-HHMMSS.wav` - Audio file

## 🐛 Known Issues

- The voice tool requires a valid Gemini API key
- Audio generation depends on Gemini's TTS service availability
- Large scripts may take longer to process
- Ensure your API key has sufficient quotas for TTS usage
