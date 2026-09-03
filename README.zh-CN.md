# LabVIEW 大学物理竞赛项目

这是整理后的完整 GitHub 上传包，包含你最初提供的 LabVIEW 材料中全部 **唯一且适合纳入源码仓库** 的程序文件，以及后来单独提供的迈德威视 `MVCAMSDK.dll`。

## 包含内容

- 26 个唯一 `.vi`
- 3 个唯一 `.ctl`
- 1 个 `.lvproj`
- 1 个 `MVCAMSDK.dll`
- 1 份已移除激活信息的原始 Word 说明备份
- 英文 README、文件名映射、来源清单、重复文件报告、GitHub 更新说明和 SHA-256 清单

后来单独上传的 `Demo_20240512(1).vi` 和 `Image for Use_0(1).vi` 与原始材料中的对应文件逐字节完全一致，因此只保留一份，并在 `docs/duplicate-report.md` 中记录。原始 Word 说明中的激活信息已经移除，脱敏备份位于 `docs/original-materials/`。

## 主要入口

- `src/InitializeCamera.vi`：迈德威视相机初始化
- `src/CameraSobelEdgeDetection.vi`：相机、串口和 Sobel/边缘检测
- `src/CameraSerialController_2024-05-12.vi`：相机与串口综合控制
- `src/DAQmxDigitalOutput_2019-11-01.vi`：DAQmx 数字输出实验
- `src/serial-debugger/SerialDebugger.lvproj`：串口调试/普朗克实验项目

## 关于英文命名

目录和可安全改名的 VI 已统一为英文。以下 3 个 `.ctl` 文件被 VI 的二进制依赖路径直接引用，因此暂时保留原名：

- `src/控件 1.ctl`
- `src/serial-debugger/SubVI/Demo/状态机.ctl`
- `src/serial-debugger/SubVI/Demo/状态机0.ctl`

不要直接在资源管理器或 GitHub 网页中改这 3 个名称。应在 LabVIEW 中打开完整调用层级后使用 **Save As / Rename**，并保存所有调用者。

## 更新现有 GitHub 仓库

你当前的 GitHub 仓库与本包大部分内容重合：在线 `manifest.csv` 列出的 30 个 LabVIEW 源文件哈希能够与原始材料对应。但实际在线目录只保留了 1 个串口项目界面 VI，另有 2 个旧版主程序缺失；3 个依赖控件还被手动改成了 `1.ctl`、`clt.ctl` 和 `s.ctl`，与 README/manifest 不一致。上传本包前，应按 `docs/github-update.md` 的方式整体替换仓库内容。

## DLL 提示

附带的 `MVCAMSDK.dll` 是 Windows 32 位 x86 文件，版本 `2.1.10.116`。使用它时需要 32 位 LabVIEW，并仍需安装迈德威视官方驱动/SDK。公开仓库前请确认 DLL 的再分发权限。

详细英文说明见 [`README.md`](README.md)。
