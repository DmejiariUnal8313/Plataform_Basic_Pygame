```
VideojuegoenPython
```
```
Presentadopor:
Daniel Felipe Mejia Rios
```
```
Profesor/a:
Nestor Dario Duque Mendez
```
```
Fecha
14 deNoviembre
```

## CONTENIDO

```
1.Puntotaller................................................................................................................................... 2
2.Ingenieríadesoftware(Videojuegoenconsoladecomandos)................................................. 3
3.Pasoapaso.................................................................................................................................... 8
4.Resultados................................................................................................................................... 15
5.Comojugaraljuego................................................................................................................... 20
6.Herramientausada.................................................................................................................... 21
7.Pasosdeinstalación.................................................................................................................... 21
```
**1. Puntotaller**
    Ingenieríadesoftware–LLM.

```
Basándoseenlapresentaciónentregadayexpuestaensesiónanterior,seleccioneunadelas
herramientaspresentadasorealicebúsquedaenhttps://theresanaiforthat.com/s/software/,
https://www.futuretools.io/,TopAI.tools,etc.paraescogerunadiferente,segúnlafasede:
```
- Definirel(los)componente(s)deldesarrollodesoftwareenqueseenfocaeltaller:
ingenieríaderequisitos;diseñoylaarquitectura;desarrollodecódigo;aseguramiento
delacalidad;documentacióndesoftware.
- Segúnelinterésseleccionarlaolasherramientasqueseadecuen)alosresultados
esperados.Ejecutarlosdiferentespasos.Probarlosresultadosarrojados,evaluary
refinarhastaqueseobtengalodeseado.
- Hacerunaguíapasoapasosobreelprocedimientoutilizado(incluyendolas
instalacionesyconfiguracionesqueserequieran)ylosresultadosobtenidos.
- Subireldocumentoeditableyelcódigogenerado.
- Seharáunapresentaciónenclase.

```
Lacalificaciónserá directamenteproporcional alamagnituddelasituación
enfrentada,elnúmerodecomponentesinvolucrados,lacalidaddelasalidaylarelevanciadel
informepresentado.


**2. Ingenieríadesoftware(Videojuegoenconsoladecomandos)**
    2.1. **IngenieríadeRequisitos** :Definiremoslosrequisitosdeljuegosimplequevamosa
       desarrollar,incluyendolasfuncionalidadesbásicasylasexpectativasdelos
       usuarios.


- VisualStudioCode:comoambientededesarrolloparapermitircorrereljuego
- Entradadetecladoparausarlasfuncionesdemovimientodelpersonaje
- SistemaOperativocompatibleconellenguajedeprogramación
2.2. **DiseñoyArquitectura** :eljuegoconsisteenunpersonajehechoapalostratando
dealcanzarunametapormediode 3 plataformasendistintasposiciones,al
alcanzarlametasereproduciráunsonidoquenotifiquelavictoriadeljugadory
reiniciandoelnivelcondiferentesposicionesdelasplataformasdeformaaleatoria,
aligualquelameta
2.3. **DesarrollodeCódigo** :ImplementaremoseljuegoenPythonutilizandola
bibliotecapygame,siguiendolasmejoresprácticasdeprogramación.
2.4. **AseguramientodelaCalidad** :Duranteelprocesodedesarrolloenconjuntoala
herramientaGithubCopilot,serealizaronpruebasdeevaluaciónydebugque
mostrabanelprocesodelpequeñoaplicativoenPython,esimportanteresaltarel
pasoapasodecómointegrarGithubCopilotaVisualStudioCode,estossonlos
pasosaseguir:
2.4.1. InstalarExtensionGitHubCopilotyGitHubCopilotChatdesdelasección
deExtensiones



2.4.2. IniciarsesióndeGitHubenVisualStudioCodeparatrabajarcontodoslas
extensionesqueofreceGitHub,enespecialconCopilotpararecomendar
códigosobreeleditoryCopilotChatsoportadoporGPT4o



```
puedeiniciarsesionconlacuentaregistradaensunavegador
predeterminadooescogerotracuentadiferente,esdetenerencuentaquela
cuentaqueseescojadebecontarconlasuscripcióndeGitHubCopilot,ya
seapersonaloadquiridapormediodelprogramaGitHubEducation
```
2.4.3. Autenticacióndelsistema

```
luegodelaautenticación,lapáginaseconectaraconVisualStudioCodey
```


```
activarálaextensión
```
2.4.4. Verificarestadodelaextensión

```
Unaformadeverelestadodelaextensiónesnotarelsímbolodela
mismaeneltablerodelaplicativo,unavezsepresionesobreelpermitirá
verelestadoylasconfiguracionesqueselepuedeaplicar
```


2.4.5. PruebadeGitHubCopilotChat

```
alpresionarenelbotongithubcopilotchatseabriráestapestañasimilara
```


```
unchatbotqueentregararecomendacionesdecódigo,ingenieríade
softwareydesarrollobásicosobreunoovariosarchivosqueseescojanpara
analizar,unejemplodesuusoesconestejuegocuyopasoapasoserá
retratadoenelsiguientecapítulo.
```
**3. Pasoapaso**
    3.1. InstalacióndePygame

```
Pygame esunabibliotecapopularparaeldesarrollodevideojuegosenPythonque
proporcionafuncionalidadesparamanejargráficos,sonidoyentradasdeusuario.
```


3.2 Definicióndecódigofuentebase



```
3.3primeraprueba
```
Paraestepuntodespuésdehaberdesarrolladoelcódigobaseyejecutarlocomoprueba
inicial,elcuadrosepermitirámoverseportodalapantallaenlos 4 ejes(arriba,abajo,izquierday
derecha)deacuerdolosbotonesqueelusuariopresiones
3.4Modificaciones



deacuerdoaalgunaspruebaselpersonajesequedabasuspendidoenelespacioono
saltabacorrectamente,asiquelospasosquesesugirieronfueronmodificarlalogicadesaltoyel
posicionamientodelpersonajedandocomoresultadolasiguienteprueba:



estoscambiossedieronenlossiguientesfragmentosdelcódigo



3.5Modificacionesfuertes
ahoraelsistemaparaestarmejordefinido,sehacreadounsistemadeplataformasyuna
metaporalcanzar,reproduciendounsonidocadaquelograalcanzarlameta,estossonloscodigos
usados



dandocomoresultadolasiguienteprueba


```
3.6Pasofinal
Despuésdealgunasúltimaspruebas,eljuegoestáensumayorpunto,desdequeeraun
cuadrohastaunapersonaenunasuperficieyahoraenplataformahastaunametaycadaque
cumpleesametaeljuegoharáunsonidodevictoria,siendoinfinitoenlageneracióndeniveles
```
**4. Resultados**
    _4.1Codigofuente_
    _import pygame_
    _import sys_
    _import random_

```
# Inicializar Pygame
pygame.init()
```
```
# Configurar la pantalla


