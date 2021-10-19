BUILD_DIR := website/build
FLASK_ARGS := --port 5000 --host 0.0.0.0 --reload
LATEX_DIR := website/other/latex
LATEX_OUT := $(BUILD_DIR)/static/img/latex
VENV := venv

.DEFAULT_GOAL := server
.PHONY: build clean clean-venv latex love server

build: $(BUILD_DIR)

$(BUILD_DIR): $(VENV) latex
	$(info Running freezer.py)
	@(. $(VENV)/bin/activate && python3 freezer.py)
	mkdir -p $(LATEX_OUT)
	cp $(LATEX_DIR)/*.png $(LATEX_OUT)

clean:
	rm -rf $(BUILD_DIR)
	make -C $(LATEX_DIR) clean

clean-venv:
	rm -rf $(VENV)

latex:
	make -C $(LATEX_DIR)

love:
	@echo "<3"

server: $(VENV)
	@(. $(VENV)/bin/activate && flask run $(FLASK_ARGS))

$(VENV):
	python3 -m venv $(VENV)
	@(. $(VENV)/bin/activate && pip install -r requirements.txt)

