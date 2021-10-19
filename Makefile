WEBSITE := website
BUILD_DIR := $(WEBSITE)/build
FLASK_ARGS := --port 5000 --host 0.0.0.0 --reload
LATEX_DIR := $(WEBSITE)/other/latex
LATEX_OUT := $(WEBSITE)/static/img/latex
VENV := venv

.DEFAULT_GOAL := server
.PHONY: build clean clean-venv latex love server

build: $(BUILD_DIR)

$(BUILD_DIR): $(VENV) latex
	$(info Running freezer.py)
	@(. $(VENV)/bin/activate && python3 freezer.py)

clean:
	rm -rf $(BUILD_DIR)
	make -C $(LATEX_DIR) clean

clean-venv:
	rm -rf $(VENV)

latex: | $(LATEX_OUT)
	make -C $(LATEX_DIR)
	cp -f $(LATEX_DIR)/*.png $(LATEX_OUT)

$(LATEX_OUT):
	mkdir -p $@

love:
	@echo "<3"

server: $(VENV) latex
	@(. $(VENV)/bin/activate && flask run $(FLASK_ARGS))

$(VENV):
	python3 -m venv $(VENV)
	@(. $(VENV)/bin/activate && pip install -r requirements.txt)

