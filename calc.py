from appJar import gui
app = gui("Coin Calculator","600x480")

#650c = 500kk
#x = 70

#500*90 / 650
#Exg coin to Gold and Gold to coin

def calculate_exg(button):
    if button == "Quit":
        app.stop()
    else:
        coin = app.getEntry("Coin") #getting coin and gold values in the entries
        gold = app.getEntry("Gold")
        if app.getRadioButton("Exg") == "Coin to Gold": #getting radio button value
            exg = round((coin*500/650),2),"K"
        elif app.getRadioButton("Exg") == "Gold to Coin":
            exg = round((gold*650/500),2),"C"
        app.setLabel("l1",exg)
            

def addOrRemove(btn):
    if app.getEntry("Coin") is None:
        app.setEntry("Coin",0)
    if app.getEntry("Gold") is None:
        app.setEntry("Gold",0)
    
    if btn == "+100C":
        app.setEntry("Coin",app.getEntry("Coin") + 100)
    elif btn == "+10C":
        app.setEntry("Coin",app.getEntry("Coin") + 10)
    elif btn == "-100C":
        app.setEntry("Coin",app.getEntry("Coin") - 100)
    elif btn == "-10C":
        app.setEntry("Coin",app.getEntry("Coin") - 10)
    elif btn == "+100G":
        app.setEntry("Gold",app.getEntry("Gold") + 100)
    elif btn == "+10G":
        app.setEntry("Gold",app.getEntry("Gold") + 10)
    elif btn == "-100G":
        app.setEntry("Gold",app.getEntry("Gold") - 100)
    elif btn == "-10G":
        app.setEntry("Gold",app.getEntry("Gold") - 10)
 

app.startTabbedFrame("Coin Calculator")
app.startTab("Exchange")   
app.setBg("lightBlue")

app.addLabel("Title","Welcome to Priston Coin Calc")

#Coin Area: Plus and Minus buttons and entry field
app.startFrame("TopL",row=1,column=0)
app.addLabel("CoinL","Coin")
app.stopFrame()
app.startFrame("Top",row=2,column=0)
app.startFrame("Top0",row=2,column=0)
app.addButton("+100C",addOrRemove)
app.stopFrame()
app.startFrame("Top1",row=2,column=1)
app.addButton("+10C",addOrRemove)
app.stopFrame()
app.startFrame("Top2",row=2,column=2)
app.addLabelNumericEntry("Coin")
app.setEntry("Coin",0)
app.setLabel("Coin","")
app.stopFrame()
app.startFrame("Top3",row=2,column=3)
app.addButton("-10C",addOrRemove)
app.stopFrame()
app.startFrame("Top4",row=2,column=4)
app.addButton("-100C",addOrRemove)
app.stopFrame()
app.stopFrame()

#Gold Area: Plus and Minus buttons and entry field
app.startFrame("LabelMid",row=3,column=0)
app.addLabel("GoldL","Gold")
app.stopFrame()

app.startFrame("Mid",row=4,column=0)
app.startFrame("Mid0",row=4,column=0)
app.addButton("+100G",addOrRemove)
app.stopFrame()
app.startFrame("Mid01",row=4,column=1)
app.addButton("+10G",addOrRemove)
app.stopFrame()
app.startFrame("Mid02",row=4,column=2)
app.addLabelNumericEntry("Gold")
app.setEntry("Gold",0)
app.setLabel("Gold","")
app.setEntryBg("Gold","Gold")
app.stopFrame()
app.startFrame("Mid03",row=4,column=3)
app.addButton("-10G",addOrRemove)
app.stopFrame()
app.startFrame("Mid04",row=4,column=4)
app.addButton("-100G",addOrRemove)
app.stopFrame()
app.stopFrame()

app.startLabelFrame("Exchange Currency")
app.addRadioButton("Exg","Coin to Gold")
app.addRadioButton("Exg","Gold to Coin")
app.stopLabelFrame()


app.addLabel("l1","")
app.setLabelBg("l1","Green")

app.addButtons(["Calculate","Quit"],calculate_exg)

app.stopTab()
app.startTab("History")
app.addLabel("History Here")
app.stopTab()
app.stopTabbedFrame()



app.go()


