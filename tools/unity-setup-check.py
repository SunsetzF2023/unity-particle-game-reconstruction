#!/usr/bin/env python3
"""
Unity开发环境检查工具
检查Unity和Visual Studio是否正确安装
"""

import os
import subprocess
import sys

def check_unity_hub():
    """检查Unity Hub是否安装"""
    unity_paths = [
        r"C:\Program Files\Unity Hub\Unity Hub.exe",
        r"C:\Program Files (x86)\Unity Hub\Unity Hub.exe",
        r"C:\Users\{}\AppData\Local\Unity\Unity Hub.exe".format(os.getenv('USERNAME', '')),
        r"C:\Program Files\Tuanjie\Hub\Tuanjie Hub.exe",
        r"C:\Program Files (x86)\Tuanjie\Hub\Tuanjie Hub.exe"
    ]
    
    for path in unity_paths:
        if os.path.exists(path):
            print(f"Unity Hub installed: {path}")
            return True
    
    print("Unity Hub not installed")
    return False

def check_unity_editor():
    """检查Unity编辑器是否安装"""
    unity_paths = [
        r"C:\Program Files\Unity\Hub\Editor\2021.3.21f1\Editor\Unity.exe",
        r"C:\Program Files (x86)\Unity\Hub\Editor\2021.3.21f1\Editor\Unity.exe",
        r"C:\Program Files\Tuanjie\Hub\Editor\2021.3.21f1\Editor\Unity.exe",
        r"C:\Program Files (x86)\Tuanjie\Hub\Editor\2021.3.21f1\Editor\Unity.exe"
    ]
    
    for path in unity_paths:
        if os.path.exists(path):
            print(f"Unity 2021.3.21f1 installed: {path}")
            return True
    
    print("Unity 2021.3.21f1 not installed")
    return False

def check_visual_studio():
    """检查Visual Studio是否安装"""
    vs_paths = [
        r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe",
        r"C:\Program Files (x86)\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe",
        r"C:\Program Files\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe",
        r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe"
    ]
    
    for path in vs_paths:
        if os.path.exists(path):
            if "2022" in path:
                print(f"Visual Studio 2022 installed: {path}")
            elif "2019" in path:
                print(f"Visual Studio 2019 installed: {path}")
            return True
    
    print("Visual Studio not installed")
    return False

def check_git():
    """检查Git是否安装"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Git installed: {result.stdout.strip()}")
            return True
    except:
        pass
    
    print("Git not installed")
    return False

def main():
    print("=== Unity Development Environment Check ===\n")
    
    checks = [
        ("Unity Hub", check_unity_hub),
        ("Unity Editor 2021.3.21f1", check_unity_editor),
        ("Visual Studio 2022", check_visual_studio),
        ("Git", check_git)
    ]
    
    results = []
    for name, check_func in checks:
        print(f"Checking {name}...")
        results.append(check_func())
        print()
    
    print("=== Check Results ===")
    if all(results):
        print("All required tools are installed! Ready for Unity development!")
        print("\nNext steps:")
        print("1. Start Unity Hub")
        print("2. Create new project")
        print("3. Configure project settings")
    else:
        print("Some tools still need to be installed")
        print("\nPlease refer to the installation guide:")
        print("docs/unity-setup-guide.md")
    
    print("\n=== Quick Links ===")
    print("Unity Hub download: https://unity.com/download")
    print("Visual Studio download: https://visualstudio.microsoft.com/zh-hans/downloads/")

if __name__ == "__main__":
    main()
