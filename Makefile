install:
	cp neoterm-apt-repo $(PREFIX)/bin/neoterm-apt-repo

pypi:
	rm -Rf dist/ build/ neoterm_apt_repo.egg-info/
	python3 setup.py sdist bdist_wheel egg_info
	twine upload dist/*

.PHONY: install pypi
