import sys
import os
import re


class LTPathFinder:
    """Finds and returns LTSpice path if not provided by the user."""

    not_implemented_string = "Platforms other than Mac, Windows and Linux (wine) are not implemented yet"

    @staticmethod
    def find_exe_ltspice_path(ltspice_path=None):
        if ltspice_path:
            ltpath = ltspice_path
        else:
            if sys.platform == 'darwin':
                ltpath = "/Applications/LTspice.app/Contents/MacOS/LTspice"
            elif sys.platform == 'win32':
                candidates = [
                    "C:\\Program Files\\ADI\\LTspice\\LTspice.exe",
                    os.path.join(os.path.expanduser('~'), "AppData", "Local", "Programs", "ADI", "LTspice",
                                 "LTspice.exe"),
                    "C:\\Program Files\\LTC\\LTspiceXVII\\XVIIx64.exe",
                ]
                ltpath = next((c for c in candidates if os.path.exists(c)), candidates[0])
            elif sys.platform == 'linux':
                ltpath = os.path.join(os.path.expanduser('~'), '.wine', 'drive_c', 'Program Files', 'LTC',
                                      'LTspiceXVII', 'XVIIx64.exe')
                ltpath = re.sub(' ', '\ ', ltpath)
            else:
                raise NotImplementedError(LTPathFinder.not_implemented_string)
        if os.path.exists(ltpath) and os.access(ltpath, os.X_OK):  # Check if it is an executable.
            return ltpath
        else:
            raise FileNotFoundError(f"The executable path: {ltpath} could not be found or I cannot access it.")

    @staticmethod
    def find_sym_folder(sym_folder=None):
        if sym_folder:
            _sym_folder = sym_folder
        else:
            if sys.platform == 'darwin':
                _sym_folder = os.path.join(os.path.expanduser('~'),
                                           "Library", "Application Support", "LTspice", "lib", "sym")
            elif sys.platform == 'win32':
                candidates = [
                    "C:\\Program Files\\ADI\\LTspice\\lib\\sym",
                    os.path.join(os.path.expanduser('~'), "AppData", "Local", "LTspice", "lib", "sym"),
                    "C:\\Program Files\\LTC\\LTspiceXVII\\lib\\sym",
                ]
                _sym_folder = next((c for c in candidates if os.path.isdir(c)), candidates[0])
            elif sys.platform == 'linux':
                _sym_folder = os.path.join(os.path.expanduser('~'), 'Documents', 'LTspiceXVII', 'lib', 'sym')
            else:
                _sym_folder = None
                raise NotImplementedError(LTPathFinder.not_implemented_string)

        if os.path.exists(_sym_folder) and os.path.isdir(_sym_folder):
            return _sym_folder
        else:
            raise FileNotFoundError(f"Folder {_sym_folder} is no a valid symbols folder.")

    @staticmethod
    def find_cmd_sep():
        if sys.platform == 'darwin':
            return '; '
        elif sys.platform == 'win32':
            return ' && '
        elif sys.platform == 'linux':
            return '; '
        else:
            raise NotImplementedError(LTPathFinder.not_implemented_string)
