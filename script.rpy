                                                                                                                              
init:
    $ dissolve = Dissolve(1.0)
    $ rightPos = Position(xpos=0.55, ypos=0.1)
    $ leftPos = Position(xpos=0.05, ypos=0.1)
    $ leftPos2 = Position(xpos=0.25, ypos=0.9)
    $ rightPos2 = Position(xpos=0.75, ypos=0.9)
    $ leftPos3 = Position(xpos=0.35, ypos=0.78)
    $ rightPos3= Position(xpos=0.65, ypos=0.78)
     
    define config.window_icon = "icon.png"
    
    
init python:
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

screen donate:
    
    tag menu

    # Include the navigation.
    use navigation
    
    # The background of the game menu.
    window:
        style "gm_root"
            # The various buttons.
            
    frame:
        xalign .5
        yalign .07
        text "Donations":
            size 60
    
    frame:
        xpos .5
        ypos .25
        ysize 250
        xsize 3
        
    frame:
        xpos .05
        ypos .25
        ysize 3
        xsize 850
        
    frame:
        xpos .05
        ypos .66
        ysize 3
        xsize 850      
    
    frame:
        xalign .25
        yalign .45
        ysize 70
        xsize 200
        button:
            action OpenURL("http://paypal.me/TheVoyage")
            ysize 58
            xsize 188
            text _("PayPal"):
                size 40 
                line_leading 5
                xalign 0.5
    
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98
        has vbox
        textbutton _("Back") action Return()
    
    window:
        text "We hope you enjoyed this visual novella and your donation would make us unspeakably happy! You can donate either by PayPal or Bitcoin. PayPal button links to our tip jar where you can choose the amount you want to tip. To donate bitcoin, use the QR-code on the screen." size 18
        xsize 900
        yalign .93
        xalign .45

    add "qr.png" xalign .85 yalign .42
    add "coin_pressed.png" xalign .6 yalign .45 zoom 0.4
    
init -2 python:
    style.gm_nav_button.size_group = "gm_nav"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image musta = "taustat/musta.png"               ##VALMIS##
image ikkuna = "taustat/tausta1.png"            ##VALMIS##
image vuori = "taustat/vuori.png"               ##VALMIS##
image linna = "taustat/linna.png"               ##VALMIS##
image tanssisali = "taustat/tanssisali.png"     ##VALMIS##
image palava = "taustat/palava.png"             ##VALMIS##
image portaikko = "taustat/portaikko.png"       ##VALMIS##
image portaikko2 = "taustat/portaikko2.png"     ##VALMIS##
image kirkko = "taustat/kirkko.png"             ##VALMIS##
image yöhepo = "taustat/horse.png"              ##VALMIS##
image tykkikansi = "taustat/tykkikansi.png"     ##VALMIS##
image satama = "taustat/satama.png"             ##VALMIS##
image laivapäivä = "taustat/laivapaiva.png"     ##VALMIS##
image laivayö = "taustat/laivayo.png"           ##VALMIS##
image cabin = "taustat/cabin.png"               ##VALMIS##
image battle = "taustat/battle.png"             ##VALMIS##
image muuri = "taustat/muuri.png"               ##VALMIS##
image teltta = "taustat/tent.png"               ##VALMIS##
image cabinyö = "taustat/cabinyo.png"           ##VALMIS##
image blood = "taustat/blood.png"               ##VALMIS##
image end = "taustat/loppu.png"                 ##VALMIS##
image dress = "taustat/dress_item.png"
image chess = "taustat/chess_item.png"
image flask = "taustat/flask_item.png"
image nest = "taustat/nest_item.png"
image whale = "taustat/whale_item.png"
image coin = "taustat/coin_item.png"

image ctc_animation = Animation("cpc1.png", 0.2, "cpc2.png", 0.2, "cpc3.png", 0.2, xpos=0.97, ypos=0.965, xanchor=1.0, yanchor=1.0)

# Declare characters used by this game.
define e = Character('Eugenie', color="#e4f4fc", show_two_window=True, callback=speaker("e"))
define v = Character('Vassan', color="#e4f4fc", show_two_window=True, callback=speaker("v"))
define m = Character('Memnon', color="#e4f4fc",show_two_window=True,ctc="ctc_animation", ctc_position="fixed", callback=speaker("m"))
define w = Character('Wazu', color="#e4f4fc",show_two_window=True)
define r = Character('Rider',  color="#e4f4fc",show_two_window=True)
define ru = Character('Rumri', color="#e4f4fc",show_two_window=True)
define k = Character('Captain', color="#e4f4fc",show_two_window=True)
define eg = Character('Egbert', color="#e4f4fc",show_two_window=True)
define vi = Character('Foe', color="#e4f4fc",show_two_window=True)
define t = Character('Gunnery Sergeant', color="#e4f4fc",show_two_window=True)
define h = Character('Hulegu', color="#e4f4fc",show_two_window=True)
define s = Character('Soldier', color="#e4f4fc",show_two_window=True)
define narrator = Character(None,ctc="ctc_animation",ctc_position="fixed",)


############
###VASSAN###
############

############
###NORMAL###
############
image vassan normal = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/vassan_normal.png",
    (0, 0), "vassan eyes normal",
    (0, 0), WhileSpeaking("v", "vassan mouth normal", "hahmot/vassan_normal_mouth0.png"),
    )
image vassan eyes normal:
    "hahmot/vassan_normal_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/vassan_normal_eyes1.png"
    .25
    repeat
    
image vassan mouth normal:
    "hahmot/vassan_normal_mouth1.png"
    .2
    "hahmot/vassan_normal_mouth2.png"
    .2
    repeat
    
###########
###SHOCK###
###########
image vassan shock = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/vassan_normal.png",
    (0, 0), "vassan eyes shock",
    (0, 0), WhileSpeaking("v", "vassan mouth shock", "hahmot/vassan_shock_mouth0.png"),
    )
image vassan eyes shock:
    "hahmot/vassan_shock_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/vassan_shock_eyes1.png"
    .25
    repeat
    
image vassan mouth shock:
    "hahmot/vassan_shock_mouth1.png"
    .2
    "hahmot/vassan_shock_mouth2.png"
    .2
    repeat
    
###########
###ANGRY###
###########
image vassan angry = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/vassan_normal.png",
    (0, 0), "vassan eyes angry",
    (0, 0), WhileSpeaking("v", "vassan mouth angry", "hahmot/vassan_angry_mouth0.png"),
    )
image vassan eyes angry:
    "hahmot/vassan_angry_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/vassan_angry_eyes1.png"
    .25
    repeat
    
image vassan mouth angry:
    "hahmot/vassan_angry_mouth1.png"
    .2
    "hahmot/vassan_angry_mouth2.png"
    .2
    repeat
    
###########
###SLEEP###
###########
image vassan sleep = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/vassan_normal.png",
    (0, 0), "vassan eyes sleep",
    (0, 0), WhileSpeaking("v", "vassan mouth sleep", "hahmot/vassan_normal_mouth0.png"),
    )
image vassan eyes sleep:
    "hahmot/vassan_normal_eyes1.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/vassan_normal_eyes1.png"
    .25
    repeat
    
image vassan mouth sleep:
    "hahmot/vassan_normal_mouth1.png"
    .2
    "hahmot/vassan_normal_mouth2.png"
    .2
    repeat

#############
###NEUTRAL###
#############
image vassan neutral = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/vassan_normal.png",
    (0, 0), "vassan eyes neutral",
    (0, 0), WhileSpeaking("v", "vassan mouth neutral", "hahmot/vassan_neutral_mouth0.png"),
    )
image vassan eyes neutral:
    "hahmot/vassan_normal_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/vassan_normal_eyes1.png"
    .25
    repeat
    
image vassan mouth neutral:
    "hahmot/vassan_normal_mouth1.png"
    .2
    "hahmot/vassan_normal_mouth2.png"
    .2
    repeat
    
###########
###SMILE###
###########
image vassan smile = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/vassan_normal.png",
    (0, 0), "vassan eyes smile",
    (0, 0), WhileSpeaking("v", "vassan mouth smile", "hahmot/vassan_smile_mouth0.png"),
    )
image vassan eyes smile:
    "hahmot/vassan_smile_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/vassan_smile_eyes1.png"
    .25
    repeat
    
image vassan mouth smile:
    "hahmot/vassan_smile_mouth1.png"
    .2
    "hahmot/vassan_smile_mouth2.png"
    .2
    repeat
    
###########
###LAUGH###
###########
image vassan laugh = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/vassan_normal.png",
    (0, 0), "vassan eyes laugh",
    (0, 0), WhileSpeaking("v", "vassan mouth laugh", "hahmot/vassan_laugh_mouth0.png"),
    )
image vassan eyes laugh:
    "hahmot/vassan_smile_eyes1.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/vassan_smile_eyes1.png"
    .25
    repeat
    
image vassan mouth laugh:
    "hahmot/vassan_laugh_mouth1.png"
    .2
    "hahmot/vassan_laugh_mouth2.png"
    .2
    repeat
    
############
###CRYING###
############
image vassan crying = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/vassan_normal.png",
    (0, 0), "vassan eyes crying",
    (0, 0), WhileSpeaking("v", "vassan mouth crying", "hahmot/vassan_angry_mouth0.png"),
    )
image vassan eyes crying:
    "hahmot/vassan_crying_eyes1.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/vassan_crying_eyes1.png"
    .25
    repeat
    
image vassan mouth crying:
    "hahmot/vassan_angry_mouth1.png"
    .2
    "hahmot/vassan_angry_mouth2.png"
    .2
    repeat

############
###MEMNON###
############

############
###NORMAL###
############
image memnon normal = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/memnon_normal.png",
    (0, 0), "memnon eyes normal",
    (0, 0), WhileSpeaking("m", "memnon mouth normal", "hahmot/memnon_normal_mouth0.png"),
    )
image memnon eyes normal:
    "hahmot/memnon_normal_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/memnon_normal_eyes1.png"
    .25
    repeat
    
image memnon mouth normal:
    "hahmot/memnon_normal_mouth1.png"
    .2
    "hahmot/memnon_normal_mouth2.png"
    .2
    repeat
    
###########
###SMILE###
###########
image memnon smile = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/memnon_normal.png",
    (0, 0), "memnon eyes smile",
    (0, 0), WhileSpeaking("m", "memnon mouth smile", "hahmot/memnon_smile_mouth0.png"),
    )
image memnon eyes smile:
    "hahmot/memnon_smile_eyes1.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/memnon_smile_eyes1.png"
    .25
    repeat
    
image memnon mouth smile:
    "hahmot/memnon_smile_mouth1.png"
    .2
    "hahmot/memnon_smile_mouth2.png"
    .2
    repeat

#############
###SERIOUS###
#############
image memnon serious = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/memnon_normal.png",
    (0, 0), "memnon eyes serious",
    (0, 0), WhileSpeaking("m", "memnon mouth serious", "hahmot/memnon_serious_mouth0.png"),
    )
image memnon eyes serious:
    "hahmot/memnon_serious_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/memnon_serious_eyes1.png"
    .25
    repeat
    
image memnon mouth serious:
    "hahmot/memnon_serious_mouth1.png"
    .2
    "hahmot/memnon_serious_mouth2.png"
    .2
    repeat
    
############
###CRYING###
############
image memnon crying = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/memnon_normal.png",
    (0, 0), "memnon eyes crying",
    (0, 0), WhileSpeaking("m", "memnon mouth crying", "hahmot/memnon_crying_mouth0.png"),
    )
image memnon eyes crying:
    "hahmot/memnon_crying_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/memnon_crying_eyes1.png"
    .25
    repeat
    
image memnon mouth crying:
    "hahmot/memnon_serious_mouth1.png"
    .2
    "hahmot/memnon_serious_mouth2.png"
    .2
    repeat
    
    
#############
###TRANSSI###
#############
image memnon transsi = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/memnon_normal.png",
    (0, 0), "memnon eyes transsi",
    (0, 0), WhileSpeaking("m", "memnon mouth transsi", "hahmot/memnon_serious_mouth0.png"),
    )
image memnon eyes transsi:
    "hahmot/memnon_transsi_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/memnon_transsi_eyes0.png"
    .25
    repeat
    
image memnon mouth transsi:
    "hahmot/memnon_serious_mouth1.png"
    .2
    "hahmot/memnon_serious_mouth2.png"
    .2
    repeat
    
###########
###ANGRY###
###########
image memnon angry = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/memnon_normal.png",
    (0, 0), "memnon eyes angry",
    (0, 0), WhileSpeaking("m", "memnon mouth angry", "hahmot/memnon_angry_mouth0.png"),
    )
image memnon eyes angry:
    "hahmot/memnon_angry_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/memnon_angry_eyes0.png"
    .25
    repeat
    
image memnon mouth angry:
    "hahmot/memnon_serious_mouth1.png"
    .2
    "hahmot/memnon_serious_mouth2.png"
    .2
    repeat
    

###########
###SHOCK###
###########
image memnon shock = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/memnon_normal.png",
    (0, 0), "memnon eyes shock",
    (0, 0), WhileSpeaking("m", "memnon mouth shock", "hahmot/memnon_serious_mouth0.png"),
    )
image memnon eyes shock:
    "hahmot/memnon_shock_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/memnon_shock_eyes1.png"
    .25
    repeat
    
image memnon mouth shock:
    "hahmot/memnon_serious_mouth1.png"
    .2
    "hahmot/memnon_serious_mouth2.png"
    .2
    repeat

#############
###EUGENIE###
#############

############
###NORMAL###
############

image eugenie normal = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/eugenie_normal.png",
    (0, 0), "eugenie eyes normal",
    (0, 0), WhileSpeaking("e", "eugenie mouth normal", "hahmot/eugenie_normal_mouth0.png"),
    )
image eugenie eyes normal:
    "hahmot/eugenie_normal_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/eugenie_normal_eyes1.png"
    .25
    repeat
    
