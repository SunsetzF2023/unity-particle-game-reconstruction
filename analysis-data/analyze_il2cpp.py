#!/usr/bin/env python3
"""
简单的IL2CPP global-metadata.dat分析器
尝试提取一些基本信息而不需要完整的libil2cpp.so
"""

import struct
import os

def analyze_metadata(metadata_path):
    """分析global-metadata.dat文件"""
    try:
        with open(metadata_path, 'rb') as f:
            data = f.read()
            
        print(f"File size: {len(data)} bytes")
        
        # 查找可能的字符串
        strings = []
        for i in range(0, len(data) - 10):
            try:
                # 尝试读取UTF-16字符串
                if data[i:i+2] == b'\x00\x00':
                    continue
                    
                # 查找ASCII字符串
                if 32 <= data[i] <= 126:  # 可打印ASCII字符
                    string_end = i
                    while string_end < len(data) and 32 <= data[string_end] <= 126:
                        string_end += 1
                    
                    if string_end - i > 3:  # 至少4个字符
                        try:
                            string_val = data[i:string_end].decode('ascii')
                            if len(string_val) > 5 and not string_val.isspace():
                                strings.append(string_val)
                        except:
                            pass
            except:
                continue
        
        # 去重并显示有趣的字符串
        unique_strings = list(set(strings))
        print(f"\nFound {len(unique_strings)} unique strings")
        
        # 显示可能相关的字符串
        interesting = []
        for s in unique_strings:
            if any(keyword in s.lower() for keyword in ['class', 'method', 'unity', 'game', 'player', 'manager']):
                interesting.append(s)
        
        print(f"\nPotentially relevant strings ({len(interesting)}):")
        for s in sorted(interesting)[:50]:  # 只显示前50个
            print(f"  {s}")
            
        # 查找可能的类名模式
        class_names = []
        for s in unique_strings:
            if '/' in s and '.' in s and len(s) < 100:
                class_names.append(s)
        
        if class_names:
            print(f"\nPossible class names ({len(class_names)}):")
            for s in sorted(class_names)[:30]:
                print(f"  {s}")
                
    except Exception as e:
        print(f"Analysis failed: {e}")

if __name__ == "__main__":
    metadata_path = "assets/bin/Data/Managed/Metadata/global-metadata.dat"
    if os.path.exists(metadata_path):
        analyze_metadata(metadata_path)
    else:
        print("Cannot find global-metadata.dat file")
