# -*- coding: utf-8 -*-
"""
Created with love

@author: sebas & Catherin
                    Círculos Sociales de Maccasiano
"""
import pandas as pd
from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx

#           Parte 1: EXTRAER LA INFORMACION DE LA BASE DE DATOS
# Ruta al archivo de Excel
ruta_archivo = 'C:/Users/'   'Inserte aquí la dirección donde se encuentra el archivo'   '/base_proyecto_grafos.xlsx'

# Leer el archivo de Excel y almacenar los datos en un DataFrame de pandas
dataframe = pd.read_excel(ruta_archivo)

# Extraer los datos de la columna 0 y almacenarlos en una lista
lista_columna_0 = dataframe.iloc[0:, 0].tolist()

# Extraer los datos de la columna 1 y almacenarlos en otra lista
lista_columna_1 = dataframe.iloc[0:, 1].tolist()

#           Parte 2: ALMACENAR LA INFORMACION DE LA BASE DE DATOS EN ARREGLOS
list_codes = ['1FJ@SYF1', '11O<9QP2', '1?K0SAJ3', '19=7<JW4', '1O3BQOY5', '1;9LB=T6', '18=V79D7', '1B0ZJU48', '1KQGZ7D9', '1TR88T10', '1EMCLB11', '1;=39Y12', '1L>F0O13', '1ME>IR14', '18=U7<15', '17QX@Z16', '19SPK<17', '1K3>NC18', '1VV7AP19', '1=OF8U20', '1R<5?K21', '12K01F22', '1HU>>A23', '1R?JQG24', '1Z8;B025', '14GO:G26', '1LR@<127', '10EPMA28', '1J@S8T29', '1<TITU30', '1QQ3K631', '10EQX132', '1Y4BVL33', '1ARXFY34', '1ZK8T?35', '11O@AS36', '1BDIGP37', '1GLBV?38', '1=CP=939', '1U?5:R40', '1;6Y5Q41', '103<2X42', '1KF=E<43', '1BVV>D44', '1Z=VVG45', '17:LF446', '1MUF;147', '14GF5Y48', '1H;=4G49', '11:9RG50', '15?G2N51', '1Y0GYM52', '1M9XW;53', '1L78@P54', '1W;D1E55', '1UB5X056', '1EO5P357', '1I;RHK58', '1J6T0859', '1T;N?A60', '12KPY>61', '1YI58I62', '18D:UV63', '194@:C64', '1IZP<D65', '1VZI3X66', '1>S4WL67', '1EP0<A68', '1?Z8S769', '19TXRS70', '1=DJ?Z71', '1E298:72', '1J28<K73', '15MZXP74', '1E5C;P75', '1N:FT;76', '1BFEBR77', '1>TQB578', '1V8HRQ79', '1:3K;H80', '169WE:81', '1V@A9K82', '1:UKXX83', '1ZIX5Y84', '1ZPEXB85', '1ZFN1?86', '1WYAN987', '174AJB88', '1D:N:Z89', '1L?NVD90', '1K<<5Z91', '16N@RS92', '1VR0KO93', '1KYU6894', '1IA1C?95', '1=GXA396', '1L206?97', '1EQ1TI98', '1PH0P999', '165J4100', '1?XSX101', '1DQGE102', '19QC7103', '173CA104', '1MC6D105', '1U=<Q106', '1Y2H;107', '1W6?M108', '1?KU3109', '15TI=110', '1;VWW111', '1A=OW112', '1U94?113', '1@3@6114', '1XPK9115', '18LUL116', '1>U52117', '12:T?118', '1OTIT119', '1YHR?120', '1T?LZ121', '1=5MC122', '1<R75123', '1>ZMY124', '1NURC125', '1SB2L126', '1BXA7127', '1YUA:128', '1G<V<129', '1@91V130', '1ZOD7131', '11VH>132', '1GUZ@133', '1P3E7134', '1UB?H135', '1X5IA136', '1IGGE137', '1YSXV138', '1<8TY139', '12;BN140', '1PAU8141', '1<CYY142', '13O:G143', '1S@E1144', '1H6QO145', '1H186146', '1OYS3147', '1:7P=148', '1KY4I149', '1>6P5150', '1EJTR151', '1DTWO152', '1ZPX9153', '1Q;MP154', '1H6>1155', '1FC8@156', '1WGS2157', '15A2=158', '1?D5K159', '1AH3D160', '1Y?YE161', '13T<9162', '1=I3W163', '1ST=Y164', '1GQVU165', '1IO8A166', '1;RXS167', '1COFF168', '1YV:Z169', '1LTWF170', '1L546171', '16FY2172', '1QZVL173', '1NDDW174', '14VX5175', '1;FYJ176', '1:YL=177', '1577J178', '14P6Z179', '1GARI180', '1X:FA181', '1<8?H182', '13JYZ183', '193=F184', '1VMRG185', '1C71Z186', '16G@T187', '1ZU2Y188', '1SO?W189', '116@R190', '1W8JY191', '1GOQO192', '1LL<Z193', '1ZO2Y194', '1AI3J195', '1X83N196', '1C>3<197', '1HR:9198', '1B8B6199', '1CNPC200', '1S<WI201', '1A@BM202', '14JEC203', '17N33204', '1LI;2205', '1YIW?206', '13H;K207', '1BRG6208', '14H10209', '19:MM210', '1S3T@211', '1O5X=212', '12?7T213', '1MFKH214', '125Y7215', '19:SB216', '1MMO=217', '191T<218', '1PHY;219', '1<FAR220', '1X4AG221', '1FOQM222', '1>0DN223', '2L3Y<BG1', '2T?1W5X2', '2ZZ69IF3', '2W4MBMO4', '25:5PXF5', '22<L9F16', '2024K:S7', '28P35228', '38@ZUQO1', '3OLYV482', '33TNP<33', '41;<8UK1', '4RFJ6S72', '4DZ?Q;O3', '49GHJOP4', '5BV340M1', '549;N8R2', '6D4K7RN1', '6965?B22', '7VGG2PV1', '7X>FP5Y2', '7L9Z@EI3', '8M>:ID01', '91>W8<Q1']
list_names = ['Alejandra Campo Archbold', 'Alejandra Contreras Carrillo', 'Alejandra Pardo Polanía', 'Alejandro Enrique Garcia Sanchez', 'Alejandro Rafael De Jesus Vega Saavedra', 'Ana Karina Pulido Gonzalez', 'Ana María Garzón Sánchez', 'Andres Felipe Cuervo Torres', 'Andres Felipe Diaz Molina', 'Andres Felipe Yañez Villarraga', 'Andres Sebastian Salazar Mejia', 'Andrey Javier Lizarazo Hernandez', 'Ángel David López Espejo', 'Angel Gabriel García Falla', 'Ángela Valeria Jiménez Contreras', 'Camila Rayen Nahuel', 'Camilo Andres Fernandez Sarmiento', 'Camilo Andres Silva Rodriguez', 'Camilo Andrés Tejada Merchán', 'Carlos Andrés Galan Pérez', 'Carlos Andrés Marín Olarte', 'Carlos Andres Muñoz Buitrago', 'Carlos Sebastian Martinez Vidal', 'Carolina Rojano Alvear', 'Catherin Rodriguez Miranda', 'Cesar Felipe Segura Perilla', 'Cristian Andres Reinales Herrera', 'Cristian David Machacado Rojas', 'Dafne Valeria Castellanos Rosas', 'Dana Isabella Acosta Castillo', 'Daniel Alejandro Arias Rodriguez', 'Daniel Andrés Zárate Vélez', 'Daniel Esteban Fandiño Rodriguez', 'Daniel Estrada Patiño', 'Daniel Felipe Rambaut Lemus', 'Daniel Jacobo Castillo Gomez', 'Daniel Jose Forero Corredor', 'Daniel Leyva Castro', 'Daniela Sofia Gil Polanco', 'Daniela Torres Gómez', 'Danna Sofia Marin Guacaneme', 'David Alejandro Meléndez Galindo', 'David Alfonso Oviedo Salamanca', 'David Gregorio Vera Castellanos', 'David Leonardo Luengas Fonseca', 'David Santiago Buitrago Prada', 'David Santiago Flórez Alsina', 'Dayana Valentina Gonzalez Vargas', 'Diana Valentina Caro Corredor', 'Diego Fernando Florez Cano', 'Diryon Yonith Mora Romero', 'Edgar Santiago Jaimes Chaparro', 'Emanuel Naval Oviedo', 'Estefania Laverde Becerra', 'Fabio Andres Rizo Montoya', 'Felipe Guzman Sierra', 'Felipe Martinez Mirque', 'Felipe Muñoz Vélez', 'Gabriela Fonseca Encinales', 'Gabriela Linares Chavez', 'Germán David Plazas Cayachoa', 'Giancarlo Guisseppe Gonzalez Uchamocha', 'Gina Maritza Martínez López', 'Giseth Natalia Chacon Tibaduiza', 'Guillermo Andres Ribero Garzon', 'Henry Alberto Velandia Quintero', 'Jaider Duvan Velasco Diaz', 'Javier Santiago Useche Acosta', 'Jham Pool Murillo Mahecha', 'Jhan Carlos Celi Maldonado', 'Joann Sebastian Samaca Medina', 'Johan Santiago Caro Valencia', 'Jorge Danilo Gallego Herrera', 'José Daniel Rodríguez Rodríguez', 'Jose David Echeverri Diaz', 'Jose Gabriel Alvarez Medina', 'José Miguel Torres Lara', 'Joseph Daniel Mancera Basto', 'Juan Andrés Alayón Ariza', 'Juan Andres Castro Carrillo', 'Juan Andrés Guevara Ángel', 'Juan Andres Ortiz Pinzon', 'Juan Andres Russy Cervera', 'Juan Camilo Canizales Beltran', 'Juan Camilo Hoyos Salgado', 'Juan Camilo Pugliese Pomares', 'Juan Camilo Rodriguez Jimenez', 'Juan Camilo Rodriguez Melo', 'Juan Daniel Amaya Polania', 'Juan Daniel Casanova Prieto', 'Juan David Benavides Gonzalez', 'Juan David Martinez Mercado', 'Juan David Obando López', 'Juan David Vargas Rodriguez', 'Juan Diego Martinez Paez', 'Juan Esteban Beltrán Ríos', 'Juan Esteban Gonzalez Soto', 'Juan Esteban Ladino Mateus', 'Juan Esteban Velandia Romero', 'Juan Fernando Morales Rojas', 'Juan Fernando Rojas Santiago', 'Juan José Caballero Fernandez', 'Juan José Martínez Garzón', 'Juan Jose Ruiz Triana', 'Juan Lucas Garcia Osorio', 'Juan Luis Ávila Montoya', 'Juan Manuel Dávila Rivera', 'Juan Manuel Ramirez Osuna', 'Juan Manuel Uribe Quintero', 'Juan Miguel Gutierrez Vidal', 'Juan Nicolas Quintero Quintero', 'Juan Nicolás Sepúlveda Arias', 'Juan Pablo Guerrero Arévalo', 'Juan Pablo Sierra Useche', 'Juan Pablo Simbaqueba Velasquez', 'Juan Sebastian Bernal Rojas', 'Juan Sebastián Caballero Roa', 'Juan Sebastian Contreras Alejo', 'Juan Sebastian Rodriguez Salazar', 'Juan Sebastian Sanchez Martin', 'Juanita Gómez Romero', 'Juanita Robles Ariza', 'Julian Andres Castro Avila', 'Julian David Tovar Gaitan', 'Julián Muriel Ospina', 'Juliana Bermúdez Guzmán', 'Julieta Montoya Quintero', 'Kiara Nicole Velasquez Ramirez', 'Laura Alejandra Rincón Castaño', 'Laura Daniela Rey Gaitan', 'Laura Sofía Ortiz Arcos', 'Laura Sofia Rincón Sierra', 'Laura Sofia Salazar Reyes', 'Laura Valentina González Rodríguez', 'Laura Valentina Hernandez Cardozo', 'Laura Ximena Ortiz Pinzon', 'Liz Yuliana Velandia Berrondo', 'Lucia Ardila Paez', 'Luis Daniel Idárraga Zea', 'Luna Gabriela Durán Pérez', 'Luna María Gutiérrez Jaramillo', 'Maria Camila Garcia Ramirez', 'Maria Camila Patarroyo Valbuena', 'Maria Fernanda Palacio Conde', 'Maria Fernanda Rodriguez Conde', 'Maria Jose Campos Ospina', 'Maria Jose Chavarro Barbosa', 'Maria Paula Gaviria Perez', 'Maria Ximena Rojas Castro', 'Mariana Cadena Moreno', 'Mariana Ramirez Alvarado', 'Marloon Louis Triana Mora', 'Matheus Braga Ferreira Da Rocha', 'Michael Gerard Jaime Iii Hernandez Lopez', 'Miguel Ángel Caicedo Carrasquilla', 'Miguel Angel Castillo Espitia', 'Miguel Angel Salamanca Ortiz', 'Miguel Valencia Zuluaga', 'Natalia Alejandra Martinez Muñoz', 'Natalia Katherine Rojas Suarez', 'Natalia Laiton Romero', 'Natalia Martinez Neira', 'Natalia Schachtebeck Gomez', 'Nelson Santiago Guayazán Palacios', 'Nicolas David Rogers Valdez', 'Nicolás Dussan Castañeda', 'Nicolas Eduardo Gallego Quiceno', 'Nicolas Fernando Botero Andramunio', 'Nicolas Giovanny Caicedo Ramirez', 'Nicolas Otero Parra', 'Nicolás Steven Peña Gómez', 'Nicolas Velandia Sanabria', 'Omar Felipe Ariza Camacho', 'Oscar Andres Gomez Hernandez', 'Oscar Velasco Chiquillo', 'Paula Andrea Castiblanco Niño', 'Paula Lorena López Romero', 'Pedro Alejandro Baquero Jiménez', 'Rafael Enrique Cabrera Jimenez', 'Rodrigo Castillo Camargo', 'Samuel Barbosa Enciso', 'Samuel David Moreno Vahos', 'Samuel Restrepo Osorio', 'Santiago Aillón Prada', 'Santiago Alvarez Barbosa', 'Santiago Andrade Gutiérrez', 'Santiago Andres Diaz Jinete', 'Santiago Arévalo Rosales', 'Santiago Guerrero Ortiz', 'Santiago Hoyos Ortiz', 'Santiago Jose Osorio Omaña', 'Santiago Linares Espinosa', 'Santiago Mora Camacho', 'Santiago Ortíz Pérez', 'Santiago Peña Rivas', 'Santiago Rodríguez Morales', 'Santiago Romero Lozano', 'Santiago Uribe Luna', 'Sara Julieth Zuleta Quevedo', 'Sara Lucia Gallego Rivera', 'Sara Rodríguez Martínez', 'Sebastian Alfonso Sarmiento', 'Sebastián Plazas Andrade', 'Sebastián Suárez García', 'Sergio Andrés García Morán', 'Sergio Gabriel Acosta Maldonado', 'Simón Francisco Arias Neira', 'Sofia Carrera Martinez', 'Sofía Duarte Sanabria', 'Sofia Ochoa Gutierrez', 'Sofia Robayo Bonilla', 'Tomas Sandoval Gordillo', 'Valentina Correa Garzón', 'Valentina Hernandez Quintana', 'Valentina Herrera Plaza', 'Valentina Lopez Montero', 'Valentina Pabon Leon', 'Valeria Ferreira Nocua', 'Victor Manuel Marquez Cifuentes', 'Victor Manuel Sicacha Cardenas', 'Wenceslao Huang', 'Winston Rafael Pernett Gonzalez', 'Yofer Quintanilla Gomez', 'Alejandro Castañeda Uribe', 'Andrés Mauricio Pérez Gordillo', 'Edgar José Andrade', 'Daniel Alfonso Bojacá Torres', 'Daniel Díaz López', 'Jesús Antonio Vega', 'María Fernanda Gómez', 'Norma Constanza Sarmiento', 'Director Carrera', 'Decano Facultad', 'Codirector Carrera', 'Coordinador', 'Secretarío Acádemico', 'Gestor', 'Director Finanzas', 'Director Principal', 'Vicerrector', 'Gerente', 'Secreatrio Hábitat', 'Becario', 'Director Salud', 'Representante', 'Encargado', 'Director Internacional']

