antlr4 -visitor gramatica.g4 
python3 logica.py < prueba.txt 


python3 -m venv venv
source venv/bin/activate

pip install antlr4-python3-runtime==4.13.2

antlr4 -Dlanguage=Python3 -visitor MLanguage.g4


