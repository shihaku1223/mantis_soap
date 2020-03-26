python3 setup.py sdist bdist_wheel
python3 -m twine upload \
  -u $pypi_user \
  -p $pypi_pass \
  --repository-url http://10.155.47.34/ipf3-offshore/pypi/ dist/*