#           Parte 3: CREACION DE GRAFO ALEATORIO CONEXO CON PROBABILIDAD MINIMA
#funcion que seleciona un vertice y encuentra sus vecinos
def encontrar_vecinos(grafo, vertice):
    vecinos = []
    for i in grafo[vertice]:
        vecinos.append(i)      
    return vecinos


#funcion que recorre el arbol en profundidad
def recorrer_arbol(grafo,vertice,marcado): #Recibe un grafo, vertice,lista de ya visitados
    lista = encontrar_vecinos(grafo, vertice) #encuentra los vecinos de dicho vertice
    marcado.append(vertice) #lo marca como visitado en la lista
    for i in lista: #recorre los vecinos encontrados
        if i not in marcado: 
            recorrer_arbol(grafo,i,marcado)#descarta los ya marcados y encuentra los vecinos de los vecinos
            

#funcion que cuenta el numero de componentes que tiene un grafo
def numero_componete(grafo,marcado,contador):  #recibe un grafo, lista de ya visitados, contador
    componente_vertice = 0 #crea un contador por cada componente que encuentra
    for i in grafo: #recorre los vertices del grafo
        if i not in marcado: 
            
            componente_vertice = +1 #marca 1 por la componente que encuentra de esta forma garantiza que se encuentra por lo menos 1 componente en el grafo
            contador += 1 #cuenta la componente que encuentró y la guarda en el contador general
            recorrer_arbol(grafo,i,marcado)#repite el proceso con el siguiente vertice

    return contador #retorna la cantidad de componentes del grafo


