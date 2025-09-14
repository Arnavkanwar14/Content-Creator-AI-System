#!/usr/bin/env python3
"""
Quick test to generate content and audio without the full crew complexity.
This bypasses any LLM overload issues by creating a simple script directly.
"""

import sys
import os
from datetime import datetime

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def count_words(text):
    """Count words in script (excluding speaker labels)"""
    # Remove speaker labels (Mike: Sara:) and count only dialogue
    lines = text.strip().split('\n')
    word_count = 0
    for line in lines:
        if ':' in line:
            # Extract dialogue after speaker name
            dialogue = line.split(':', 1)[1].strip()
            word_count += len(dialogue.split())
        else:
            word_count += len(line.split())
    return word_count

def create_sample_script(topic):
    """Create a sample educational script about the given topic."""
    
    scripts = {
        "How plants make oxygen": """
Mike: Hey Sara, how do plants actually make oxygen?

Sara: It's photosynthesis, Mike! Plants use sunlight, water, and CO2 to make food. Oxygen is the amazing byproduct!

Mike: So they're like solar-powered food factories?

Sara: Exactly! Chlorophyll in leaves captures sunlight, roots pull up water, and tiny pores grab CO2 from air.

Mike: Then what happens?

Sara: The magic occurs in chloroplasts! They combine everything using sun's energy to make glucose, and release oxygen we breathe!

Mike: So every breath depends on plants?

Sara: Pretty much! One large tree makes enough oxygen for two people daily. Without photosynthesis, no oxygen, no us!

Mike: Amazing! Plants keep us alive while feeding themselves.

Sara: That's why protecting forests matters - they're our life support!
        """,
        
        "default": f"""
Mike: Hey Sara, what's the coolest thing about {topic}?

Sara: Great question, Mike! The fascinating part is how the basic principles actually work in everyday life.

Mike: Can you give a quick example?

Sara: Absolutely! Think about it this way - the fundamental process involves key interactions that most people don't notice.

Mike: That's amazing! What should people remember?

Sara: The main takeaway is understanding these core concepts helps us appreciate the world around us better!

Mike: Perfect! Thanks for explaining {topic} so clearly, Sara.

Sara: Anytime, Mike! Science is everywhere once you know what to look for.
        """
    }
    
    return scripts.get(topic, scripts["default"])

def main():
    # Get topic
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = input("Enter topic: ").strip() or "How plants make oxygen"
    
    print(f"🎙️ Creating content about: {topic}")
    
    # Create script
    script = create_sample_script(topic)
    
    # Count words and validate length
    word_count = count_words(script)
    print(f"📝 Script word count: {word_count} words")
    
    if word_count > 150:
        print(f"⚠️  WARNING: Script exceeds 150-word limit! Audio may be over 1 minute.")
    else:
        print(f"✅ Script length OK for 1-minute audio target")
    
    # Save script to file
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    os.makedirs('outputs', exist_ok=True)
    script_file = os.path.join('outputs', f'script-{timestamp}.md')
    
    with open(script_file, 'w') as f:
        f.write(f"# Educational Content Script: {topic}\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Word Count: {word_count} words (Target: ≤150 for 1-minute audio)\n\n")
        f.write(script.strip())
    
    print(f"✅ Script saved to: {script_file}")
    
    # Generate audio
    try:
        from content_creator.tools.custom_tool import gemini_voice_tool
        
        print("🎤 Generating audio...")
        result = gemini_voice_tool._run(script.strip())
        
        if "SUCCESS" in result:
            print("✅ Audio generated successfully!")
            print(f"📁 Check the outputs folder for your content!")
            return True
        else:
            print(f"❌ Audio generation failed: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Error generating audio: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        print("🔧 Try running: python test_voice_tool.py to test audio generation independently")