#!/usr/bin/env python3
"""
Unity游戏结构总结器
提取关键的游戏类和脚本信息
"""

import struct
import os
import re

def extract_game_summary(metadata_path):
    """提取游戏关键信息总结"""
    try:
        with open(metadata_path, 'rb') as f:
            data = f.read()
            
        print("=== Unity IL2CPP Game Structure Summary ===\n")
        
        # 提取字符串
        strings = set()
        for i in range(len(data) - 20):
            try:
                if data[i:i+4] == b'\x00\x00\x00\x00':
                    continue
                    
                for length in [10, 20, 30, 50, 100]:
                    if i + length <= len(data):
                        chunk = data[i:i+length]
                        null_pos = chunk.find(b'\x00')
                        if null_pos > 0:
                            string_bytes = chunk[:null_pos]
                            try:
                                decoded = string_bytes.decode('utf-8')
                                if len(decoded) > 3 and decoded.isprintable():
                                    strings.add(decoded)
                                break
                            except:
                                pass
            except:
                continue
        
        # 分析游戏结构
        game_scripts = []
        unity_components = []
        managers = []
        ui_elements = []
        
        for s in strings:
            s_lower = s.lower()
            
            # 游戏脚本文件
            if 'assets\\' in s_lower and '.cs' in s_lower:
                game_scripts.append(s)
            # Unity组件
            elif any(comp in s_lower for comp in ['monobehaviour', 'scriptableobject', 'component']):
                unity_components.append(s)
            # 管理器类
            elif 'manager' in s_lower:
                managers.append(s)
            # UI相关
            elif any(ui in s_lower for ui in ['button', 'canvas', 'panel', 'ui', 'menu']):
                ui_elements.append(s)
        
        print("Game Scripts Found:")
        if game_scripts:
            for script in sorted(set(game_scripts))[:15]:
                print(f"  FILE: {script}")
        else:
            print("  No explicit script paths found")
        
        print(f"\nUnity Components ({len(unity_components)}):")
        for comp in sorted(set(unity_components))[:10]:
            print(f"  COMP: {comp}")
        
        print(f"\nManager Classes ({len(managers)}):")
        for manager in sorted(set(managers))[:15]:
            print(f"  MGR: {manager}")
        
        print(f"\nUI Elements ({len(ui_elements)}):")
        for ui in sorted(set(ui_elements))[:15]:
            print(f"  UI: {ui}")
        
        # 查找可能的游戏逻辑类
        game_logic = []
        for s in strings:
            s_lower = s.lower()
            if any(keyword in s_lower for keyword in ['player', 'character', 'enemy', 'npc', 'weapon', 'inventory', 'score', 'level']):
                if '.' in s and len(s) < 60:
                    game_logic.append(s)
        
        if game_logic:
            print(f"\nGame Logic Classes ({len(game_logic)}):")
            for logic in sorted(set(game_logic))[:20]:
                print(f"  LOGIC: {logic}")
        
        # 统计信息
        print(f"\nStatistics:")
        print(f"  Total strings extracted: {len(strings)}")
        print(f"  Game scripts: {len(game_scripts)}")
        print(f"  Unity components: {len(unity_components)}")
        print(f"  Manager classes: {len(managers)}")
        print(f"  UI elements: {len(ui_elements)}")
        print(f"  Game logic classes: {len(game_logic)}")
        
        return True
        
    except Exception as e:
        print(f"Analysis failed: {e}")
        return False

if __name__ == "__main__":
    metadata_path = "assets/bin/Data/Managed/Metadata/global-metadata.dat"
    if os.path.exists(metadata_path):
        extract_game_summary(metadata_path)
    else:
        print("Cannot find global-metadata.dat file")