#funcion que encuentra la menor probabilidad con la cual el grafo queda conexo 
def probabilidad_correcta(n,p,contador,marcado):
    grafo = erdos_renyi_graph(n, p)
    G = nx.Graph() 
    G.add_edges_from(grafo.edges)
    retornar = []
    new = (numero_componete(grafo, marcado, contador))
    
    if new != 1:
        contador1=0
        marcado1 =[]
        probabilidad_correcta(n,p+0.01,contador1,marcado1)
    else:
        return p
        
n = len(list_codes) #cantidad de vertices del grafo
m = []#lista para marcar los vertices ya visitado
contador = 0#contador de la componente
p_base = 0.01 #se inicializa con una probabilidad relativamente baja, luego la funcion probabilidad correcta nos retorna dara la mejor probabilidad
probabilidad_correcta(n, p_base, contador, m)
p = 0.04#Es la probabilidad encontrada con la funcion probabilidad_correcta
g = erdos_renyi_graph(n, p)#se hace la creacion de un grafo aletorio con una cantidad de vertices de 250 y probabilidad 0.03
""" En caso que desee ver las conexiones que se crearon, no comente las siguientes dos líneas """
#print(g.edges)
#print(len(g.edges)) 

#           Parte 4: ASIGNACIÓN DE LOS NOMBRES Y/O CÓDIGOS A LOS VERTICES CREADAS EN EL GRAFO ALEATORIO
#se crea una lista en la cual cada tupla representa la conexion (arista) que tiene un vertice con otro

