all:
	python -c 'import compileall; compileall.compile_dir(".", force=1)'

install: all
	cp *.pyc /usr/local/bin/.
	chmod +x /usr/local/bin/*.pyc

clean:
	rm -f *.pyc
