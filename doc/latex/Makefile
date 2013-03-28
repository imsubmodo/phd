
# Makefile to compilation latex sources
#
# @author Medvedev Ilya
# @email imedvedev@elvees.com


# VARIABLES

PROJECT_NAME = text

SRC += packages/package.tex
SRC += styles/style.tex
SRC += contents/contents.tex
SRC += chapters/review.tex
SRC += chapters/generation.tex
SRC += chapters/rtl.tex
SRC += chapters/verification.tex
SRC += names/name.tex
SRC += references/reference.tex
SRC += $(PROJECT_NAME).bib
SRC += $(PROJECT_NAME).tex


# TARGETS

$(PROJECT_NAME).pdf: $(SRC)
	pdflatex $(PROJECT_NAME)
	bibtex $(PROJECT_NAME)
	pdflatex $(PROJECT_NAME)
	pdflatex $(PROJECT_NAME)

clean:
	# clean temporal files
	@find . -name "*~" -exec rm -rf {} \;
	@find . -name "*.swp" -exec rm -rf {} \;
	# clean speciefic latex files
	@rm -rf *.aux *.log *.out *.bbl *.blg

clean_all: clean
	@rm -rf *.pdf

