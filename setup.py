from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["colorama"]}


setup(
    name="Collège Simulator",
    version="0.3.0",
    description="no",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)
