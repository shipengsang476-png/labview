# Source Inventory

This inventory accounts for every file supplied by the user. Exact duplicate uploads are represented once, and excluded non-source items are listed explicitly.

## Uploaded containers and standalone files

| Input | SHA-256 | Disposition |
|---|---|---|
| `大物竞赛labview材料 (2)(1).zip` | `972542f1285ce12259f55c0b0bbe11ee27ddbe2769d5acb07a8154bb5576daaf` | Extracted for source review; not embedded because it contains excluded third-party installers, credentials, and patch files |
| `MVCAMSDK(1).dll` | `8b2e43458102257bbbb4de0bfb4c7f61a9dcb94c17f8d035ae48462cfd041a7a` | Added as `third_party/mindvision/bin/win32/MVCAMSDK.dll` |
| `Demo_20240512(1).vi` | `98f938ea8b7eca6072df893f61d4c33870683c9e9f5b9080f4fff6a85c29c3c5` | Exact duplicate of `src/CameraSerialController_2024-05-12.vi`; represented once |
| `Image for Use_0(1).vi` | `7d7cd3ac4da60e27cd176ff033cf85dbcc033dce6c2c362c914a643c93b94df4` | Exact duplicate of `src/demo/Image for Use_0.vi`; represented once |

## Files inside the original archive

