#install requirements to run the program
install:
	@echo "Installing Requirements"
	python -m venv venv
	bash -c "source venv/bin/activate && pip install pandas Flask Flask-Scss Flask-SQLAlchemy"
	@echo "Requirements Installed"

#install requirements and linting+formatting tools
install-dev:
	@echo "Installing Requirements and Tools"
	python -m venv venv
	bash -c "source venv/bin/activate && pip install pandas Flask Flask-Scss Flask-SQLAlchemy black pylint"
	@echo "Requirements and Tools Installed"

#run the site app
run:
	@echo "Running Site"
	python3 app.py

#format and lint a file given from input
format:
	@if [ -z "$(file)" ]; then \
		echo "Error: Please specify a file using 'make formatted file=<filename>'"; \
		exit 1; \
	fi
	@echo "Formatting $(file)..."
	bash -c "source venv/bin/activate && black $(file)"
	@echo "File $(file) has been formatted."
	bash -c "source venv/bin/activate && pylint $(file)"
