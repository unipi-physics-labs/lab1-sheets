
SHEETS = densita pendolo_fisico conducibilita_termica dad_catenaria

all:
	for i in $(SHEETS); do \
		make $$i; \
	done

%:
	python tools/py2tex.py snippy/$*.py
	pdflatex sheets/$*.tex

clean:
	rm -f *~ *.aux *.log *.out *.fls *.fdb_latexmk *.synctex.gz

cleanall:
	make clean; rm -f *.pdf *.zip