| Original relative path | Size (bytes) | SHA-256 | Final disposition |
|---|---:|---|---|
| `1111.vi` | 23948 | `8e94e821680ae96a5e709c7900023073eb8d7073ec1daa51908ebc7b1214cf5d` | Included as `src/SerialPortConfig_Example.vi` |
| `20191101DEMO.vi` | 327724 | `fd5ecb99aefa015ac6c53b0d2da1e1bc6a78bcb6b8220d942ba1741fda34023c` | Included as `src/DAQmxDigitalOutput_2019-11-01.vi` |
| `2222.vi` | 5968 | `a4c6af095eb9d808904105f252d48f9316121144f1d4780dac0caee7d8a2560c` | Included as `src/Unclassified_2222.vi` |
| `Demo.vi` | 949380 | `14fb43f9601534f26df684bd24ba1fa0cdbbac0dca9a043e5805e6e9ed478233` | Included as `src/CameraVision_Demo_v01.vi` |
| `demo/Demo111.vi` | 927203 | `bce4d3e8cf469f96e7b3a17d071cabfdfa9bdaade097bf6d46ebbf9277215aa4` | Included as `src/demo/CameraSerialPrototype_111.vi` |
| `demo/Demo222.vi` | 1056603 | `74e68d9a973fcd783a088a0080fae2ca55a6f3683b870aeda1f8734455f0a94d` | Included as `src/demo/CameraSerialPrototype_222.vi` |
| `demo/Image for Use_0.vi` | 18147 | `7d7cd3ac4da60e27cd176ff033cf85dbcc033dce6c2c362c914a643c93b94df4` | Included as `src/demo/Image for Use_0.vi` |
| `demo/清除.vi` | 8092 | `e403b316d5ddbc589721268fde2a11661371e3c714f76f7eda8d4acecf483b1f` | Included as `src/demo/CloseIMAQdxCamera.vi` |
| `Demo2.vi` | 955573 | `025cacc16a704cef7a8b09959cc2dc37987526689c25df08fafe256f9fcd2e5b` | Included as `src/CameraVision_Demo_v02.vi` |
| `Demo2删除.vi` | 941329 | `c14b93f13ef6241e9e83cae25a5ea96f59ee38d3f67d4f8d255c92e09b054a7f` | Included as `src/CameraSerial_Demo_Legacy.vi` |
| `Demo3.vi` | 1014489 | `48cf5455013a82be7feaf107f898b5ede754e8a613e434d75dae859e6e258ae3` | Included as `src/CameraVision_Demo_v03.vi` |
| `Demo4.vi` | 1039717 | `a9cb78aa473369b985dc387f054b12677849445e7c5a336624a37acf812f1123` | Included as `src/CameraSerialController_v04.vi` |
| `Demo5555.vi` | 1032624 | `2c1f0172c05c3e12e424b517d2e3184e1743bd812887806ec9083ee5c46d2102` | Included as `src/CameraSerialController_Experiment5555.vi` |
| `Demo6.vi` | 1050225 | `a1db53ade790dabb22b1595b932b2008afde8b3ce075af068f5c6e00ba28bdfa` | Included as `src/CameraSerialController_v06.vi` |
| `Demo_20240512.vi` | 1105685 | `98f938ea8b7eca6072df893f61d4c33870683c9e9f5b9080f4fff6a85c29c3c5` | Included as `src/CameraSerialController_2024-05-12.vi` |
| `Demo_new.vi` | 1105012 | `aaf03825fccac1b6aad490e4af40b1839052f7a56b180615f3cbe566d4a4a8ba` | Included as `src/CameraSerialController_2024-04-21.vi` |
| `Demo_sobel.vi` | 1084442 | `b930ee6e362a817da6e35e2875c17f0e8d77ae5470a518eb939b91e8d44a4308` | Included as `src/CameraSobelEdgeDetection.vi` |
| `Demo删除.vi` | 913488 | `8a3900fe989878b4ae5e1c1b4441f365bae2c457f2fd0d594887d0c6cd931e7b` | Included as `src/CameraVision_Demo_Legacy.vi` |
| `Image for Use_0.vi` | 18147 | `562947b810363a2965d49447b521df5c505e08f0071b25c66e969ba6166ae2f9` | Included as `src/Image for Use_0.vi` |
| `Initialize the camera.vi` | 32885 | `6c20d9ae04f4019d8966986573ad28a2307a8ceab85ad03002cd5e2929e3ae35` | Included as `src/InitializeCamera.vi` |
| `LabVIEW串口调试/Document/LabVIEW串口调试.docx` | 14586 | `c4578711554aaa73d5d2e9092bd778be40ee90304f07e2ca35183e7aaf339a23` | Unredacted source excluded; sanitized archival copy included as `docs/original-materials/SerialDebugger_LegacyGuide_Redacted.docx`, with an English transcription in `docs/serial-debugger-guide.md`. |
| `LabVIEW串口调试/Document/serial-tool/[redacted-license-key].txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Excluded: activation/license credential. |
| `LabVIEW串口调试/Document/串口调试助手/serial_port_utility_latest.exe` | 9111882 | `2de4fa536de7e57fa3f37c3c768f7daa0bc89652e8deb2eb7ae13829f423e734` | Excluded: third-party executable without supplied redistribution terms. |
| `LabVIEW串口调试/Document/虚拟串口VSPD6.9/snd.nfo` | 19267 | `651d293fd1332fe8482593926a8d1e71663d99e4f8929fba2b53529d4d26e15d` | Excluded: third-party package metadata. |
| `LabVIEW串口调试/Document/虚拟串口VSPD6.9/vspd.exe` | 3153216 | `aed76560391a34a86641685e7baab8d5c56165568b5ae37a36876dbe9c5f672b` | Excluded: third-party installer without supplied redistribution terms. |
| `LabVIEW串口调试/Document/虚拟串口VSPD6.9/补丁/vspdconfig.exe` | 3623424 | `e71b025cf403c4d311ea3aa65e71ae0bc27b71ed2e22b7c34b323c7677792dd5` | Excluded: patch/crack-related executable. |
| `LabVIEW串口调试/Document/虚拟串口VSPD6.9/补丁/vspdctl.dll` | 139264 | `bc5c66f376e5f6b634f03cc8ed141431f4587498e1af395e99648edc1bf0be31` | Excluded: patch/crack-related binary. |
| `LabVIEW串口调试/LabVIEW串口调试.aliases` | 42 | `3ca4231a53d817f0895a746e88bd9c54c8ea8b49ce78f0b9b259699f492a095d` | Excluded: machine-specific LabVIEW aliases. |
| `LabVIEW串口调试/LabVIEW串口调试.lvlps` | 85 | `70a4e95c1803df66a939a65497aa4df41bce5f0985caa6cbbbaac32d99fca76c` | Excluded: machine/local LabVIEW settings. |
| `LabVIEW串口调试/LabVIEW串口调试.lvproj` | 1820 | `8f496ce4d3b17429f895508a81324837911b504c65263455fbc91dc6f57d59c9` | Included as `src/serial-debugger/SerialDebugger.lvproj` (project XML labels/path references localized) |
| `LabVIEW串口调试/SubVI/Demo/XY图多条曲线显示.vi` | 15388 | `f86b9beec963bcb1bf34d596ba7c04bb27021e737cd377736dcd83850eb451ed` | Included as `src/serial-debugger/SubVI/Demo/PlotMultipleXYCurves.vi` |
| `LabVIEW串口调试/SubVI/Demo/串口通讯Demo.vi` | 25668 | `3677e735798e00df7898d3d6267e2e04e32ec6ab3e57ca716cb0d423347288f1` | Included as `src/serial-debugger/SubVI/Demo/SerialCommunication_Demo.vi` |
| `LabVIEW串口调试/SubVI/Demo/状态机.ctl` | 13183 | `8d482343064fbebd4d9b82b39fcb6c86689ef14ccd7be959d42ce2cd2a614c5c` | Included as `src/serial-debugger/SubVI/Demo/状态机.ctl` |
| `LabVIEW串口调试/SubVI/Demo/状态机0.ctl` | 6220 | `24e20c887ccfd8e909ba39ddc7e8381a09cba32bad9f9f80029589ee26e14f9a` | Included as `src/serial-debugger/SubVI/Demo/状态机0.ctl` |
| `LabVIEW串口调试/User Interface/Planck_UP.vi` | 97881 | `a24c8e93d717f4bcba6b820e8d3320d94a393a5b0ea3a97d2b0129522e4f834a` | Included as `src/serial-debugger/user-interface/PlanckExperiment_Main.vi` |
| `LabVIEW串口调试/User Interface/主程序1 - 副本.vi` | 44015 | `942c0cadaf06ee7c878aed8447bade774669a9535114f3885edd0392c1f4a8cf` | Included as `src/serial-debugger/user-interface/PlanckExperiment_LegacyMain_Copy.vi` |
| `LabVIEW串口调试/User Interface/主程序1.vi` | 44071 | `11fdad5a2699375d4b594b3341bf66723a4d66c716ebc15bd84da9537a5de3b1` | Included as `src/serial-debugger/user-interface/PlanckExperiment_LegacyMain.vi` |
| `上位机.vi` | 24878 | `312e8ce53963a95db7d745ca58260f4551801701a985bf4e79d5848b3109197e` | Included as `src/SerialHostUI.vi` |
| `控件 1.ctl` | 4235 | `ebe0909ce17d9426f4e88eb41d6128c34ecef57df237e2bd219ed56e77d471c1` | Included as `src/控件 1.ctl` |
