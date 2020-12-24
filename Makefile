.PHONY: setup venv update clean

PYTHON = python3.8

# ----- Setup -----

setup:
	apt-get install --no-install-recommends -y \
		$(PYTHON) \
		$(PYTHON)-venv \
		$(PYTHON)-dev \
		python3-dev \
		python3-pip

# ----- Virtualenv -----

venv:
	@if [ ! -f "venv/bin/activate" ]; then $(PYTHON) -m venv venv ; fi;

# ----- Update -----

update:
	@echo "----- Updating requirements -----"
	@$(PYTHON) -m pip install --upgrade wheel pip setuptools
	@$(PYTHON) -m pip install --upgrade --requirement requirements.txt

# ----- Clean -----

clean:
	-@find . \( \
		-name "__pycache__" -o \
		-name "*.pyc" -o \
		-name ".cache" -o \
		-name ".eggs" -o \
		-name "*.egg-info" \) \
		-prune \
		-exec rm -rf {} \;
	@rm -f .coverage
	@rm -rf .pytest_cache
	@rm -rf .cov_html
	@rm -rf build
	@rm -rf dist