lista_conexiones = [(0, 8), (0, 45), (0, 58), (0, 72), (0, 85), (0, 99), (0, 122), (0, 141), (0, 142), (0, 144), (0, 169), (1, 13), (1, 46), (1, 112), (1, 141), (1, 166), (1, 170), (1, 201), (1, 223), (1, 236), (2, 26), (2, 30), (2, 41), (2, 64), (2, 102), (2, 104), (2, 119), (2, 130), (2, 148), (2, 160), (2, 191), (2, 192), (2, 232), (3, 6), (3, 37), (3, 49), (3, 58), (3, 76), (3, 88), (3, 114), (3, 124), (3, 153), (3, 207), (3, 214), (3, 240), (3, 243), (4, 51), (4, 63), (4, 71), (4, 72), (4, 76), (4, 138), (4, 195), (4, 226), (4, 238), (5, 69), (5, 79), (5, 130), (5, 158), (5, 184), (5, 221), (5, 243), (6, 29), (6, 33), (6, 53), (6, 72), (6, 79), (6, 85), (6, 105), (6, 128), (6, 132), (6, 135), (6, 150), (6, 172), (6, 173), (6, 227), (7, 26), (7, 75), (7, 82), (7, 99), (7, 106), (7, 138), (7, 165), (7, 192), (7, 194), (7, 229), (7, 242), (8, 27), (8, 42), (8, 52), (8, 91), (8, 93), (8, 117), (8, 148), (8, 159), (8, 171), (8, 202), (8, 219), (9, 144), (9, 172), (9, 203), (9, 221), (9, 227), (10, 11), (10, 12), (10, 17), (10, 18), (10, 36), (10, 37), (10, 63), (10, 85), (10, 92), (10, 103), (10, 126), (10, 128), (10, 145), (10, 221), (11, 21), (11, 23), (11, 42), (11, 76), (11, 90), (11, 104), (11, 164), (11, 244), (12, 28), (12, 51), (12, 68), (12, 88), (12, 122), (12, 159), (12, 185), (12, 228), (12, 243), (13, 39), (13, 50), (13, 84), (13, 129), (13, 134), (13, 170), (13, 199), (13, 239), (13, 245), (14, 34), (14, 76), (14, 144), (14, 193), (14, 235), (15, 28), (15, 40), (15, 52), (15, 53), (15, 82), (15, 120), (15, 156), (15, 226), (16, 22), (16, 67), (16, 101), (16, 106), (16, 119), (16, 132), (16, 136), (16, 170), (16, 195), (16, 216), (16, 227), (17, 26), (17, 32), (17, 137), (17, 148), (17, 162), (17, 188), (17, 195), (18, 39), (18, 41), (18, 60), (18, 73), (18, 88), (18, 95), (18, 98), (18, 100), (18, 106), (18, 107), (18, 131), (18, 148), (18, 157), (18, 194), (18, 222), (19, 38), (19, 52), (19, 89), (19, 94), (19, 116), (19, 129), (19, 137), (19, 141), (19, 170), (19, 235), (19, 239), (19, 241), (19, 244), (20, 57), (20, 68), (20, 74), (20, 152), (20, 172), (20, 175), (20, 224), (20, 233), (21, 121), (21, 135), (21, 138), (21, 231), (22, 72), (22, 78), (22, 96), (22, 112), (22, 132), (22, 186), (22, 188), (22, 212), (22, 220), (22, 227), (22, 237), (22, 241), (23, 29), (23, 62), (23, 72), (23, 92), (23, 193), (23, 198), (23, 230), (24, 108), (24, 123), (24, 133), (24, 143), (24, 156), (24, 182), (24, 211), (24, 215), (24, 217), (24, 225), (24, 236), (25, 47), (25, 57), (25, 58), (25, 63), (25, 107), (25, 138), (25, 143), (25, 215), (26, 32), (26, 65), (26, 75), (26, 93), (27, 79), (27, 98), (27, 100), (27, 114), (27, 128), (27, 140), (27, 153), (27, 162), (28, 35), (28, 37), (28, 52), (28, 77), (28, 105), (28, 121), (28, 139), (28, 181), (28, 190), (28, 218), (28, 221), (28, 222), (29, 72), (29, 99), (29, 111), (29, 136), (29, 140), (29, 151), (29, 218), (29, 230), (29, 245), (30, 31), (30, 124), (30, 143), (30, 144), (30, 174), (31, 48), (31, 65), (31, 104), (31, 162), (31, 174), (31, 180), (31, 190), (31, 211), (31, 217), (32, 47), (32, 64), (32, 98), (32, 151), (32, 177), (32, 188), (32, 190), (32, 219), (32, 240), (33, 54), (33, 85), (33, 95), (33, 100), (33, 116), (33, 134), (33, 136), (33, 150), (33, 188), (33, 224), (33, 226), (34, 85), (34, 94), (34, 100), (34, 106), (34, 116), (34, 143), (34, 150), (34, 211), (34, 216), (35, 60), (35, 70), (35, 101), (35, 121), (35, 176), (35, 192), (35, 237), (35, 242), (35, 244), (36, 71), (36, 75), (36, 83), (36, 118), (36, 208), (36, 216), (37, 81), (37, 103), (37, 111), (37, 120), (37, 145), (37, 148), (37, 170), (37, 182), (37, 198), (38, 63), (38, 67), (38, 109), (38, 131), (38, 148), (38, 159), (38, 165), (38, 241), (39, 86), (39, 104), (39, 110), (39, 116), (39, 144), (39, 183), (39, 219), (39, 241), (40, 42), (40, 52), (40, 53), (40, 186), (40, 208), (40, 220), (40, 222), (40, 228), (41, 49), (41, 87), (41, 115), (41, 145), (41, 206), (42, 49), (42, 81), (42, 102), (42, 182), (42, 196), (42, 211), (42, 212), (42, 221), (43, 87), (43, 104), (43, 111), (43, 151), (43, 157), (43, 166), (43, 223), (43, 242), (44, 101), (44, 107), (44, 131), (44, 180), (44, 205), (45, 50), (45, 74), (45, 129), (45, 135), (45, 146), (45, 196), (45, 211), (45, 213), (45, 229), (45, 235), (46, 54), (46, 139), (46, 154), (46, 167), (46, 227), (46, 241), (46, 245), (47, 74), (47, 93), (47, 106), (47, 164), (48, 81), (48, 88), (48, 125), (48, 144), (48, 223), (48, 246), (49, 52), (49, 129), (49, 198), (49, 199), (49, 206), (49, 234), (49, 240), (50, 69), (50, 80), (50, 83), (50, 99), (50, 134), (50, 200), (50, 228), (50, 234), (50, 240), (51, 57), (51, 58), (51, 63), (51, 137), (51, 205), (51, 225), (52, 80), (52, 83), (52, 90), (52, 148), (52, 181), (52, 202), (52, 226), (52, 227), (52, 237), (53, 121), (53, 138), (53, 142), (53, 170), (53, 180), (53, 213), (53, 219), (54, 74), (54, 84), (54, 99), (54, 102), (54, 123), (54, 128), (54, 144), (54, 168), (54, 208), (54, 246), (55, 60), (55, 129), (55, 172), (55, 195), (55, 206), (55, 214), (55, 231), (55, 243), (56, 61), (56, 67), (56, 91), (56, 96), (56, 122), (56, 139), (56, 147), (56, 148), (56, 149), (56, 184), (56, 194), (56, 200), (57, 75), (57, 95), (57, 98), (57, 146), (57, 169), (57, 185), (57, 206), (58, 74), (58, 78), (58, 115), (58, 118), (58, 168), (58, 172), (58, 190), (58, 213), (58, 215), (58, 235), (58, 239), (59, 100), (59, 160), (59, 177), (59, 226), (59, 230), (60, 66), (60, 76), (60, 85), (60, 90), (60, 128), (60, 129), (60, 149), (60, 171), (60, 173), (60, 183), (60, 209), (60, 227), (61, 91), (61, 105), (61, 163), (61, 167), (61, 176), (61, 178), (61, 184), (61, 206), (61, 243), (61, 245), (62, 148), (62, 151), (62, 156), (62, 174), (62, 184), (62, 222), (63, 83), (63, 120), (63, 127), (63, 139), (63, 143), (63, 146), (63, 154), (63, 172), (63, 174), (63, 220), (63, 224), (64, 69), (64, 88), (64, 91), (64, 92), (64, 97), (64, 111), (64, 114), (64, 170), (64, 186), (64, 191), (64, 209), (64, 226), (65, 70), (65, 79), (65, 108), (65, 118), (65, 153), (65, 224), (65, 237), (66, 80), (66, 102), (66, 104), (66, 118), (66, 147), (66, 208), (66, 215), (66, 225), (67, 81), (67, 91), (67, 129), (67, 166), (67, 167), (68, 101), (68, 109), (68, 119), (68, 155), (68, 157), (68, 176), (68, 196), (68, 241), (69, 70), (69, 170), (69, 213), (70, 108), (70, 115), (70, 141), (70, 146), (70, 175), (70, 180), (71, 81), (71, 92), (71, 95), (71, 160), (71, 195), (71, 241), (72, 94), (72, 101), (72, 124), (72, 220), (72, 236), (73, 77), (73, 116), (73, 132), (73, 137), (73, 213), (73, 230), (73, 234), (73, 241), (74, 77), (74, 128), (74, 137), (74, 147), (74, 160), (74, 189), (74, 211), (74, 212), (74, 214), (74, 224), (74, 239), (75, 81), (75, 86), (75, 99), (75, 129), (75, 130), (75, 144), (75, 172), (75, 193), (75, 214), (76, 81), (76, 117), (76, 139), (76, 140), (76, 156), (76, 175), (76, 194), (76, 210), (77, 123), (77, 134), (77, 164), (77, 218), (77, 227), (77, 236), (78, 88), (78, 105), (78, 164), (78, 179), (78, 182), (78, 221), (78, 225), (78, 244), (79, 99), (79, 126), (79, 162), (79, 199), (79, 235), (80, 97), (80, 118), (80, 127), (80, 170), (80, 178), (80, 188), (81, 140), (81, 184), (81, 206), (81, 227), (81, 239), (82, 94), (82, 103), (82, 115), (82, 122), (82, 127), (82, 214), (82, 244), (83, 105), (83, 125), (83, 175), (83, 182), (83, 202), (83, 225), (83, 236), (83, 237), (83, 241), (83, 243), (84, 100), (84, 132), (84, 182), (84, 190), (84, 238), (85, 113), (85, 157), (85, 160), (85, 162), (85, 199), (85, 202), (85, 207), (85, 243), (85, 245), (86, 97), (86, 117), (86, 151), (86, 158), (86, 182), (86, 241), (87, 118), (87, 130), (87, 144), (87, 151), (88, 97), (88, 135), (88, 142), (88, 171), (88, 172), (88, 186), (88, 193), (88, 196), (88, 202), (88, 222), (89, 92), (89, 110), (89, 124), (89, 133), (89, 152), (89, 164), (89, 179), (89, 200), (89, 229), (90, 95), (90, 134), (90, 138), (90, 143), (90, 160), (90, 180), (90, 188), (91, 119), (91, 140), (91, 148), (91, 152), (91, 175), (91, 199), (91, 222), (91, 228), (92, 104), (92, 108), (92, 146), (92, 210), (92, 244), (93, 102), (93, 118), (93, 144), (93, 150), (93, 159), (93, 187), (93, 201), (94, 100), (94, 146), (94, 190), (94, 219), (94, 232), (95, 114), (95, 132), (95, 151), (95, 233), (95, 235), (96, 173), (96, 177), (96, 201), (96, 218), (97, 192), (97, 211), (97, 230), (97, 240), (97, 246), (98, 105), (98, 119), (98, 137), (98, 151), (98, 171), (98, 221), (98, 223), (98, 237), (99, 171), (99, 194), (99, 218), (99, 222), (100, 130), (100, 145), (100, 201), (100, 207), (100, 244), (101, 149), (101, 156), (101, 160), (101, 187), (101, 220), (101, 230), (101, 239), (102, 203), (102, 222), (102, 232), (103, 106), (103, 143), (103, 195), (103, 201), (103, 206), (103, 238), (104, 138), (104, 176), (104, 192), (105, 106), (105, 138), (105, 157), (105, 230), (105, 231), (106, 112), (106, 150), (106, 155), (106, 159), (106, 181), (106, 186), (106, 228), (107, 174), (107, 178), (107, 191), (107, 196), (107, 214), (108, 110), (108, 177), (108, 196), (108, 219), (108, 226), (108, 228), (108, 236), (108, 240), (109, 142), (109, 211), (109, 232), (109, 234), (110, 146), (110, 148), (110, 150), (110, 154), (110, 166), (110, 174), (110, 182), (110, 185), (110, 186), (111, 149), (111, 163), (111, 165), (111, 173), (111, 203), (111, 204), (112, 157), (112, 158), (112, 161), (112, 168), (112, 172), (112, 189), (112, 191), (112, 210), (112, 216), (113, 154), (114, 209), (115, 190), (115, 200), (115, 227), (115, 235), (116, 125), (116, 145), (116, 184), (116, 193), (116, 225), (116, 228), (117, 121), (117, 123), (117, 151), (117, 174), (117, 176), (117, 195), (117, 203), (117, 217), (118, 148), (118, 150), (118, 167), (118, 168), (118, 245), (119, 123), (119, 150), (119, 152), (119, 154), (119, 218), (119, 223), (120, 173), (120, 174), (120, 186), (120, 238), (120, 241), (122, 190), (122, 243), (123, 124), (123, 134), (123, 135), (123, 137), (123, 138), (123, 158), (124, 189), (124, 200), (124, 207), (125, 164), (125, 218), (126, 136), (126, 147), (126, 152), (126, 163), (126, 182), (126, 203), (126, 231), (126, 246), (127, 128), (127, 156), (127, 160), (127, 182), (127, 220), (127, 239), (128, 135), (128, 141), (128, 171), (128, 174), (128, 184), (128, 237), (129, 160), (129, 169), (129, 185), (129, 221), (129, 226), (130, 188), (130, 202), (130, 208), (130, 219), (131, 159), (131, 160), (131, 183), (131, 194), (131, 204), (131, 233), (132, 136), (132, 204), (132, 215), (133, 144), (133, 161), (133, 166), (133, 190), (133, 194), (133, 199), (133, 235), (134, 147), (134, 163), (134, 198), (134, 209), (135, 141), (135, 153), (135, 165), (135, 171), (135, 181), (135, 197), (135, 202), (136, 147), (136, 152), (136, 205), (136, 206), (137, 167), (137, 198), (137, 203), (137, 237), (138, 151), (138, 168), (138, 186), (138, 213), (139, 164), (139, 167), (139, 178), (139, 181), (139, 201), (139, 215), (139, 219), (139, 233), (140, 153), (140, 169), (140, 170), (140, 213), (140, 237), (141, 180), (141, 182), (141, 200), (141, 228), (142, 157), (142, 160), (142, 187), (142, 222), (142, 224), (143, 168), (143, 180), (143, 186), (143, 192), (143, 213), (144, 171), (145, 161), (145, 206), (145, 225), (145, 233), (145, 235), (146, 156), (146, 194), (146, 204), (146, 235), (147, 149), (147, 186), (147, 188), (148, 150), (148, 220), (148, 231), (149, 150), (149, 166), (149, 177), (149, 192), (149, 237), (149, 239), (150, 185), (150, 188), (150, 213), (150, 241), (151, 224), (152, 199), (153, 170), (153, 177), (153, 194), (153, 244), (153, 246), (154, 155), (154, 175), (154, 194), (154, 204), (155, 166), (155, 170), (155, 187), (155, 239), (155, 244), (156, 171), (156, 190), (156, 216), (156, 243), (157, 194), (157, 214), (157, 228), (157, 232), (157, 243), (158, 226), (159, 197), (159, 242), (160, 188), (160, 195), (160, 206), (161, 167), (161, 175), (161, 231), (162, 184), (162, 186), (162, 190), (162, 193), (162, 209), (162, 216), (162, 228), (162, 230), (162, 241), (162, 243), (162, 246), (163, 196), (163, 210), (163, 219), (163, 225), (164, 196), (164, 206), (164, 227), (164, 243), (165, 214), (165, 216), (165, 224), (166, 193), (166, 221), (166, 234), (167, 172), (167, 182), (167, 205), (167, 215), (168, 198), (168, 226), (171, 174), (171, 177), (171, 204), (171, 209), (171, 229), (173, 220), (173, 246), (174, 201), (174, 206), (174, 211), (174, 215), (174, 222), (174, 245), (175, 205), (175, 209), (175, 239), (176, 187), (176, 193), (176, 207), (178, 202), (178, 214), (179, 180), (179, 239), (180, 196), (180, 238), (181, 219), (182, 213), (182, 243), (183, 185), (183, 212), (183, 214), (184, 203), (184, 205), (184, 239), (184, 240), (185, 216), (185, 219), (185, 246), (186, 196), (187, 229), (187, 233), (188, 198), (188, 200), (188, 206), (188, 239), (189, 203), (189, 231), (190, 215), (190, 226), (190, 231), (190, 239), (191, 221), (192, 199), (192, 228), (193, 223), (194, 221), (194, 232), (194, 243), (195, 204), (195, 224), (195, 225), (196, 213), (196, 215), (196, 232), (197, 214), (197, 240), (197, 241), (198, 227), (199, 205), (199, 210), (200, 219), (200, 224), (201, 203), (202, 217), (203, 216), (203, 218), (203, 222), (203, 234), (203, 237), (204, 227), (204, 230), (206, 246), (207, 215), (208, 220), (208, 221), (208, 228), (208, 229), (209, 227), (211, 215), (211, 220), (211, 228), (211, 243), (213, 214), (213, 234), (213, 236), (216, 231), (217, 237), (220, 229), (221, 236), (222, 246), (223, 225), (224, 225), (224, 244), (224, 246), (225, 229), (225, 238), (231, 236), (232, 238), (233, 234), (236, 243), (236, 245), (238, 244), (241, 243), (244, 246)]
conexiones_oficial = [] #Ya que las conexiones otrogadas por el metodo van desde el 0 hasta el 250 se crea una nueva lista para almacenar la conexiones con los codigos asignados a las personas 
conexiones_nombres = []
#se asigna a cada numero su respectivo codigo de acuerdo a la posicion que presenta en la columna.
for i in range(len(lista_conexiones)):
    conexiones_oficial.append((list_codes[lista_conexiones[i][0]],list_codes[lista_conexiones[i][1]]))
    conexiones_nombres.append((list_names[lista_conexiones[i][0]],list_names[lista_conexiones[i][1]]))

