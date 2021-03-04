import sys
from cx_Freeze import setup, Executable

bdist_msi_options = {
    "add_to_path": True
    }

exe = Executable(
      script="microCheck.py",
      base=None,
      targetName="microCheck.exe"
     )

setup(
      name="microCheck",
      version="10.0",
      author="Jan Hamacek / nicx321",
      description="Nástroj pro kontrolu programů v C",
      executables=[exe],
      scripts=['microCheck.py'],
      options={'bdist_msi': bdist_msi_options}
      ) 