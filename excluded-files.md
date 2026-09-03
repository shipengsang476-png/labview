# Files Excluded from the GitHub Package

The final package includes every unique LabVIEW source artifact from the original archive and the separately supplied MindVision DLL. The following non-source items were intentionally excluded.

| Original item | Reason for exclusion |
|---|---|
| `LabVIEW串口调试.aliases` | LabVIEW machine-specific alias file; ignored by source control |
| `LabVIEW串口调试.lvlps` | LabVIEW local/project settings; machine-specific |
| Unredacted `Document/LabVIEW串口调试.docx` | Contained third-party activation information; a redacted archival copy is included at `docs/original-materials/SerialDebugger_LegacyGuide_Redacted.docx`, and an English transcription is in `docs/serial-debugger-guide.md` |
| `Document/串口调试助手/serial_port_utility_latest.exe` | Third-party executable; no redistribution terms supplied |
| `Document/serial-tool/[redacted-license-key].txt` | Activation/license credential; must not be published |
| `Document/虚拟串口VSPD6.9/vspd.exe` | Third-party installer; no redistribution terms supplied |
| `Document/虚拟串口VSPD6.9/snd.nfo` | Third-party package metadata unrelated to source code |
| `Document/虚拟串口VSPD6.9/补丁/vspdconfig.exe` | Patch/crack-related executable; not appropriate for a public source repository |
| `Document/虚拟串口VSPD6.9/补丁/vspdctl.dll` | Patch/crack-related binary; not appropriate for a public source repository |

The original archive itself is not embedded in the final repository because it would reintroduce all of the excluded files. Its SHA-256 and disposition are recorded in `docs/source-inventory.md`.