#Parte 5: CREACIÓN DEL GRAFO CON LOS CÓDIGOS Y/O NOMBRES Y ASIGNACION DE ARISTAS CON PESOS 
Grafo = nx.Graph()
for i in conexiones_oficial:
   Grafo.add_edge(i[0],i[1],weight=1)#a partir de las conexiones creadas con el metodo, añadir la arista correspondiete a cada vertice


Grafo1 = nx.Graph()
for i in conexiones_nombres:
   Grafo1.add_edge(i[0],i[1],weight=1)#a partir de las conexiones creadas con el metodo, añadir la arista correspondiete a cada vertice


colores = []
for i in Grafo.nodes():
    if '1' == i[0]:
        colores.append("red")
    elif '2' == i[0]:
        colores.append("green")
    else:
        colores.append("blue")

"""Aquí se visualiza el grafo en su totalidad"""
#           Parte 6: REPRESENTACIÓN DEL GRAFO CON LOS CÓDIGOS Y/O NOMBRES (DESCOMENTE SOLAMENTE UNA DE LAS DOS OPCIONES!!)
#OPCION 1 REPRESENTACION GRAFICA CON LOS CODIGOS    
nx.draw(Grafo,with_labels=True,node_color=colores)

#OPCION 2 REPRESENTACION GRAFICA CON LOS NOMBRES  
#nx.draw(Grafo1,with_labels=True,node_color=colores)