_screen = pygame.display.set_mode(( 800 , 600 ))
pygame.display.set_caption('Juego Plataforma')_

_# Colores
BLACK = ( 0 , 0 , 0 )
WHITE = ( 255 , 255 , 255 )
GREEN = ( 0 , 255 , 0 )
BLUE = ( 0 , 0 , 255 )
RED = ( 255 , 0 , 0 )_

_# Superficie plana
ground_y = 550_

_# Posición inicial del jugador
player_pos = [ 400 , ground_y - 50 ]
player_size = 50_

_# Velocidad del jugador
player_speed = 5
jump_speed = 10
gravity = 0.
is_jumping = False
jump_velocity = 0_

_# Meta
goal_size = 50
goal_pos = [ 0 , 0 ]_

_# Plataformas
platforms = [
pygame.Rect( 200 , 450 , 100 , 10 ),
pygame.Rect( 400 , 350 , 100 , 10 ),
pygame.Rect( 600 , 250 , 100 , 10 )
]_

_# Cargar sonido de victoria
victory_sound = pygame.mixer.Sound('victory.wav')_

_def reset_level():
global player_pos, is_jumping, jump_velocity, goal_pos



```
player_pos = [ 400 , ground_y - 50 ]
is_jumping = False
jump_velocity = 0
randomize_platforms()
place_goal()
```
_def randomize_platforms():
for platform in platforms:
platform.x = random.randint( 0 , 700 )
platform.y = random.randint( 100 , 500 )_

_def place_goal():
platform = random.choice(platforms)
goal_pos[ 0 ] = platform.x + (platform.width - goal_size) // 2
goal_pos[ 1 ] = platform.y - goal_size_

_# Inicializar el primer nivel
reset_level()_

_# Bucleprincipal del juego
running = True
while running:
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False_

```
# Obtener las teclas presionadas
keys = pygame.key.get_pressed()
```
```
# Mover al jugador horizontalmente
if keys[pygame.K_LEFT]:
player_pos[ 0 ] -= player_speed
if keys[pygame.K_RIGHT]:
player_pos[ 0 ] += player_speed
```
```
# Saltar
if keys[pygame.K_SPACE]:
jump_velocity = -jump_speed
is_jumping = True
```


```
# Aplicar gravedad
if is_jumping:
player_pos[ 1 ] += jump_velocity
jump_velocity += gravity
if player_pos[ 1 ] >=ground_y - player_size:
player_pos[ 1 ] = ground_y - player_size
is_jumping = False
jump_velocity = 0
```
_# Colisiones con plataformas
player_rect = pygame.Rect(player_pos[ 0 ], player_pos[ 1 ], player_size,
player_size)
for platform in platforms:
if player_rect.colliderect(platform) and jump_velocity > 0 :
player_pos[ 1 ] = platform.y - player_size
is_jumping = False
jump_velocity = 0_

