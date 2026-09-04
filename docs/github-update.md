# Updating the Existing GitHub Repository

Target repository:

```text
https://github.com/shipengsang476-png/labview
```

The existing repository already contains the main LabVIEW source set. Replace the repository contents rather than uploading the new folders on top of the old tree. Otherwise both `src/LabVIEW/` and `src/serial-debugger/`, or both `src/1.ctl` and `src/控件 1.ctl`, may remain.

## Recommended Git workflow

1. Extract `labview-github-complete-en.zip` to a temporary directory.
2. Clone the existing repository:

```bash
git clone https://github.com/shipengsang476-png/labview.git
cd labview
```

3. Remove the tracked working-tree contents while preserving `.git`:

```bash
git rm -r .
```

4. Copy **all contents inside the extracted `labview/` folder** into the cloned repository root. Include hidden files such as `.gitignore` and `.gitattributes`.
5. Review the change set:

```bash
git status
git diff --stat
```

6. Commit and push:

```bash
git add -A
git commit -m "Consolidate LabVIEW sources and MindVision dependency"
git push origin main
```

## Expected structural changes

- `src/LabVIEW/` is replaced by `src/serial-debugger/`.
- `src/1.ctl`, `clt.ctl`, and `s.ctl` are replaced by their original dependency-sensitive control filenames.
- The two legacy main VIs that are absent from the live tree are restored with English names under `src/serial-debugger/user-interface/`.
- README and manifest files are replaced with the complete English set.
- MindVision DLL documentation, source inventory, duplicate report, scripts, and third-party notices are added.

## Browser upload note

The bundled DLL is below GitHub's browser per-file limit, but browser uploads can miss hidden files and make deletion/rename cleanup awkward. Git command-line upload is strongly preferred for this replacement.

GitHub documentation:

- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
