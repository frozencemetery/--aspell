bytecode:
	python -c 'import compileall; compileall.compile_dir(".", force=1)'

clean:
	rm -f *.pyc
