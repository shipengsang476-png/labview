# LabVIEW 大学物理竞赛项目

本仓库整理自一组大学物理竞赛相关的 LabVIEW 材料，主要包含以下几类程序：

- MindVision 工业相机采集与图像显示
- NI Vision 图像处理与 Sobel/边缘检测
- NI-VISA 串口通信与上位机界面
- NI-DAQmx 数字输出示例
- 普朗克常量相关串口实验界面

源文件位于 `src/`。仓库共包含 **26 个 `.vi`、3 个 `.ctl` 和 1 个 `.lvproj`**。

> 这些文件来自不同时间的实验版本和原型，不是一个已经统一构建、统一测试的单一应用。上传 GitHub 前已移除第三方可执行文件、补丁、序列号及机器相关配置。

## 建议从这里开始

| 入口 | 用途 | 备注 |
|---|---|---|
| `src/CameraSobelEdgeDetection.vi` | 相机采集、串口控制和 Sobel/边缘检测 | 当前材料中修改时间最新的综合图像处理版本 |
| `src/CameraSerialController_2024-05-12.vi` | 相机与串口综合控制 | 按原文件日期保留的稳定快照 |
| `src/InitializeCamera.vi` | MindVision 相机初始化 | 依赖相机 SDK |
| `src/DAQmxDigitalOutput_2019-11-01.vi` | DAQmx 数字输出示例 | 依赖 NI-DAQmx |
| `src/LabVIEW串口调试/SerialDebugger.lvproj` | 串口调试/普朗克实验项目 | 项目入口，建议优先通过此文件打开 |
| `src/LabVIEW串口调试/User Interface/PlanckExperiment_Main.vi` | 普朗克实验主界面 | 依赖 NI-VISA 和状态机控件 |

## 目录结构

```text
.
├── README.md
├── manifest.csv                 # 当前源码路径、大小、时间和 SHA-256
├── docs/
│   ├── name-map.csv             # 原文件名到优化后文件名的映射
│   └── renaming-notes.md        # LabVIEW 二进制依赖与后续改名说明
└── src/
    ├── Camera*.vi               # 相机、图像与串口综合实验版本
    ├── DAQmx*.vi                # DAQmx 示例
    ├── Serial*.vi               # 串口示例/上位机
    ├── Image for Use_0.vi       # 被多个 VI 引用的图像辅助 VI，保留原名
    ├── 控件 1.ctl               # 被多个 VI 引用的自定义控件，保留原名
    ├── demo/                    # 相机/串口原型实验
    └── LabVIEW串口调试/         # 串口调试项目及其 UI、SubVI、控件
```

## 运行环境

从项目版本字段和 VI 内嵌信息判断，原始工程主要使用 **LabVIEW 2015**。根据程序中检测到的调用，可能需要安装：

- LabVIEW 2015 或能够兼容打开旧版本 VI 的更高版本
- NI-VISA：串口通信
- NI Vision Development Module：IMAQ 图像处理
- NI Vision Acquisition Software：IMAQdx 相机访问
- NI-DAQmx：数字量输出示例
- MindVision 相机 SDK，以及匹配位数的 `MVCAMSDK.dll`

实际运行还需要对应的相机、串口设备或 NI DAQ 硬件。不同 LabVIEW/驱动版本之间可能需要重新链接依赖或重新保存 VI。

## 打开方式

### 串口调试项目

1. 安装 LabVIEW 和 NI-VISA。
2. 打开 `src/LabVIEW串口调试/SerialDebugger.lvproj`。
3. 在项目中打开 `User Interface/PlanckExperiment_Main.vi` 或 `User Interface/主程序1.vi`。
4. 根据设备设置 COM 口、波特率、数据位、停止位和校验位。
5. 若项目显示缺失项，先检查 `SubVI/Demo/` 下的状态机控件是否被正确找到。

### 相机与图像处理

1. 安装 MindVision 相机驱动/SDK、NI Vision Development Module 和 Vision Acquisition Software。
2. 确认 `MVCAMSDK.dll` 的位数与 LabVIEW 位数一致。
3. 先测试 `src/InitializeCamera.vi`。
4. 再打开 `src/CameraSobelEdgeDetection.vi` 或其他 `Camera*.vi`。
5. 若提示找不到 `Image for Use_0.vi`，手动指向当前 VI 同目录下的同名文件，并保存链接。

### DAQmx 示例

打开 `src/DAQmxDigitalOutput_2019-11-01.vi`，在运行前确认 NI-DAQmx 已安装并将物理通道修改为本机设备对应的数字输出通道。

## 命名规则

本次整理采用以下规则：

- 使用 ASCII 英文功能名，减少 Git、终端和跨平台路径问题。
- 使用 `Main`、`Demo`、`Prototype`、`Legacy` 等后缀表达角色。
- 连续实验版本使用 `v01`、`v02` 等编号。
- 已带明确日期的快照改为 ISO 日期格式 `YYYY-MM-DD`。
- 无法从二进制元数据可靠判断用途的文件不强行命名，例如 `Unclassified_2222.vi`。

完整的原名与新名映射见 [`docs/name-map.csv`](docs/name-map.csv)。

## 为什么仍有少量旧文件名

LabVIEW 的 `.vi` 和 `.ctl` 是带有调用路径信息的二进制文件。以下文件被多个 VI 直接引用，未在文件系统中强制改名：

- `src/Image for Use_0.vi`
- `src/demo/Image for Use_0.vi`
- `src/控件 1.ctl`
- `src/LabVIEW串口调试/SubVI/Demo/状态机.ctl`
- `src/LabVIEW串口调试/SubVI/Demo/状态机0.ctl`
- `src/LabVIEW串口调试/User Interface/主程序1.vi`

本次只对静态检查中未发现本仓库内部调用者的入口 VI、示例 VI 和项目文件进行改名。后续若要继续改名，应在 LabVIEW 中加载完整调用层级后使用 **Save As / Rename**，不要直接在资源管理器中修改依赖文件名。详见 [`docs/renaming-notes.md`](docs/renaming-notes.md)。

## GitHub 与版本控制

`.vi` 和 `.ctl` 属于二进制文件，GitHub 可以保存，但网页端无法像文本源码一样显示程序框图差异。本仓库的 `.gitattributes` 已将它们标记为二进制文件。

建议提交前先在本机 LabVIEW 中完成一次：

1. 打开主要入口 VI。
2. 检查是否存在缺失 SubVI、CTL、DLL 或驱动。
3. 执行一次运行箭头/错误列表检查。
4. 保存已修复的依赖路径。
5. 再提交 Git。

初始化仓库可使用：

```bash
git init
git add .
git commit -m "Import and organize LabVIEW sources"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

## 完整性与限制

- `manifest.csv` 记录全部 `.vi`、`.ctl` 和 `.lvproj` 的 SHA-256，可用于核对文件是否被意外修改。
- 本次整理未修改 VI 内部程序框图或前面板，只调整了部分文件名和文档。
- 当前环境没有 LabVIEW、相机、串口设备或 DAQ 硬件，因此无法执行运行级验证。
- 原材料没有明确的开源许可证。公开仓库前请确认代码、相机 SDK 示例及其他素材的授权范围；不要擅自添加不确定的许可证。
