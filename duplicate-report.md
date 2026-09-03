# Duplicate and Existing-Repository Report

## Separately uploaded files

| Uploaded file | SHA-256 | Final representation | Result |
|---|---|---|---|
| `Demo_20240512(1).vi` | `98f938ea8b7eca6072df893f61d4c33870683c9e9f5b9080f4fff6a85c29c3c5` | `src/CameraSerialController_2024-05-12.vi` | Exact byte-for-byte duplicate; stored once |
| `Image for Use_0(1).vi` | `7d7cd3ac4da60e27cd176ff033cf85dbcc033dce6c2c362c914a643c93b94df4` | `src/demo/Image for Use_0.vi` | Exact byte-for-byte duplicate; stored once |
| `MVCAMSDK(1).dll` | `8b2e43458102257bbbb4de0bfb4c7f61a9dcb94c17f8d035ae48462cfd041a7a` | `third_party/mindvision/bin/win32/MVCAMSDK.dll` | Unique supplied dependency; added with the vendor-standard filename |

## Same-name image helper files

The repository contains two files named `Image for Use_0.vi`:

- `src/Image for Use_0.vi` — SHA-256 `562947b810363a2965d49447b521df5c505e08f0071b25c66e969ba6166ae2f9`
- `src/demo/Image for Use_0.vi` — SHA-256 `7d7cd3ac4da60e27cd176ff033cf85dbcc033dce6c2c362c914a643c93b94df4`

They have the same size but different hashes. They are not duplicates and may serve different callers, so both are retained.

## Duplicates inside the final source tree

No two `.vi`, `.ctl`, or `.lvproj` files in the final source tree have the same SHA-256 hash.

## Existing GitHub repository comparison

Comparison reference: `https://github.com/shipengsang476-png/labview`, inspected on 2026-09-03.

The repository's published `manifest.csv` lists the same 26 VI hashes, 3 CTL hashes, and 1 LVPROJ hash as the supplied source set. Therefore most LabVIEW program content already online is duplicate content and should be replaced in place rather than uploaded as a second tree.

The live GitHub tree is not consistent with that manifest:

- `src/LabVIEW/User Interface/` exposes only `PlanckExperiment_Main.vi`; the two legacy VIs listed by the manifest are absent.
- the root dependency control is displayed as `src/1.ctl` instead of `src/控件 1.ctl`;
- the two serial-project controls are displayed as `clt.ctl` and `s.ctl` instead of `状态机0.ctl` and `状态机.ctl`;
- the serial project directory is `src/LabVIEW/`, while the old README/manifest still refer to a previous Chinese directory name.

This final package restores the two missing legacy VIs, uses the descriptive English directory `src/serial-debugger/`, and restores all three dependency-sensitive control filenames. Upload by replacement, not by addition, to avoid parallel old/new directories and broken LabVIEW links.
