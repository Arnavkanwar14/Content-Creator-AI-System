#!/usr/bin/env python3
"""
Quick setup script for the Content Creator crew.
This script will check your environment and guide you through any missing steps.
"""

import os
import sys
import subprocess

def check_dotenv():
    """Check if python-dotenv is installed"""
    try:
        import dotenv
        print("✅ python-dotenv is installed")
        return True
    except ImportError:
        print("❌ python-dotenv is not installed")
        return False

def check_env_file():
    """Check if .env file exists and has the right content"""
    env_file = os.path.join(os.getcwd(), ".env")
    
    if os.path.exists(env_file):
        print("✅ .env file exists")
        
        # Check if it contains an API key
        try:
            with open(env_file, 'r') as f:
                content = f.read()
                if "GEMINI_API_KEY=" in content and "your_actual_api_key_here" not in content:
                    print("✅ .env file contains a Gemini API key")
                    return True
                elif "GOOGLE_API_KEY=" in content and "your_actual_api_key_here" not in content:
                    print("✅ .env file contains a Google API key")
                    return True
                else:
                    print("⚠️ .env file exists but may not contain a valid API key")
                    return False
        except Exception as e:
            print(f"❌ Error reading .env file: {e}")
            return False
    else:
        print("❌ .env file does not exist")
        return False

def check_api_key():
    """Check if API key is available in environment"""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    
    if api_key and api_key != "your_actual_api_key_here":
        print("✅ API key found in environment")
        return True
    else:
        print("❌ API key not found in environment")
        return False

def create_env_file():
    """Create a .env file template"""
    env_file = os.path.join(os.getcwd(), ".env")
    
    if os.path.exists(env_file):
        print("⚠️ .env file already exists")
        return False
    
    try:
        with open(env_file, 'w') as f:
            f.write("# Gemini API Configuration\n")
            f.write("# Get your API key from: https://aistudio.google.com/\n")
            f.write("GEMINI_API_KEY=your_actual_api_key_here\n\n")
            f.write("# Alternative: You can also use GOOGLE_API_KEY\n")
            f.write("# GOOGLE_API_KEY=your_actual_api_key_here\n")
        
        print("✅ Created .env file template")
        print("📝 Please edit .env file and replace 'your_actual_api_key_here' with your real API key")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def install_dependencies():
    """Install missing dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def main():
    """Main setup function"""
    print("🔧 Content Creator Crew Quick Setup")
    print("=" * 40)
    
    # Check current status
    dotenv_ok = check_dotenv()
    env_file_ok = check_env_file()
    api_key_ok = check_api_key()
    
    print("\n📋 Status Summary:")
    print(f"  python-dotenv: {'✅' if dotenv_ok else '❌'}")
    print(f"  .env file: {'✅' if env_file_ok else '❌'}")
    print(f"  API key: {'✅' if api_key_ok else '❌'}")
    
    # Provide guidance
    print("\n🚀 Next Steps:")
    
    if not dotenv_ok:
        print("1. Install python-dotenv:")
        print("   pip install python-dotenv")
        print("   OR run: python quick_setup.py --install")
    
    if not env_file_ok:
        print("2. Create .env file:")
        print("   python quick_setup.py --create-env")
        print("   Then edit the file with your actual API key")
    
    if not api_key_ok:
        print("3. Set your API key:")
        print("   - Edit .env file with your real API key")
        print("   - OR set environment variable: export GEMINI_API_KEY='your_key'")
    
    if dotenv_ok and env_file_ok and api_key_ok:
        print("🎉 Everything looks good! You can now:")
        print("   1. Test the voice tool: python test_voice_tool.py")
        print("   2. Run the full crew: python -m content_creator.main")
    
    # Handle command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--install":
            install_dependencies()
        elif sys.argv[1] == "--create-env":
            create_env_file()
        elif sys.argv[1] == "--help":
            print("\n📖 Usage:")
            print("  python quick_setup.py              # Check status")
            print("  python quick_setup.py --install    # Install dependencies")
            print("  python quick_setup.py --create-env # Create .env template")
            print("  python quick_setup.py --help       # Show this help")

if __name__ == "__main__":
    main()
