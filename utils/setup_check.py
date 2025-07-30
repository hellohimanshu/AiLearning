#!/usr/bin/env python3
"""
Setup Check Script for AI Learning Environment
This script checks if all required packages are available and working.
"""

import sys
import importlib
from typing import List, Tuple

def check_package(package_name: str) -> Tuple[bool, str]:
    """Check if a package is available and return status."""
    try:
        importlib.import_module(package_name)
        return True, f"✅ {package_name} is available"
    except ImportError:
        return False, f"❌ {package_name} is not installed"

def main():
    """Main function to check all packages."""
    print("🤖 AI Learning Environment Setup Check")
    print("=" * 50)
    
    # Core packages to check
    packages = [
        "numpy",
        "pandas", 
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "jupyter",
        "tensorflow",
        "torch",
        "opencv",
        "pillow",
        "nltk",
        "transformers"
    ]
    
    all_good = True
    results = []
    
    for package in packages:
        status, message = check_package(package)
        results.append((status, message))
        if not status:
            all_good = False
    
    # Print results
    for status, message in results:
        print(message)
    
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 All packages are available! Your AI environment is ready.")
    else:
        print("⚠️  Some packages are missing. Please install them using:")
        print("   pip install -r requirements.txt")
    
    # Python version check
    print(f"\n🐍 Python version: {sys.version}")
    
    # Additional recommendations
    print("\n📝 Next steps:")
    print("1. Create a virtual environment: python -m venv venv")
    print("2. Activate it: venv\\Scripts\\activate (Windows)")
    print("3. Install packages: pip install -r requirements.txt")
    print("4. Start Jupyter: jupyter lab")

if __name__ == "__main__":
    main() 