#           Parte 7: HALLAR LOS CÍRCULOS DE INFLUENCIA DE UNA PERSONA
#Funcion que encuentra TODOS los circulos de influencia optimos entre dos personas
def caminos_optimos(Grafo):
    k = input("Escriba un codigo y/o nombre de usuario:") #Persina inicial
    k1 = input("Escriba el codigo y/o nombre de usuario de la persona a la cual quiere contactar:") #persona objetivo
    print('\n')
    vecino_de = encontrar_vecinos(Grafo,k) #encuentra los vecinos del vertice inicial
    distancia_min = nx.dijkstra_path_length(Grafo, k, k1) #encuentra la menor distancia entre los vértices
    opciones_minimas = []#almacena todas las opciones
    for i in vecino_de:    
        todos_caminos = nx.dijkstra_path(Grafo, i, k1)#Utiliza el algoritmo de dijsktra por cada vecino que tiene el vertice inicial
        opciones_minimas.append(todos_caminos)#almacena todos los posibles caminos

    for a in opciones_minimas:
        if k in a:
            a.remove(k)#se elimina el punto inicial de la posicion incorrcta
     
    #Se imprimen todos los posibles caminos con la distancia minima entre k y k1
    print("Estas son los circulos de influencia mas óptimos para contactar a la persona:",k1) 
    for j in opciones_minimas:
        j.insert(0,k)
        if len(j)-1 == distancia_min:
            print('\n')
            print(j,"\nNúmero Miau(Erdos):",len(j)-1)

