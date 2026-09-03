# MindVision Camera SDK and `MVCAMSDK.dll`

## Purpose

`MVCAMSDK.dll` is a Windows native library used by MindVision camera software. Several supplied VIs contain LabVIEW Call Library Function Nodes configured for this library. Static inspection found function names including:

- `CameraEnumerateDeviceEx`
- `CameraInitEx`
- `CameraGetImageBufferEx3`
- `CameraGetImageBufferPriorityEx3`
- `CameraSdkClean`

This only confirms that the calls are present. It does not verify that every parameter definition is correct for the connected camera or SDK version.

## Bundled file

| Property | Value |
|---|---|
| Repository path | `third_party/mindvision/bin/win32/MVCAMSDK.dll` |
| Uploaded name | `MVCAMSDK(1).dll` |
| File version | `2.1.10.116` |
| Format | Windows PE32 DLL |
| Architecture | Intel i386 / x86 / 32-bit |
| Size | 9,115,248 bytes |
| SHA-256 | `8b2e43458102257bbbb4de0bfb4c7f61a9dcb94c17f8d035ae48462cfd041a7a` |
| PE timestamp | 2019-07-24 09:58:14 UTC |

The PE timestamp is a build clue, not a reliable release date.

## Architecture requirement

A 32-bit DLL must be loaded by a 32-bit process. Therefore this exact file requires 32-bit LabVIEW on Windows. A 64-bit LabVIEW installation needs a compatible 64-bit MindVision library and a review of every Call Library Function Node parameter type.

## Driver and SDK requirement

The DLL alone is not a complete camera installation. Typical runtime requirements include:

- the correct Windows device driver;
- the rest of the MindVision Camera Platform/SDK runtime;
- a supported camera and interface configuration;
- 32-bit LabVIEW for this DLL;
- NI Vision/IMAQ components used by the selected VI.

Install the official vendor package first and confirm camera operation with the vendor utility.

## Library discovery

The supplied VIs appear to refer to the bare library name `MVCAMSDK.dll`. LabVIEW can locate a named library through the process search path. The included launcher temporarily prepends the repository DLL directory to `PATH` for the launched LabVIEW process:

```bat
scripts\start-labview-with-mindvision-dll.cmd "C:\Program Files (x86)\National Instruments\LabVIEW 2015\LabVIEW.exe"
```

The script does not install drivers and does not permanently modify the system environment.

Official NI references:

- https://www.ni.com/docs/en-US/bundle/labview/page/configuring-the-call-library-function-node.html
- https://www.ni.com/docs/en-US/bundle/labview/page/specifying-the-location-of-shared-libraries-on-disk.html

## Suggested test order

1. Verify the camera in the MindVision utility.
2. Start 32-bit LabVIEW with the SDK environment or the included launcher.
3. Run `src/InitializeCamera.vi`.
4. Open a camera controller VI.
5. Resolve any missing NI Vision, NI-VISA, or custom-control dependencies.
6. Review Call Library Function Node parameter types before extended operation.

## Common failures

| Symptom | Likely cause |
|---|---|
| DLL not found | Search path does not contain the DLL, or vendor SDK is not installed |
| Not a valid Win32 application / load failure | 64-bit LabVIEW is attempting to load the 32-bit DLL |
| Function not found | SDK version or exported function name differs |
| Camera list is empty | Driver, cable, permissions, interface, or camera compatibility issue |
| LabVIEW crash in a DLL call | Incorrect pointer, buffer, structure, calling convention, or parameter width |

## Redistribution

No redistribution license was supplied with the DLL. Review `THIRD_PARTY_NOTICES.md` before publishing it in a public repository.
