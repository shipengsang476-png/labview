# Serial Debugger Project Guide

This page is an English, sanitized transcription of the useful material in the original Word document. A redacted archival copy of that document is available at `docs/original-materials/SerialDebugger_LegacyGuide_Redacted.docx`.

## Original preparation list

- LabVIEW application structure: state machine
- A virtual serial-port pair, when no physical loopback pair is available
- A serial-port test utility

The original document named specific third-party installers and contained activation information. Those files and credentials are not included in this repository.

## Baud rate note

The source note describes baud rate as the amount of signaling/data transferred per unit time. Common values listed in the original material were:

```text
1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200
```

Both ends of a serial connection normally need compatible settings for baud rate, data bits, parity, and stop bits.

## Opening the project

1. Install LabVIEW and NI-VISA.
2. Open `src/serial-debugger/SerialDebugger.lvproj`.
3. Start with `user-interface/PlanckExperiment_Main.vi`.
4. Select the correct VISA/COM resource.
5. Match the connected device's serial settings.
6. If the VI reports a missing state-machine control, relink it to `SubVI/Demo/状态机.ctl` and save the caller.

## Testing without the original third-party utilities

Use a legally licensed serial terminal and, if required, a legally licensed virtual serial-port implementation. The repository does not endorse or redistribute the installers that appeared in the source archive.
