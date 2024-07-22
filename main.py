#Coin Calculator by Gaspar Lourenço

from appJar import gui
import datetime


app = gui("Coin Calculator","600x480")

#650c = 500kk

coinRate = 650
goldRate = 500


ratesFile = "ExchangeRates.txt"

historyPath = "History.txt"

def init(): #Initializes the rates and history .txt files and initializes the rates


    file = open(ratesFile,"a")
    file.close()
    file = open(historyPath,"a")
    file.close()

    LoadRates()
    ReadHistory()




def CalculateExg(button): #Function to handle the calculate button

    curr = ""
    value = 0 

    if button == "Quit":
        app.stop()



    else:
        coin = app.getEntry("Coin") #getting coin and gold values in the entries

        gold = app.getEntry("Gold")
        
        if app.getRadioButton("Exg") == "Coin to Gold": #getting radio button value
            


            if(coin == 0):


                app.errorBox("Invalid","Coin Exchange Value cannot be 0 for this operation. Change settings in the options menu.")
                return



            exg = round((coin*goldRate/coinRate),2)

            curr="KK" #currency to be added to label


            value = coin

        elif app.getRadioButton("Exg") == "Gold to Coin":
            


            if(gold == 0):


                app.errorBox("Invalid","Gold Exchange Value cannot be 0 for this operation. Change settings in the options menu.")
                return



            exg = round(gold*coinRate/goldRate,2)


            value = gold

            curr="C"


        lblMsg = exg,curr #adding the Label msg
        AddToHistory(coinRate,goldRate,value,exg,curr)
        app.setLabel("l1",lblMsg)

        ReadHistory()
            

def AddToHistory(cRate,gRate,value,exg,x): #Adds this exchange to the history tab and file
    file = open(historyPath,"a")

    if(x == "KK"):


        file.write(f"Coin Rate: {cRate}, Gold Rate: {gRate}\nCoin Value: {value}C = {exg}{x} || Date: {datetime.datetime.now().strftime("%x")} {datetime.datetime.now().strftime("%X")}\n-----\n")

    else:


        file.write(f"Coin Rate: {cRate}, Gold Rate: {gRate}\nGold Value: {value}K = {exg}{x} || Date: {datetime.datetime.now().strftime("%x")} {datetime.datetime.now().strftime("%X")}\n-----\n")

    file.close()

def ReadHistory(): #Reads from the history file and updates history tab

    file = open(historyPath,"r")

    history = file.read()

    app.setLabel("History",history)
        
def AddOrRemove(btn): #Handles add or remove gold/coin buttons

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
 



def SaveRates(btn): #Saves the rates from the options menu and sets the global rate value to be used in the app
    global coinRate
    global goldRate
    
    coinVal = app.getEntry("CoinRate")
    goldVal = app.getEntry("GoldRate")
    UpdateRates(coinVal,goldVal)
    coinRate,goldRate = LoadRates()
    SetRatesEntries("CoinRate","GoldRate")
    app.infoBox("Saved",f"Coin Rate: {coinRate}, Gold Rate: {goldRate} saved succesfully!")



def UpdateRates(coin,gold): #Updates the rates file with the new rates.

    file = open(ratesFile,"w")
    file.write(str(coin) + "\n")
    file.write(str(gold))
    file.close()
    


def LoadRates(): #reads the values from the files
    global coinRate
    global goldRate
    
    file = open(ratesFile,"r")
    
    if(file.read() != '' ):
        file.seek(0,0)
        
        coinRate = float(file.readline())
        goldRate = float(file.readline())


    file.close()
    
    SetRatesEntries("CoinRate","GoldRate")
    return coinRate,goldRate
    

def SetRatesEntries(cEntry,gEntry):  #Sets the rates entries with the according values from the file.
    app.setEntry(cEntry,coinRate)

    app.setEntry(gEntry,goldRate)



def ClearHistory(): #Clear history from history tab and file
    file = open(historyPath,"w")
    file.close()
    ReadHistory()


#Start of the app GUI

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

app.addButton("+100C",AddOrRemove)

app.stopFrame()

app.startFrame("Top1",row=2,column=1)

app.addButton("+10C",AddOrRemove)

app.stopFrame()

app.startFrame("Top2",row=2,column=2)

app.addLabelNumericEntry("Coin")

app.setEntry("Coin",0)

app.setLabel("Coin","")

app.stopFrame()

app.startFrame("Top3",row=2,column=3)

app.addButton("-10C",AddOrRemove)

app.stopFrame()

app.startFrame("Top4",row=2,column=4)

app.addButton("-100C",AddOrRemove)

app.stopFrame()

app.stopFrame()

#Gold Area: Plus and Minus buttons and entry field

app.startFrame("LabelMid",row=3,column=0)

app.addLabel("GoldL","Gold(KK)")

app.stopFrame()

app.startFrame("Mid",row=4,column=0)

app.startFrame("Mid0",row=4,column=0)

app.addButton("+100G",AddOrRemove)

app.stopFrame()

app.startFrame("Mid01",row=4,column=1)

app.addButton("+10G",AddOrRemove)

app.stopFrame()

app.startFrame("Mid02",row=4,column=2)

app.addLabelNumericEntry("Gold")

app.setEntry("Gold",0)

app.setLabel("Gold","")

app.setEntryBg("Gold","Gold")

app.stopFrame()

app.startFrame("Mid03",row=4,column=3)

app.addButton("-10G",AddOrRemove)

app.stopFrame()

app.startFrame("Mid04",row=4,column=4)

app.addButton("-100G",AddOrRemove)

app.stopFrame()

app.stopFrame()

app.startLabelFrame("Exchange Currency")

app.addRadioButton("Exg","Coin to Gold")

app.addRadioButton("Exg","Gold to Coin")

app.stopLabelFrame()

app.addLabel("l1","")

app.setLabelBg("l1","Green")

app.addButtons(["Calculate","Quit"],CalculateExg)




#History Tab -> Shows past exchange rates.

app.stopTab()

app.startTab("History")

app.addLabel("Exchange History")

app.setLabelBg("Exchange History","Yellow")

app.startScrollPane("Pane")

app.addLabel("History")

app.stopScrollPane()

app.stopTab()



#Options tab. Manage history and Exchange Rate

app.startTab("Options")

app.startLabelFrame("Rates")

app.startFrame("Exchange Rate",row=0,column=0)

app.addLabelNumericEntry("CoinRate")

app.setEntry("CoinRate",coinRate)

app.setLabel("CoinRate","Coin Rate")

app.stopFrame()

app.startFrame("Rate1",row=0,column=1)

app.addLabel("Equals","=",row=None,column=3)

app.setLabelFont("Equals",16)

app.stopFrame()

app.startFrame("Rate2",row=0,column=5)

app.addLabelNumericEntry("GoldRate")

app.setEntry("GoldRate",goldRate)

app.setLabel("GoldRate","Gold Rate")

app.stopFrame()

app.addButton("Save",SaveRates,row=None,column=1)

app.stopLabelFrame()

app.addButton("Clear History",ClearHistory)

app.stopTab()

app.stopTabbedFrame()

init() #Initialization of default values
app.go() #Starting the GUI






