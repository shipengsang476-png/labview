# LabVIEW File Renaming and Dependency Notes

## Why three Chinese filenames remain

LabVIEW `.vi` and `.ctl` files are binary resources that can store dependency paths. Static inspection found the following exact filenames embedded in callers:

| Retained filename | Known callers | Suggested future English name |
|---|---|---|
| `src/控件 1.ctl` | Several camera/serial controller VIs | `CameraControl.ctl` |
| `src/serial-debugger/SubVI/Demo/状态机.ctl` | `PlanckExperiment_Main.vi` | `StateMachine.ctl` |
| `src/serial-debugger/SubVI/Demo/状态机0.ctl` | The two legacy Planck main VIs | `StateMachineLegacy.ctl` |

Changing these filenames only in the operating system or Git changes the file on disk but does not update binary callers. NI recommends renaming LabVIEW files through LabVIEW so callers and project items can be updated.

Official NI reference:

- https://www.ni.com/docs/en-US/bundle/labview/page/renaming-files-and-project-items.html

## Safe future procedure

1. Make a clean Git commit before renaming.
2. Open the complete project/calling hierarchy in LabVIEW.
3. Confirm all current dependencies resolve.
4. Use **File > Save As** with the rename option, or the project rename operation.
5. Save every caller and the project.
6. Close and reopen the project to verify there are no missing items.
7. Commit the rename and all caller changes together.

## Renames performed in this package

- Entry VIs that are not referenced by other supplied files were renamed to descriptive English names.
- The serial project root was renamed to `serial-debugger` while keeping the relative `SubVI/Demo` layout used by the VIs.
- The two legacy main VIs were renamed to English because no other supplied binary contains their old filenames.
- The three dependency-sensitive controls were not renamed.
- `Image for Use_0.vi` remains unchanged because multiple VIs reference that exact English filename.
