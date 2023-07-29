path='/home/volvo/blackbox'

run:
	@.venv/bin/python -m src $(path);

setup: requirements.txt
	@rm -rf .venv;
	@python3 -m venv .venv;
	@.venv/bin/pip install -r requirements.txt;

setup_dev: requirements-dev.txt
	@rm -rf .venv_dev;
	@python3 -m venv .venv_dev;
	@.venv_dev/bin/pip install -r requirements-dev.txt;

test:
	@.venv_dev/bin/python -m unittest;

clean:
	@rm -rf build;
	@rm -rf .venv;
	@rm -rf .venv_dev;
	@rm -rf __pycache__;
	@rm -rf tests/__pycache__;
	@rm -rf tests/lib/__pycache__;
	@rm -rf src/__pycache__;
	@rm -rf src/lib/__pycache__;