#!/usr/bin/env python3
"""
Test script for the gemini_voice_tool to verify it works independently.
Run this manually to test if the voice generation is working before running the full crew.
"""

import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Try to load .env file first
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ .env file loaded (if it exists)")
except ImportError:
    print("⚠️ python-dotenv not installed, .env file won't be loaded")
except Exception as e:
    print(f"⚠️ Could not load .env file: {e}")

from content_creator.tools.custom_tool import gemini_voice_tool

def test_voice_tool():
    """Test the voice tool with a simple script"""
    
    # Check if API key is set
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY or GOOGLE_API_KEY environment variable not set!")
        print("Please set one of these environment variables:")
        print("  export GEMINI_API_KEY='your_api_key_here'")
        print("  export GOOGLE_API_KEY='your_api_key_here'")
        print("\nOr create a .env file in the project root with:")
        print("  GEMINI_API_KEY=your_api_key_here")
        print("  GOOGLE_API_KEY=your_api_key_here")
        return False
    
    print("✅ API key found")
    
    # Test script
    test_script = """
    Mike: Welcome to our podcast about AI and technology!
    Sara: That's right, Mike! Today we're going to discuss some fascinating developments.
    Mike: Absolutely! Let's dive right in.
    """
    
    print("🎤 Testing voice generation with sample script...")
    print(f"Script: {test_script.strip()}")
    
    try:
        result = gemini_voice_tool._run(test_script)
        print(f"Result: {result}")
        
        if result.startswith("SUCCESS"):
            print("✅ Voice generation successful!")
            return True
        else:
            print("❌ Voice generation failed!")
            return False
            
    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return False

if __name__ == "__main__":
    print("🔊 Testing Gemini Voice Tool...")
    success = test_voice_tool()
    
    if success:
        print("\n🎉 Voice tool test passed! You can now run the full crew.")
    else:
        print("\n💥 Voice tool test failed! Please check the errors above.")
        sys.exit(1)
