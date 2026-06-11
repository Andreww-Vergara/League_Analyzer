'''clases'''
class LeagueAnalyzer():
    '''class para sacar las estadísticas solicitadas, ésta es la clase más alta'''
    def __init__(self):
        self.teams=[]#array que inicia vacío

    '''funcion para añadir un nuevo equipo a una liga'''
    def add_team(self,team):
        self.teams.append(team)

    '''funcion para mostrar equipos descendientemente por victorias'''
    def get_standings(self):
        con=0
        for i in range(len(self.teams)-1):
            for j in range(len(self.teams)-1-i):
                if self.teams[j].get_win_percentage()<self.teams[j+1].get_win_percentage():
                    silla=self.teams[j+1]
                    self.teams[j+1]=self.teams[j]
                    self.teams[j]=silla
        for team in self.teams:#for creado por IA
            con=con+1
            print(f"Team {con}: {team.name}")                    
class Team():
    '''la class team crea los objetos que representan equipos de basketbol
    cada uno con sus características, además de varias funciones
    únicas como clase'''
    def __init__(self,name,wins,pointsScored,pointsAllowed,fieldGoal):
        self.name=name#en init mando los atributos de mi nuevo objeto
        self.wins=wins#lo demás es defecto o aparte del objeto
        self.pointsScored=pointsScored
        self.pointsAllowed=pointsAllowed
        self.fieldGoal=fieldGoal
        self.gamesPlayed=20#juegos ya declarados en 20 por defecto
        self.players=[]#lista de players que se añadirán posteriormente
        self.stats = ([self.gamesPlayed,self.wins,self.pointsScored,self.pointsAllowed,self.fieldGoal])
            #el doble corchete convierte la lista en una matriz y no un simple array
        #datos guardados van a una matriz
    '''funcion para obtener porcentaje de victorias respecto a partidas jugadas'''
    def get_win_percentage(self):#para saber si está bien, piensa que 10/20=50%
        return (self.wins/self.gamesPlayed)*100
    
    '''función para obtener la diferencia de puntos entre anotados y permitidos'''
    def get_points_differential(self):
        return self.pointsScored-self.pointsAllowed#si es al revés solo cambialos y ya
    
    '''funcion para añadir un nuevo jugador al equipo'''
    def add_player(self,player):#se añade objeto player dentro del objeto team, como en la vida real
        self.players.append(player)

    '''funcion para mostrar equipos descendientemente por puntos'''
    def get_roster_stats(self):
        for i in range(len(self.players)):
            print(f"Player: {self.players[i].name}")#por terminar 
class Player():
    '''class player crea objetos que representan jugadores de los equipos
    cada jugador pertenece a unequipo y tiene funciones únicas como clase'''
    def __init__(self,name,ppg,rpg,apg,mpg):
        self.name=name
        self.ppg=ppg
        self.rpg=rpg
        self.apg=apg
        self.mpg=mpg
        self.stats = ([
            self.ppg,
            self.rpg,
            self.apg,
            self.mpg
            ])#matriz para cada player

    '''funcion para mostrar la eficiencia del jugador''' 
    #no sé de basket pero según así se calcula
    def get_efficiency_rating(self):
        return (self.ppg+self.rpg+(self.apg*1.5))
    
    '''funcion que muestra la eficiencia del jugador respecto a su tiempo'''
    #esto tiene más sentido para mí
    def get_value_per_minute(self):
        return self.get_efficiency_rating()/self.mpg
'''funciones que me ahorran código'''
def team_stats(team):
    print(f"-- Team: {team.name}")
    print(f"-- Wins: {team.wins}")
    print(f"-- Points Scored: {team.pointsScored}")
    print(f"-- Points Allowed: {team.pointsAllowed}")
    print(f"-- Field Goal Percentage: {team.fieldGoal}")
    print(f"-- Win Percentage: {team.get_win_percentage()} %")
    print(f"-- Points Differential: {team.get_points_differential()}")
