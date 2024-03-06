bumpver update --patch
python -m build
twine upload dist/*
@RD /S /Q dist