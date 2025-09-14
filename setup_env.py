#!/usr/bin/env python3
"""
Environment setup script for the Podcaster crew.
This script helps verify that all required environment variables and dependencies are set up correctly.
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major == 3 and 10 <= version.minor < 14:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.10-3.13")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'crewai',
        'google.genai'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('.', '_'))
            print(f"✅ {package} - Installed")
        except ImportError:
            print(f"❌ {package} - Missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📦 Install missing packages:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def check_environment_variables():
    """Check if required environment variables are set"""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    
    if api_key:
        print(f"✅ API Key - Found (length: {len(api_key)})")
        return True
    else:
        print("❌ API Key - Missing")
        print("\n🔑 Set one of these environment variables:")
        print("  export GEMINI_API_KEY='your_api_key_here'")
        print("  export GOOGLE_API_KEY='your_api_key_here'")
        print("\nFor Windows PowerShell:")
        print("  $env:GEMINI_API_KEY='your_api_key_here'")
        print("  $env:GOOGLE_API_KEY='your_api_key_here'")
        return False

def check_outputs_directory():
    """Check if outputs directory exists and is writable"""
    outputs_dir = os.path.join(os.getcwd(), "outputs")
    
    if os.path.exists(outputs_dir):
        if os.access(outputs_dir, os.W_OK):
            print(f"✅ Outputs directory - Exists and writable: {outputs_dir}")
            return True
        else:
            print(f"❌ Outputs directory - Exists but not writable: {outputs_dir}")
            return False
    else:
        try:
            os.makedirs(outputs_dir, exist_ok=True)
            print(f"✅ Outputs directory - Created: {outputs_dir}")
            return True
        except Exception as e:
            print(f"❌ Outputs directory - Could not create: {e}")
            return False

def main():
    """Main setup verification function"""
    print("🔧 Podcaster Crew Environment Setup Check")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Environment Variables", check_environment_variables),
        ("Outputs Directory", check_outputs_directory)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        print(f"\n📋 {check_name}:")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("🎉 All checks passed! Your environment is ready.")
        print("\n🚀 You can now:")
        print("  1. Test the voice tool: python test_voice_tool.py")
        print("  2. Run the full crew: python -m podcaster.main")
    else:
        print("💥 Some checks failed. Please fix the issues above before proceeding.")
        sys.exit(1)

if __name__ == "__main__":
    main()
