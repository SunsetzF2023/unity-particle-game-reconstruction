# Unity Particle Game Reconstruction

🎮 Unity IL2CPP游戏复现项目 - 基于逆向分析的Unity移动游戏重建

## 项目概述

本项目通过逆向分析Unity IL2CPP编译的移动游戏，重建其技术架构和核心系统。项目展示了如何从编译后的APK中提取游戏结构信息，并基于这些信息创建一个功能相似的游戏框架。

## 技术特色

- 🔍 **IL2CPP逆向分析** - 从global-metadata.dat提取游戏结构
- 🎮 **Unity移动框架** - 完整的移动游戏架构重建
- ✨ **粒子特效系统** - 基于Cartoon FX Remaster的特效实现
- 📱 **UI管理系统** - 移动端优化的用户界面
- 🌐 **GitHub Pages** - 在线演示和文档
- 📚 **详细文档** - 完整的开发和分析过程

## 项目结构

```
unity-particle-game-reconstruction/
├── docs/                        # 📖 项目文档
│   ├── game-analysis.md         # 原游戏分析报告
│   ├── recreation-plan.md       # 复现计划
│   └── development-log.md        # 开发日志
├── unity-project/               # 🎮 Unity项目
│   ├── Assets/
│   │   ├── Scripts/             # C#脚本
│   │   ├── Scenes/              # 场景文件
│   │   ├── Prefabs/             # 预制体
│   │   └── Materials/           # 材质
│   └── Packages/                # 包管理配置
├── web-preview/                 # 🌐 GitHub Pages
│   ├── index.html              # 预览主页
│   └── assets/                 # 静态资源
└── tools/                       # 🔧 分析工具
    ├── analyze_il2cpp.py       # IL2CPP分析工具
    ├── unity_game_info.py      # Unity信息提取
    └── game_summary.py         # 游戏总结工具
```

## 原游戏分析结果

基于IL2CPP分析，原游戏包含以下核心系统：

### 🎯 主要组件
- **Cartoon FX Remaster** - 粒子特效系统
- **Google Play Games** - 社交集成
- **UI管理系统** - 界面框架
- **场景管理器** - 场景切换
- **输入管理器** - 用户交互

### 📊 数据统计
- **2,215** 个游戏脚本文件
- **5,945** 个管理器类
- **26,532** 个UI元素
- **1,168** 个游戏逻辑类

## 复现计划

### Phase 1: 基础框架 ✅
- [x] 项目结构搭建
- [x] GitHub仓库配置
- [x] 文档系统建立
- [ ] Unity项目初始化

### Phase 2: 核心系统 (进行中)
- [ ] 管理器框架实现
- [ ] UI系统搭建
- [ ] 场景管理实现
- [ ] 基础特效添加

### Phase 3: 游戏逻辑
- [ ] 敌人系统实现
- [ ] 交互逻辑开发
- [ ] UI功能完善
- [ ] Google Play集成

### Phase 4: 优化部署
- [ ] 性能优化
- [ ] WebGL构建
- [ ] GitHub Pages部署
- [ ] 文档完善

## 技术栈

### 开发环境
- **Unity 2021.3.21f1** (LTS)
- **Visual Studio 2022**
- **Git** 版本控制

### Unity包
- **TextMeshPro 3.0.6** - UI文本系统
- **Addressables 1.21.12** - 资源管理
- **Google Play Games 2.3.0** - 社交功能

### 分析工具
- **Python 3.9+** - 分析脚本
- **Il2CppDumper** - IL2CPP反编译
- **自定义分析工具** - 信息提取

## 在线演示

🌐 [GitHub Pages预览](https://sunsetzf2023.github.io/unity-particle-game-reconstruction/)

*演示页面正在建设中...*

## 开发进度

| 模块 | 状态 | 进度 | 备注 |
|------|------|------|------|
| 项目架构 | ✅ | 100% | 基础结构完成 |
| IL2CPP分析 | ✅ | 100% | 提取游戏信息 |
| Unity项目 | 🔄 | 0% | 准备开始 |
| 核心系统 | ⏳ | 0% | 计划中 |
| UI系统 | ⏳ | 0% | 计划中 |
| 特效系统 | ⏳ | 0% | 计划中 |
| Web部署 | ⏳ | 0% | 计划中 |

## 贡献指南

欢迎参与项目开发！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

本项目基于MIT许可证开源 - 查看 [LICENSE](LICENSE) 文件了解详情

## 联系方式

- **项目维护者**: @SunsetzF2023
- **项目主页**: https://github.com/SunsetzF2023/unity-particle-game-reconstruction

## 致谢

- [Perfare/Il2CppDumper](https://github.com/Perfare/Il2CppDumper) - IL2CPP反编译工具
- Unity Technologies - Unity引擎
- 所有为开源社区做出贡献的开发者

---

⭐ 如果这个项目对你有帮助，请给它一个星标！
