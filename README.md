# P vs NP / Dean

> **Public page:** https://redogit.github.io/pnp-dean/ · **Main / About:** https://redogit.github.io/redogit/

Solvers, probes, proofs, contracts, and evidence for the declared research scope.

This export preserves original source paths and bytes. Necessary cross-project dependencies are copied with explicit provenance; ownership and historical evidence remain with their source projects.

## Start here

- [Dean probes and records](<redogit/research/pnp/README.md>)
- [PNP repair implementation](<Other-Projects-/projects/research/P versus NP Repair Lab/README.md>)

## Validate locally

Preparation used Python 3.12.14 and Node.js 24.19.0 for the included Python/Node checks. Coordinate-space checks additionally use the pinned NumPy requirement in their source directory. RMAL builds require CMake 3.25 or later and a C23/C++23 compiler; Clang 19 was tested. No package downloads or remote mutations are performed by the validation runner.

```sh
python validate.py --integrity-only
python validate.py
```

Individual checks can be selected with `--check NAME`; names and exact commands are in `VALIDATE.json`. For RMAL, select a suitable compiler with `CC` and `CXX`; `CMAKE` and `CTEST` may specify executable paths.

## Provenance and limits

- `EXPORT_PROVENANCE.json` is the unchanged historical scope snapshot and original file inventory. Its initial candidate status is historical, not a fresh readiness result.
- `EXPORT_DEPENDENCIES.json` records every additional source file and explicit compatibility/validation repair.
- `EXPORT_EXCLUSIONS.json` keeps all fifteen original withheld paths absent. No private-origin publication approval is inferred.
- `VALIDATION_STATUS.json` records the latest export checks and remaining limitations.
- Original source history remains unchanged in the original repositories; this export does not import unrelated commit history.
- Existing commercial-access policy files and licenses remain in their original source paths. No new license grant is implied.

Source READMEs, workflows under source subdirectories, manifests, and evidence remain historical bytes. Their references to original repository layouts or prior deployments are not claims that a new deployment exists. Use this root validation runner for this export. Full browser, Windows/Android and native LLVM/MLIR validation is outside the tested scope.

## Recovered native source

The exact original `GYRO-DEAN-4-source.zip` is preserved under `recovery/`. Missing native dependencies were restored byte-for-byte; `NATIVE_RECOVERY_MANIFEST.json` records hashes, modes and archive origins. Four shared code/test files match; three differing historical documentation files retain their Git versions, with archive originals preserved in the ZIP. `python validate.py` now verifies identity, builds the C++20 implementation in a temporary directory, and runs both native test executables. See `NATIVE_RECOVERY_VALIDATION.json` for fresh validation evidence and limitations.

The uploaded extended archive has identical source and additional generated build products; those products were not imported. Native tests provide finite implementation evidence, not a proof of P=NP or a universal polynomial runtime bound. Existing licenses, access policies and explicit exclusions are retained without a new license grant.