data = {'Nombre': ['Andrey Javier Lizarazo Hernandez', 'Ángel David López Espejo', 'Angel Gabriel García Falla', 'Ángela Valeria Jiménez Contreras', 'Camila Rayen Nahuel', 'Camilo Andres Fernandez Sarmiento', 'Camilo Andres Silva Rodriguez', 'Camilo Andrés Tejada Merchán', 'Carlos Andrés Galan Pérez', 'Carlos Andrés Marín Olarte', 'Carlos Andres Muñoz Buitrago', 'Carlos Sebastian Martinez Vidal', 'Carolina Rojano Alvear', 'Catherin Rodriguez Miranda', 'Cesar Felipe Segura Perilla', 'Cristian Andres Reinales Herrera', 'Cristian David Machacado Rojas', 'Dafne Valeria Castellanos Rosas', 'Dana Isabella Acosta Castillo', 'Daniel Alejandro Arias Rodriguez', 'Daniel Andrés Zárate Vélez', 'Daniel Esteban Fandiño Rodriguez', 'Daniel Estrada Patiño', 'Daniel Felipe Rambaut Lemus', 'Daniel Jacobo Castillo Gomez', 'Daniel Jose Forero Corredor', 'Daniel Leyva Castro', 'Daniela Sofia Gil Polanco', 'Daniela Torres Gómez', 'Danna Sofia Marin Guacaneme', 'David Alejandro Meléndez Galindo', 'David Alfonso Oviedo Salamanca', 'David Gregorio Vera Castellanos', 'David Leonardo Luengas Fonseca', 'David Santiago Buitrago Prada', 'David Santiago Flórez Alsina', 'Dayana Valentina Gonzalez Vargas', 'Diana Valentina Caro Corredor', 'Diego Fernando Florez Cano', 'Diryon Yonith Mora Romero', 'Edgar Santiago Jaimes Chaparro', 'Emanuel Naval Oviedo', 'Estefania Laverde Becerra', 'Fabio Andres Rizo Montoya'],
        'Codigo': [ '1;=39Y12', '1L>F0O13', '1ME>IR14', '18=U7<15', '17QX@Z16', '19SPK<17', '1K3>NC18', '1VV7AP19', '1=OF8U20', '1R<5?K21', '12K01F22', '1HU>>A23', '1R?JQG24', '1Z8;B025', '14GO:G26', '1LR@<127', '10EPMA28', '1J@S8T29', '1<TITU30', '1QQ3K631', '10EQX132', '1Y4BVL33', '1ARXFY34', '1ZK8T?35', '11O@AS36', '1BDIGP37', '1GLBV?38', '1=CP=939', '1U?5:R40', '1;6Y5Q41', '103<2X42', '1KF=E<43', '1BVV>D44', '1Z=VVG45', '17:LF446', '1MUF;147', '14GF5Y48', '1H;=4G49', '11:9RG50', '15?G2N51', '1Y0GYM52', '1M9XW;53', '1L78@P54', '1W;D1E55'],
        }
df = pd.DataFrame(data)
""" Si desea ver el dataframe no comente la siguiente línea (opcional)"""
#print(df)

""" Abajo puede buscar a la persona de interés"""
caminos_optimos(Grafo)

"""Esto a continuación es un ejemplo de la vecindad de una gran persona"""
print(\n A continuación vemos a la vecindad de Daniel Alfonso Bojacá Torres\n)
print(encontrar_vecinos(Grafo1,'Daniel Alfonso Bojacá Torres'))
