# AWS Saving Makefile

PACKAGE_NAME = "aws-cdk-test-synth"
YOUR_USERNAME = "bilardi"

.PHONY: help # print this help list
help:
	grep PHONY Makefile | sed 's/.PHONY: /make /' | grep -v grep

.PHONY: unittest # run unit tests
unittest:
	python3 -m unittest discover -v

.PHONY: clean # remove packaging files
clean:
	rm -rf build dist *.egg-info; rm -rf */*pyc; rm -rf */*/*pyc; rm -rf */__pycache__

.PHONY: doc # build documentation
doc: 
	cd docs; make html; cd -

.PHONY: buildtest # build package on testpypi
buildtest: clean
	python3 setup.py sdist bdist_wheel; python3 -m twine upload --repository testpypi dist/*

.PHONY: installtest # install package from testpypi
installtest:
	mkdir -p test; cd test; python3 -m pip install --upgrade --index-url https://test.pypi.org/simple/ --no-deps $(PACKAGE_NAME)-$(YOUR_USERNAME); cd -

.PHONY: build # build package on pypi
build: clean
	python3 setup.py sdist bdist_wheel; python3 -m twine upload dist/*

.PHONY: install # install package from pypi
install:
	python3 -m pip install --upgrade $(PACKAGE_NAME)
