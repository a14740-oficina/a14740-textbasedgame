import time
print("Bem vindo ao meu textbased game ")
time.sleep(2.5)
print("És vitinha  um bilionário que gostava muito de viajar com o seu jato privado. Seu destino favorito? São Paulo uma cidade no Brasil, todos os anos você a visita e esse ano não é diferente. Porém este ano um ciclone tropical que dificultava muito as viagens tanto de barco como de avião atacava as águas do pacífico, apesar do seu amigo e piloto particular André o avisar  que talvez o melhor era não fazer essa viagem ele insistiu, e vocês lá foram  sobrevoando o pacífico. Quando estavam quase a chegar depararam-se com uma enorme tempestade que vos engoliu por completo,o jato perdeu o controle e acabou por cair numa ilha chamada Ilha de Queimada Grande que fica situada a noroeste de São Paulo. O único sobrevivente é você Vitinha.")
time.sleep(3)
print("Acordaste no meio dos destroços do jato porém reparas que estás de cabeça para baixo a única coisa que te segura é o cinto do banco onde estavas sentado bebendo a tua uma Cognac está tudo em chamas tens de sair daí!!!!")


cm=int(input("Carrega na tecla 1 para pegar na faca que tens no bolso de trás da calça:"))

if cm == 1:
  print("Conseguiste cortar o cinto e escapar das chamas mas começou a chover precisas te abrigar, se não podes ficar doente e como não tens acessa a qualquer tipo de antibiótico qualquer tipo de doença seria fatal para tí!!!")
else:
  print("HEEHEHEHE diz lá é quentinho não é vitinha")
  time.sleep(1)
  print("FIM DA LINHA PARA TÍ MORRESTE QUEIMADO")
  exit()
print("começas a ir em direção á densa floresta, entrando nela, percebes que será muito difícil te orientares pois tem muita vegetação e árvores enormes ")
time.sleep(2)
escolha=int(input("o caminho para a frente está bloqueado queres ir para a esquerda(1) ou direita(2)?"))

if escolha == 1 :
  print ("encontraste um acampamento que parece ter sido usado recentemente tens uma fogueira apagada e uma tenda onde podes descansar queres ficar aqui ou procurar outro lugar? Não sei porque irias fazer isso mas eu dou-te sempre opção de escolha lembra-te estás fraco e precisas de descansar")
  s = int(input("passar a noite no acampamento(1), voltar atrás e ir pela direita(2): "))
elif escolha == 2 :
  print("encontaste uma caverna, ao entrar nela encontras uma fortuna em barras de ouro e um explorador deitado sem vida ao lado pegas recursos do viagante que esta sem vida para te ajudar a sobreviver e te deparas com um rádio porém não tem pilhas pode ser uma forma de saíres daqui precisas de descansar amanhã poderás procurar")
  s = int(input("passar a noite na caverna(1), voltar atrás e ir pela esquerda(2): "))
if s != 1 :
  print("ao voltar para trás acabaste por te perder e foste picado por uma víbora uma das cobras mais venenosas do mundo esqueci de te dizer esta ilha também é conhecida por ilha das cobras")
  exit()


time.sleep(3)
if escolha == 1 :
  print("Bom dia vitinha estás pronto para explorar a ilha ? Primeiro explora mais o acampamento pode haver algo de útil")
  time.sleep(2)
  print("a única coisa que encontras são pilhas porém podem ser úteis")
  print("agora podes explorar o outro lado da floresta ao caminhar um pouco encontras uma caverna lá encontras um pote cheio de barras de ouro provavelmente deixadas por piratas a muito tempo atrás, surpreendeste ao encontrar também um corpo que provavelmente era da pessoa do acampamento,vasculhas o corpo e encontras um rádio!!!   Agora podes colocar as pilhas nele")
  f =int(input("mete as pilhas no rádio(1)"))
  
elif escolha == 2 :
  print("agora que está de dia podes ir vasculhar encontras-te um mapa no explorador que te leva ao acampamento dele ")
  time.sleep(2)
  print("depois de algumas horas a andar a pé encontras o acampamento e encontras as pilhas para o rádio!!!!")
  f =int(input("mete as pilhas no rádio(1):"))
while f != 1:
  f =int(input("mete as pilhas no rádio(1):"))

print("Consegues contactar um dos teus amigos que estava a caminho do Brazil para uma festa privada, falas com ele e ele vem te resgatar ")

if escolha == 1 :
  print("tens uma conversa com ele e perguntas se podes ir a festa porém ele recusa pois é preciso pagar caro para entrar lá parece que vais voltar para casa.Que pena ")
  time.sleep(2)
  print("obrigado por jogar o meu jogo!!!")
  exit()

elif escolha == 2 :
  print("chegas ao helicoptero e o teu amigo fica abismado com oque a quantidade de barras de ouro que levas ele avisa-te da festa e diz para ires pois com essa quantidade de ouro podias aproveitar a festa se é que me entendes hehehehehe.")
  time.sleep(2)
  g =int(input("queres ir á festa(1) ou ir para casa descansar(2)"))
if g == 1 :
  print("Chegando lá tiveste a melhor festa da tua vida porém aproveitas-te um pouco de mais e morreste por overdose")
  time.sleep(2)
  print("obrigado por Jogar!!!!!")
  exit()
elif g == 2 :
  ("foste para casa e gannhaste muito dinheiro com a tua História chegando até a escrever um livro viveste uma vida longa e feliz morrendo aos 96 anos de idade com 15 filhos em uma das tuas masões.Um final que na minha opinião um final bem honrado!!!!")
  time.sleep(2)
  print("obrigado por Jogar!!!!!")
  exit()