def player_stats(player, team):
    print(f"-- Name: {player.name}")
    print(f"-- Team: {team.name}")
    print(f"-- Points Per Game: {player.ppg}")
    print(f"-- Rebounds Per Game: {player.rpg}")
    print(f"-- Assists Per Game: {player.apg}")
    print(f"-- Minutes Played: {player.mpg}")
    print(f"-- Efficiency Rating: {player.get_efficiency_rating()}")
    print(f"-- Value Per Minute: {player.get_value_per_minute()}")
'''Validaciones'''
def valfl():#valida floats
    while True:
        try:
            local=float(input("..."))
            return local
        except:
            print("Invalid input. Please enter a correct value.")
def valint():#valida integers
    while True:
        try:
            local=int(input("..."))
            return local
        except:
            print("Invalid input. Please enter a correct value.")
def valpos(local, min, max,tipo):#valida rangos, presta atención a cómo hiciste que funcionara
    while True:
        if min<=local<=max:
            return local
        else:
            print("Invalid number.")
            try:
                local=tipo(input("..."))
                return local
            except:
                print("Invalid input. Please enter a correct value.")
def next():#ahorra una linea por uso pero al menos no escribo tanto jaja
    print("")
    input("Continue...")
#while creado unicamente para esconder registros
while True:#registros
    stats=["Games Played","Wins","Points Scored","Points Allowed","Field Goal"]
    p_stats=["Points Per Game","Rebounds Per Game","Assists Per Game","Minutes Played"]
    #datos para guardar, aqui mandamos a crear los objetos
    #ligas(solo 1 para entender todo esto)
    liga=LeagueAnalyzer()
    #equipos, datos creados por IA
    Lions=Team("Lions",15,2150,1980,0.485)
    Tigers=Team("Tigers",12,2080,2010,0.462)
    Bears=Team("Bears",18,2280,1890,0.512)
    Bulls=Team("Bulls", 18, 2300, 2001, 0.501)
    Hawks=Team("Hawks", 10, 1890, 2100, 0.455)
    Wolves=Team("Wolves", 14, 2085, 1999, 0.478)
    Sharks=Team("Sharks", 9, 1750, 2050, 0.441)
    Eagles=Team("Eagles", 16, 2220, 1955, 0.492)
    Panthers=Team("Panthers", 11, 1935, 2022, 0.463)
    Dragons=Team("Dragons", 13, 2075, 1988, 0.476)
    Falcons=Team("Falcons", 17, 2255, 1910, 0.498)
    #jugadores, datos inventados por IA
    #Lions
    lions_p1 = Player("Alex Carter", 24.1, 6.2, 5.8, 34)
    lions_p2 = Player("Brian Scott", 18.5, 4.1, 6.3, 31)
    lions_p3 = Player("Chris Young", 15.2, 7.9, 2.1, 29)
    lions_p4 = Player("David Hall", 12.8, 5.4, 3.7, 27)
    lions_p5 = Player("Evan King", 10.3, 3.2, 4.9, 25)
    lions_p6 = Player("Frank Moore", 9.1, 6.8, 1.5, 22)
    lions_p7 = Player("Gary Adams", 7.4, 2.5, 2.2, 18)
    lions_p8 = Player("Henry Lee", 6.0, 1.9, 1.3, 15)
    #tigers
    tigers_p1 = Player("Isaac Cruz", 26.4, 5.1, 6.9, 36)
    tigers_p2 = Player("Jason Reed", 20.2, 3.8, 5.0, 33)
    tigers_p3 = Player("Kevin Diaz", 17.0, 8.4, 2.6, 30)
    tigers_p4 = Player("Luis Vega", 14.5, 6.1, 3.1, 28)
    tigers_p5 = Player("Marco Ruiz", 11.8, 4.0, 4.2, 26)
    tigers_p6 = Player("Nate Cole", 9.7, 7.2, 1.4, 23)
    tigers_p7 = Player("Oscar Hill", 8.3, 2.3, 2.8, 19)
    tigers_p8 = Player("Pablo Soto", 5.9, 1.7, 1.1, 14)
    #bears
    bears_p1 = Player("Quinn Fox", 23.0, 9.1, 3.4, 35)
    bears_p2 = Player("Ryan Stone", 19.6, 4.4, 6.2, 32)
    bears_p3 = Player("Sam Green", 16.3, 7.0, 2.0, 30)
    bears_p4 = Player("Tom White", 13.7, 5.3, 3.6, 27)
    bears_p5 = Player("Uriel Snow", 12.1, 3.6, 4.5, 25)
    bears_p6 = Player("Victor Lane", 9.4, 6.5, 1.8, 22)
    bears_p7 = Player("Will Grant", 7.6, 2.8, 2.1, 18)
    bears_p8 = Player("Xavier Ross", 6.2, 1.5, 1.0, 14)
    #bulls
    bulls_p1 = Player("Yahir Cruz", 27.3, 6.7, 5.5, 37)
    bulls_p2 = Player("Zane Brooks", 21.1, 4.2, 6.8, 34)
    bulls_p3 = Player("Alan Price", 18.4, 8.1, 2.3, 31)
    bulls_p4 = Player("Bruno Miles", 15.0, 5.9, 3.0, 29)
    bulls_p5 = Player("Cody West", 12.6, 3.7, 4.1, 26)
    bulls_p6 = Player("Derek Shaw", 10.2, 7.4, 1.6, 23)
    bulls_p7 = Player("Eli Ward", 8.0, 2.6, 2.7, 19)
    bulls_p8 = Player("Finn Cole", 6.4, 1.8, 1.2, 15)
    #hawks
    hawks_p1 = Player("Gabe Hunt", 22.9, 5.5, 7.1, 35)
    hawks_p2 = Player("Hugo Perez", 19.0, 4.3, 5.6, 32)
    hawks_p3 = Player("Ivan Luna", 16.8, 7.6, 2.2, 30)
    hawks_p4 = Player("Joel King", 14.1, 5.1, 3.8, 27)
    hawks_p5 = Player("Kyle Nash", 11.9, 3.9, 4.0, 25)
    hawks_p6 = Player("Leo Grant", 9.3, 6.2, 1.7, 22)
    hawks_p7 = Player("Mason Boyd", 7.5, 2.1, 2.3, 18)
    hawks_p8 = Player("Noel Ray", 5.8, 1.6, 1.4, 14)
    #wolves
    wolves_p1 = Player("Omar Silva", 25.0, 6.0, 6.4, 36)
    wolves_p2 = Player("Pedro Campos", 20.7, 4.8, 5.1, 33)
    wolves_p3 = Player("Raul Ortiz", 17.2, 8.5, 2.5, 30)
    wolves_p4 = Player("Sergio Leon", 13.9, 5.7, 3.3, 28)
    wolves_p5 = Player("Tomas Rios", 12.0, 3.4, 4.6, 26)
    wolves_p6 = Player("Ulises Mena", 9.8, 6.9, 1.9, 23)
    wolves_p7 = Player("Victor Cruz", 7.1, 2.2, 2.0, 18)
    wolves_p8 = Player("Walter Ibarra", 6.3, 1.9, 1.2, 15)
    #sharks
    sharks_p1 = Player("Ximena Vega", 21.8, 5.0, 7.4, 35)
    sharks_p2 = Player("Yuri Soto", 18.6, 4.1, 5.9, 32)
    sharks_p3 = Player("Zaid Luna", 16.0, 7.2, 2.1, 30)
    sharks_p4 = Player("Adan Flores", 13.4, 5.3, 3.5, 27)
    sharks_p5 = Player("Beto Ruiz", 11.2, 3.8, 4.3, 25)
    sharks_p6 = Player("Cesar Neri", 9.0, 6.1, 1.6, 22)
    sharks_p7 = Player("Diego Paz", 7.2, 2.4, 2.5, 18)
    sharks_p8 = Player("Enzo Gil", 5.6, 1.7, 1.0, 14)
    #eagles
    eagles_p1 = Player("Fabian Cruz", 26.1, 6.4, 6.0, 36)
    eagles_p2 = Player("Gael Mora", 21.5, 4.0, 6.7, 34)
    eagles_p3 = Player("Hector Ruiz", 18.1, 8.0, 2.4, 31)
    eagles_p4 = Player("Iker Salas", 15.3, 5.6, 3.2, 29)
    eagles_p5 = Player("Jorge Lara", 12.4, 3.5, 4.8, 26)
    eagles_p6 = Player("Kevin Ponce", 10.1, 7.1, 1.7, 23)
    eagles_p7 = Player("Luis Nieto", 8.2, 2.7, 2.2, 19)
    eagles_p8 = Player("Mario Rojas", 6.5, 1.8, 1.3, 15)
    #panthers
    panthers_p1 = Player("Nico Reyes", 24.7, 5.9, 6.3, 35)
    panthers_p2 = Player("Oscar Peña", 20.0, 4.3, 5.5, 33)
    panthers_p3 = Player("Pablo León", 17.6, 7.7, 2.0, 30)
    panthers_p4 = Player("Quico Mejia", 14.8, 5.2, 3.4, 28)
    panthers_p5 = Player("Rene Soto", 12.2, 3.9, 4.1, 26)
    panthers_p6 = Player("Saul Vega", 9.5, 6.6, 1.8, 23)
    panthers_p7 = Player("Tadeo Cruz", 7.3, 2.3, 2.6, 18)
    panthers_p8 = Player("Uriel Diaz", 5.7, 1.5, 1.1, 14)
    #dragons
    dragons_p1 = Player("Victor Chan", 27.0, 6.8, 5.7, 37)
    dragons_p2 = Player("Wei Lin", 22.1, 4.5, 6.2, 34)
    dragons_p3 = Player("Xiao Peng", 18.9, 8.3, 2.6, 31)
    dragons_p4 = Player("Yan Zhou", 15.6, 5.4, 3.1, 29)
    dragons_p5 = Player("Zhen Liu", 13.0, 3.6, 4.4, 26)
    dragons_p6 = Player("Bo Fang", 10.4, 7.0, 1.5, 23)
    dragons_p7 = Player("Chen Hao", 8.1, 2.5, 2.2, 19)
    dragons_p8 = Player("Dong Lei", 6.6, 1.9, 1.0, 15)
    #falcons
    falcons_p1 = Player("Aaron Blake", 25.8, 6.1, 6.6, 36)
    falcons_p2 = Player("Brent Cole", 21.0, 4.2, 5.8, 33)
    falcons_p3 = Player("Caleb Ford", 17.9, 7.8, 2.3, 31)
    falcons_p4 = Player("Dylan Shaw", 14.6, 5.5, 3.7, 28)
    falcons_p5 = Player("Ethan Ross", 12.3, 3.4, 4.9, 26)
    falcons_p6 = Player("Felix Grant", 9.9, 6.3, 1.6, 23)
    falcons_p7 = Player("Gavin Price", 7.8, 2.6, 2.4, 19)
    falcons_p8 = Player("Hunter Lane", 6.1, 1.7, 1.2, 15)
    #con esto los guardamos en sus respectivas listas
    #equipos a ligas
    liga.add_team(Lions)#1
    liga.add_team(Tigers)#2
    liga.add_team(Bears)#3
    liga.add_team(Bulls)#4
    liga.add_team(Hawks)#5
    liga.add_team(Wolves)#6
    liga.add_team(Sharks)#7
    liga.add_team(Eagles)#8
    liga.add_team(Panthers)#9
    liga.add_team(Dragons)#10
    liga.add_team(Falcons)#11
    #jugadores a equipos
    #lions
    Lions.add_player(lions_p1)
    Lions.add_player(lions_p2)
    Lions.add_player(lions_p3)
    Lions.add_player(lions_p4)
    Lions.add_player(lions_p5)
    Lions.add_player(lions_p6)
    Lions.add_player(lions_p7)
    Lions.add_player(lions_p8)
    #tigers
    Tigers.add_player(tigers_p1)
    Tigers.add_player(tigers_p2)
    Tigers.add_player(tigers_p3)
    Tigers.add_player(tigers_p4)
    Tigers.add_player(tigers_p5)
    Tigers.add_player(tigers_p6)
    Tigers.add_player(tigers_p7)
    Tigers.add_player(tigers_p8)
    #bears
    Bears.add_player(bears_p1)
    Bears.add_player(bears_p2)
    Bears.add_player(bears_p3)
    Bears.add_player(bears_p4)
    Bears.add_player(bears_p5)
    Bears.add_player(bears_p6)
    Bears.add_player(bears_p7)
    Bears.add_player(bears_p8)
    #bulls
    Bulls.add_player(bulls_p1)
    Bulls.add_player(bulls_p2)
    Bulls.add_player(bulls_p3)
    Bulls.add_player(bulls_p4)
    Bulls.add_player(bulls_p5)
    Bulls.add_player(bulls_p6)
    Bulls.add_player(bulls_p7)
    Bulls.add_player(bulls_p8)
    #hawks
    Hawks.add_player(hawks_p1)
    Hawks.add_player(hawks_p2)
    Hawks.add_player(hawks_p3)
    Hawks.add_player(hawks_p4)
    Hawks.add_player(hawks_p5)
    Hawks.add_player(hawks_p6)
    Hawks.add_player(hawks_p7)
    Hawks.add_player(hawks_p8)
    #wolves
    Wolves.add_player(wolves_p1)
    Wolves.add_player(wolves_p2)
    Wolves.add_player(wolves_p3)
    Wolves.add_player(wolves_p4)
    Wolves.add_player(wolves_p5)
    Wolves.add_player(wolves_p6)
    Wolves.add_player(wolves_p7)
    Wolves.add_player(wolves_p8)
    #sharks
    Sharks.add_player(sharks_p1)
    Sharks.add_player(sharks_p2)
    Sharks.add_player(sharks_p3)
    Sharks.add_player(sharks_p4)
    Sharks.add_player(sharks_p5)
    Sharks.add_player(sharks_p6)
    Sharks.add_player(sharks_p7)
    Sharks.add_player(sharks_p8)
    #eagles
    Eagles.add_player(eagles_p1)
    Eagles.add_player(eagles_p2)
    Eagles.add_player(eagles_p3)
    Eagles.add_player(eagles_p4)
    Eagles.add_player(eagles_p5)
    Eagles.add_player(eagles_p6)
    Eagles.add_player(eagles_p7)
    Eagles.add_player(eagles_p8)
    #panthers
    Panthers.add_player(panthers_p1)
    Panthers.add_player(panthers_p2)
    Panthers.add_player(panthers_p3)
    Panthers.add_player(panthers_p4)
    Panthers.add_player(panthers_p5)
    Panthers.add_player(panthers_p6)
    Panthers.add_player(panthers_p7)
    Panthers.add_player(panthers_p8)
    #dragons
    Dragons.add_player(dragons_p1)
    Dragons.add_player(dragons_p2)
    Dragons.add_player(dragons_p3)
    Dragons.add_player(dragons_p4)
    Dragons.add_player(dragons_p5)
    Dragons.add_player(dragons_p6)
    Dragons.add_player(dragons_p7)
    Dragons.add_player(dragons_p8)
    #falcons
    Falcons.add_player(falcons_p1)
    Falcons.add_player(falcons_p2)
    Falcons.add_player(falcons_p3)
    Falcons.add_player(falcons_p4)
    Falcons.add_player(falcons_p5)
    Falcons.add_player(falcons_p6)
    Falcons.add_player(falcons_p7)
    Falcons.add_player(falcons_p8)
    break
