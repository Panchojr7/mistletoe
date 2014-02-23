"""
Usage:
    Test Build:
        python setup.py build
    MacOS X Distribution:
        python setup.py bdist_dmg
    Windows Distribution (not yet working):
        python setup.py (Eventually will use bdist_nsi)
"""

# Application setup variables
NAME = 'Mistletoe'
VERSION = '0.8'
DESCRIPTION = 'GUI for MOSS'

ENTRYPOINT = 'mistletoe.py'
DATA_FILES = [ 'mistletoe.ui' ]
MODULES = [ 'PySide.QtXml' ]
MAC_ICON = 'mistletoe.icns'
WIN_ICON = 'mistletoe.ico'

# Make sure prereqs are available
import ez_setup
ez_setup.use_setuptools()

import sys
from cx_Freeze import setup, Executable

# Deal with Windows-specific requirements
if sys.platform == 'win32':
    import bdist_nsi
    BASE = 'Win32GUI'
else:
    BASE = None

# Prepare setup options
EXECUTABLES = [ Executable(ENTRYPOINT, base=BASE) ]
FREEZE_OPTIONS = {'includes': MODULES, 'include_files': DATA_FILES, 'icon': WIN_ICON, 'include_msvcr': True }

NSIS_OPTIONS = {}
BUNDLE_OPTIONS = {'iconfile': MAC_ICON, 'bundle_name': NAME }
DMG_OPTIONS = {'volume_label': NAME }
#DMG_OPTIONS = {'volume_label': NAME, 'applications-shortcut': True }

# Perform application setup (execute command)
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    executables = EXECUTABLES,
    options =
    {
        'build_exe': FREEZE_OPTIONS, 'bdist_nsi': NSIS_OPTIONS,
        'bdist_mac': BUNDLE_OPTIONS, 'bdist_dmg': DMG_OPTIONS
    }
)