# 完整开发环境搭建指南

## 🎯 概述

本指南提供Unity粒子游戏复现项目的完整开发环境搭建步骤，包括所有必需工具的下载、安装和配置。

## 📋 工具清单

### 🎮 游戏引擎
- [ ] Unity Hub (最新版)
- [ ] Unity Editor 2021.3.21f1
- [ ] Godot Engine 4.x (最新版)

### 🛠️ 开发工具
- [ ] Visual Studio Community 2019/2022
- [ ] Python 3.9+ (最新版)
- [ ] Git for Windows
- [ ] GitHub Desktop (可选)

### 🔧 Unity插件和工具
- [ ] Visual Studio Tools for Unity
- [ ] Unity Analytics
- [ ] Google Play Games SDK
- [ ] IL2CPP分析工具

---

## 🚀 安装步骤

### 第一步：基础开发工具

#### 1.1 安装 Visual Studio Community

**下载地址**：
- 官方网站：https://visualstudio.microsoft.com/zh-hans/downloads/
- 选择版本：Visual Studio Community 2019 或 2022

**安装步骤**：
1. 访问下载页面
2. 下载 Visual Studio Community Installer
3. 运行安装程序
4. 选择工作负载：
   - ✅ **.NET 桌面开发**
   - ✅ **Unity 游戏开发**
   - ✅ **使用 C++ 的游戏开发** (可选)
5. 点击安装
6. 等待安装完成

**验证安装**：
```
运行我们的检查脚本：
python tools/check-vs-unity.py
```

#### 1.2 安装 Python 3.x

**下载地址**：
- 官方网站：https://www.python.org/downloads/
- 推荐版本：Python 3.9.16 或 3.10.11

**安装步骤**：
1. 访问Python下载页面
2. 下载Windows安装包
3. 运行安装程序
4. **重要**：勾选 "Add Python to PATH"
5. 选择 "Install for all users"
6. 点击 "Install Now"
7. 等待安装完成

**验证安装**：
```bash
python --version
pip --version
```

#### 1.3 安装 Git for Windows

**下载地址**：
- 官方网站：https://git-scm.com/download/win

**安装步骤**：
1. 下载Git for Windows安装包
2. 运行安装程序
3. 使用默认设置（推荐）
4. 完成安装

**验证安装**：
```bash
git --version
```

---

### 第二步：游戏引擎安装

#### 2.1 安装 Unity Hub

**下载地址**：
- 官方网站：https://unity.com/download
- 直接下载：https://download.unity3d.com/download_unity/UnityHubSetup.exe

**安装步骤**：
1. 下载Unity Hub安装包
2. 运行安装程序
3. 选择安装路径
4. 完成安装

**许可证配置**：
1. 启动Unity Hub
2. 登录Unity账号
3. 进入 "License Management"
4. 激活 "Personal" 许可证（免费）

#### 2.2 安装 Unity Editor

**在Unity Hub中安装**：
1. 启动Unity Hub
2. 进入 "Installs" 标签
3. 点击 "Install Editor"
4. 选择版本：**Unity 2021.3.21f1**
5. 选择模块：
   - ✅ **Windows Build Support (IL2CPP)**
   - ✅ **Android Build Support (IL2CPP)**
   - ✅ **WebGL Build Support**
   - ✅ **Documentation**
   - ✅ **Example Project**
6. 点击 "Install"
7. 等待下载和安装完成

#### 2.3 安装 Godot Engine

**下载地址**：
- 官方网站：https://godotengine.org/download/
- 选择版本：Godot 4.x 最新稳定版

**安装步骤**：
1. 下载Godot可执行文件
2. 解压到目标目录
3. 运行Godot.exe
4. （可选）创建桌面快捷方式

**C#支持配置**：
1. 在Godot中创建项目
2. 进入 "Project -> Project Settings"
3. 启用 "C#" 支持
4. 按提示安装.NET SDK

---

### 第三步：Unity插件和工具

#### 3.1 验证 Visual Studio Tools for Unity

**检查方法**：
```
运行我们的检查脚本：
python tools/check-vs-unity.py
```

**如果缺失**：
1. 打开 "Visual Studio Installer"
2. 找到已安装的VS版本
3. 点击 "Modify"
4. 勾选 "Unity 游戏开发"
5. 点击 "Modify" 更新

#### 3.2 安装 IL2CPP分析工具

**工具列表**：
- **Il2CppDumper** - GitHub开源工具
- **Il2CppInspector** - 图形化分析工具
- **Il2CppRecompiler** - 代码重构工具

**下载地址**：
- Il2CppDumper：https://github.com/Perfare/Il2CppDumper
- Il2CppInspector：https://github.com/deroad/Il2CppInspector

