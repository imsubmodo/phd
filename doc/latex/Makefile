
TOP = text

SRC += packages/package.tex
SRC += styles/style.tex
SRC += names/name.tex
SRC += references/reference.tex
SRC += $(TOP).bib
SRC += $(TOP).tex

$(TOP).pdf: $(SRC)
	pdflatex $(TOP)
	bibtex $(TOP)
	pdflatex $(TOP)
	pdflatex $(TOP)

clean:
	@rm -rf *.aux *.log *.out *.bbl *.blg

clean_all: clean
	@rm -rf *.pdf
