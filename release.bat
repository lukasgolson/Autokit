bumpver update --minor
python -m build
twine upload dist/*
@RD /S /Q dist