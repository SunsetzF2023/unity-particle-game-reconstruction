#!/usr/bin/env python3
"""
Unity IL2CPP游戏信息提取器
从global-metadata.dat中提取游戏相关的类名和方法名
"""

import struct
import os
import re

def extract_unity_info(metadata_path):
    """提取Unity游戏相关信息"""
    try:
        with open(metadata_path, 'rb') as f:
            data = f.read()
            
        print("=== Unity IL2CPP Game Analysis ===\n")
        
        # 尝试提取所有可读字符串
        strings = set()
        for i in range(len(data) - 20):
            try:
                # 查找以null结尾的字符串
                if data[i:i+4] == b'\x00\x00\x00\x00':
                    continue
                    
                # 尝试读取不同长度的字符串
                for length in [10, 15, 20, 30, 50, 100]:
                    if i + length <= len(data):
                        chunk = data[i:i+length]
                        # 查找null终止符
                        null_pos = chunk.find(b'\x00')
                        if null_pos > 0:
                            string_bytes = chunk[:null_pos]
                            try:
                                # 尝试UTF-8解码
                                decoded = string_bytes.decode('utf-8')
                                if len(decoded) > 3 and decoded.isprintable():
                                    strings.add(decoded)
                            except:
                                try:
                                    # 尝试ASCII解码
                                    decoded = string_bytes.decode('ascii')
                                    if len(decoded) > 3 and decoded.isprintable():
                                        strings.add(decoded)
                                except:
                                    pass
                            break
            except:
                continue
        
        # 分类字符串
        unity_classes = []
        game_classes = []
        methods = []
        namespaces = []
        other_interesting = []
        
        for s in strings:
            s_lower = s.lower()
            
            # Unity引擎相关
            if 'unityengine' in s_lower:
                unity_classes.append(s)
            # 游戏相关类名
            elif any(keyword in s_lower for keyword in ['manager', 'controller', 'player', 'game', 'ui', 'menu', 'scene', 'level']):
                game_classes.append(s)
            # 方法名
            elif '(' in s or ')' in s or s.startswith('get_') or s.startswith('set_'):
                methods.append(s)
            # 命名空间
            elif '.' in s and not any(char in s for char in ['(', ')', '<', '>', ' ']) and len(s) < 50:
                namespaces.append(s)
            # 其他有趣的内容
            elif any(keyword in s_lower for keyword in ['start', 'update', 'awake', 'onenable', 'ondisable']):
                other_interesting.append(s)
        
        # 显示结果
        print(f"Total strings extracted: {len(strings)}")
        
        if unity_classes:
            print(f"\n=== Unity Engine Classes ({len(unity_classes)}) ===")
            for s in sorted(set(unity_classes))[:20]:
                print(f"  {s}")
        
        if namespaces:
            print(f"\n=== Namespaces ({len(namespaces)}) ===")
            for s in sorted(set(namespaces))[:30]:
                print(f"  {s}")
        
        if game_classes:
            print(f"\n=== Game-related Classes ({len(game_classes)}) ===")
            for s in sorted(set(game_classes))[:30]:
                print(f"  {s}")
        
        if methods:
            print(f"\n=== Methods ({len(methods)}) ===")
            for s in sorted(set(methods))[:30]:
                print(f"  {s}")
        
        if other_interesting:
            print(f"\n=== Unity Lifecycle Methods ({len(other_interesting)}) ===")
            for s in sorted(set(other_interesting)):
                print(f"  {s}")
        
        # 查找可能的脚本文件名
        script_names = []
        for s in strings:
            if s.endswith('.cs') or (len(s) > 5 and s[0].isupper() and s.replace('_', '').replace(' ', '').isalnum()):
                script_names.append(s)
        
        if script_names:
            print(f"\n=== Possible Script Names ({len(script_names)}) ===")
            for s in sorted(set(script_names))[:40]:
                if len(s) < 50:
                    print(f"  {s}")
        
        return True
        
    except Exception as e:
        print(f"Analysis failed: {e}")
        return False

if __name__ == "__main__":
    metadata_path = "assets/bin/Data/Managed/Metadata/global-metadata.dat"
    if os.path.exists(metadata_path):
        extract_unity_info(metadata_path)
    else:
        print("Cannot find global-metadata.dat file")