#programa en sí
while True:
    print("")
    print("-"*3,"choose something: ","-"*3)
    print("-- 1.  Teams -------")
    print("-- 2.  Players -----")
    print("-- 3.  Statistics --")
    print("-- 4.  Exit --------")
    numero=valint()
    if numero==1:#si escoge teams
        print("-"*5,"Teams: ","-"*5)
        print("-"*3,"choose something: ","-"*3)
        print("-- 1.  See teams ------")
        print("-- 2.  Add new team ---")
        print("-- 3.  Exit -----------")
        teamnum=valint()
        if teamnum==1:#ver team
            print("--- Select a team to analyze: ---")
            for i in range(len(liga.teams)):
                print(f"-- {i+1}. {liga.teams[i].name} ---")
            deuxnum=valpos(valint(),1,len(liga.teams),int)
            print("--- What do you want to see? ---")
            print("-- 1.  See team statistics -----")
            print("-- 2.  See team players --------")
            troisnum=valint()
            if troisnum==1:
                for j in range(len(liga.teams)):
                    if deuxnum==j+1:
                        team_stats(liga.teams[j])
                next()  
            elif troisnum==2:
                for j in range(len(liga.teams)):
                    if deuxnum==j+1:
                        for k in range(8):
                            print(liga.teams[j].players[k].name)#linea muy importante de repasar
                next()
            else:
                print("Invalid input.")
                next()
            continue
        elif teamnum==2:#añadir team
            print("--- Enter team name:")
            name=input("...")#estos son valores locales
            print("--- Enter wins:")#no afecta que se llamen igual
            wins=valpos(valint(),0,20,int)
            print("--- Enter points scored:")
            pointsScored=valpos(valint(),0,4000,int)
            print("--- Enter points allowed:")
            pointsAllowed=valpos(valint(),0,4000,int)
            print("--- Enter field goal percentage:")
            fieldGoal=valpos(valfl(),0,1,float)
            new_team=Team(name,wins,pointsScored,pointsAllowed,fieldGoal)
            liga.add_team(new_team)
            print("--- Team added successfully! ---")
            next()
        elif teamnum==3:
            False
        else:
            print("Invalid input.")
            next()
    elif numero==2:#si escoge players
        print("--- Select a team first: ---")
        for i in range(len(liga.teams)):#for para impresion de nombres-team
            print(f"-- {i+1}. {liga.teams[i].name} ---")
        deuxnum=valpos(valint(), 1,len(liga.teams),int)
        for k in range(len(liga.teams)):#for para busqueda de team
            if deuxnum==k+1:
                print("--- Team: ", liga.teams[k].name," ---")
                print("--- Select a player: ---")
                for j in range(len(liga.teams[k].players)):#for para impresion-players
                    print(f"-- {j+1}. {liga.teams[k].players[j].name}")
                troisnum=valpos(valint(),1,len(liga.teams[k].players),int)
                for m in range(len(liga.teams[k].players)):
                    if troisnum==m+1:
                        player_stats(liga.teams[k].players[m],liga.teams[k])
                next()
    elif numero==3:#si escoge statistics
        print("-"*5,"Statistics: ","-"*5)
        print("-- 1.  To Compare Teams -----")#comparar equipos
        print("-- 2.  To Compare Players ---")#comparar jugadores
        print("-- 3.  Standings ------------")#clasificacion por %
        print("-- 4.  Top Scorers ----------")#top 5 equipos
        print("-- 5.  Exit To Menu ---------")#salir
        statnum=valint()
        if statnum==1:#comparar equipos
            print("-- To Compare Teams -----")
            print("--- Select 1 team to compare: ---")
            for i in range(0,len(liga.teams)):
                print(f"-- {i+1}. {liga.teams[i].name} ---")
            unnum=valpos(valint(),1,len(liga.teams),int)
            print("--- Select the team to compare to: ---")
            deuxnum=valpos(valint(),1,len(liga.teams),int)
            while unnum==deuxnum:
                print("You can't compare the same team")
                deuxnum=valpos(valint(),1,len(liga.teams),int)
            for k in range(len(liga.teams)):#busca primer equipo
                if unnum==k+1:
                    print("")
                    break
            for r in range(len(liga.teams)):#busca segundo equipo
                if deuxnum==r+1:
                    print("")
                    print(f"--- Comparison between {liga.teams[k].name} and {liga.teams[r].name}")
                    for m in range(len(liga.teams[k].stats)):
                        print(f"{m+1}. {stats[m-1]} of {liga.teams[k].name}: {liga.teams[k].stats[m-1]}")
                        print(f"{m+1}. {stats[m-1]} of {liga.teams[r].name}: {liga.teams[r].stats[m-1]}")
                        print("")
            next()
            continue
        if statnum==2:#comparar jugadores
            print("-- To Compare Players ---")
            print("--- Select a team first: ---")
            for i in range(len(liga.teams)):#for para impresion de nombres-team
                print(f"-- {i+1}. {liga.teams[i].name} ---")
            unnum=valpos(valint(), 1,len(liga.teams),int)
                    
            print("--- Team: ", liga.teams[unnum-1].name," ---")
            print("--- Select a player: ---")
            for j in range(0,len(liga.teams[unnum-1].players)):#for para impresion-players
                print(f"-- {j+1}. {liga.teams[unnum-1].players[j].name}")
            p1=valpos(valint(),1,len(liga.teams[unnum-1].players),int)
            print("--- Player: ", liga.teams[unnum-1].players[p1-1].name," ---")

            print("--- Select the other team: ---")
            for i in range(0,len(liga.teams)):#for para impresion de nombres-team
                print(f"-- {i+1}. {liga.teams[i].name} ---")
            deuxnum=valpos(valint(), 1,len(liga.teams),int)

            print("--- Team: ", liga.teams[deuxnum-1].name," ---")

            print("--- Select a player: ---")
            for l in range(0,len(liga.teams[deuxnum-1].players)):#for para impresion-players
                print(f"-- {l+1}. {liga.teams[deuxnum-1].players[l].name}")
            p2=valpos(valint(),1,len(liga.teams[deuxnum-1].players),int)    
            print("--- Player: ", liga.teams[deuxnum-1].players[p2-1].name," ---")

            print(f"--- Comparison between {liga.teams[unnum-1].players[p1-1].name} from {liga.teams[unnum-1].name} and {liga.teams[deuxnum-1].players[p2-1].name} from {liga.teams[deuxnum-1].name}")
            
            for m in range(4):
                print(f"{m+1}. {p_stats[m-1]} of {liga.teams[unnum-1].players[p1-1].name} from {liga.teams[unnum-1].name}: {liga.teams[unnum-1].players[p1-1].stats[m-1]}")
                print(f"{m+1}. {p_stats[m-1]} of {liga.teams[deuxnum-1].players[p2-1].name} from {liga.teams[deuxnum-1].name}: {liga.teams[deuxnum-1].players[p2-1].stats[m-1]}")
                print("")
            next()
            continue
        elif statnum==3:#clasificacion por %
            print("--  Standings ------------")
            liga.get_standings()
        elif statnum==4:#top 5 equipos
            print("--  Top Scorers ----------")
            for i in range(len(liga.teams)-1):
                for j in range(len(liga.teams)-1-i):
                    if liga.teams[j].get_win_percentage()<liga.teams[j+1].get_win_percentage():
                        silla=liga.teams[j+1]
                        liga.teams[j+1]=liga.teams[j]
                        liga.teams[j]=silla
            for i in range (5):#for creado por IA
                print(f"Team {i+1}: {liga.teams[i].name}") 
        elif statnum==5:#salir
            print("--  Exit To Menu ---------") 
        else:
            print("Invalid input.")
            next()
    elif numero==4:#si decide salir
        break
    else:#si no le atina
        print("Invalid input.")
        next()
print("Thank you for trying me!")
#examen hecho 95% por mi cuenta, las partes hechas con IA están señaladas
