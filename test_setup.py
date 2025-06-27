#!/usr/bin/env python3
"""
Test script to verify the basic setup of the Art Descriptions AI system.
This script tests the configuration and basic functionality without making API calls.
"""

import os
import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_directory_structure():
    """Test that all required directories exist."""
    print("Testing directory structure...")
    
    required_dirs = ['assets', 'descriptions', 'src']
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✓ {dir_name}/ directory exists")
        else:
            print(f"✗ {dir_name}/ directory missing")
            return False
    return True

def test_required_files():
    """Test that all required files exist."""
    print("\nTesting required files...")
    
    required_files = [
        'requirements.txt',
        'env.example',
        'main.py',
        'example_usage.py',
        'src/__init__.py',
        'src/config.py',
        'src/art_descriptor.py'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} missing")
            return False
    return True

def test_config_import():
    """Test that the config module can be imported."""
    print("\nTesting configuration import...")
    
    try:
        from src.config import Config
        print("✓ Config module imported successfully")
        
        # Test that the accessibility prompt exists
        if hasattr(Config, 'ACCESSIBILITY_PROMPT') and Config.ACCESSIBILITY_PROMPT:
            print("✓ Accessibility prompt is configured")
        else:
            print("✗ Accessibility prompt is missing")
            return False
            
        return True
    except Exception as e:
        print(f"✗ Failed to import config: {e}")
        return False

def test_art_descriptor_import():
    """Test that the art descriptor module can be imported."""
    print("\nTesting art descriptor import...")
    
    try:
        from src.art_descriptor import ArtDescriptor
        print("✓ ArtDescriptor class imported successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to import ArtDescriptor: {e}")
        return False

def test_image_formats():
    """Test that supported image formats are defined."""
    print("\nTesting supported image formats...")
    
    try:
        from src.config import Config
        formats = Config.SUPPORTED_FORMATS
        
        if formats and len(formats) > 0:
            print(f"✓ {len(formats)} supported formats defined: {', '.join(formats)}")
            return True
        else:
            print("✗ No supported formats defined")
            return False
    except Exception as e:
        print(f"✗ Failed to test image formats: {e}")
        return False

def test_assets_directory():
    """Test the assets directory setup."""
    print("\nTesting assets directory...")
    
    assets_dir = Path('assets')
    if assets_dir.exists():
        # Check for any image files
        image_files = []
        for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']:
            image_files.extend(assets_dir.glob(f"*{ext}"))
            image_files.extend(assets_dir.glob(f"*{ext.upper()}"))
        
        if image_files:
            print(f"✓ Found {len(image_files)} image files in assets/")
            for img in image_files[:5]:  # Show first 5
                print(f"  - {img.name}")
            if len(image_files) > 5:
                print(f"  ... and {len(image_files) - 5} more")
        else:
            print("ℹ No image files found in assets/ (this is normal for a new setup)")
        
        # Check for README
        if (assets_dir / 'README.md').exists():
            print("✓ Assets README exists")
        else:
            print("ℹ Assets README missing")
        
        return True
    else:
        print("✗ Assets directory missing")
        return False

def test_descriptions_directory():
    """Test the descriptions directory setup."""
    print("\nTesting descriptions directory...")
    
    desc_dir = Path('descriptions')
    if desc_dir.exists():
        # Check for README
        if (desc_dir / 'README.md').exists():
            print("✓ Descriptions README exists")
        else:
            print("ℹ Descriptions README missing")
        
        return True
    else:
        print("✗ Descriptions directory missing")
        return False

def main():
    """Run all tests."""
    print("Art Descriptions AI - Setup Test")
    print("=" * 40)
    
    tests = [
        test_directory_structure,
        test_required_files,
        test_config_import,
        test_art_descriptor_import,
        test_image_formats,
        test_assets_directory,
        test_descriptions_directory
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
    
    print("\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Copy env.example to .env")
        print("2. Add your OpenAI API key to .env")
        print("3. Add artwork images to the assets/ folder")
        print("4. Run: python main.py --bulk")
    else:
        print("⚠ Some tests failed. Please check the setup.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 