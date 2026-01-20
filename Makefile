
SHEETS = densita pendolo_fisico conducibilita_termica dad_catenaria ottica oscillazioni_accoppiate random_walk dad_conteggi dad_caduta

all:
	for i in $(SHEETS); do \
		make $$i; \
	done

pdf:
	for i in $(SHEETS); do \
		pdflatex sheets/$$i.tex; \
		pdflatex sheets/$$i.tex; \
	done

%:
	@if [ "$*" != "ottica" ] && [ "$*" != "oscillazioni_accoppiate" ]; then \
		python tools/py2tex.py "snippy/$*.py"; \
	fi
	pdflatex "sheets/$*.tex"

clean:
	rm -f *~ *.aux *.log *.out *.fls *.fdb_latexmk *.synctex.gz

cleanall:
	make clean; rm -f *.pdf *.zip
