# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#start.
    def enterStart(self, ctx:gramaticaParser.StartContext):
        pass

    # Exit a parse tree produced by gramaticaParser#start.
    def exitStart(self, ctx:gramaticaParser.StartContext):
        pass


    # Enter a parse tree produced by gramaticaParser#sentencias.
    def enterSentencias(self, ctx:gramaticaParser.SentenciasContext):
        pass

    # Exit a parse tree produced by gramaticaParser#sentencias.
    def exitSentencias(self, ctx:gramaticaParser.SentenciasContext):
        pass


    # Enter a parse tree produced by gramaticaParser#asignacion.
    def enterAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#asignacion.
    def exitAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#v_input.
    def enterV_input(self, ctx:gramaticaParser.V_inputContext):
        pass

    # Exit a parse tree produced by gramaticaParser#v_input.
    def exitV_input(self, ctx:gramaticaParser.V_inputContext):
        pass


    # Enter a parse tree produced by gramaticaParser#printf.
    def enterPrintf(self, ctx:gramaticaParser.PrintfContext):
        pass

    # Exit a parse tree produced by gramaticaParser#printf.
    def exitPrintf(self, ctx:gramaticaParser.PrintfContext):
        pass


    # Enter a parse tree produced by gramaticaParser#var_casteo.
    def enterVar_casteo(self, ctx:gramaticaParser.Var_casteoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#var_casteo.
    def exitVar_casteo(self, ctx:gramaticaParser.Var_casteoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#casteo.
    def enterCasteo(self, ctx:gramaticaParser.CasteoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#casteo.
    def exitCasteo(self, ctx:gramaticaParser.CasteoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cadena.
    def enterCadena(self, ctx:gramaticaParser.CadenaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cadena.
    def exitCadena(self, ctx:gramaticaParser.CadenaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcion.
    def enterFuncion(self, ctx:gramaticaParser.FuncionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcion.
    def exitFuncion(self, ctx:gramaticaParser.FuncionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#v_return.
    def enterV_return(self, ctx:gramaticaParser.V_returnContext):
        pass

    # Exit a parse tree produced by gramaticaParser#v_return.
    def exitV_return(self, ctx:gramaticaParser.V_returnContext):
        pass


    # Enter a parse tree produced by gramaticaParser#llamafuncion.
    def enterLlamafuncion(self, ctx:gramaticaParser.LlamafuncionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#llamafuncion.
    def exitLlamafuncion(self, ctx:gramaticaParser.LlamafuncionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condicional.
    def enterCondicional(self, ctx:gramaticaParser.CondicionalContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condicional.
    def exitCondicional(self, ctx:gramaticaParser.CondicionalContext):
        pass


    # Enter a parse tree produced by gramaticaParser#elifBlock.
    def enterElifBlock(self, ctx:gramaticaParser.ElifBlockContext):
        pass

    # Exit a parse tree produced by gramaticaParser#elifBlock.
    def exitElifBlock(self, ctx:gramaticaParser.ElifBlockContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condicional_elif.
    def enterCondicional_elif(self, ctx:gramaticaParser.Condicional_elifContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condicional_elif.
    def exitCondicional_elif(self, ctx:gramaticaParser.Condicional_elifContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condicional_else.
    def enterCondicional_else(self, ctx:gramaticaParser.Condicional_elseContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condicional_else.
    def exitCondicional_else(self, ctx:gramaticaParser.Condicional_elseContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ciclo_for.
    def enterCiclo_for(self, ctx:gramaticaParser.Ciclo_forContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ciclo_for.
    def exitCiclo_for(self, ctx:gramaticaParser.Ciclo_forContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ciclo_while.
    def enterCiclo_while(self, ctx:gramaticaParser.Ciclo_whileContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ciclo_while.
    def exitCiclo_while(self, ctx:gramaticaParser.Ciclo_whileContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parametro.
    def enterParametro(self, ctx:gramaticaParser.ParametroContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parametro.
    def exitParametro(self, ctx:gramaticaParser.ParametroContext):
        pass


    # Enter a parse tree produced by gramaticaParser#func.
    def enterFunc(self, ctx:gramaticaParser.FuncContext):
        pass

    # Exit a parse tree produced by gramaticaParser#func.
    def exitFunc(self, ctx:gramaticaParser.FuncContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expresion.
    def enterExpresion(self, ctx:gramaticaParser.ExpresionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expresion.
    def exitExpresion(self, ctx:gramaticaParser.ExpresionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#matriz_operaciones.
    def enterMatriz_operaciones(self, ctx:gramaticaParser.Matriz_operacionesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#matriz_operaciones.
    def exitMatriz_operaciones(self, ctx:gramaticaParser.Matriz_operacionesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#matriz.
    def enterMatriz(self, ctx:gramaticaParser.MatrizContext):
        pass

    # Exit a parse tree produced by gramaticaParser#matriz.
    def exitMatriz(self, ctx:gramaticaParser.MatrizContext):
        pass


    # Enter a parse tree produced by gramaticaParser#fila_matriz.
    def enterFila_matriz(self, ctx:gramaticaParser.Fila_matrizContext):
        pass

    # Exit a parse tree produced by gramaticaParser#fila_matriz.
    def exitFila_matriz(self, ctx:gramaticaParser.Fila_matrizContext):
        pass


    # Enter a parse tree produced by gramaticaParser#importss.
    def enterImportss(self, ctx:gramaticaParser.ImportssContext):
        pass

    # Exit a parse tree produced by gramaticaParser#importss.
    def exitImportss(self, ctx:gramaticaParser.ImportssContext):
        pass


    # Enter a parse tree produced by gramaticaParser#termino.
    def enterTermino(self, ctx:gramaticaParser.TerminoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#termino.
    def exitTermino(self, ctx:gramaticaParser.TerminoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#lista.
    def enterLista(self, ctx:gramaticaParser.ListaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#lista.
    def exitLista(self, ctx:gramaticaParser.ListaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#arreglo.
    def enterArreglo(self, ctx:gramaticaParser.ArregloContext):
        pass

    # Exit a parse tree produced by gramaticaParser#arreglo.
    def exitArreglo(self, ctx:gramaticaParser.ArregloContext):
        pass


    # Enter a parse tree produced by gramaticaParser#graficas.
    def enterGraficas(self, ctx:gramaticaParser.GraficasContext):
        pass

    # Exit a parse tree produced by gramaticaParser#graficas.
    def exitGraficas(self, ctx:gramaticaParser.GraficasContext):
        pass


    # Enter a parse tree produced by gramaticaParser#arange.
    def enterArange(self, ctx:gramaticaParser.ArangeContext):
        pass

    # Exit a parse tree produced by gramaticaParser#arange.
    def exitArange(self, ctx:gramaticaParser.ArangeContext):
        pass


    # Enter a parse tree produced by gramaticaParser#regresion_lineal.
    def enterRegresion_lineal(self, ctx:gramaticaParser.Regresion_linealContext):
        pass

    # Exit a parse tree produced by gramaticaParser#regresion_lineal.
    def exitRegresion_lineal(self, ctx:gramaticaParser.Regresion_linealContext):
        pass


    # Enter a parse tree produced by gramaticaParser#k_means.
    def enterK_means(self, ctx:gramaticaParser.K_meansContext):
        pass

    # Exit a parse tree produced by gramaticaParser#k_means.
    def exitK_means(self, ctx:gramaticaParser.K_meansContext):
        pass


    # Enter a parse tree produced by gramaticaParser#dbscan.
    def enterDbscan(self, ctx:gramaticaParser.DbscanContext):
        pass

    # Exit a parse tree produced by gramaticaParser#dbscan.
    def exitDbscan(self, ctx:gramaticaParser.DbscanContext):
        pass


    # Enter a parse tree produced by gramaticaParser#mlp.
    def enterMlp(self, ctx:gramaticaParser.MlpContext):
        pass

    # Exit a parse tree produced by gramaticaParser#mlp.
    def exitMlp(self, ctx:gramaticaParser.MlpContext):
        pass



del gramaticaParser