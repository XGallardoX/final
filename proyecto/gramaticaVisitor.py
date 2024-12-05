# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#start.
    def visitStart(self, ctx:gramaticaParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#sentencias.
    def visitSentencias(self, ctx:gramaticaParser.SentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#asignacion.
    def visitAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#v_input.
    def visitV_input(self, ctx:gramaticaParser.V_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printf.
    def visitPrintf(self, ctx:gramaticaParser.PrintfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#var_casteo.
    def visitVar_casteo(self, ctx:gramaticaParser.Var_casteoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#casteo.
    def visitCasteo(self, ctx:gramaticaParser.CasteoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#cadena.
    def visitCadena(self, ctx:gramaticaParser.CadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcion.
    def visitFuncion(self, ctx:gramaticaParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#v_return.
    def visitV_return(self, ctx:gramaticaParser.V_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#llamafuncion.
    def visitLlamafuncion(self, ctx:gramaticaParser.LlamafuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condicional.
    def visitCondicional(self, ctx:gramaticaParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#elifBlock.
    def visitElifBlock(self, ctx:gramaticaParser.ElifBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condicional_elif.
    def visitCondicional_elif(self, ctx:gramaticaParser.Condicional_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condicional_else.
    def visitCondicional_else(self, ctx:gramaticaParser.Condicional_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ciclo_for.
    def visitCiclo_for(self, ctx:gramaticaParser.Ciclo_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ciclo_while.
    def visitCiclo_while(self, ctx:gramaticaParser.Ciclo_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#parametro.
    def visitParametro(self, ctx:gramaticaParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#func.
    def visitFunc(self, ctx:gramaticaParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#expresion.
    def visitExpresion(self, ctx:gramaticaParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#matriz_operaciones.
    def visitMatriz_operaciones(self, ctx:gramaticaParser.Matriz_operacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#matriz.
    def visitMatriz(self, ctx:gramaticaParser.MatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fila_matriz.
    def visitFila_matriz(self, ctx:gramaticaParser.Fila_matrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#importss.
    def visitImportss(self, ctx:gramaticaParser.ImportssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#termino.
    def visitTermino(self, ctx:gramaticaParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#lista.
    def visitLista(self, ctx:gramaticaParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#arreglo.
    def visitArreglo(self, ctx:gramaticaParser.ArregloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#graficas.
    def visitGraficas(self, ctx:gramaticaParser.GraficasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#arange.
    def visitArange(self, ctx:gramaticaParser.ArangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#regresion_lineal.
    def visitRegresion_lineal(self, ctx:gramaticaParser.Regresion_linealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#k_means.
    def visitK_means(self, ctx:gramaticaParser.K_meansContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#dbscan.
    def visitDbscan(self, ctx:gramaticaParser.DbscanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#mlp.
    def visitMlp(self, ctx:gramaticaParser.MlpContext):
        return self.visitChildren(ctx)



del gramaticaParser