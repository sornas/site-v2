TEX := $(wildcard *.tex)
PDF := $(TEX:.tex=.pdf)
PNG := $(PDF:.pdf=.png)

.PHONY: all clean

all: ${PDF} ${PNG}

%.pdf: %.tex
	$(info Building $@)
	@latexmk -pdf -f -interaction=nonstopmode $< &>/dev/null

%.png: %.pdf
	$(info  Converting $@)
	@convert -density 960 -quality 100 $< $@ &>/dev/null

clean:
	@latexmk -C
	@rm -f *.png
