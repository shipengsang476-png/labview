# LabVIEW Physics Competition Project

This repository consolidates the LabVIEW files supplied for a university physics competition project. It contains MindVision industrial-camera acquisition, NI Vision image processing, NI-VISA serial communication, NI-DAQmx digital-output experiments, and a Planck-constant serial user interface.

## Repository contents

- **26** LabVIEW VIs (`.vi`)
- **3** LabVIEW controls/type definitions (`.ctl`)
- **1** LabVIEW project (`.lvproj`)
- **1** MindVision camera SDK library (`MVCAMSDK.dll`)
- **1** sanitized archival Word guide (`.docx`) with activation information removed
- English documentation, source provenance, duplicate analysis, checksums, and upload instructions

The two VIs that were uploaded separately are byte-for-byte duplicates of files already present in the original material, so they are represented once rather than stored twice. The supplied DLL is unique and has been added under `third_party/`.

> **Camera compatibility:** the bundled `MVCAMSDK.dll` is a Windows **32-bit x86** DLL, version **2.1.10.116**. Use 32-bit LabVIEW with this file. The DLL does not replace the MindVision device driver or the rest of the vendor SDK.

A Chinese overview is available in [`README.zh-CN.md`](README.zh-CN.md).

## Recommended entry points

| File | Purpose | Main dependencies |
|---|---|---|
| `src/InitializeCamera.vi` | Enumerate and initialize a MindVision camera | 32-bit LabVIEW, MindVision SDK/driver |
| `src/CameraSobelEdgeDetection.vi` | Camera acquisition, serial control, and Sobel/edge detection | MindVision SDK, NI Vision, NI-VISA |
| `src/CameraSerialController_2024-05-12.vi` | Camera and serial controller snapshot dated 2024-05-12 | MindVision SDK, NI Vision, NI-VISA |
| `src/DAQmxDigitalOutput_2019-11-01.vi` | NI-DAQmx digital-output experiment | NI-DAQmx; also contains camera-related calls |
| `src/serial-debugger/SerialDebugger.lvproj` | Serial debugger and Planck experiment project | NI-VISA |
| `src/serial-debugger/user-interface/PlanckExperiment_Main.vi` | Main Planck experiment interface | NI-VISA and a state-machine control |

## Directory layout

```text
.
├── README.md
├── README.zh-CN.md
├── THIRD_PARTY_NOTICES.md
├── manifest.csv
├── SHA256SUMS.txt
├── docs/
│   ├── duplicate-report.md
│   ├── excluded-files.md
│   ├── github-update.md
│   ├── mindvision-camera-sdk.md
│   ├── original-materials/
│   │   └── SerialDebugger_LegacyGuide_Redacted.docx
│   ├── name-map.csv
│   ├── renaming-notes.md
│   ├── serial-debugger-guide.md
│   └── source-inventory.md
├── scripts/
│   ├── start-labview-with-mindvision-dll.cmd
│   └── verify-manifest.py
├── src/
│   ├── Camera*.vi
│   ├── DAQmx*.vi
│   ├── Serial*.vi
│   ├── demo/
│   └── serial-debugger/
└── third_party/
    └── mindvision/bin/win32/MVCAMSDK.dll
```

## Required software

The original project metadata identifies LabVIEW 2015. Depending on the VI being opened, the following components may be required:

- 32-bit LabVIEW 2015, or a compatible later 32-bit LabVIEW version
- NI-VISA for serial communication
- NI Vision Development Module for image-processing functions
- NI Vision Acquisition Software for IMAQdx access
- NI-DAQmx for the digital-output experiment
- MindVision Camera Platform/SDK and the matching camera driver

Camera, serial, and NI DAQ hardware are also required for full runtime testing. A newer LabVIEW or driver version may ask you to relink dependencies and resave the VIs.

## MindVision camera setup

1. Install 32-bit LabVIEW and the NI modules required by the selected VI.
2. Install the official MindVision Camera Platform/SDK and driver for the camera model.
3. Confirm camera operation with the vendor utility before testing LabVIEW.
4. Make `MVCAMSDK.dll` discoverable. The preferred method is the vendor-installed SDK environment. A temporary launcher is also included:

