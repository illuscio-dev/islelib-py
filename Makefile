install:
	pip install --no-cache-dir .

install-dev:
	pip install --upgrade pip
	pip install --no-cache-dir -e .[dev]

name:
	$(eval DO_INSTALL := $(python3 ./zdevelop/make_scripts/make_name.py $(n)))
	sleep 1
	cd ../$(n)-py/
	ifeq (DO_INSTALL, 1)
		pip install --no-cache-dir -e .[dev]
	endif

version:
	bumpversion patch
	python ./zdevelop/make_scripts/make_version.py

version-minor:
	bumpversion minor

version-major:
	bumpversion major

version-reset:
	bumpversion --new-version 0.0.0 patch

test:
	-pytest
	sleep 1
	open ./zdevelop/tests/_reports/coverage/index.html
	open ./zdevelop/tests/_reports/test_results.html

lint:
	-flake8
	-black . --diff
	-mypy .

venv:
ifeq ($(py), )
	$(eval PY_PATH := python3)
else
	$(eval PY_PATH := $(py))
endif
	$(eval VENV_PATH := $(shell $(PY_PATH) ./zdevelop/make_scripts/make_venv.py))
	@echo "venv created!"
	@echo "to enter virtual env, run '. ~/.bash_profile', then '$(VENV_PATH)'"

format:
	-autopep8 --in-place --recursive --aggressive .
	-black .

doc:
	python setup.py build_sphinx -E
	sleep 1
	open ./zdocs/build/html/index.html

mock:
ifeq ($(py), )
	@echo True
else
	@echo False
endif
