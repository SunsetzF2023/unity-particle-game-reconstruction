# Unity IL2CPP 游戏分析数据

## 目录说明

本目录包含从Unity IL2CPP编译的APK文件中提取的所有原始数据和分析结果。

## 文件结构

### 🎮 核心游戏文件
- **AndroidManifest.xml** - Android应用清单文件
- **classes.dex / classes2.dex** - Android应用的编译代码
- **assets/** - Unity游戏资源目录
  - **bin/Data/** - Unity游戏数据
    - **Managed/Metadata/global-metadata.dat** - IL2CPP元数据文件（最重要）
    - **data.unity3d** - Unity资源包
    - **resources.resource** - 资源文件

### 🔧 分析工具
- **analyze_il2cpp.py** - IL2CPP元数据分析工具
- **unity_game_info.py** - Unity游戏信息提取工具
- **game_summary.py** - 游戏结构总结工具

### 📊 分析结果
- **GAME_ANALYSIS_REPORT.txt** - 完整的游戏分析报告
- **recreation_plan.md** - 游戏复现计划

### 📱 Android资源
- **res/** - Android应用资源文件
  - **drawable-*/** - 各分辨率图片资源
  - **layout*/** - UI布局文件
  - **mipmap-*/** - 应用图标
  - **xml/** - 配置文件

### ⚙️ 配置文件
- **resources.arsc** - Android资源编译表
- **META-INF/** - 应用签名和元信息
- **kotlin/** - Kotlin运行时库

## 关键文件说明

### 🎯 global-metadata.dat
这是最重要的文件，包含：
- 所有C#类的元数据
- 方法签名和属性信息
- 字符串常量
- 类型定义

**大小**: 8,468,444 字节 (8.1MB)

### 📦 data.unity3d
Unity资源包，包含：
- 场景数据
- 预制体
- 资源引用

**大小**: 33,844,945 字节 (32.3MB)

## 使用方法

### 1. 运行分析工具
```bash
# 基础分析
python analyze_il2cpp.py

# 详细信息提取
python unity_game_info.py

# 游戏结构总结
python game_summary.py
```

### 2. 查看分析报告
```bash
# 查看完整分析报告
cat GAME_ANALYSIS_REPORT.txt

# 查看复现计划
cat recreation_plan.md
```

## 分析结果摘要

### 📊 数据统计
- **总字符串提取**: 597,683 个
- **游戏脚本**: 2,215 个
- **管理器类**: 5,945 个
- **UI元素**: 26,532 个
- **游戏逻辑类**: 1,168 个

### 🎮 识别的核心系统
1. **粒子特效系统** (Cartoon FX Remaster)
2. **UI管理系统**
3. **场景管理系统**
4. **输入管理系统**
5. **游戏逻辑系统**

### 🔍 主要发现
- Unity IL2CPP编译的移动游戏
- 使用Google Play Games集成
- 丰富的粒子特效系统
- 完整的UI管理框架
- 模块化的管理器架构

## 复现指导

基于这些分析数据，可以：
1. ✅ 重建游戏技术架构
2. ✅ 实现核心系统框架
3. ⚠️ 推测游戏逻辑设计
4. ❌ 无法获取原始美术资源

## 注意事项

⚠️ **重要提醒**:
- 这些数据仅用于学习和研究目的
- 请勿用于商业用途或侵犯原作版权
- 复现时应创建原创的美术和音效资源
- 遵守相关法律法规和开源协议

## 技术要求

### 运行分析工具
- Python 3.9+
- 标准库：struct, os, re

### Unity开发
- Unity 2021.3 LTS
- TextMeshPro
- Addressables
- IL2CPP编译支持

## 文件大小统计

```
global-metadata.dat: 8.1MB  (核心元数据)
data.unity3d:        32.3MB (Unity资源)
classes.dex:         8.4MB  (Android代码)
classes2.dex:        7.7MB  (Android代码)
resources.arsc:      0.5MB  (资源表)
总大小:              ~100MB+
```

## 下一步工作

1. **Unity项目初始化** - 基于分析结果创建项目
2. **核心系统实现** - 管理器框架搭建
3. **UI系统开发** - 界面框架实现
4. **特效系统** - 粒子效果开发
5. **游戏逻辑** - 基于推测实现玩法

---

**分析日期**: 2024-02-24  
**工具版本**: 自定义Python分析脚本  
**数据来源**: Unity IL2CPP APK逆向工程
