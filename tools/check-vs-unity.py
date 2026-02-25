#!/usr/bin/env python3
"""
检查Visual Studio是否安装了Unity开发组件
"""

import os
import subprocess
import sys

def check_vs_unity_components():
    """检查VS 2019 Unity组件"""
    vs_path = r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community"
    
    # 更准确的Unity组件检查路径
    unity_components = [
        r"Common7\IDE\Extensions\Microsoft\Visual Studio Tools for Unity",
        r"Common7\IDE\Extensions\Microsoft\Visual Studio Tools for Unity\extension.vsixmanifest",
        r"Common7\IDE\Extensions\Microsoft\Visual Studio Tools for Unity\Analyzers",
        r"Common7\IDE\Extensions\Microsoft\Visual Studio Tools for Unity\ItemTemplates"
    ]
    
    print("=== Visual Studio 2019 Unity Components Check ===\n")
    
    vs_installed = os.path.exists(os.path.join(vs_path, "Common7", "IDE", "devenv.exe"))
    
    if not vs_installed:
        print("Visual Studio 2019 not found")
        return False
    
    print("Visual Studio 2019 installed")
    
    # 检查Unity组件
    unity_found = False
    for component in unity_components:
        component_path = os.path.join(vs_path, component)
        if os.path.exists(component_path):
            print(f"Unity component found: {component}")
            unity_found = True
    
    # 检查扩展清单文件
    extension_manifest = os.path.join(vs_path, "Common7", "IDE", "Extensions", "Microsoft", "Visual Studio Tools for Unity", "extension.vsixmanifest")
    if os.path.exists(extension_manifest):
        print("Unity extension manifest found")
        try:
            with open(extension_manifest, 'r', encoding='utf-8') as f:
                content = f.read()
                if "unity" in content.lower():
                    print("Unity extension verified")
                    unity_found = True
        except:
            pass
    
    if not unity_found:
        print("Unity components not detected")
        print("You may need to install Unity workload:")
        print("1. Open Visual Studio Installer")
        print("2. Click 'Modify' on VS 2019")
        print("3. Check 'Unity game development' workload")
        print("4. Click 'Modify' to install")
    else:
        print("Unity components are ready!")
    
    return unity_found

def main():
    unity_ready = check_vs_unity_components()
    
    print("\n=== Recommendation ===")
    if unity_ready:
        print("Visual Studio 2019 is ready for Unity development!")
        print("You can start creating Unity projects.")
    else:
        print("Install Unity workload in VS 2019:")
        print("1. Open Visual Studio Installer")
        print("2. Select VS 2019 and click 'Modify'")
        print("3. Check 'Unity game development' workload")
        print("4. Click 'Modify' to install")

if __name__ == "__main__":
    main()
