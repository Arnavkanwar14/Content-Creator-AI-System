#!/usr/bin/env python3
"""
Educational Content Creator Bot
Creates engaging conversations and generates audio using Gemini Pro.
"""

import sys
import os
from datetime import datetime

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    print("🎙️ Educational Content Creator Bot")
    print("=" * 50)
    print("Creates engaging conversations and generates audio using Gemini Pro!")
    print()
    
    # Get topic from user input
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        print("Examples of great topics:")
        print("• How Photosynthesis Works")
        print("• Why the Sky is Blue")
        print("• How GPS Works")
        print("• Why We Get Goosebumps")
        print("• How Solar Panels Work")
        print("• Why Ice Floats on Water")
        print()
        topic = input("Enter the educational topic: ").strip()
        if not topic:
            topic = "How Photosynthesis Works"
    
    print(f"\n🎙️ Creating educational content about: {topic}")
    print("⏱️  Comprehensive educational format")
    print("👥 Format: Two friends chatting (Mike & Sara)")
    print("🎵 Output: Script + Audio")
    print("\n🚀 Starting content generation...")
    
    try:
        from content_creator.main import run_with_topic
        run_with_topic(topic)
        
        print("\n✅ Content generation completed!")
        print("📁 Check the 'outputs' folder for:")
        print("   - Research report")
        print("   - Content script")
        print("   - Audio file (.wav)")
        print("\n🎙️ Ready for listening!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you have set your GEMINI_API_KEY environment variable")
        print("2. Check that all dependencies are installed: pip install -e .")
        print("3. Verify your internet connection")

if __name__ == "__main__":
    main()