```
# Verificar si el jugador ha llegado a la meta
goal_rect = pygame.Rect(goal_pos[ 0 ], goal_pos[ 1 ], goal_size, goal_size)
if player_rect.colliderect(goal_rect):
victory_sound.play()
reset_level()
```
```
# Rellena la pantalla con el color de fondo
screen.fill(BLUE)
```
```
# Dibuja la superficie plana
pygame.draw.rect(screen, GREEN, ( 0 , ground_y, 800 , 50 ))
```
```
# Dibuja la meta
pygame.draw.rect(screen, RED, goal_rect)
```
```
# Dibuja las plataformas
for platform in platforms:
pygame.draw.rect(screen, WHITE, platform)
```
```
# Dibuja la persona hecha a palos
# Cuerpo
```


_pygame.draw.line(screen, WHITE, (player_pos[ 0 ] + player_size // 2 ,
player_pos[ 1 ]), (player_pos[ 0 ] + player_size // 2 , player_pos[ 1 ] +
player_size), 5 )
# Cabeza
pygame.draw.circle(screen, WHITE, (player_pos[ 0 ] + player_size // 2 ,
player_pos[ 1 ] - 10 ), 10 )
# Brazos
pygame.draw.line(screen, WHITE, (player_pos[ 0 ] + player_size // 2 ,
player_pos[ 1 ] + 20 ), (player_pos[ 0 ] + player_size // 2 - 20 , player_pos[ 1 ]
+ 40 ), 5 )
pygame.draw.line(screen, WHITE, (player_pos[ 0 ] + player_size // 2 ,
player_pos[ 1 ] + 20 ), (player_pos[ 0 ] + player_size // 2 + 20 , player_pos[ 1 ]
+ 40 ), 5 )
# Piernas
pygame.draw.line(screen, WHITE, (player_pos[ 0 ] + player_size // 2 ,
player_pos[ 1 ] + player_size), (player_pos[ 0 ] + player_size // 2 - 20 ,
player_pos[ 1 ] + player_size + 20 ), 5 )
pygame.draw.line(screen, WHITE, (player_pos[ 0 ] + player_size // 2 ,
player_pos[ 1 ] + player_size), (player_pos[ 0 ] + player_size // 2 + 20 ,
player_pos[ 1 ] + player_size + 20 ), 5 )_

```
# Actualiza la pantalla
pygame.display.flip()
```
```
# Controla lavelocidad del juego
pygame.time.Clock().tick( 30 )
```
_pygame.quit()
sys.exit()_

_juego_



**5. Comojugaraljuego**
    ObjetivodelJuego
    Elobjetivodeljuegoesmoveralpersonajeatravésdelasplataformasyalcanzarlameta
    (representadaporunrectángulorojo)encadanivel.Alalcanzarlameta,sereproduciráunsonido
    devictoriaysegeneraráunnuevonivelconplataformasyunametaennuevasposiciones
    aleatorias.
    ControlesdelJuego
       ● MoveralaIzquierda:Presionalatecladeflechaizquierda(←)paramoveralpersonaje
          hacialaizquierda.
       ● MoveralaDerecha:Presionalatecladeflechaderecha(→)paramoveralpersonajehacia
          laderecha.


```
● Saltar:Presionalabarraespaciadora(Space)parahacerqueelpersonajesalte.Elpersonaje
puederealizarhastadossaltosconsecutivosantesdeaterrizarenunaplataformaoenel
suelo.
MecánicasdelJuego
```
1. MovimientoHorizontal:
    ○ Usalasteclasdeflechaizquierdayderechaparamoveralpersonaje
       horizontalmenteatravésdelapantalla.
2. SaltoyDobleSalto:
    ○ Presionalabarraespaciadoraparahacerqueelpersonajesalte.
    ○ Elpersonajepuederealizarunsegundosaltomientrasestáenelaire,permitiendo
       alcanzarplataformasmásaltas.
    ○ Elcontadordesaltosserestablececuandoelpersonajeaterrizaenelsuelooenuna
       plataforma.
3. InteracciónconPlataformas:
    ○ Elpersonajepuedeaterrizarenplataformasdistribuidasaleatoriamenteenelnivel.
    ○ Lasplataformaspermitenalpersonajemoverseadiferentesalturasyalcanzarla
       meta.
4. Meta:
    ○ Lametaestárepresentadaporunrectángulorojocolocadoaleatoriamenteenuna
       delasplataformas.
    ○ Alalcanzarlameta,sereproduciráunsonidodevictoriaysegeneraráunnuevo
       nivel.
**6. Herramientausada**

```
GitHubCopilot
```
7. **Pasosdeinstalación**
    ● InstalarPython:
    ● DescargaeinstalaPythondesdepython.org.
    ● AsegúratedeagregarPythonalPATHdurantelainstalación.
    ● InstalarPygame:
