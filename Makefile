.PHONY: install
install:
	pip install --no-cache-dir .

.PHONY: install-dev
install-dev:
	pip install --upgrade pip
	pip install --no-cache-dir -e .[dev]

.PHONY: name
name:
	$(eval DO_INSTALL := $(python3 ./zdevelop/make_scripts/make_name.py $(n)))
	sleep 1
	cd ../$(n)-py/
	ifeq (DO_INSTALL, 1)
		pip install --no-cache-dir -e .[dev]
	endif

.PHONY: version
version:
	bumpversion patch
	$(eval VERSION := $(shell python ./zdevelop/make_scripts/make_version.py))
	git commit -am '_version file update'

version-minor:
	bumpversion minor

version-major:
	bumpversion major

version-reset:
	bumpversion --new-version 0.0.0 patch

.PHONY: test
test:
	-pytest
	sleep 1
	open ./zdevelop/tests/_reports/coverage/index.html
	open ./zdevelop/tests/_reports/test_results.html

.PHONY: lint
lint:
	-flake8
	-black . --diff
	-mypy .

.PHONY: venv
venv:
ifeq ($(py), )
	$(eval PY_PATH := python3)
else
	$(eval PY_PATH := $(py))
endif
	$(eval VENV_PATH := $(shell $(PY_PATH) ./zdevelop/make_scripts/make_venv.py))
	@echo "venv created!"
	@echo "to enter virtual env, run '. ~/.bash_profile', then '$(VENV_PATH)'"

.PHONY: format
format:
	-autopep8 --in-place --recursive --aggressive .
	-black .

.PHONY: doc
doc:
	python setup.py build_sphinx -E
	sleep 1
	open ./zdocs/build/html/index.html