image eugenie mouth normal:
    "hahmot/eugenie_normal_mouth1.png"
    .2
    "hahmot/eugenie_normal_mouth2.png"
    .2
    repeat
    
###########
###SLEEP###
###########

image eugenie sleep = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/eugenie_normal.png",
    (0, 0), "eugenie eyes sleep",
    (0, 0), WhileSpeaking("e", "eugenie mouth sleep", "hahmot/eugenie_normal_mouth0.png"),
    )
image eugenie eyes sleep:
    "hahmot/eugenie_normal_eyes1.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/eugenie_normal_eyes1.png"
    .25
    repeat
    
image eugenie mouth sleep:
    "hahmot/eugenie_normal_mouth1.png"
    .2
    "hahmot/eugenie_normal_mouth2.png"
    .2
    repeat
    
############
###CRYING###
############

image eugenie crying = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/eugenie_normal.png",
    (0, 0), "eugenie eyes crying",
    (0, 0), WhileSpeaking("e", "eugenie mouth crying", "hahmot/eugenie_crying_mouth0.png"),
    )
image eugenie eyes crying:
    "hahmot/eugenie_crying_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/eugenie_crying_eyes1.png"
    .25
    repeat
    
image eugenie mouth crying:
    "hahmot/eugenie_crying_mouth1.png"
    .2
    "hahmot/eugenie_crying_mouth2.png"
    .2
    repeat
    
###########
###SHOCK###
###########

image eugenie shock = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/eugenie_normal.png",
    (0, 0), "eugenie eyes shock",
    (0, 0), WhileSpeaking("e", "eugenie mouth shock", "hahmot/eugenie_normal_mouth0.png"),
    )
image eugenie eyes shock:
    "hahmot/eugenie_shock_eyes1.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/eugenie_normal_eyes1.png"
    .25
    repeat
    
image eugenie mouth shock:
    "hahmot/eugenie_normal_mouth1.png"
    .2
    "hahmot/eugenie_normal_mouth2.png"
    .2
    repeat
    
###########
###HAPPY###
###########

image eugenie happy = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/eugenie_normal.png",
    (0, 0), "eugenie eyes happy",
    (0, 0), WhileSpeaking("e", "eugenie mouth happy", "hahmot/eugenie_happy_mouth0.png"),
    )
image eugenie eyes happy:
    "hahmot/eugenie_happy_eyes1.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/eugenie_happy_eyes1.png"
    .25
    repeat
    
image eugenie mouth happy:
    "hahmot/eugenie_happy_mouth1.png"
    .2
    "hahmot/eugenie_happy_mouth2.png"
    .2
    repeat

###########
###ANGRY###
###########

image eugenie angry = LiveComposite(
    (380, 482),
    (0, 0), "hahmot/eugenie_normal.png",
    (0, 0), "eugenie eyes angry",
    (0, 0), WhileSpeaking("e", "eugenie mouth angry", "hahmot/eugenie_crying_mouth0.png"),
    )
image eugenie eyes angry:
    "hahmot/eugenie_angry_eyes0.png"
    choice:
        8.5
    choice:
        6.5
    choice:
        3.5
    # This randomizes the time between blinking.
    "hahmot/eugenie_angry_eyes1.png"
    .25
    repeat
    
image eugenie mouth angry:
    "hahmot/eugenie_crying_mouth1.png"
    .2
    "hahmot/eugenie_crying_mouth2.png"
    .2
    repeat
    