**安装步骤**：
1. 下载工具压缩包
2. 解压到项目工具目录
3. 运行可执行文件
4. 按工具说明使用

---

### 第四步：项目环境配置

#### 4.1 克隆项目仓库

**使用Git**：
```bash
git clone https://github.com/SunsetzF2023/unity-particle-game-reconstruction.git
cd unity-particle-game-reconstruction
```

**使用GitHub Desktop**：
1. 安装GitHub Desktop
2. 登录GitHub账号
3. 克隆仓库到本地

#### 4.2 配置Python环境

**安装依赖**：
```bash
pip install -r requirements.txt
```

**如果没有requirements.txt**：
```bash
pip install requests beautifulsoup4 lxml
```

#### 4.3 验证开发环境

**运行检查脚本**：
```bash
# 检查Unity环境
python tools/unity-setup-check.py

# 检查VS Unity组件
python tools/check-vs-unity.py

# 分析IL2CPP文件
python tools/analyze_il2cpp.py
```

---

## 📁 推荐目录结构

```
Development/
├── Engines/
│   ├── Unity/
│   │   ├── Hub/
│   │   └── Editor/2021.3.21f1/
│   └── Godot/
├── Tools/
│   ├── Visual Studio/
│   ├── Python/
│   └── IL2CPP Tools/
├── Projects/
│   └── unity-particle-game-reconstruction/
└── Resources/
    └── Game Analysis/
```

---

## ⚙️ 配置优化

### Unity配置

**编辑器设置**：
1. 打开Unity Editor
2. 进入 "Edit -> Preferences"
3. 外部工具设置：
   - External Script Editor: Visual Studio
   - Version Control: Git
4. 保存设置

**项目设置**：
1. 创建新项目
2. 进入 "Edit -> Project Settings"
3. 配置：
   - Player Settings
   - Quality Settings
   - Input Manager
   - Physics Settings

### Godot配置

**编辑器设置**：
1. 打开Godot
2. 进入 "Editor -> Editor Settings"
3. 配置：
   - Interface Theme
   - File System
   - Network

---

## 🚀 快速开始

### 创建Unity项目

**步骤**：
1. 启动Unity Hub
2. 点击 "New project"
3. 选择 "2D" 模板
4. 项目名称：`ParticleGame`
5. 选择项目路径
6. 点击 "Create project"

### 创建Godot项目

**步骤**：
1. 启动Godot
2. 点击 "New Project"
3. 项目名称：`ParticleGame`
4. 选择渲染器：OpenGL ES 3.0
5. 启用C#支持
6. 点击 "Create"

---

## 🔧 故障排除

### 常见问题

**Unity许可证问题**：
- 症状：许可证过期或无法激活
- 解决：重新申请Personal许可证

**VS Unity组件缺失**：
- 症状：无法调试Unity脚本
- 解决：运行Visual Studio Installer，添加Unity工作负载

**Python环境问题**：
- 症状：脚本运行失败
- 解决：重新安装Python，确保添加到PATH

**Git连接问题**：
- 症状：无法连接GitHub
- 解决：检查网络和SSH密钥配置

### 获取帮助

**官方文档**：
- Unity: https://docs.unity3d.com
- Godot: https://docs.godotengine.org
- Visual Studio: https://docs.microsoft.com/en-us/visualstudio/

**社区支持**：
- Unity论坛：https://forum.unity.com
- Godot社区：https://godotengine.org/community
- Stack Overflow：https://stackoverflow.com

---

## 📋 安装检查清单

### 安装完成后验证

**基础工具**：
- [ ] Visual Studio Community 2019/2022
- [ ] Python 3.x
- [ ] Git for Windows
- [ ] GitHub Desktop (可选)

**游戏引擎**：
- [ ] Unity Hub
- [ ] Unity Editor 2021.3.21f1
- [ ] Godot Engine 4.x

**Unity插件**：
- [ ] Visual Studio Tools for Unity
- [ ] Unity Analytics
- [ ] IL2CPP分析工具

**项目配置**：
- [ ] 项目仓库已克隆
- [ ] Python环境已配置
- [ ] 检查脚本可运行

---

## 🎯 下一步

安装完成后，可以开始：

1. **分析原游戏**：运行IL2CPP分析脚本
2. **创建项目**：Unity或Godot项目
3. **复现功能**：基于分析结果实现游戏
4. **版本控制**：使用Git管理代码

---

## 📞 技术支持

如果遇到问题，可以：
1. 查看官方文档
2. 搜索相关论坛
3. 检查GitHub Issues
4. 联系项目维护者

---

*最后更新：2026-02-25*
*版本：1.0*
