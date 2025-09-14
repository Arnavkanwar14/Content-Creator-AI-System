# 🎙️ Educational Content Creator Bot

This content creator crew creates engaging educational conversations and generates audio using your Gemini Pro API key!

## 🚀 Quick Start

### 1. Setup (Same as before)
```bash
# Set up your Gemini API key
export GEMINI_API_KEY="your_api_key_here"
# OR for Windows PowerShell:
# $env:GEMINI_API_KEY="your_api_key_here"

# Install dependencies
pip install -e .
```

### 2. Test Audio Generation
```bash
# Test audio generation tool
python test_voice_tool.py
```

### 3. Run Content Generation
```bash
# Generate content with specific topic
python run_content_creator.py "Why the Sky is Blue"

# Or use the original method
python -m content_creator.main "How Photosynthesis Works"
```

## 🎙️ What You Get

The bot now generates **3 outputs**:

1. **Research Report** - Detailed research about your topic
2. **Content Script** - Conversation between Mike and Sara
3. **Audio File** - Two-voice narration (.wav)

## 📁 Output Files

- `report-YYYYMMDD-HHMMSS.md` - Research findings
- `script-YYYYMMDD-HHMMSS.md` - Conversation script
- `content-YYYYMMDD-HHMMSS.wav` - Audio narration

## 🔧 How It Works

### Content Generation Process:
1. **Research** - Gathers information about your topic
2. **Report** - Organizes findings into a comprehensive report
3. **Script** - Creates engaging conversation between Mike and Sara
4. **Audio** - Generates two-voice narration using Gemini TTS

## 🎯 Perfect For

- **Educational content** that feels like chatting with friends
- **Audio content** for learning platforms
- **Conversational learning** that doesn't feel like a lecture
- **Two-voice narration** for engaging explanations

## 💡 Usage Examples

```bash
# Science topics
python run_content_creator.py "Why the Sky is Blue"
python run_content_creator.py "How Photosynthesis Works"
python run_content_creator.py "Why Ice Floats on Water"

# Technology topics
python run_content_creator.py "How GPS Works"
python run_content_creator.py "How WiFi Works"
python run_content_creator.py "How Solar Panels Work"

# Nature topics
python run_content_creator.py "Why We Get Goosebumps"
python run_content_creator.py "Why Leaves Change Color"
python run_content_creator.py "How Bees Make Honey"
```

## 🔧 Troubleshooting

### Common Issues:

1. **Audio Generation Issues**
   - Check that your GEMINI_API_KEY is set correctly
   - Ensure your API key has text-to-speech permissions

2. **Import Errors**
   - Run `pip install -e .` to install all dependencies
   - Check that you're using Python 3.10-3.13

3. **API Key Issues**
   - Ensure GEMINI_API_KEY is set correctly
   - Check that your API key has the necessary permissions

### Debug Steps:

1. **Test the setup**:
   ```bash
   python test_voice_tool.py
   ```

2. **Check API key**:
   ```bash
   echo $GEMINI_API_KEY  # Linux/Mac
   echo $env:GEMINI_API_KEY  # Windows PowerShell
   ```

3. **Test individual tools**:
   ```python
   from content_creator.tools.custom_tool import gemini_voice_tool
   result = gemini_voice_tool("Test script")
   print(result)
   ```

## 🎨 Audio Customization

### Script Format:
The bot creates natural conversations between:
- **Mike** - Curious friend asking questions
- **Sara** - Knowledgeable friend explaining with examples

### Audio Specifications:
- **Duration**: Under 60 seconds (strictly enforced)
- **Quality**: High
- **Style**: Natural, conversational, engaging
- **Format**: Short, focused on 3-4 key points maximum

## 🌟 Advanced Usage

### Custom Topics:
```python
from content_creator.main import run_with_topic
run_with_topic("Your Custom Topic Here")
```

## 📊 Expected Results

When successful, you should see:
- ✅ Research report generated
- ✅ Conversation script created
- ✅ Audio file with two voices

## 🆘 Getting Help

1. **Run the test script**: `python test_voice_tool.py`
2. **Check the troubleshooting guide** above
3. **Review the logs** for detailed error messages
4. **Verify your API key** has text-to-speech permissions

## 🎉 Ready to Create!

Your educational content creator bot is now ready to create engaging, educational content with audio generation! 

Run `python run_content_creator.py` and start creating amazing educational content! 🚀

