@echo off
IF %1.==. GOTO No1
bumpver update %1

:No1
  bumpver update --patch
GOTO End1

:End1






python -m build
twine upload dist/*
@RD /S /Q dist