label start:
    
    scene musta
    play music "musiikki/Harp.mp3"
    show ikkuna behind musta
    show vuori behind ikkuna, musta
    hide musta with fade
    window show
    
    "Pitch black night hung above the mountains."
    "The long line of high peaks followed the ocean shore until it suddenly broke off into the sea and transformed into a chain of steep islands."
    "At the point where mountains became islands, was situated the town of Flayes."
    "Since the hour was late and the people slept in their beds, the city appeared a dark, dim maze of streets, surrounded by the brightly lit walls."
    
    show musta behind vuori,ikkuna
    hide vuori with dissolve
    show linna behind ikkuna with dissolve
    
    "The dark zone only ended when it reached the royal palace, the pulsing heart of Flayes."
    "It shone like the north star."
    
    stop music fadeout 1.0
    
    "A party was underway."
    
    play music "musiikki/waltz2.ogg"
    hide linna with dissolve
    show tanssisali behind ikkuna with dissolve
    
    "A host of guests danced in the light provided by an army of chandeliers."
    "From some dark corner, the orchestra provided them with music, which no one was listening to."
    "Amid all the revelry, there was no indication that the city had been under siege for four months."
    "The royal court celebrated like the world was ending and feasted on the dwindling food supplies far from the walls, where blood was spilled daily."
    "On the fringes, far from the bright dance floors, a number of lonelier souls observed the fun without partaking to it."
    
    show vassan normal at rightPos2 with dissolve
      
    "Among them sat a young man, pretending to be studying a parchment."
    "As usual with boring pieces of paper, this one too was mostly an excuse." 
    
    show dress at leftPos3 with easeintop
    
    "The youth`s eyes followed one of the dancers. Tonight she wore a dress which was the color of a blue sky or a calm ocean."
    "Sighing, he watched the girl slip further away, into the crowd."
    
    hide dress with easeouttop
    
    m"Does she please you?"
    "A soft voice inquired from behind him." 
    "The young man froze instantly. He`d thought his paper was shield enough."

    show memnon normal at leftPos2 with dissolve
        
    v"Memnon." 
    m"Indeed."
    m"Forgive me for intruding, I`ve had a busy day and long for some company."
    m" And an answer to my question." 
    
    show vassan angry at rightPos2
    
    "The young man turned and gave Memnon a deeply hostile look." 
    "Memnon was some years older than him and far better dressed. The collection of colors, feathers, and jewelry put peacocks to shame." 
    
    show vassan normal at rightPos2
    
    v"Fine." 
    v"She pleases me greatly."
    
    show memnon smile at leftPos2
    
    m"It could happen."
    
    show vassan angry at rightPos2
    
    v"You`re crazy, Memnon."
    v"I always knew you were." 
    
    show memnon normal at leftPos2
    
    "Memnon shrugged." 
    m"Perhaps. But I know many girls like her." 
    v"You are the Ambassador of the Yribid Empire." 
    
    show memnon smile at leftPos2
    
    "Memnon laughed."
    m"My dearest Vassan, how long have you resided in this city?" 
    "Vassan thought for a while."
    
    show vassan normal at rightPos2
    
    v"Three years." 
    m"Three years and you still haven`t seen that nothing is the way it seems? Here is a secret for you." 
    m"I`m a barber and my so-called embassy has a staff of gamblers, pimps, a few robbers and one baker."
    m"And that was the most truthful thing you will hear tonight. Oh, and the baker is really a smuggler. He can`t even bake."
    "Vassan, uncomfortable with this gibberish, pretended to return to his manuscript."
    v"Listen, you`re my friend and I like you but you must be either drunk or insane."
    m"Me? You`re the one who came to a royal ball to read."
    v" I was invited. I couldn`t refuse."
    m"So you decided to make sure you`re never invited again?"
    v"I thought her company might improve my mood. Give me the will to write. It doesn`t."
    m"Well have you spoken to her?"
    v" I don`t want to intrude. She seems to be having fun."
    m"But are you?"
    v"No, I`m not having fun. Then again, when you`re at war and everyone around you is pretending it`s New Year`s Eve, are you supposed to?"
    v"I feel it's my fate to be alone in party crowds and in good company when I`m alone with a book. Or my quill."
    m"I think you`re being harsh. And as for the war, soon it`ll reach us all."
    v"What do you mean?"
    
    show memnon serious at leftPos2    
    show vassan shock at rightPos2
    stop music fadeout 1.0
    
    "Memnon grabbed the youth`s shoulder so hard it hurt."
    m"Enough with the jokes. Forget her." 
    m"Forget everything." 
    m"Pack your things and make for the harbor. Climb aboard the first ship you see. The enemy is about to break through."
    
    show vassan angry at rightPos2
    
    "Vassan was baffled. It was not like Memnon to behave this erratically." 
    
    hide memnon with dissolve
    hide vassan with dissolve
    play music "musiikki/terror.mp3"
    
    "He was about to respond with a flurry of questions as the twin doors to the hall suddenly burst open."
    "In stormed a lone rider on horseback, who fired once into the air as if he didn`t already have the crowd`s absolute attention."
    r"The enemy is in the city!" 
    r"The walls have been broken!" 
    r"Flee, people of Flayes, for the city is dying and it won`t recover!" 
    "Then the rider stormed off, presumably to follow his own advice."
    "It took a minute for all the people in the hall to comprehend the situation."
    "Vassan rolled up his parchment." 
    "He then packed his ink and quill."
    "He was smarter than most guests. He made it halfway to the still open twin doors."
    "Then hell broke loose."
    "The pompously dressed, highly noble crowd screamed and scrambled to the doors like so many ostriches."
    
    hide tanssisali with dissolve
    show linna behind ikkuna with dissolve

    "Vassan was among the first." 
    "Pushing and punching his way through the mass of perfumed men and women he tried to catch a glimpse of Memnon or the girl in blue."
    "He saw neither." 
    "Once out in the streets, the mob dispersed quickly as most ran towards their homes to gather what valuables they could." 
    "Vassan didn`t bother. He lived above an inn and carried with him whatever scant possessions he had." 
    "He remembered Memnon`s words and headed for the docks." 
    "Until he changed his mind, anyway. He had to see. He ran to the church."
    "He knew it was suicide. But surely it was better to die in one`s home than run away?"
    
    hide linna with dissolve
    show kirkko behind ikkuna with dissolve
    
    "The Church of Flayes was a proud, old cathedral, rising above the roofs like a loving parent, watchful and inviting." 
    "It was currently in the hasty process of being stripped clean of clergymen, sacrificial sheep and most of all gold."
    "More than enough had been gathered inside the stout walls over the past centuries."
    "No one tried to stop Vassan from entering the building." 
    "He thought it likely no one even noticed him."
    "Inside he paused at the gilded altar and said a quick, habitual prayer."
    "Then he rushed quite inelegantly toward the spiral of stairs leading to the top of the church tower."
    
    stop music fadeout 1.0
    hide kirkko with dissolve
    show portaikko behind ikkuna with dissolve
    pause 0.2
    hide portaikko with dissolve
    show portaikko2 behind ikkuna with dissolve
    pause 0.2
    hide portaikko2 with dissolve
    show portaikko behind ikkuna with dissolve
    pause 0.2
    hide portaikko with dissolve
    show kirkko behind ikkuna with dissolve
    
    "Panting, drooling and sweating, he eventually arrived at the end of the stairway, to a fenceless ledge normally only accessible to the high priest." 
    
    show vassan shock at leftPos2 with dissolve
    
    "The heavy iron door to the terrace had been detached for its gold ornaments, so the path was clear." 
    "The ledge itself was a frightening place." 
    "It was small and so slippery that Vassan quickly collapsed on all fours. Even then the drop ahead made him tremble."
    "A hard wind blew into his face. Somehow it reminded him of the hardness of the ground below."
    "How many men had died falling from here, he wondered. And how many more had died building it, only to live forever in the magnificent tower they left behind?" 
    "He peeked over the ledge. He couldn`t see the ground, only a strangely inviting abyss."
    ru"Did you know that the high priest wears nailed shoes so he can remain standing during sermons?"
    "Vassan peeked over his shoulder and saw Rumri, the old bell ringer." 
    v"No, I did not. But it doesn`t surprise me." 
    v"Shouldn`t you be fleeing with the others?" 
    ru"Shouldn`t you? I was born here long before your people claimed this land." 
    ru"And now I welcome another conqueror with open arms. Who knows? Maybe I`ll live to see the next one." 
    ru"Besides, I would never miss this sight."
    
    hide vassan with dissolve
    hide kirkko with dissolve
    play music "musiikki/grave.mp3"
    show palava behind ikkuna with dissolve

    "For the first time, Vassan now had the opportunity watch the dying city." 
    "It was beautiful in a way." 
    "A flood of torches swarmed through the breached walls, bringing light to the dark houses that caught flame one by one." 
    "On the streets, the remnants on an army made a valiant but futile resistance, as their noble masters fled by the hundreds." 
    "Horsemen crashed again and again into a wall of fire and bayonets as the men on both sides screamed in terror." 
    "Musketeers fired their last shots into the neverending mass of foes, with no noticeable effect."
    "Now the ordinary townsfolk joined in, carrying pistols, knives or just sharpened poles. Men, women and children."
    
    show vassan shock at leftPos2 with dissolve
    
    v"They`re insane! They`ll all die!" 
    "The words hardly came out. The sheer madness of it all had stolen his voice. He had never seen death before." 
    ru"Of course they`ll die." 
    ru"They must make way for the newcomers. Don`t think the enemy camp is just soldiers. Their families are there too, ready to move in."
    
    show vassan angry at leftPos2
    
    "Vassan looked at the old man with disgust. How could he be so cold in the face of such horror?"
    v"You`re insane." 
    "The old man laughed, and all three of his remaining teeth shone brightly in the night."
    ru"No, young man, you are! You could have fled, yet came here instead."
    ru"Down there everyone is trying to live. Compared to what you chose to do, they are reason itself." 
    ru"If you wish to die a hero, you`re in the wrong place. All they`re doing is being erased. Disappear."
    ru"The only ones not sentenced to oblivion are them." 
    
    stop music fadeout 1.0
    hide vassan with dissolve
    
    "The bell ringer raised his long, crooked arms pointed towards the sea."
    "Vassan followed the pale finger with his eyes and saw the first ships rowing out of the harbor. Terror struck him."
    "He didn`t much care for life. But he wouldn`t be erased. He would be remembered. Like the men who built the  bell tower."
    
    hide palava with dissolve
    show portaikko behind ikkuna with dissolve
    
    "He rushed to the stairs so fast he nearly pushed the old man over the ledge." 
    
    hide portaikko with dissolve
    show portaikko2 behind ikkuna with dissolve
    
    "A million steps flew by, with Vassan stepping on roughly every fifth."
    "He wasn`t sure that he wanted to live, but he wouldn`t die here." 
    
    hide portaikko2 with dissolve
    show portaikko behind ikkuna with dissolve
    pause 0.2
    
    "The momentum gained in the stairwell flew him through the now lightless and deserted church all the way to the street." 
    
    hide portaikko with dissolve
    show kirkko behind ikkuna with dissolve
    play music "musiikki/terror.mp3"
    
    "He stopped for a second to gain his breath and raced on."
    "The docks seemed so far away." 
    "He tripped over and fell face down on the pavement." 
    "Cursing, he struggled to gather all his fallen papers. A part of him knew they were worthless. His hands did not care." 
    "Suddenly he noticed a figure nearby. A riderless horse. He presumed the rider had drowned in a sea of fire and lead somewhere downtown." 
    
    hide kirkko with dissolve
    show yöhepo behind ikkuna with dissolve
    
    "The horse, pitch black, stood next to him as if waiting."
    "Vassan cursed again." 
    "He`d never ridden a horse in his life." 
    "In the corner of his eye, he saw movement. The approaching torches cast a pale light on his face." 
    "Lacking the time to hesitate, he scrambled on the saddle and held on tight." 
    "Nothing happened." 
    "The horse stood still as a rock." 
    "The men were getting closer." 
    "Vassan had once seen a parade on the grand square." 
    "The royal dragoons had done it so effortlessly." 
    "He spanked the horse, but it just stood still." 
    "Now he heard shouts and gunshots. He had been noticed. He sank his heels in the sides of the animal and cursed loudly." 
    "The horse reared and then it catapulted down the street, fast as the pursuing bullets." 
    "Vassan was mortified with fear."
    "Just to stay astride he had to squeeze the animal`s neck with both hands so hard he thought the horse might choke." 
    "He didn`t need to guide the horse, it galloped for the harbor on its own. Not that Vassan would have known how."

    "He could not see it, but the horse`s hooves struck sparks when they met the stone." 
    "Later those who lived through the sack of Flayes told," 
    "that on the hour of city`s demise a ghost rider in bloody armor had galloped through the city astride a pitch black steed," 
    "whose eyes burned like cinders and whose mouth breathed fire." 
    "Needless to say, the miserable and petrified young poet in a dirty coat made for a much less striking image."
    
    stop music fadeout 1.0
    
    "Before he knew it, Vassan felt the sea wind on his face." 
    
    hide yöhepo with dissolve
    show satama behind ikkuna with dissolve

    "The mighty uptown mansions shrunk into brothels and warehouses. Soon Vassan saw the docks ahead." 
    "Only a single ship was left and it was being packed with great haste." 
    "The horse brought Vassan to the end of the pier and then stopped moving so suddenly, that Vassan kept going for another few meters before hitting the ground." 
    
    show vassan shock at leftPos2 with dissolve
    
    "On the ground, he rolled on a while before he found himself at the feet of a man standing on the pier." 
    k"You have a fine steed, lad! This one we`ll take with us!" 
    "The man, whom Vassan now understood to be the captain of the ship, gestured for two slaves, who escorted the animal aboard." 
    k"All righty, get going, lad! Be a shame to leave ye here after such a ride. We`ll be raising the anchor soon."
    "Nodding, Vassan climbed aboard, using a net hanging from ship`s side." 
    
    hide vassan with dissolve
    hide satama with dissolve
    show laivayö behind ikkuna with dissolve
    
    play music "musiikki/nightsea.mp3"
    
    "Once aboard he collapsed and lost his consciousness."
    "He came to much later and did not see how the ship raised its anchor just in time or how Memnon galloped through the charging enemy on a white mare." 
    "To the utter humiliation of the advancing army, he leaped straight from horseback and grabbed the anchor chain, pulling himself up." 
    "As the crowd aboard cheered, the enemy set to work on finishing what was left of Flayes. Fire engulfed the high towers of the church. The city was dead."
    
    stop music fadeout 1.0
    hide laivayö with dissolve
    show laivayö behind ikkuna with dissolve
    play music "musiikki/nightsea.mp3"
    show eugenie crying at rightPos2 with dissolve

    "Eugenie Anna-Maria Heloise Valentine de Mollerfiol was weeping." 
    "The night had been such fun for a while." 
    "She`d danced and laughed for hours. It had been one of the best balls she`d ever been to. She`d even tried wine." 
    "Then the cursed rider had broken in." 
    "In a blink, the best night of her life had turned into a nightmarish escape through crowded streets." 
    "They were safe now, but so much had been left behind. All her possessions. All her friends. The mansion of her family and those of her now dead suitors." 
    "And all her clothes. She now owned nothing except the blue dress on her, and it was in tatters." 
    "Losing the dress was reason enough to cry."

    "The ship which was now their home was crowded and dirty and the sailors were filthy brutes." 
    "The only even slightly interesting person aboard was the diplomat who`d ridden in on a white steed, handsome as a knight." 
    "And he paid her no heed." 
    "The man was busy tending to the sleeprider." 
    "That was the nickname people called the anonymous, skinny youth, who`d also made it on the eleventh hour." 
    "The worst part was not the escape or even the cold, but the sheer loneliness. Most of those aboard were men and had no time for her." 
    "This vexed her greatly, for the people of her status were deeply terrified by the prospect of not being pampered."

    show eugenie shock at rightPos2
    
    "Suddenly Memnon rose and came to her."
    
    show memnon normal at leftPos2 with dissolve
    
    "Eugenie felt her spirits lift immediately. He was truly handsome." 
    m"Good evening, my lady. I hope you are well?" 
    
    show eugenie happy at rightPos2
    
    "No, she wanted to say. Nothing at all was well. Her entire world had been undone." 
    e"Splendidly, my lord, but thank you for your concern." 
    m"I`m afraid we haven`t been introduced."
    m"Memnon de Clere, Grand Ambassador of the radiant Yribid Empire at the court of his majesty the king of Flayes, may the god keep him." 
    "Eugenie fought against cursing." 
    "Why was it that she had to retain such formality in the company of attractive men? The etiquette concerning young women was dreadful." 
    "One day she would do something about it." 
    e"Eugenie de Mollerfiol. Pleased to meet you, master de Clere." 
    "Memnon was surprised." 
    m"De Mollerfiol? Is your father the Scratcher of the Royal Dogs?" 
    "Eugenie nodded. It was a prestigious title, not that her father ever had to go near a dog himself." 
    e" And I am his eldest daughter." 
    e"My future husband will inherit that worthy title." 
    "An unmarried woman was expected to parade her credentials as a spouse." 
    "Memnon did not react but smiled and continued." 
    m"Mademoiselle, it would be my pleasure to chat the night away in your company. But I must cut to the chase. May I ask a favor?" 
    "Eugenie was shocked. Surely it was not habitual among the Yribids to make so candid suggestions?" 
    "On the other hand, it`s not like she wasn`t interested. And mother wasn`t around." 
    e"Whatever you desire, master de Clere. I am only happy to ease your burdens." 
    
    show memnon smile at leftPos2
    
    "Thanks only to years of exercise, Memnon managed an even bigger, friendlier smile. Being a diplomat sometimes made your face feel like a carnival mask."
    m"Glad to hear that, mademoiselle. I`ve been invited to counsel, but am unwilling to abandon my friend." 
    m"Would you be so kind as to keep him company and pour him a drink from this bottle when he wakes up?" 
    
    show eugenie shock at rightPos2
    
    "And, without waiting for a response, he handed her a silver flask and left."

    hide memnon with dissolve

    "Eugenie stared at his back with her mouth open. She`d clearly misread the situation. Badly."
   
    show vassan sleep at leftPos2 with dissolve
    show eugenie angry at rightPos2
    
    "She then turned to the unconscious man on the deck. She blamed him for everything that had gone wrong that night. The escape, the cold, the fruitless flirt." 
    "Sure it was completely unjustified but it wasn`t like he would mind."
    "He`d been unconscious for hours." 
    "Defiantly she opened the bottle and took a swig of rum."
    
    hide vassan with dissolve
    hide eugenie with dissolve
    stop music fadeout 1.0
    hide laivayö with dissolve
    show laivayö behind ikkuna with dissolve
    play music "musiikki/nightsea.mp3"
    
    "The ships floated silently in the night."
    "It was the moment before dawn, the darkest hour of the night." 
    "In the sky, the moon and the stars reigned still unchallenged, with the sun only preparing to usurp their throne."
    "The fleet was silent. From afar it could have been mistaken for a cluster of ghost ships." 
    "The refugees, after an ample dose of crackers and wine, had all fallen asleep." 
    "From the lower decks a steady, monotonous drumbeat made sure the slaves kept rowing." 
    "Not a word was spoken. Only the Captain`s cabin was lit."

    show vassan normal at rightPos2 with dissolve

    "That light was the first thing Vassan saw when he woke up." 
    "He was stiff. He must have been lying there for some time." 

    show eugenie sleep at leftPos2 with dissolve
    
    "To his great bewilderment, he noticed the girl in the blue dress from the party sleeping right next to her." 
    "For a while he just sat there, enjoying her warmth and the smell of her hair." 
    "He heard the drums and realized the ship was moving." 
    "Looking at the stars, he rested in silence."
    
    hide eugenie with dissolve

    "He heard voices, muffled but clearly angry. He looked again at the light from the cabin." 
    "With great difficulty, he got up and went towards it." 
    "Every movement was pure agony. Vassan wasn`t a man of frequent exercise and now every one of his muscles was reminding him to jog once in a while." 
    "He opened the heavy, creaking door."
    
    stop music fadeout 1.0
    hide vassan with dissolve
    hide laivayö with dissolve
    show cabin behind ikkuna with dissolve
    show vassan shock at rightPos2 with dissolve

    "And entered another world." 
    "Where the deck had been serene and quiet, the cabin seemed a chaotic battlefield, louder than a cannonade." 
    "Through the thick, black smoke of a dozen pipes and cigars, he could see the outlines of yelling and cursing men." 
    "In the middle of the room, there was a large nautical chart with tiny tin ships on it." 
    "Messages were being dictated in a dozen contradictory voices. Some poor souls were trying to decipher the cacophony of opinions into written notes." 
    "In the center of it all stood the Captain, stalwart as ever, bellowing orders with a voice like a foghorn." 
    "Vassan scouted the room for a single friendly face. It found him first."
    
    show memnon normal at leftPos2 with dissolve

    m"Vassan, good to see you awake! I trust you were in adequate company?" 
    "It took a while for Vassan to get it." 
    v"Ah, her."
    v" I should`ve known you had a hand in it." 
    
    show vassan normal at rightPos2
    
    v"And good to see you too. How`d you make it? And what`s this noise?"
    "Memnon smiled and pulled his friend to the quietness of the deck."
    
    hide vassan with dissolve
    hide memnon with dissolve
    hide cabin with dissolve
    show laivayö behind ikkuna with dissolve
    play music "musiikki/nightsea.mp3"
    show vassan normal at rightPos2 with dissolve
    show memnon normal at leftPos2 with dissolve
    
    m"Which question do you wish to hear answered first?" 
    v"The first." 
    
    show memnon smile at leftPos2
    
    m"I reported to an enemy officer. Told him I was a spy with an urgent message to deliver." 
    m"A few silver coins and he arranged a good horse for me." 
    m"I imagine the poor man will be court-martialed."
    
    show vassan laugh at rightPos2
    
    v"Memnon, is there a pinch too hard for you to talk your way out of?" 
    "Memnon smiled." 
    m"Haven`t found one yet." 
    
    show vassan normal at rightPos2
    
    v" And for your sake, I hope you never will."
    v"But what on earth is the matter with all the noise?" 
    
    show memnon serious at leftPos2
    
    m"What they`re trying is to assemble the fleet and stick together, not to mention formulate a workable plan for the future."
    m"It becomes a surprisingly formidable task when you have to rely on lanterns and flags for messaging." 
    v"You`d think there was some kind of an emergency plan?" 
    m"There is." 
    m"The argument they`re having is about who will get to execute it." 
    m"For the past hours they`ve been comparing family trees and the nobility of their ancestors to determine a suitable leader." 
    m"It gets quite personal." 
    m"Just now a trireme signaled to us in wuluese, calling our captain a pest-ridden mule with bad hygiene." 
    
    show vassan laugh at rightPos2
    
    "Vassan couldn`t help but laugh at the pettiness of these supposedly great nobles." 
    
    show memnon serious at leftPos2
    
    m"Vassan this is not a laughing matter by any means!" 
    m"If they cannot agree on a leader, the fleet might disperse. And no ship can survive on its own for long." 
    
    show vassan neutral at rightPos2
    
    "Vassan stopped laughing. He`d just remembered the gravity of their situation. He looked into Memnon`s eyes." 
    "Memnon seemed like he had aged years in just a day." 
    "Vassan could almost have sworn he had gray hair." 
    
    show vassan normal at rightPos2
    
    v"You look tired." 
    "He finally said after a good look at his friend." 
    m"I`m exhausted." 
    m"The sun is coming up. The captain was kind enough to grant me a cabin."
    m"If you`ll excuse me, I must get some rest now." 
    
    hide memnon with dissolve
    stop music fadeout 1.0
    
    "Without waiting for a response Memnon disappeared below deck." 

    show vassan smile at rightPos2

    "Vassan gazed upon the sun as it peeked from behind the dark blue waves somewhere far away." 
    "Despite yesterday`s perils, or maybe because of them, he was overcome by absolute serenity." 
    
    hide laivayö with dissolve
    play music "musiikki/daysea2.mp3"
    show laivapäivä behind ikkuna with dissolve
    
    "As the sky reddened with the rise of the sun, the shapes in the morning mist once again took the form of wooden ships." 
    "The ocean around them was boundless, deep blue plain, both dangerous and beautiful." 
    
    show eugenie sleep at leftPos2 with dissolve
    
    "Vassan looked upon the sleeping Eugenie. Her hair and dress were a mess and her makeup had come off in patches. She snored loudly."
    "And was so beautiful." 
    
    hide eugenie with dissolve
    show flask at leftPos3 with easeintop
    
    "In her hand was Memnon`s flask. Carefully Vassan took it and drank deep. The rum softened his aching muscles." 
    "The journey had begun."
    
    hide flask with easeouttop
    hide vassan with dissolve
    stop music fadeout 1.0
    hide laivapäivä with dissolve
    
    #####################################################################################################################################################
    #####################################################################################################################################################
    #####################################################################################################################################################
    
    show muuri behind ikkuna with dissolve
    play music "musiikki/dream.mp3"
    show memnon serious at rightPos2 with dissolve
    
    "Memnon walked along the wall with a steady, confident stride." 
    "He gripped his cane tightly. His knuckles were white." 
    "With his eyes, he spied a tiny sally port, sealed shut and guarded." 
    "The gate was built long ago, before the cannon and the musket had come along and made obsolete the battlements of old." 
    "Now it was guarded by only one man and a young boy at that. On seeing Memnon the guard at once redied his musket." 
    eg"Who goes there? Halt at once or I must shoot!" 
    
    show memnon normal at rightPos2
    
    "Memnon raised his head." 
    m"Calm down Egbert, it`s me. Have you considered what we spoke?" 
    "Egbert cocked his musket." 
    eg"Yes master de Clere. And I reckon you`re nothin` but a bloody traitor!" 
    m"You would do well to consider the benefits. There is more than money on the table." 
    m"And you absolutely must learn how you speak to your betters." 
    
    show memnon serious at rightPos2
    
    m"But must I assume that you will not cooperate? Think carefully." 
    "The guard shook his head." 
    "Memnon took a step forward." 
    "Egbert aimed at his chest. Memnon didn`t hesitate long." 
    "He shoved aside the barrel. The gun went off with a crack." 
    
    hide muuri
    show blood behind ikkuna

    "Then he struck the guard on the head with the heavy pommel of his cane. A small knife flashed in the night and Egbert collapsed against the wall."
    hide blood
    show muuri behind ikkuna
    
    "Gasping Memnon detached the guardsman`s keys and opened the heavy iron gate." 
    "Outside the enemy was ready." 
    "Two dozen soldiers in black uniforms were hiding in shell holes nearby and thousands more scattered behind every ridge and hill for miles." 
    "When the gate opened and Memnon hoisted the lantern he`d taken from a guardsman, the nearest shadows began crawling to him." 
    "The first at the walls was an officer, who promptly presented Memnon with a silk pouch and a sealed letter." 
    vi"Fine work, master. May this pouch be a front payment for your reward. This document will guarantee your survival. Now, run for it, for a storm is rising!" 
    "Memnon turned around and ran for the palace, while his generous new friends began pouring in."

    "Then he saw the gatekeeper, twitching and gasping, dying again and again." 
    
    hide muuri
    stop music
    show laivapäivä behind ikkuna
    show memnon crying at rightPos2
    
    "Finally he woke up, sweaty and in tears." 
    "It took him awhile to realize where he was. In his hammock. Aboard the ship." 
    
    show memnon serious at rightPos2
    
    "He couldn`t breathe. He couldn`t hold back the tears." 
    "He had to do it, he told himself as he reached for the pouch." 
    "They were on to him. His barbershop embassy was out of money. Someone would have exposed him as a fraud and commoner and then it would have been the gallows." 
    "Now all the someone`s were dead, he was a hero and there were 239 heavy gold coins clutched in his hands." 
    "All he`d lost were his home, honor, conscience, and soul. The pouch felt heavier than the ship he was on." 
    "All those lost in the fire flashed before his eyes. Men, women, and children. Butchered, pillaged and enslaved." 
    "Thousands of homes, temples and the royal splendor of a hundred palaces, abandoned and burned to cinders." 
    "With some difficulty, he opened the pouch." 
    "The gold had been so shiny when the enemy first approached him." 
    "These coins were much dimmer, stained." 
    
    show coin at leftPos3 with easeintop
    
    "Carefully he picked one. It appeared perfectly genuine." 
    "One side had something written on it in a foreign script, the other bore the images of the lion and the eagle." 
    "There was something dark and reddish on the coin. Like rust." 
    "Gold doesn`t rust." 
    
    show memnon crying at rightPos2
    
    "Memnon scraped the coin with his dagger and began to weep. Underneath a thin veil of pale gold was dark, black lead." 
    
    hide coin with easeouttop
    hide memnon with dissolve
    hide laivapäivä with dissolve
    show laivapäivä behind ikkuna with dissolve
    play music "musiikki/daysea2.mp3"
    show vassan normal at leftPos2

    "Meanwhile Vassan was listening to the captain, who was briefing the passengers on their situation." 
    "The speech was long and elegant, but in the end, there wasn`t much to tell." 
    "The city was lost, that was clear to all. 76 ships were known to have fled the docks. 34 had gone missing in the night. Whether they were lost, sunk or captured, no one knew." 
    "The 42 ships remaining were now in formation, under the leadership of a certain admiral Hulegu." 
    "The plan was to flee the pursuing enemy and find the distant Rword Archipelago, where long ago a colony of Flayes had been founded." 

    "The captain was standing next to the wheel with a stern look on his face." 
    "It had not been an easy night for the old sailor. His face was wrinkled and pale and there were deep blue spots under his eyes." 
    "Based on their brief meeting last night Vassan had thought him a strong, passionate man." 
    "The old, hunchbacked man on the bridge did not match the image." 
    "Except for the fire burning under his frail form, fed by years of anticipation." 
    "Based on the look in his eyes the sixtysomething captain was a boy on his first adventure." 
    "Vassan had to admire such passion. He`d never felt it himself."

    k"Right, gents and ladies. Let me tell ye somethin`!" 
    "The Captain`s cheeks were forever rosy from decades of hard winds."
    k" Yesterday was no doubt the least pleasant day in all our lives." 
    k"In a stroke o` real bad luck, we`ve become a nation of widows and orphans. And we will grieve those lost when the time comes." 
    k" And given the chance, we`ll avenge them."
    k"But time is a luxury we do not have." 
    "The Captain held a dramatic pause." 
    k"Now we must hold on to our hats and prepare for the great sea journey." 
    k" And while I cannot guarantee we`ll make it to safety, I can promise a cruise to remember!" 
    k"All of us have spent our lives in the city, surrounded by walls, eating off someone else`s hard work and surrounded by slaves." 
    k"Now, mates, those days are over! From now on we`ll show them..." 
    k"... that we don`t need slaves to cook for us! We don`t need to be paraded on pillows around fancy palaces! We can roll our sleeves and work!" 
    "Some in the audience would clearly have preferred being carried around on pillows to vomiting aboard a creaky ship."
    "Vassan remained unconvinced. He could hear the slaves pulling the oars below deck while the hard-working citizens held speeches."

    "Vassan took a step away from the captain." 
    "The old man was moved to tears by his own words and was now on his knees." 
    "Not to say that he wasn`t a good speaker. Vassan was just really hard to impress."

    k"So join me now, and we`ll endure this storm together! Let us pray!"
    
    stop music fadeout 1.0

    "The Captain reached out and the passengers took his hands, forming an unbroken circle." 
    "Vassan too was grabbed along, though against his will." 
    "The Captain led them to prayer and one by one the passengers joined." 
   
    hide vassan with dissolve

    "Even the rowing slaves joined the sermon. Vassan was baffled how they might find comfort in the gods of their masters." 
    "Finally the entire ship was praying, defying the roaring waves with a loud cry, except for two people." 
    
    show memnon transsi at rightPos2 with dissolve
    
    "One was Memnon, who was still bedridden. He thought it safer not to seek the attention of the gods, lest they remembered to punish him." 
    
    hide memnon with dissolve
    show vassan angry at leftPos2 with dissolve
    
    "The other was Vassan, who stood amid the kneeling believers and was utterly bored." 
    "With his tired eyes, he observed the crowd and felt he was truly,completely alone."
    
    show vassan neutral at leftPos2
    
    "It was a strange thing, to feel so unattached." 
    "Some of the passengers had burst into tears. It must be marvelous to feel anything that strongly, Vassan thought."

    show vassan shock at leftPos2
    play music "musiikki/dream.mp3"
    
    "Suddenly someone grabbed his shoulder." 
    
    show memnon transsi at rightPos2 with dissolve
    
    "Vassan turned to see a pale, shivering Memnon behind him." 
    "He was brandishing a razor, squeezing it so hard his knuckles were white. His eyes shone with a bright shade of madness." 
    m"Let me shave you" 
    "Nothing in his tone was reassuring." 
    
    show vassan normal at leftPos2
    
    v" I... don`t think I need a shave." 
    "Vassan said and tried to turn away, only to be pulled into Memnon`s cabin by force." 
    
    hide memnon with dissolve
    hide vassan with dissolve
    hide laivapäivä with dissolve
    show cabin behind ikkuna with dissolve
    show memnon transsi at rightPos2 with dissolve
    show vassan normal at leftPos2
    
    "There Memnon sat the young man into his chair and glared at him, breathing heavily and soaked with sweat." 
    m"I beg you, grant me a chance to prove that I can still do honest work." 
    v" Working hard does seem to be today`s theme." 
    v"Do you even know how to shave?" 
    m"I thought I told you I was a barber." 
    "Vassan stared at him like a madman." 
    v" I thought you were making a bad joke." 
    "Memnon shook his head." 
    m"I am neither count, nor nobility, nor any realm`s ambassador." 
    "Vassan raised an eyebrow. He thought it best not to do sudden movements when his friend had a razor on his throat." 
    m"I was born in the Yribid Empire, that much is true. I was the court barber there with a wife I no longer loved and three children I never did." 
    m"I hated the cards fate had issued me. When the empire was attacked, I joined the army. I wanted excitement, I wanted to live before I died." 
    m"The army was decimated before I even joined it. I had a choice, then. To fight on and die a meaningless death, or return to my horrid life." 
    m"I chose neither. I gathered some friends. Together we shot our officers, stole parade uniforms and rode in the wilderness for months." 
    m"Finally we arrived in Flayes and presented ourselves to the king as envoys from our homeland." 
    
    show vassan shock at leftPos2
    
    "Vassan couldn`t believe his ears." 
    "Memnon began to shave his chin with firm strokes." 
    m"We were treated like royalty. The facade was easy enough to maintain until yesterday."
    m"Of course, the enemy would have known. They were the ones who destroyed the Yribids all those years ago." 
    v"What of all the maids and secretaries? Surely they weren`t all your mates from the army?" 
    
    show memnon normal at rightPos2

    m"Isn`t it marvelous, what clean clothes and a bath can do?" 
    m"We recruited our staff from the streets. They were beggars and thieves, like the women you grew up with." 
    "Vassan didn`t know what to think. He`d always thought Memnon was the one person he really knew." 
    
    show vassan normal at leftPos2
    
    v" And what of your wife? Surely you miss her?" 
    
    stop music fadeout 1.0
    show memnon smile at rightPos2
    
    "Memnon laughed." 
    "For a long time."
    "A really, uncomfortably long time." 
    "Vassan moved his chair a bit further. Then Memnon calmed down and replied." 
    
    show memnon normal at rightPos2
    
    m"In Flayes I attended balls and hunts with royalty. I shared mistresses with the king himself." 
    m"I slept in silk sheets and had a golden carriage." 
    m"In my homeland I was nothing. I had nothing, except a wife who looked like she`d swallowed a siege cannon." 
    m"No, I do not miss her."
    "Caught up in his story, Memnon made a small cut on Vassan`s white cheek."
    
    show vassan shock at leftPos2
    
    "Hot blood streamed down the recently shaved cheek until a single drop fell on the barber`s white socks." 
    "Desperate to change the topic, Vassan looked down and saw another, dried stain next to the fresh blood." 
    v"Are you wounded? That looks like dried blood." 
    
    show memnon transsi at rightPos2
    
    "Memnon was pale. It was blood all right, just not his own." 
    m"It`s just dirt. Last night was rather chaotic. I must`ve tripped over at some point. But I`m sorry." 
    m"I don`t know what got to me. I must still be in shock. Now I need a moment alone. Can I count on  you to keep my secret?" 
    v"Yea, of course. Are you sure you`re not hurt?"
    "Memnon shoved him out without replying."
    
    hide vassan with dissolve
    hide memnon with dissolve
    hide cabin with dissolve
    show laivapäivä behind ikkuna with dissolve
    show vassan normal at rightPos2 with dissolve
    play music "musiikki/daysea2.mp3"
    
    "Outside the prayers had finally ended and the sailors were back at work." 
    "The Captain gestured Vassan." 
    "Quickly he made his way to the old sailor."
    k" I noticed you slacking off during prayers, boy."
    v"I didn`t want to shed tears in front of the women. Your speech moved me."
    "Vassan was surprised by how adept he was at lying. Memnon`s company was truly affecting him."
    k"Aye, no love purer than love for one`s country. Now follow me, I must show you somethin`." 
    "The Captain led him below deck."
    
    hide laivapäivä with dissolve
    stop music fadeout 1.0
    show tykkikansi behind ikkuna with dissolve
    
    "The gun deck had been turned into a dormitory. Mattresses and hammocks had been arranged between the bronze cannons."
    "Vassan couldn`t imagine sleeping between such dreadful instruments of destruction. At least not after watching Flayes burn."
    v"Won`t the civilians be on the way if it comes to a battle?"
    k"No such thing as civilians in battle, boy."
    k"Only those that`re prepared and those that aren`t."
    v"Surely you won`t ask the women to take up arms?"
    k"The army don`t ask, boy."
    k"This noble folk`s spent years pretending there isn`t a war on. That`s over now."
    "Without saying a word further the Captain led him further down, to the rowing deck." 
    "The sweat of some six hundred slaves, arranged on three decks, was fuelling the cumbersome vessel on its way." 
    "Vassan pitied the men, though they puzzled him. Who would choose to live such a life? Why didn`t they throw themselves into the sea?"
    k"Don`t bother pitying `em. Pity makes ye weak."
    v"We`d all be dead if they didn`t row. Don`t we owe them our thanks?"
    k"Only thing they must know is they`ll be dead if they don`t row."
    k"If we want to keep floatin`, we can`t be bothered with who`s got the shortest stick." 
    "After passing through two more decks of rowers moving the ships to the beat of a monotone drum, they finally arrived in the ship`s hold." 
    
    show vassan shock at rightPos2
    play music "musiikki/dream.mp3"
    
    "At the very back of the ship, there was space reserved for three horses. Vassan recognized one instantly."
    
    hide tykkikansi with dissolve
    show yöhepo behind ikkuna with dissolve

    "The black steed that had so gallantly saved him from being bayonetted to death was munching hay." 
    
    show vassan normal at rightPos2
    
    k"That is the finest stallion I have ever seen." 
    v"It is a wonderful beast." 
    "Until last night every horse had been nothing but a walking sausage to him but this stallion had changed his view greatly."  
    k"How strange that I couldn`t recognize it last night." 
    k" Only one horse can gallop such a distance while carrying a grown man. Take a look at its saddle." 
    "Vassan took a step closer and obeyed." 
    
    show vassan shock at rightPos2
    
    "They were embroidered with silver linings and on the smooth leather was imprinted the phoenix emblem of the royal family. Vassan was mortified." 
    v"This is the king`s horse." 
    "The king was sacred. So were his belongings." 
    "He turned to see the Captain point a gun at him." 
    k"There`s a punishment for touching that animal without the permission of the high priest."
    k" And you know what`s funny? No one`s seen the king since the night of the ball. Only his horse." 
    "Anyone normal would have fallen to their knees and begged for their life." 
    "Anyone normal. But Vassan didn't move an inch." 
    "This way of dying amused him. It would be beautifully ironic." 
    
    show vassan normal at rightPos2
    
    "The animal that saved his life would be his death." 
    
    hide yöhepo with dissolve
    show tykkikansi behind ikkuna with dissolve
    
    "Vassan stood straight." 
    "This was truly a good way to die. The best he`d encountered so far." 
    k"I should kill you." 
    "His aim wavered. Though his face was grim, there was desperation in his eyes." 
    k"By law, you are to die. No excuses, no mitigating circumstances." 
    
    show vassan sleep at rightPos2
    
    "Vassan stood calmly." 
    "He didn`t really have anyone to say goodbye to. Eugenie didn`t care for him and Memnon he wasn`t sure he even knew anymore." 
    "He was sad his works hadn`t been published. All his unfinished scripts and poems would no doubt be thrown overboard with his body."
    "The only one aboard who knew his real name was Memnon, who would no doubt be dead himself within days."
    "Now he was terrified."
    "Death didn`t scare him. Oblivion did."
    k" I`m sorry, lad. We can`t let the folk think they can get away with a crime. Have to keep them in line."
    "Vassan stood absolutely immobile."
    "The Captain was speaking the whole time but Vassan couldn`t hear it."
    "He hoped his execution would at least be a public affair. So that people could see and he could smile defiantly."
    "After an eternity the old man lowered his gun."

    k"You win, lad. I can`t bring meself to shoot ye." 
    k"Truth is, I´ve never shot anyone in my life. Some soldier, huh?"
    
    show vassan shock at rightPos2
    
    v"..."
    k"I`ll be honest, t`is a rare thing to see someone look death in the face like you did. Consider yerself pardoned."
    v"T-thank you, sir."
    k"Don`t waste this,lad. Make yerself useful and stay out of my way."
    v"But, what will I do? I`m not a sailor."
    k"You`ve got young eyes, don`t you? Climb to the mast and keep a lookout. Could be we`re being followed." 
    v"Aye aye, sir."
    k"Oh and one more thing."
    v"Yes?"
    k"Tell anyone about this and I`ll have you hanged. Can`t let people think that crime won`t be punished."
    "The captain turned to go."
    v"No wait!"
    k"What?"
    v"I deserve the punishment. Please, let us end it here."
    k"Don`t mock me, lad. I`ve given ye orders. Follow them and we`ll all make it."
    
    stop music fadeout 1.0
    
    "With that, the Captain left him."
    
    show vassan normal at rightPos2
    
    "Vassan stood alone in the dark hold. He could hear the horses munch their lunch."
    "The serene darkness was soothing."
    "For a moment he imagined that this was what death must be like."
    "Peaceful darkness, with only the gentle rocking of waves."
    "He knew he`d been given life twice now, yet he felt like he`d missed two chances."
    
    show vassan sleep at rightPos2
    
    v"What`s the point?"
    "He was determined not to suffer existence for much longer."
    
    hide vassan with dissolve
    hide tykkikansi with dissolve
    
     #####################################################################################################################################################
    #####################################################################################################################################################
    #####################################################################################################################################################
    
    show laivapäivä behind ikkuna with dissolve
    play music "musiikki/daysea2.mp3"
    show memnon serious at leftPos2 with dissolve

    "Memnon leaned on the railing and watched the waves crash against the ship`s hull." 
    "Even the sea was against them." 
    "He was quite sure this was the worst day of his life." 
    "On top of everything he was constantly being bothered by mademoiselle Mollerfiol." 
    "She visited him constantly, pretending to have some frivolous matter." 
    "He could`ve taken that much, but the girl was constantly mincing like she was the finest of seductresses." 
    "In the end, he`d told her to leave him be, in a very unfriendly manner."
    "She`d gone below deck to sulk." 
    "Memnon hadn`t intended to harm her feelings. Now he felt guilty for that too. His bad mood was interrupted by Vassan storming to him." 
    
    show vassan shock at rightPos2 with dissolve
    
    v"Memnon! Memnon!" 
    m"Yes?" 
    "Vassan ran against him, nearly fell and then just stood there, gasping for air." 
    m"Calm down, you`ll suffocate. Breathe." 
    v"What`s the point? We`re all dead. In fact, I want to be." 
    m"What on earth are you babbling?" 
    v"This is all pointless. Why toil and fear and flee when we`ll all end up just the way the people in Flayes have." 
    v"Aren`t you sick of life?" 
    m"The gods know I am. But you should sit down. You`re obviously losing it." 
    m" None of us are feeling good. There`s no reason to make it worse." 
    v"But can`t you see? We don`t have to suffer through this. Tell me, what`s there on the other side of this trip?" 
    v"Will we all be happy and wealthy again? Will the slaves build us mansions and carry us around them?" 
    "Memnon grabbed him by his neck and pulled him closer."
    m"I certainly hope so. What about Eugenie? I thought you loved her."
    v" And what has that ever brought me but unhappiness? I don`t even know her." 
    m"But you could. Now you sound like you`ve been drinking. If I have to listen to this, would you pour me a pint?" 
    
    show vassan laugh at rightPos2
    stop music fadeout 1.0
    
    "Vassan laughed. Facing death had left him in a good mood." 
    v" I haven`t drunk. I feel soberer than ever." 
    v"This is all pointless. There`s no avoiding death. We`re all just mice in a bucket of water. Eventually, we`ll all drown." 
    "Memnon punched him. The pain was real enough."
    
    show memnon angry at leftPos2
    
    m"You`re younger than me in more ways than one. So trust me when I say: there`s no point in longing for death." 
    m"Yes, life isn`t much more than the lies we tell ourselves. The trick is to pick a fun lie and tell it well."
    m"But there`s so much you haven`t had a chance to see. After death, there won`t be pain or lies but really there won`t be anything else either."
    m"Now why don`t you try to calm down? This madness will pass."
    
    show vassan crying at rightPos2
    
    "Vassan was quiet. He`d been so sure that Memnon would understand his pain." 

    show memnon serious at leftPos2

    "Tears flowed down his cheeks. On seeing them Memnon embraced him."
    v" I`m just so tired of it all."
    m"Listen, everyone gets these moments sometimes. I do too. And I`ll be here if you need to talk."
    m"Besides, why would you die now, and rob the world of your talent?"
    m"You should try and write something. Channel you anxiety. Make your masterpiece." 
    "Suddenly some light emerged on Vassan`s face." 
    
    show vassan smile at rightPos2
    
    v"My church tower!"
    m"What?"
    v"I`ll write something that I`ll be remembered by. That`ll keep me occupied. Then I can die in peace." 
    
    hide vassan with dissolve
    
    "Vassan ran away."
    "Memnon shook his head." 
    "Sometimes he felt like the difference between adults and children was that adults don`t like getting compared to children."
    "Or maybe they`d all fled so quickly they`d had to leave their sanity behind."
    
    hide memnon with dissolve
    hide laivapäivä with dissolve
    show laivapäivä behind ikkuna with dissolve
    play music "musiikki/daysea2.mp3"
    show eugenie happy at rightPos2 with dissolve
    
    "Eugenie was drinking again." 
    "She wasn`t sure what had gotten to her." 
    "Since the first night, she`d gone back time and again to the crew`s rum barrels." 
    "It helped her sleep, she would say."
    "It helped her cope with the stress."
    "She would stop the moment they landed ashore."
    "She didn`t feel so lonely when she was tipsy."
    "Her mother insisted that she dress and behave like a lady despite the circumstances."
    "Her dress was suffocating her and she was sharing a dorm with the men anyway."
    "As far as she was concerned, the rules could go to hell. They certainly weren`t making her mother happy."
    "She spent her days below deck, staring at the walls."
    "Everyone coped in their way, she thought."
    "They`d been at sea for three weeks and had seen no land for the last two." 
    "She could see they were running out of food. The daily dose of crackers and sauerkraut was getting smaller by the day." 
    "There were simply too many people on board."  

    "The Captain tried to keep morale up with his daily speeches and prayer sessions, but by now he was just repeating himself. No one listened anymore." 
    "The crew was so spent they barely had any strength left." 
    "Finally the passengers had been ordered to do light work like clean the deck." 
    "This scandalous idea had deeply distressed the classy crowd of refugees on board."
    "Some men had defiantly refused to do any physical labor, with one count declaring that forcing them to work would be slavery."
    "One full day on the rowing bench with the actual slaves had changed his mind."
    "The others went to hunger strike and told that they would not eat until the work requirements were lifted."
    "The Captain had shrugged and told them no one was required to eat."
    "The most persistent few had starved themselves for three whole days until they gave in."
    
    "Eugenie had been assigned to distribute meals." 
    "At first she was appalled at the thought of serving meals to ordinary sailors." 
    "In fact, she`d been one of the last to stop their hunger strike." 
    "Now she was getting more used to it. It was nice to have something to do."
    "She even found it pleasant in a strange way to serve food to others. Plus she had access to the rum barrel." 
    "She only took one swig a day. That was her rule that she would not break." 
    "Unless the day was incredibly hot, in which case she took two swigs." 
    "Or if she couldn`t sleep, which was common, she would take three." 
    "When she was really feeling miserable, she took four." 
    "If she was in an especially good mood, she sometimes took an extra swig." 
    "But otherwise she never broke her rule: one swig per day."

    "She put down the cup and licked her lips."
    
    show eugenie normal at rightPos2
    
    "Then she lifted the heavy basket of crackers and climbed the stairs to the deck." 
    "Everyone was looking just as bored as yesterday." 
    "All the gentleman knew that it would have been far more comfortable downstairs." 
    "But then they would have had to spend time with the crew members, who were commoners. It wouldn`t have been fitting." 
    "So all the noble counts and dukes and marquises basked in the sun, wearing their heaviest wigs and hottest clothes."
    "Desperately fanning themselves they struggled to converse in the appropriate manner and appear content."
    "What a bunch of idiots, Eugenie thought." 
    
    show memnon normal at leftPos2
    
    "All the men were in line to Memnon. The Ambassador was offering free shaves to all willing men. He was quite skilled." 
    "The shaves were needed. Most noblemen aboard had never touched a razor themselves and would not risk learning this skill now." 
    "Monsieur de Clere also happily offered his services to commoners. He`d asked a permission to shave the slaves, but this had been denied." 
    "The ambassador was truly a curious gentleman, though he`d been unnecessarily rude in the past."
    
    show eugenie happy at rightPos2
    
    e"Good morning, Monsieur de Clere! Would you like a dry cracker?" 
    "Despite her emerging drinking habit, she found herself happier now than before. At least these weeks had been different." 
    m"I would love one, Mademoiselle Eugenie! Dry crackers are a favorite of mine! How are you today?" 
    e"Brilliant, thank you! It is a beautiful day, not even the hint of wind." 
    
    show memnon smile at leftPos2
    
    m"I wouldn`t mind the weather being just a bit worse." 
    m"We`ll need the wind if we`re going to get anywhere." 
    
    show eugenie normal at rightPos2
    
    e"What of the rowers? Won`t they get us there?" 
    
    show memnon normal at leftPos2
    
    m"Even the rowers can`t go on forever. And sailing would be faster in any case." 
    m"Besides, we must be running low on supplies." 
    
    show memnon serious at leftPos2
    
    m"Because a cracker this small will not keep a grown man standing all day." 
    "Eugenie felt her stomach grumble as well and quickly changed topics." 
    e"Is your poet friend still up there in the crow`s nest?" 
    "Memnon nodded" 
    m"I think he may have finally lost it." 
    m"He only gets down once a day to visit the privy." 
    m" I bring him food and paper so he can focus on writing." 
    
    show eugenie angry at rightPos2
    
    e"He has no right to ask that. Why would you?" 
    "Memnon sighed." 
    m"You`re right." 
    m"He`s always been unstable. On the first day, he broke down in tears and wanted to die, with no cause whatsoever." 
    m"I persuaded him to write something spectacular before dying. His great masterpiece." 
    m"The longer I keep him there the more time he`ll have to recover. Maybe once we settle somewhere he`ll have regained his senses." 
    
    show eugenie shock at rightPos2
    
    "Eugenie looked up, horrified." 
    e"Aren`t you afraid he`ll finish his book and jump into the sea? He`s been there for weeks."
    
    show memnon normal at leftPos2

    m"No." 
    m"I know him." 
    m"He`ll never be happy with his writing. Sooner or later he burns or tears everything he writes." 
    m"That would the main reason why he isn`t more known amongst poets. Even now he throws away most of the paper I bring him." 
    
    show eugenie normal at rightPos2
    
    e" I hope he`ll come to his senses. And write something. Gods know this ship could use some literature." 
    "She continued the round and delivered food to many a happy hand."
    
    hide eugenie with dissolve
    hide memnon with dissolve
    stop music fadeout 1.0
    hide laivapäivä with dissolve
    show laivapäivä behind ikkuna with dissolve
    show vassan angry at leftPos2 with dissolve
    show nest at rightPos3 with easeintop

    "Up, up in the crow`s nest, Vassan was writing feverishly." 
    "His magnum opus would be astonishing." 
    "It was epic poetry, with heroes and gods and the like. A bit old-fashioned, but it would be memorable." 
    "But was it too old fashioned? Shouldn`t it resonate with more modern audiences? Shouldn´t it reflect the predicament of his people?" 
    "Would he ever finish his work? He was starting to think no. But he was also starting to think it didn`t matter."
    "He was feeling better now."
    "Of course he was seasick."
    "And he had developed a nasty fever over the last couple of days. Honestly, much of his paper was spent wiping his leaking nose."
    "But he no longer constantly thought of dying." 
    "He`d long ago realized this had been Memnon`s intention all along. To distract him."
    "Should he formally thank Memnon in his preface? Should he write a preface?"
    "He began to draft one but abandoned it quickly. It was too formulaic to preface one`s work! It distracted the reader from the core text." 

    "The tiny basket he was in was indeed most uncomfortable." 
    "He shivered every night and his back hurt like hell." 
    "He wiped his nose on the half-a-preface and threw it away." 
    "What a waste of time."
    
    hide nest with easeouttop
    hide vassan with dissolve
    hide laivapäivä with dissolve
    show laivapäivä behind ikkuna with dissolve
    play music "musiikki/daysea2.mp3"
    show eugenie normal at leftPos2 with dissolve

    "Eugenie was dealing out his last crackers when the Captain began his daily monologue about discipline and patriotic values." 
    "Nobody was interested at this point. The crowd ate their crackers and chatted in silent voices." 
    "All were careful not to speak too loud. One sailor had laughed out loud last week and he had been whipped."  

    k"People o`Flayes!It has been 23 days and all of us are alive and well! Spit on my grave if we aren`t the favorites of god!" 
    "The speech would go on for some time, but by now people had lost interest." 
    "Eugenie watched the sea and remembered all the times she`d swum in the sea and hoped to sail the great ocean. One time she`d played a pirate and her mother had seen it."
    "She had whipped her thoroughly and told her that the only company she should dream of was the company of princes." 
    "This ship was full of princes but they were all incredibly dull people." 

    show eugenie shock at leftPos2
    
    "While lost in these thoughts she saw something." 
    "A massive blue shape broke the waves, unleashed a column of water and then disappeared." 
    "Eugenie screamed."
    "She screamed loudly and only two people aboard missed it." 
    "One was the captain, deep in his oration." 
    "And the other Vassan, who was sick and so deep in his own thoughts, he might not have noticed if the ship sunk."

    "Everyone on board rushed to the railings and were frozen by horror." 
    
    show whale at rightPos3 with easeintop
    
    "Amid the ships swam dozens, if not hundreds of monstrous sea beasts." 
    "They resembled fish, except no fish was that massive." 
    "Their thick skin was dark blue and they had small, red eyes." 
    "Their huge mouths were filled by what looked like long blades of grass in the place of teeth. Even they were thick as anchor ropes." 
    "Whenever the beasts broke the surface, they unleashed water in high columns that sprayed far and wide, leaving everyone aboard soaked in salt water." 
    "One such monster swam right underneath the ship." 
    "Some of the men fainted."
    e"Good heavens, what are they?"  
    
    hide whale with easeouttop
    show memnon normal at rightPos2 with dissolve
    
    m"Do not worry, Mademoiselle de Mollerfiol. They are harmless." 
    
    show eugenie angry at leftPos2
    
    e"Harmless? How can anything that huge be harmless?" 
    m"They only eat fish. They`ve no cause to attack ships." 
    
    hide eugenie with dissolve
    show memnon serious at rightPos2
    
    "To calm people down Memnon lit his pipe and repeated his soothing words much louder." 
    m"Calm down, everyone! They`re harmless! Look, aren`t they beautiful?" 
    "Nothing he said had any effect on the crowd." 
    "All the passengers scrambled about in terror, searching for their loved ones, their pistols or the lifeboats." 
    "The Captain, stalwart as ever, was quickly issuing orders." 
    k"Man the gun deck! Prepare to fire! Get every man a musket and munitions!" 
    k"I will not let some overgrown fish endanger my ship!" 
    k" And someone silence that screeching duke! I cannot bear his screaming!" 
    "One of his officers looked hesitant." 
    "Sir, it would be highly improper to gag a man of such a high status..." 
    "The Captain went red as a tomato." 
    k"If I order you to gag someone, you will!" 
    k" I will tolerate annoying nobles and cowardly nobles, but not both! This vessel..." 
    "Memnon interrupted the Captain." 
    
    show memnon angry at rightPos2
    
    m"Sir! Do not shoot those creatures! They are perfectly harmless!" 
    "The Captain was breathing loudly. He looked like he was about to have a heart attack." 
    k"Monsieur de Clere, those fish are twice the length of this vessel!" 
    k"Carnivore or not, if they make one bad move this damned thing`ll capsize and you`ll drown." 
    m"But..." 
    k"No buts!" 

    k" And you`ve just earned a place for yourselves below, loading our bronze girls." 
    k" And you`ll be firing the cannon when we send those demons to the pit where they belong!"  
    "The officer tried to force Memnon below but he shook him off." 
    m"I`ll find my way." 
    
    hide memnon with dissolve
    hide laivapäivä with dissolve
    stop music fadeout 1.0
    #####################################################################################################################################################
    #####################################################################################################################################################
    #####################################################################################################################################################

    show tykkikansi behind ikkuna with dissolve
    show memnon serious at rightPos2 with dissolve
    
    "On the gun deck, the mood was calm compared to the one above." 
    "Cannons were being transferred into position with the speed of professionals, while gunpowder and shot were brought from below." 
    "Memnon sought with his eyes the Gunnery Chief, who was found giving orders." 
    "Memnon ran to him, hopping over a barrel of lead balls." 
    m"No fish are to be killed!Captain`s orders!" 
    "The Gunnery Sergeant looked baffled." 
    t"Why in the name of the gods?" 
    t"We were just told to fill `em up with lead until so they`ll stay at the bottom till judgment day." 
    "Memnon froze." 
    "He hadn`t thought this plan through." 
    "Then he saw a silver icon on the man`s neck." 
    "Thank god he was a believer." 
    m"Because our Captain`s been granted a vision. Angels have told him that our survival depends on the fish surviving." 
    m"Instead of killing them we`re to aim high and salute them by firing the cannons into the air ten times." 
    "Memnon was sweating." 
    "The man stared at him for a long while."

    t"Well ain`t that stupid. He must be goin` nuts. Well, orders are to be followed. Let`s please the old man." 
    "Memnon was relieved beyond measure. Too many lives were already on his conscience."

    t"Aim the cannons high!" 
    t"Prepare to salute with fire!" 

    show memnon normal at rightPos2

    "Memnon was pleased." 
    "The guns wouldn`t touch the animals and the muskets would only annoy them." 
    "He knew the other ships would fire all they could, but hoped the fish would flee soon." 
    "The same fish lived on the shores of his old homeland, and he hadn`t seen them in years." 
    "They had been considered sacred in the Yribid Empire, though not as sacred as hedgehogs." 
    "As the cannons roared time and again Memnon thought of the family and home he`d left behind when he fled to Flayes to live the high life."

    hide memnon with dissolve

    "The great fish escaped soon after the first volley." 
    "STill, fifteen were counted to have been killed or hurt beyond recovery." 
    "Their blood dyed the ocean red for miles around."
    "The crews celebrated victory with rum and gin."
    "Memnon gazed upon the tainted water and worried. He hoped no one would find the blood before the ocean swallowed it."
    
    hide tykkikansi with dissolve
    show laivayö behind ikkuna with dissolve
    play music "musiikki/nightsea.mp3"
    show vassan angry at leftPos2 with dissolve
    
    "Vassan cursed loudly in the mast." 
    "His lantern had gone out and climbing down to fetch fire would cost him several valuable minutes." 
    "`Twas midnight and, discounting the rowers, he thought he was the only one awake." 
    "Of the forty-something pages he`d written, he`d approved three." 
    "They`d asked him not to waste valuable paper by throwing it into the sea, so now he lived amid a pile of crossed out pages." 
    
    show vassan normal at leftPos2
    
    "The solution came to him: he would burn the abandoned pages for light and warmth." 
    "Before that, he decided to stretch his legs." 
    "With considerable effort he stood up, groaning his sore joints and muscles that only seemed to exist when they hurt real bad." 
    "Two weeks past Memnon had brought him a blanket and his fever had gone down a notch." 
    "His cough remained, though, and his nose was like a waterfall." 
    "He was leaning on the railing and gazing upon the deserted deck. Then he saw someone."
    
    show eugenie happy at rightPos2 with dissolve
    
    "It was Eugenie." 
    "Dancing in the moonlight, she giggled to herself." 
    "She was happy, beautiful and full of grace. Just like on the night of the attack."
    
    show vassan shock at leftPos2
    
    "Suddenly she leaned over the railing to look upon her image in the waves." 
    v"Look out, you might fall!" 
    e"Ah, mister poet. How fare you tonight? Are the words in your favor?" 
    
    show vassan smile at leftPos2
    
    v"No, but I`m fine now, that I see you." 
    v"Your dancing reminded me of the last night in Flayes." 
    e"Were you there? It feels like it was so long ago." 
    v" I was. I guess the world was a different place then." 
    e"It was. Do you miss Flayes, sir poet?"
    v" I`m not a sir. And oddly enough I do."
    e" Oddly? It was our home."
    v"Well I didn`t have much there. I suppose you had to leave quite a wealthy life behind."
    e"We had money. But I don`t miss money nearly as much as I miss the space."
    v"Space?"
    e"You know, room to go around. I had a room and a bathroom of my own. I could take walks in the garden. Here we`re all crammed."
    v"Why don`t you come up here? The air is fresh and you can see really far."
    e"Thank you but I`ve had some rum and it might not be smart to do acrobatics on ladders."
    e"But, tracking back, I do miss having money."
    v" I`m surprised by your honesty."
    e"It`s not about the money, it`s about being free. And that`s a lot easier when you have money. Or are a man."
    
    show vassan angry at leftPos2
    
    "Vassan was left speechless." 
    v"Miss, is everything all right?" 
    e"All right?" 
    e"No. I`m lonely. Our predicament denies me pleasure, my status denies me the right to useful work. My gender even denies me the right to honesty."
    e"Even you have your words to distract you up there. I have nothing."
    
    hide eugenie with dissolve
    
    "And, saying no more, she made off, nearly tripping over on the way." 
    "Vassan could smell the rum all the way to the mast." 
    "Her words made him uncomfortable." 
    "Somehow he felt guilty for her foul mood."
    "That was stupid, he thought. He`d done nothing to her. Everyone had it just as bad on this ship."
    "Except the slaves, he remembered. They had it worse." 
    "To distract himself from these unhappy thoughts he peered to the horizon." 
    "There was something far off in the distance. Like the outline of a ship, but not one of theirs." 
    stop music fadeout 1.0
    "Then more appeared." 
    
    show vassan shock at leftPos2
    
    "Rubbing his eyes, he looked again." 
    "Now he could see them clearly." 
    "Ships without lanterns. Following them." 
    "The enemy."
    "The word had struck terror as long as Vassan had lived." 
    "The revolution had begun somewhere on the periphery of the civilized world." 
    "The masses had risen up, butchered their masters and formed new governments, armies, and religions to replace the ones they`d destroyed." 
    "Priests were killed, cities burned and entire kingdoms had collapsed in the face of the ever-spreading revolt." 
    "No name could describe such barbarity in the eyes of the noblemen whose lives were on the line." 
    "They were just the enemy." 
    "They brought their families with them to settle the towns they`d emptied. Their masses swelled from every plantation, every slum and every ship they captured." 
    "And now they were legion." 
    "Their army was like a swarm of locusts: unstoppable and in numbers beyond count." 
    "Vassan had never seen them until their hosts made their way through the streets of Flayes."
    "He did not fear death." 
    "But he did fear the enemy." 
    
    show vassan normal at leftPos2
    play music "musiikki/terror.mp3"
    "Without hesitation, he reached for the great horn by his side." 
    "It was to be blown only in one situation." 
    "He blew with all his strength." 
    
    hide vassan with dissolve
    
    "The horn rang miles away on the waves." 
    "The whole fleet was guaranteed to hear it. That was the point." 
    "The Captain woke up." 
    "You couldn`t mistake that sound." 
    "He`d heard it so many times in Naval School and in drills after that. And once before for real." 
    "In seconds the Captain was up and bellowing orders, though all the ships other officers were still struggling to put on their breeches." 
    "The others joined their commander on the deck." 
    "With his telescope, the Captain could make out with clarity what Vassan had squinted at from the mast." 
    k"They`re here."  
    "A real battle, at last."

    "To the Captain`s great disappointment admiral Hulegu chose not to give battle under the conditions." 
    "Aboard the ship, only Vassan had the vantage point to see the situation and he had no idea what was going on." 
    "The admiral transmitted his orders by lantern from ship to ship. Amid the chaos the fleet was in, the clear simplicity of the message gave strange comfort:"
    "Run for your lives and expect no mercy." 
    "For a second the Captain considered turning about and facing the enemy alone, but decided not to risk the civilians." 
    "Instead, the Captain held a speech."

    "While the Captain spoke the rowers worked so hard five of them died of exhaustion."
    
    stop music fadeout 1.0
    hide laivayö with dissolve
    show tykkikansi behind ikkuna with dissolve
    play music "musiikki/daysea2.mp3"
    show memnon serious at rightPos2 with dissolve
    
    "Memnon volunteered on the gun deck, which he knew from the battle against the 'sea monsters'." 
    "Not to say he had much to do." 
    "As soon as the guns were loaded and placed in position, the crew began to play card and dice. If they were all going to die, a little gambling debt hardly mattered." 
    "Someone played violin."

    show chess at leftPos3 with easeintop

    t"Think we`re going to win?" 
    "the gunnery sergeant asked him while they played chess."
    m"Only one of us can win. Check." 
    t"I meant the battle." 
    m"What battle? We`re running away again. We`re good at that." 
    "Memnon sipped his coffee. It might be the last cup he enjoyed in a while." 
    t"We wouldn`t run if the Cap had any say in it. Another speech?" 
    
    show memnon normal at rightPos2
    
    m"That`s why I`m down here."  
    "The gunnery sergeant laughed." 
    
    show memnon smile at rightPos2
    
    m"Checkmate." 
    "The gunnery sergeant stopped laughing." 
    
    hide chess with easeouttop
    hide memnon with dissolve
    stop music fadeout 1.0
    hide tykkikansi with dissolve
    show laivayö behind ikkuna with dissolve
    play music "musiikki/nightsea.mp3"
    show eugenie crying at rightPos2 with dissolve
    
    "Eugenie wept out of horror." 
    "It was Flayes all over again. The chaos, the screams, the violence, the running." 
    "She`d never seen a ship go so fast." 
    "Then again, they were in a hurry." 
    "Sailors ran around her, cursing and yelling."  
    "Somewhere far behind them, the enemy was rowing twice as hard." 
    "Now she heard thunder." 
    "A storm, right now?" 
    "Then she realized, it wasn`t a storm." 
    "The enemy had caught the last, straggling ships in the fleet. The battle had begun." 
    "Eugenie grabbed her mother`s arm. She was scared."
    
    hide eugenie with dissolve
    hide laivayö with dissolve
    show laivayö behind ikkuna with dissolve
    show vassan shock at leftPos2 with dissolve

    "Vassan did his best to keep up with things." 
    "The enemy had caught two ships and no one had gone to aid them." 
    "They sank in minutes." 

    "The fleet raced towards the shore. They`d spotted the shoreline only the previous evening." 
    "There the ships would be emptied of people and cargo, set ablaze and turned to meet the enemy." 
    "Whatever remained of the ships at that point, anyway."
    
    hide vassan with dissolve
    
    "The only significant change during the tense hours that followed the decision were the three further ships that were lost." 
    "And of course Memnon and the gunnery sergeant moving on to play poker instead of chess. The cards favored the sergeant."
    
    stop music fadeout 1.0
    hide laivayö with dissolve
    show laivapäivä behind ikkuna with dissolve

    "At dawn, the beach was reached, with the enemy already catching up." 
    "Half the ships were emptied into boats at sea and then sent to hold back the enemy. The other half was beached." 
    "Landing was done in a small bay, where all the ships could only barely be fit."
 

    #####################################################################################################################################################
    #####################################################################################################################################################
    #####################################################################################################################################################

    show eugenie crying at rightPos2 with dissolve

    "Eugenie was freezing and in shock when she was escorted aboard a lifeboat." 
        
    show vassan shock at leftPos2 with dissolve
    
    "Aboard she woke up from her trance when Vassan yelled and struggled to get back on board the ship that had carried them for so long."
    v"But I want to fight! Let me go! I can fight!" 
    "He tried to wrestle his way out of the boat and nearly capsized it."
    
    show eugenie angry at rightPos2
    
    e"Calm down! You`ll get your chance to die with a musket in your hand!" 
    
    show vassan angry at leftPos2
    
    "Vassan stared at her angrily." 
    v"Why do you care? You couldn`t understand, you`re a woman!" 
    
    show eugenie shock at rightPos2
    
    "Eugenie saw red." 
    
    show eugenie angry at rightPos2
    
    "The next thing Vassan saw was her fist." 
    
    show vassan shock at leftPos2

    "gasping of pain, Vassan fell to the bottom of the boat and held a hand at his bleeding nose." 
    "Eugenie said nothing. She just sat there. Her mother was astonished." 
    "Eugenie knew what was coming." 
    "Even if there was an army of a million men coming up against them, her mother would find the time to do some preaching about proper behavior."
    "At least the poet was calm now."

    hide vassan with dissolve
    hide eugenie with dissolve
    hide laivapäivä with dissolve
    show tykkikansi behind ikkuna with dissolve
    play music "musiikki/dream.mp3"
    show memnon serious at leftPos2 with dissolve

    "Memnon lifted a new ball and lowered it into the barrel."  
    "He raised his thumb and the cannon was pushed back to the hatch." 
    "The order was given and old Bertha went off with sixty of her friends." 
    "Smoke, ash and hot fumes rushed out of the barrel, accompanied by a magnificent thunder." 
    "Faster than the eye could see the heavy lump of lead flew towards the enemy ship." 
    "Load. Aim. Fire. Repeat." 
    "Memnon swiped some of the sweat off his brow and lifted another ball." 

    show memnon shock at leftPos2

    "In that instant a swarm of identical balls punctured the ship`s hull, sending hundreds of deadly wood shards in every direction." 
    "Memnon dived to the floor and narrowly dodged a large, loose piece of timber, which struck through the floor and killed two rowers." 
    "Memnon was deaf." 
    
    show memnon serious at leftPos2
    
    "He slowly got up and looked around." 
    "Wounded, dead and dying lay everywhere, crying, gasping for air, screaming for their mothers." 
    "He was one of the lucky few without a scratch." 
    "A messenger came on deck." 
    "He tried to yell his orders but Memnon couldn`t hear them. Finally, he showed in on paper." 
    "Abandon ship." 
    "Memnon nodded and began helping his comrades up."  
    "They would leave the deck together. Then another volley tore the ship."
    "Memnon reached the stairs, but only barely, before another deadly rain showered the remains of the gun deck." 
    "He forgot his comrades instantly." 
    
    hide tykkikansi with dissolve
    show cabin behind ikkuna with dissolve
    
    "He ran for his cabin across a field of fire and smoke." 
    "There were some things he wanted to save." 
    "Inside he put on his finest coat, his most expensive hat and then took his cane and a pouch with the leaden coins he so dreaded. They were heavy." 
    "While he was dressing two more volleys ripped the vessel." 
    
    hide cabin with dissolve
    show laivapäivä behind ikkuna with dissolve
    
    "Outside he noticed a light shining from the Captain`s cabin."
    
    hide laivapäivä with dissolve
    show cabin behind ikkuna with dissolve
    
    "Memnon opened the door." 
    "The Captain sat in uniform and wrote a letter." 
    "On the table lay a pistol and a dagger." 
    k"Master de Clere, aren`t you handsome this morning." 
    
    show memnon normal at leftPos2
    
    m"If I must die, I`ll die well dressed." 
    k"Peacock." 
    k"Take this to whoever leads you on land." 
    "Memnon looked at the scroll the Captain had given him." 
    "He looked up to see the Captain drape himself in the flag of Flayes and yell:" 
    k"The king is dead! Long live the king!"
    
    show memnon serious at leftPos2
    
    "Memnon saluted and fled the room." 
    "He knew what was coming." 
    
    hide cabin with dissolve
    show laivapäivä behind ikkuna with dissolve
    
    "Outside he heard a gunshot." 
    "Why was everyone in such a hurry to die these days?"
    
    hide memnon with dissolve
    stop music fadeout 1.0
    
    "Memnon dove into the cold embrace of the sea as the ship began to sink behind him. He made for the shore, without looking back at the vessel that had saved so many lives."
    "Only once ashore  did he realize that no one had set free any of the rowers."
    "He collapsed out of exhaustion and swore that no one else would die on his account."
   
    hide laivapäivä with dissolve
    show battle behind ikkuna with dissolve
    show vassan smile at rightPos2 with dissolve
    
    "Vassan was enchanted by the ghastly morning sight." 
    "The bay was full of ships, afloat and sinking, sending up columns of smoke. Bodies were washing ashore every minute." 
    "Some of the dying ships were from the enemy, but most were not." 
    "Only a couple of ships had been set ablaze and sent towards the enemy as had been the plan." 
    "Most ships had been caught at sea and sunk after a valiant but brief resistance." 
    "The enemy had lost ships too, but with their numbers, the losses hardly mattered." 
    "And yet the enemy had pulled back." 
    "The shallow bay was full of dying ships, and living ones could hardly attempt to navigate it." 
    "So the enemy had fallen back." 
    "For now."

    show memnon serious at leftPos2 with dissolve
    show vassan normal at rightPos2
    
    m"It`s not over" 
    "Vassan nodded" 
    v"Quite a morning, wasn`t it?" 
    
    show memnon normal at leftPos2
    
    m"And it`s going to be quite an afternoon." 
    m"The enemy is already landing their forces some leagues north." 
    
    show vassan angry at rightPos2
    
    "Vassan cursed" 
    v"What do we do now? There is nowhere to run." 
    
    show memnon serious at leftPos2
    
    m"Now we fight."
    
    hide vassan with dissolve
    hide memnon with dissolve

    "The two men walked back to the emerging camp, where weapons were being dealt out to everyone strong enough to carry a musket."
    m"Some of them are barely taller than a musket." 
    "Truth be told, not nearly every man in fighting condition got a musket: most of them were now in the bottom of the bay." 
    "In the end, every third fighter had a musket. The rest had to settle for axes, picks, and sharpened shovels. Some only got sharpened poles." 
    "The rest included the slaves, who were expected to fight but not deemed worthy of proper weapons." 

    "When everyone had some sort of weapon, orders were given to find and make ammunition." 
    h"All objects of lead, great or small, must be melted to make musket balls!" 
    "The man shouting orders was admiral Hulegu, who wasn`t nearly as impressive a sight as the Captain had been." 
    "He was a rat in more ways than one: he was small, twitchy, and scared." 
    "And yet he smiled at the motley army like he owned every man in it. In fact, his family did own many of the men in it." 
    "Memnon felt like punching him right in the smile." 

    show memnon shock at rightPos2 with dissolve
    play music "musiikki/dream.mp3"

    "As the admiral gathered jewelry, seals, and paperweights, Memnon heard voices again." 
    "All those who`d died. In Flayes, aboard the ships, even those who would die in the coming hours." 
    "He saw buildings ablaze and a guardsman die." 
    m"I did it!" 
    "He shouted, crashing into the admiral, who squealed like a small child." 
    h"What are you doing, mister?" 
    "Memnon stood up, raised his head and shouted so loud everyone nearby could hear:" 
    m"I sold Flayes to the enemy! I murdered guardsman Egbert and opened the gates. All your loved ones are dead... because of me." 
    
    hide memnon with dissolve
    
    "A long, deep silence followed. It took a while for the people around to understand what was happening." 
    "Then began the screams." 
    
    show eugenie angry at rightPos2 with dissolve
    
    "Eugenie could not believe her ears. The man must have gone insane."
    "The admiral was speechless. It took him eight attempts to formulate a sentence." 
    h"hmm, ahm, hmpfm, very well, uhh, guards! Seize this man! He will be, uhh interrogated and tried after we`ve won the battle. Then he`ll be, uhh, hung." 
    
    show eugenie shock at rightPos2
    
    "Without saying anything more the admiral gestured to his soldiers to tie Memnon up and take him away. He gave away his lead coins." 
    m"For bullets.. you should melt them...."
    
    hide eugenie with dissolve
    show vassan shock at rightPos2 with dissolve
    stop music fadeout 1.0

    "Vassan felt like he was struck by a lighting." 
    "All he could do was stare in disbelief at his so-called friend, being dragged in chains past him." 
    "Memnon gave him an apologetic smile." 
    "Vassan couldn`t believe it." 
    "Not Memnon." 
    "Of all the people in the world. Not him. He`d always been brave, Vassan had always envied him. Not Memnon."
    "Then again, he`d lied before. About his family. About his past. For years. What`s one more lie?" 
    "Vassan was still in shock when someone handed him a musket, some powder and a bag of shot." 
    "He hardly noticed when the columns of gentlemen, sailors, and slaves dragged him with them to a steep hilltop away from the camp." 
    "Someone told him to dig a trench, and he did, without question. His mind was dysfunctioning. Good thing his body still worked." 
    "A couple of his comrades tried to talk to him but got no response."
    "Vassan woke up from his dreamlike state only when the enemy was forming up before them" 
    v"Wau." 
    "He said after a while, not sure if anyone heard." 
    w"Aye. If we beat them, I won`t shave my beard for ten years." 
    
    show vassan normal at rightPos2
        
    "Vassan looked at the man beside him." 
    "He was an old man, clearly a slave, but still looking rather merry." 
    "He had a tall, wooden pole that was sharpened." 
    v"I don`t think you`ll live to see that many years." 
    "The slave laughed." 
    w"You`re right, but let me say:" 
    w"A lot of them are never gonna walk again, even if we all died on this hill." 
    v"Were you a soldier once?" 
    "The slave laughed again." 
    w"Soldier? Boy, I was a king! I had an army, subjects, a palace and slaves of my own. I hosted balls just as fancy as your king." 
    
    show vassan shock at rightPos2
    
    "Vassan did not know what to say." 
    v"Are you serious? What happened?" 
    w"You happened." 
    w"Flayes happened with an army, fourteen times larger than ours. That was before the revolutions."
    w"After eight days of war my palace was gone and my people in chains, being led away to work your people`s fields and mines." 
    "Vassan felt the sting of shame."
    v" And yet you fight for Flayes?" 
    "The former king smiled again."
    w"But of course! I`m a Flayesian now. But before I was Wazu, the last king of the Wulu nation." 
    v"Vassan. But why fight for your oppressors? And with such glee?" 
    w"These are desperate times when masters arm their slaves. I shall like to see them try and take these weapons back. Besides, it is much better to die fighting than working in a mine." 
    v" I thought so too." 
    v"But now I see them and all I want is to run away, get married and live my life far away." 
    "The king nodded." 
    w"All warriors feel that way before a battle. It is fear, and your fear is always serving your enemy." 
    "Vassan gave no reply. He only saw the endless black host."
    
    hide vassan with dissolve
    hide battle with dissolve
    show teltta behind ikkuna with dissolve
    play music "musiikki/dream.mp3"
    show memnon transsi at leftPos2 with dissolve

    "Memnon sat in a tent." 
    "Since everyone else was fighting, no one was guarding him." 
    "He`d been tied up and left there." 
    "He could hear the roar of the guns." 
    "The battle had begun. Vassan was somewhere over there, as was the gunnery sergeant whose name he`d never asked. And he sat here." 
    "He cursed and tried to wrestle himself free. Suddenly he felt something in his boot." 
    "His old razor. He smiled."
    
    hide memnon with dissolve
    hide teltta with dissolve
    stop music fadeout 1.0
    show battle behind ikkuna with dissolve
    show vassan angry at rightPos2 with dissolve
    play music "musiikki/battle.wav"
    
    "The battle had not lasted long."
    "The army of Flayes had been organized into sections led by noble officers and their sons. Colorful banners had dotted the line."
    "There was a string of last minute changes, to assure that every man of noble blood had someone to bark orders at."
    "Vassan and Wazu were serving a boy of just sixteen years. A son of duke this and that."
    "For a while, everything had been quiet."
    "Then all hell had broken loose."
    "A thunderous barrage of artillery fire had torn the neatly arranged battle line into bits and pieces."
    "Everywhere the stench of gunpowder and death invaded the senses. It was hard to see amid the smoke."
    "The officers still standing had just enough time to shout orders that no one could hear before the black flood hit them."
    "And just like that, the line broke. Those that still could, ran for their lives towards the sprawling tent camp behind them."
    "And past it."
    
    hide vassan with dissolve
    hide battle with dissolve
    show battle behind ikkuna with dissolve
    show eugenie normal at leftPos2 with dissolve

    "Eugenie was ready" 
    "The first cart stopped at the wound dressing station." 
    "The wounded men were thrown down with great haste and little comfort and the cart wheeled around." 
    "Eugenie dashed to aid the first man with a bucket of water and some bandages." 
    "She turned the man, lying face down, on his back and nearly threw up." 
    "The youth had a gaping hole in his stomach." 
    s"Am I dead?" 
    e"Not yet." 
    s" And I thought you were an angel." 
    "Eugenie gave the man some water and began to tie the wound feverishly."
    
    show eugenie angry at leftPos2
    
    "If it were up to her, the man would live."
    
    hide eugenie with dissolve
    stop music fadeout 1.0
    hide battle with dissolve
    show teltta behind ikkuna with dissolve
    show memnon angry at leftPos2 with dissolve

    "Memnon cursed loudly." 
    "He`d dropped the knife and couldn`t reach it." 
    
    show memnon crying at leftPos2
    
    "He burst into tears. He prayed to all the gods he knew to let him go." 
    "Why should you run free? You betrayed those who were kind to you. Our blood is on your hands." 
    
    show memnon shock at leftPos2
    play music "musiikki/dream.mp3"
    
    "The voices again." 
    "So many of them. So many, that their choir of agony mixed with the orchestra of death he could hear from outside his tent." 
    m"The ghosts of Flayes." 
    "You killed us, said the voices." 
    m"I`ll make amends. Please. Just let me out." 
    m"I wish to fight. My friends. I want to help them." 
    "Oh, friends get your help. But what of us?" 
    "Memnon looked up." 
    
    show memnon crying at leftPos2
    
    "He could have sworn his wife and daughters were there, beside him." 
    "He suddenly realized he`d missed their faces." 
    m"I miss you." 
    "Memnon was now openly crying." 
    "Do you now? Not enough to send a letter. Or visit." 
    m"Please, let me go. I`ll help my friends. And then I`ll come to you and never leave." 
    "The ghosts of Flayes interrupted them." 
    "Do you wish to fight, Memnon de Clere?" 
    m"Yes."
    "Good. Then fight."
    
    hide memnon with dissolve
    hide teltta with dissolve
    stop music fadeout 1.0
    show battle behind ikkuna with dissolve
    show eugenie angry at rightPos2 with dissolve

    "They were out of bandages." 
    "Another young man was moaning in pain. He would bleed out in minutes." 
    "With her bare hands she`d found the bullet, but now there was nothing to dress the wound with." 
    "She poured rum on the wound and looked around for any fabric at all."
    "The soldier`s coat was filthy. It wouldn`t do. She looked at her pretty, blue dress. Was there really nothing else?"
    "With a deep sigh, she tore the seams in the silk. She would never have a dress like it again."
    "The sounds of battle were coming closer."
    "Good, she thought. Now she was closer to those needing her help."
    
    hide eugenie with dissolve
    hide battle with dissolve
    show battle behind ikkuna with dissolve
    play music "musiikki/battle.wav"
    show vassan shock at rightPos2 with dissolve

    "The enemy was now looting the rows of tents."
    "Vassan was gathering his breath in the bushes behind the camp, which was now in enemy hands."
    "Memnon was somewhere in there, and likely Eugenie as well."
    "He couldn`t believe they`d lost. Not after getting so far."
    "The enemy had given up the pursuit and stopped to rob the tents clear of supplies, animals, and gold."
    "How were they able to save so much gold from the ships, and yet so few bullets?"
    "Most officers had either died or fled. Amongst the trees Vassan could still spy hundreds of men like him, wondering what they could do."
    w"We should attack now."
    v"Are you insane? We`ve lost!"
    w"So they think. They`ve lowered their guard. If we charged now, we could catch them unawares."
    "Vassan thought of the words. They made a strange kind of sense. But who would lead them? Admiral Hulegu was likely dead."
    v"Wazu, you were the king of all our slaves once, weren`t you?"
    w" I was. Why?"
    v"Care to rally your people?"
    "Wazu smiled."
    w"On it."

    hide vassan with dissolve
    hide battle with dissolve
    show battle behind ikkuna with dissolve
    show memnon serious at leftPos2 with dissolve

    "Memnon was impatiently cutting the ropes when suddenly they snapped and he was free." 
    "He wasn`t sure how he`d gotten the razor." 
    "But he had suddenly rediscovered his long lost faith in gods, fate, and ghosts." 
    "He rushed out of the tent and was shocked." 
    "He didn`t have to go to the battle. The battle had come to him."
    "All around him, the enemy was looting the tents, getting drunk on rum and celebrating their victory."
    
    hide battle with dissolve
    show yöhepo behind ikkuna with dissolve

    "He saw the king`s horse alone, unharassed. It had been the first thing to get out of the ships, before anything or anyone else." 
    "Now a hasty shelter had been erected in the center of the camp." 
    "Memnon mounted it and struck his heels into its sides." 
    "The animal shot ahead with dreadful speed and Memnon needed not guide it. It knew where to go."
    
    hide memnon with dissolve
    hide yöhepo with dissolve
    show battle behind ikkuna with dissolve
    show vassan shock at rightPos2 with dissolve

    "No attack had ever emerged." 
    "The slaves would have followed Wazu willingly enough, but the remaining officers had denounced their plan as madness." 
    "Vassan had thought of shooting one just for show."
    
    show memnon serious at leftPos2 with dissolve
    
    "Suddenly he heard yells." 
    "Vassan saw the peacock hat from afar." 
    "It was Memnon. He was riding to them, on the king`s horse."
    
    hide vassan with dissolve
    
    "Memnon grabbed a banner from one officer and waved it around his head."
    
    show memnon angry at leftPos2
    
    m"Why are you covering here? Your families are dying! Turn around, you scum, or I`ll kill every one of you myself!"
    "Memnon was so serious, with a sword in his hand, that no one doubted his words." 
    "Lighting struck. A storm was coming. Memnon looked like a ghost."
    w"All right, boys. Follow the ghost! Kill them all!" 
    "And, just like that, the cowering Flayesians turned and followed their new leaders." 
    
    hide memnon with dissolve
    
    "The enemy was caught with his pants down." 
    "There was no line to meet the charge. The army had lost discipline and most of its men were already drunk." 
    "Like a warm knife through butter, the Flayesian counter-attack cut through its foes." 
    "The enemy was quick to rally around its black banners and form pockets that fought back." 
    "For a while." 
    "Then their famous discipline failed them and they fell back, first while fighting, then with their backs turned."
    
    show vassan smile at leftPos2
    
    "The enemy had been broken."
    "Vassan was among the first to chase them across the camp, the fields and over the hill where the trenches still were."
    "For once he was certain. He had a purpose."
    "He knew where his place was. He was where he wanted to be."
    "In a word, he was happy. Then one foe turned back." 
    
    show vassan shock at leftPos2
    hide battle
    stop music
    show blood behind ikkuna
    
    "Vassan saw the bayonet in the corner of his eye. Then he felt it in his side." 
    "Gasping in pain, he fell to the ground."
    
    hide blood
    show battle behind ikkuna
    
    "He saw the foe being cut down by Flayesians."
    
    show vassan smile at leftPos2
    
    "He smiled."
    "He was a hero now. For as long as he lived, he could boast of this day. From now on he would always belong."
    "He was in incredible pain but smiled none the less. He wouldn`t die."
    "There was so much he still had to do."
    "Not now, on the moment of victory. He wouldn`t die."
    v "Eugenie..."
    "He whispered, wishing he could see her dance in the blue dress again."
    
    hide vassan with dissolve
    
    "Then he died."
    
    hide battle with dissolve
    show battle behind ikkuna with dissolve
    
    "The enemy was chased almost until sundown." 
    "When the chase finally ended, the fields were red for miles around." 
    "The enemy had been beaten. For the first time in years, their bloody revolution had been pushed back." 
    "No one had thought it was possible." 
    "But the price was heavy. Only one in two of those who left came back, half of them in carts."
    "Wazu was the one to find Vassan. With the loyalty of a battle comrade, he stayed with him until the corpse wagons came." 
    
    show memnon serious at rightPos2 with dissolve
    
    "He met Memnon." 
    w"The boy fought well. He would have made a great warrior." 
    "Memnon gave no reply." 
    "There was a tear in his eye." 
    w"Are you leaving?" 
    "Memnon nodded again." 
    m"I couldn`t stay here." 
    m"We`re a week away from where the Yribid Empire once was. I`ll return home." 
    "Wazu nodded" 
    w"Many here would see you as king." 
    m"And many others would hang me, and rightfully so." 
    m"How could I rule those who suffered so much on my account? Any idea who will?"
    "Wazu shrugged." 
    w"Admiral Hulegu fell while fleeing like the rat he was." 
    w"Many of the slaves were once my people. They`ll never be slaves again. I imagine they would take me back." 
    w"Even though they too have suffered, largely on my account."
    w"They make up the majority, I believe."
    w"This is good land. I imagine we`ll build a village on the hill where the battle was fought."
    
    show memnon normal at rightPos2
    play music "musiikki/waltz2.ogg"
    
    "Memnon smiled." 
    m"Then I wish your majesty good fortune. And your city as well."
    w" And I give you my royal pardon. It saddens me that you won`t stay to help us, though I can hardly blame you."
    m"If they ask around, tell them I died fighting. Best for everyone."
    "Wazu nodded."
    
    show memnon serious at rightPos2
    
    "And so Memnon rode away. He couldn`t bear to look on Vassan`s body."
    
    show eugenie happy at leftPos2 with dissolve
    
    "On the way, he met Eugenie, who was escorting a wounded young man." 
    "She was all smiles and giggles and held the young man`s hand." 
    m"Goodbye, Eugenie!" 
    "She was so enamored by her new acquittance, she didn`t even notice him. Perhaps it was for the best."
    
    hide eugenie with dissolve
    
    "Memnon shook his head, took one last look at the camp, and its people, finally free of danger, and guided his horse towards the sunset."
    "The people of Flayes had found a new home. It was time he went back to his."
   
    hide memnon with dissolve
    hide battle with dissolve
    show end behind ikkuna with dissolve
    pause 5.0
    hide end with dissolve
    window hide ##pois itch io
    hide ikkuna with dissolve
    stop music fadeout 2.0
    
    ##"Thank you for reading! Would you like to support us by making a donation? (Yes brings you to the donation page)"
    
    ##menu:
    ##    "Yes":
    ##        "Awesome! We are eternally grateful!"
    ##        window hide
    ##        show screen donate
    ##        pause
    ##    "No":
    ##        "It's okay. We understand! You reading to the end is more than we could ask for."

