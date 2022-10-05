GRAMMAR = YAPL
TEST = executable.cl

%: all

all: compile run clean

compile:
	@echo Grammar is being compiled: $(GRAMMAR) 
	java org.antlr.v4.Tool -Dlanguage=Python3 $(GRAMMAR).g4 -visitor -o Compiled
	@echo Compiled successfully!

run:
	@echo run Main...
	find 'main.py' -exec sed -i '' s/__my__/$(GRAMMAR)/g {} +
	find 'visitor.py' -exec sed -i '' s/__my__/$(GRAMMAR)/g {} +
	find 'semanticVisitor.py' -exec sed -i '' s/__my__/$(GRAMMAR)/g {} +
	python3 main.py ./$(TEST)

clean:
	rm -rf Compiled
	find 'main.py' -exec sed -i '' s/$(GRAMMAR)/__my__/g {} +
	find 'visitor.py' -exec sed -i '' s/$(GRAMMAR)/__my__/g {} +
	find 'semanticVisitor.py' -exec sed -i '' s/$(GRAMMAR)/__my__/g {} +
