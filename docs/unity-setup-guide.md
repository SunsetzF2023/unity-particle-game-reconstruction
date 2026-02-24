# Unity开发环境安装指南

## 🎯 需要安装的组件

### 1. Unity Hub (必需)
**作用**: Unity版本管理器和项目启动器
- **下载地址**: https://unity.com/download
- **用途**: 管理Unity引擎版本、创建项目、启动项目

### 2. Unity编辑器 (必需)
**作用**: Unity游戏开发的主要工具
- **推荐版本**: Unity 2021.3.21f1 LTS
- **为什么选这个版本**: 稳定、兼容性好、支持IL2CPP

### 3. Visual Studio 2022 (必需)
**作用**: C#代码编写和调试
- **版本**: Visual Studio 2022 Community (免费)
- **组件**: Unity开发工作负载

## 📥 详细安装步骤

### 步骤1: 安装Unity Hub

1. 访问 https://unity.com/download
2. 点击 "Download Unity Hub"
3. 下载完成后运行安装程序
4. 按照提示完成安装

### 步骤2: 安装Unity编辑器

1. 启动Unity Hub
2. 点击左侧 "Installs" 标签
3. 点击 "Add" 按钮
4. 选择版本: **Unity 2021.3.21f1 LTS**
5. 选择组件:
   - ✅ Unity Editor (核心编辑器)
   - ✅ Windows Build Support IL2CPP (重要!)
   - ✅ Android Build Support IL2CPP (可选)
   - ✅ Documentation (文档)
   - ✅ Example Project (示例项目)

### 步骤3: 安装Visual Studio 2022

1. 访问 https://visualstudio.microsoft.com/zh-hans/downloads/
2. 下载 "Visual Studio 2022 Community"
3. 运行安装程序
4. 选择工作负载:
   - ✅ **Unity游戏开发** (最重要!)
   - ✅ .NET桌面开发
5. 点击安装

## 🔧 Unity项目初始化和配置说明

### 什么是"Unity项目初始化"?

**初始化** = 创建一个新的Unity项目，包含：
- 基础项目结构
- 默认配置文件
- 核心文件夹
- 包管理配置

### 什么是"Unity项目配置"?

**配置** = 设置项目参数，包括：
- 目标平台 (Android/iOS/PC)
- 渲染设置
- 包管理器
- 项目设置
- 脚本编译设置

## 🎮 我们的项目配置计划

### 基于分析结果的配置：

#### 1. 项目设置
- **Unity版本**: 2021.3.21f1 LTS
- **渲染管线**: Built-in Render Pipeline
- **脚本后端**: IL2CPP (与原游戏一致)
- **API兼容性**: .NET Standard 2.1

#### 2. 必需包 (Package Manager)
- **TextMeshPro 3.0.6** - UI文本系统
- **Addressables 1.21.12** - 资源管理
- **Unity UI** - UI系统

#### 3. 项目结构
```
Assets/
├── Scripts/           # C#脚本
│   ├── Managers/     # 管理器类
│   ├── UI/           # UI相关
│   ├── Effects/      # 特效系统
│   └── Game/         # 游戏逻辑
├── Scenes/           # 场景文件
├── Prefabs/          # 预制体
├── Materials/        # 材质
├── Textures/         # 贴图
└── Settings/         # 配置文件
```

## 🚀 安装完成后做什么

### 验证安装
1. 启动Unity Hub
2. 确认Unity 2021.3.21f1已安装
3. 创建一个测试项目验证功能正常

### 开始我们的项目
1. 在Unity Hub中点击 "Projects"
2. 点击 "New project"
3. 选择 "3D" 模板
4. 配置项目设置
5. 开始开发

## ⚠️ 常见问题解决

### 问题1: Unity Hub下载慢
- 使用官方下载链接
- 考虑使用国内镜像源

### 问题2: Visual Studio安装失败
- 确保网络连接稳定
- 选择离线安装包

### 问题3: Unity编辑器启动慢
- 首次启动需要初始化
- 后续启动会更快

## 📋 安装检查清单

- [ ] Unity Hub已安装并启动
- [ ] Unity 2021.3.21f1 LTS已安装
- [ ] Visual Studio 2022 Community已安装
- [ ] Unity开发工作负载已安装
- [ ] 可以创建新项目
- [ ] 可以编写C#脚本

## 🎯 下一步计划

安装完成后我们将：
1. 创建Unity项目
2. 配置项目设置
3. 安装必需包
4. 搭建基础架构
5. 开始编写管理器系统

## 💡 小贴士

- Unity Hub会自动管理版本，不用担心版本冲突
- Visual Studio Community版本完全免费
- Unity编辑器首次启动可能需要几分钟
- 建议使用SSD硬盘，提升加载速度

---

**需要帮助**: 如果安装过程中遇到问题，随时询问！  
**预计安装时间**: 30-60分钟 (取决于网络速度)
