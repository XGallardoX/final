#!/bin/bash

antlr4 -visitor gramatica.g4 

python3 logica.py < prueba.txt
