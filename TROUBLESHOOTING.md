# WAV File Generation Troubleshooting Guide

## Problem: Script and research are generated but WAV file is not created

### Root Causes Identified:

1. **Missing API Key**: The `gemini_voice_tool` requires a valid Gemini API key
2. **Tool Not Being Called**: The agent might not be explicitly instructed to use the voice tool
3. **Audio Data Format Issues**: Gemini might return audio in an unexpected format
4. **Permission Issues**: The script might not have permission to write to the outputs directory
5. **Environment File Issues**: .env file might not be loaded correctly

### Step-by-Step Fixes:

#### 1. Set Up API Key

**Option A: Environment Variables**
```bash
# Set one of these environment variables:
export GEMINI_API_KEY="your_actual_api_key_here"
# OR
export GOOGLE_API_KEY="your_actual_api_key_here"
```

**For Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="your_actual_api_key_here"
# OR
$env:GOOGLE_API_KEY="your_actual_api_key_here"
```

**Option B: .env File (Recommended)**
1. Create a `.env` file in the project root directory
2. Add your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
3. The application will automatically load this file

**Verify .env file is loaded:**
- Look for "✅ .env file loaded successfully" in the logs
- If you see "⚠️ python-dotenv not installed", run: `pip install python-dotenv`

#### 2. Test the Voice Tool Independently
Before running the full crew, test the voice tool:
```bash
cd podcaster_crew
python test_voice_tool.py
```

#### 3. Check the Outputs Directory
Ensure the outputs directory exists and is writable:
```bash
ls -la outputs/
# Should show the directory with write permissions
```

#### 4. Verify Dependencies
Make sure all required packages are installed:
```bash
pip install -e .
# This will install all dependencies including python-dotenv
```

#### 5. Check Logs
The updated tool now includes comprehensive logging. Look for:
- API key validation messages
- .env file loading confirmation
- Gemini client initialization
- Audio generation progress
- WAV file creation confirmation

### Common Error Messages and Solutions:

#### "GEMINI_API_KEY or GOOGLE_API_KEY environment variable not set"
- **Solution**: Set the environment variable or create a .env file
- **Verify**: Run `echo $GEMINI_API_KEY` (Linux/Mac) or `echo $env:GEMINI_API_KEY` (PowerShell)
- **Alternative**: Check if .env file exists and contains the correct API key

#### "python-dotenv not installed"
- **Solution**: Install the package: `pip install python-dotenv`
- **Alternative**: Set environment variables manually

#### "Gemini did not return inline audio data"
- **Cause**: The API response format might have changed
- **Solution**: Check the Gemini API documentation for the latest response format
- **Workaround**: The tool now logs the full response for debugging

#### "Error creating WAV file"
- **Cause**: Permission issues or invalid audio data
- **Solution**: Check directory permissions and ensure audio data is valid PCM

### Debugging Steps:

1. **Run the test script first**:
   ```bash
   python test_voice_tool.py
   ```

2. **Check environment variables**:
   ```bash
   env | grep -i gemini
   env | grep -i google
   ```

3. **Verify .env file**:
   ```bash
   # Check if .env file exists
   ls -la .env
   
   # Check .env file contents (be careful not to expose your key)
   cat .env | grep -v "your_actual_api_key_here"
   ```

4. **Verify the outputs directory**:
   ```bash
   ls -la outputs/
   ```

5. **Check Python path**:
   ```bash
   python -c "import sys; print(sys.path)"
   ```

6. **Test with minimal script**:
   ```python
   from podcaster.tools.custom_tool import gemini_voice_tool
   result = gemini_voice_tool("Hello world")
   print(result)
   ```

### Expected Behavior:

When working correctly, you should see:
1. ✅ .env file loaded successfully
2. ✅ API key found
3. 🎤 Testing voice generation...
4. 📝 Initializing Gemini client...
5. 🔊 Generating audio content...
6. 🔧 Processing response...
7. 📁 Creating WAV file...
8. 🎉 Audio generation successful!

### If Still Not Working:

1. **Check Gemini API Status**: Visit [Google AI Studio](https://aistudio.google.com/) to verify service status
2. **Verify API Quotas**: Ensure you haven't exceeded your API usage limits
3. **Check Network**: Ensure your system can reach Google's servers
4. **Review Logs**: The enhanced logging should provide specific error details
5. **Verify .env File**: Ensure the .env file is in the correct location and format

### Support:

If you continue to have issues:
1. Check the console output for specific error messages
2. Verify your API key is valid and has the necessary permissions
3. Test with a minimal script to isolate the issue
4. Check the Gemini API documentation for any recent changes
5. Ensure the .env file is properly formatted and located in the project root
