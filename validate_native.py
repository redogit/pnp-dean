#!/usr/bin/env python3
"""Verify recovered archive bytes and build/run both native test executables."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import tempfile

export = Path(__file__).resolve().parent
manifest = json.loads((export/'NATIVE_RECOVERY_MANIFEST.json').read_text())
assert hashlib.sha256((export/manifest['source_archive']).read_bytes()).hexdigest() == manifest['source_archive_sha256']
for item in manifest['imported_missing_files']:
    p = export/item['path']
    data = p.read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256'], item['path']
    assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == item['git_blob']
    assert bool(p.stat().st_mode & 0o111) == (item['mode'] == '100755')
root = export/'Other-Projects-/projects/research/P versus NP Repair Lab/GYRO-DEAN-4'
with tempfile.TemporaryDirectory(prefix='gyro-dean-native-') as build:
    # The original tests use assert(), so keep NDEBUG disabled.
    subprocess.run([os.environ.get('CMAKE', 'cmake'), '-S', str(root), '-B', build, '-DCMAKE_BUILD_TYPE=Debug'], check=True, timeout=120)
    subprocess.run([os.environ.get('CMAKE', 'cmake'), '--build', build, '--parallel', '2'], check=True, timeout=240)
    subprocess.run([os.environ.get('CTEST', 'ctest'), '--test-dir', build, '--verbose', '--output-on-failure', '--timeout', '120'], check=True, timeout=240)
print('PASS recovered native source identity, C++ build and both native tests', flush=True)
