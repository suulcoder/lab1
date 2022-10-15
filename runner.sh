#!/bin/bash
echo Grammar is being compiled: YAPL 
java org.antlr.v4.Tool -Dlanguage=Python3 YAPL.g4 -visitor -o Compiled
echo Compiled successfully!


echo run Main...
find 'main.py' -exec sed -i '' s/__my__/YAPL/g {} +
find 'visitor.py' -exec sed -i '' s/__my__/YAPL/g {} +
find 'semanticVisitor.py' -exec sed -i '' s/__my__/YAPL/g {} +
python3 main.py ./executable.cl


rm -rf Compiled
find 'main.py' -exec sed -i '' s/YAPL/__my__/g {} +
find 'visitor.py' -exec sed -i '' s/YAPL/__my__/g {} +
find 'semanticVisitor.py' -exec sed -i '' s/YAPL/__my__/g {} +