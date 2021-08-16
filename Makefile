BUILD_DIR := website/build
FLASK_ARGS := --port 5000 --host 0.0.0.0 --reload
VENV := venv

.DEFAULT_GOAL := server
.PHONY: build clean clean-venv love server 

build: $(BUILD_DIR)

$(BUILD_DIR): $(VENV)
	@(. $(VENV)/bin/activate && python3 freezer.py)

clean:
	rm -rf $(BUILD_DIR)

clean-venv:
	rm -rf $(VENV)

love:
	@echo "<3"

server: $(VENV)
	@(. $(VENV)/bin/activate && flask run $(FLASK_ARGS))

$(VENV):
	python3 -m venv $(VENV)
	@(. $(VENV)/bin/activate && pip install -r requirements.txt)