```bat
scripts\start-labview-with-mindvision-dll.cmd "C:\Program Files (x86)\National Instruments\LabVIEW 2015\LabVIEW.exe"
```

5. Run `src/InitializeCamera.vi` first.
6. Then open `src/CameraSerialController_2024-05-12.vi` or `src/CameraSobelEdgeDetection.vi`.
7. If LabVIEW reports a missing DLL, VI, or control, relink the node to the file in this repository and save all callers.

See [`docs/mindvision-camera-sdk.md`](docs/mindvision-camera-sdk.md) for architecture, checksum, search-path, and troubleshooting details.

## Serial debugger project

1. Install LabVIEW and NI-VISA.
2. Open `src/serial-debugger/SerialDebugger.lvproj`.
3. Open `user-interface/PlanckExperiment_Main.vi` or one of the two legacy main VIs.
4. Configure the COM port, baud rate, data bits, stop bits, and parity for the connected device.
5. If a control is missing, relink it to `SubVI/Demo/` and save the caller.

The original serial-debugger note has been translated and sanitized in [`docs/serial-debugger-guide.md`](docs/serial-debugger-guide.md). A redacted archival copy is retained at [`docs/original-materials/SerialDebugger_LegacyGuide_Redacted.docx`](docs/original-materials/SerialDebugger_LegacyGuide_Redacted.docx). Third-party installers, activation information, and patch files from the source archive are intentionally not included.

## English naming and compatibility exceptions

All directories and all safely renameable entry-point VIs use English names. Three Chinese control filenames remain because the supplied VIs store those exact dependency names internally:

- `src/控件 1.ctl` — suggested future name: `CameraControl.ctl`
- `src/serial-debugger/SubVI/Demo/状态机.ctl` — suggested future name: `StateMachine.ctl`
- `src/serial-debugger/SubVI/Demo/状态机0.ctl` — suggested future name: `StateMachineLegacy.ctl`

Renaming these three files only in Windows Explorer or Git would likely break callers. Open the full hierarchy in LabVIEW, use **Save As / Rename**, and save every caller before committing the new names. Details are in [`docs/renaming-notes.md`](docs/renaming-notes.md).

## Duplicate and existing-repository comparison

The current GitHub repository's published manifest lists the same 30 LabVIEW source hashes, so most program content overlaps with this package. The live tree is out of sync with that manifest: it exposes only one of the three serial-project UI VIs, and its three controls were manually renamed to `src/1.ctl`, `clt.ctl`, and `s.ctl`. This package restores the two missing legacy VIs, normalizes the serial project to `src/serial-debugger/`, and restores the original dependency-sensitive control filenames so binary callers can locate them.

See [`docs/duplicate-report.md`](docs/duplicate-report.md) for exact hashes and [`docs/github-update.md`](docs/github-update.md) for replacing the existing repository without leaving duplicate folders behind.

## Integrity verification

`manifest.csv` lists every repository file except the manifest itself. `SHA256SUMS.txt` contains standard SHA-256 entries for repository content files and excludes the two checksum metadata files to avoid circular hashes. To verify the package after extraction:

```bash
python scripts/verify-manifest.py
```

## Publishing and licensing

No open-source license was supplied for the LabVIEW source. Do not add a license unless the ownership and licensing terms are known.

`MVCAMSDK.dll` is a third-party MindVision binary and is not covered by any license for the surrounding project. Before making the repository public, confirm that you are allowed to redistribute this DLL. If redistribution cannot be confirmed, remove `third_party/mindvision/bin/win32/MVCAMSDK.dll` and keep the documentation that directs users to the vendor SDK.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Validation limits

The package has been checked for archive integrity, file counts, hashes, duplicate content, XML validity, and excluded unsafe/proprietary source-archive items. The LabVIEW block diagrams were not executed because this environment does not contain LabVIEW or the required hardware.
