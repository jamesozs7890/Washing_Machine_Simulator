import tkinter.font
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

# colors
MSGREEN = "#3cb371"
GWHITE = '#F1F1F0'
TGRAY = '#ADA9AD'
LGRAY = '#353941'
DGRAY = '#262B2B'

# Window's Properties
root.geometry("810x750")
root.title("Industrial Washing Machine")
root.resizable(False, False)
root.configure(bg=DGRAY)

# Variables
s1TimeCount = tkinter.IntVar()
s1TimeCount.set(5)

s2TimeCount = tkinter.IntVar()
s2TimeCount.set(5)

s3TimeCount = tkinter.IntVar()
s3TimeCount.set(5)

wValveTime = StringVar()
wValveTime.set("0")
dValveTime = StringVar()
dValveTime.set("0")

hour = StringVar()
hour.set(0)
minute = StringVar()
minute.set(0)
second = StringVar()
second.set(0)

confirmS1Time = tkinter.IntVar()
confirmS2Time = tkinter.IntVar()
confirmS3Time = tkinter.IntVar()

isOff = True
countDown = False

# Images
powerOnIcon = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\PowerButtonOn.png")
smallPowerOnIcon = powerOnIcon.subsample(8, 8)

powerOffIcon = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\PowerButton.png")
smallPowerOffIcon = powerOffIcon.subsample(8, 8)

resetIcon = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\resetButtonWhite.png")
smallResetIcon = resetIcon.subsample(12, 12)
startIcon = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\startButtonWhite.png")
smallStartIcon = startIcon.subsample(12, 12)

eStop = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\emergencyStop.png")
smalleStop = eStop.subsample(8, 8)
contProcess = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\continueButton.png")
smallcontProcess = contProcess.subsample(8, 8)

wValveOpen1 = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\wValveOpen1.png")
smallwValveOpen1 = wValveOpen1.subsample(5, 5)
wValveOpen2 = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\wValveOpen2.png")
smallwValveOpen2 = wValveOpen2.subsample(5, 5)
wValveOpen3 = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\wValveOpen3.png")
smallwValveOpen3 = wValveOpen3.subsample(5, 5)

wValveClose = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\wValveClose.png")
smallwValveClosed = wValveClose.subsample(5, 5)

dValveOpen1 = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\DetergentOpen1.png")
smalldValveOpen1 = dValveOpen1.subsample(5, 5)
dValveOpen2 = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\DetergentOpen2.png")
smalldValveOpen2 = dValveOpen2.subsample(5, 5)
dValveOpen3 = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\DetergentOpen3.png")
smalldValveOpen3 = dValveOpen3.subsample(5, 5)

dValveClose = PhotoImage(
    file=r"C:\Users\James\Desktop\Bachelor's Sem 2\Programming for IS\Assignment\Images\DetergentClosed.png")
smalldValveClosed = dValveClose.subsample(5, 5)

# font
print(tkinter.font.names())

hFont = tkinter.font.nametofont('TkHeadingFont')
hFont.config(size=18)
sFont = tkinter.font.nametofont("TkDefaultFont")
sFont.config(size=15)
titleFont = tkinter.font.nametofont("TkMenuFont")
titleFont.config(size=30, weight=tkinter.font.BOLD)
subtitleFont = tkinter.font.nametofont("fixed")
subtitleFont.config(size=15, weight=tkinter.font.BOLD)
detailFont = tkinter.font.nametofont("ansifixed")
detailFont.configure(size=12)


# functions
def power():
    global isOff
    global countDown

    if isOff:
        StartButton.configure(state='normal')
        ResetButton.configure(state='normal')
        modeList.configure(state='readonly')
        detergentList.configure(state='readonly')
        s1PlusButton.configure(state='normal')
        s1MinusButton.configure(state='normal')
        s2PlusButton.configure(state='normal')
        s2MinusButton.configure(state='normal')
        s3PlusButton.configure(state='normal')
        s3MinusButton.configure(state='normal')

        additionalInfoLabel.configure(text="Informative advices will be stated here.")

        PowerButton.configure(image=smallPowerOnIcon)

        isOff = False
    else:
        pOff = messagebox.askquestion("Power Off", "Press 'Yes' to confirm power off.")

        if pOff == "yes":
            countDown = False

            StartButton.configure(state='disable')
            ResetButton.configure(state='disable')
            modeList.configure(state='disable')
            detergentList.configure(state='disable')
            s1PlusButton.configure(state='disable')
            s1MinusButton.configure(state='disable')
            s2PlusButton.configure(state='disable')
            s2MinusButton.configure(state='disable')
            s3PlusButton.configure(state='disable')
            s3MinusButton.configure(state='disable')
            StopButton.configure(state="disabled")

            selectedM.set("Select a Mode")
            selectedD.set("Select a Detergent")
            s1TimeCount.set(5)
            s2TimeCount.set(5)
            s3TimeCount.set(5)

            selectedMode.configure(text="Awaiting Selection")
            selectedDetergent.configure(text="Awaiting Selection")

            confirmS1Time.set(0)
            confirmS2Time.set(0)
            confirmS3Time.set(0)

            dValveTime.set(0)
            wValveTime.set(0)

            second.set(0)
            minute.set(0)
            hour.set(0)

            additionalInfoLabel.configure(text="Machine Offline")

            PowerButton.configure(image=smallPowerOffIcon)
            isOff = True
        else:
            pass


# Stage 1's Buttons
def s1TimeIncrease():
    if s1TimeCount.get() >= 25:
        messagebox.showwarning("Maximum Value Reached", "The maximum amount of time for washing is 25 minutes only")
        s1TimeCount.set(25)
    else:
        s1TimeCount.set(s1TimeCount.get() + 5)


def s1TimeDecrease():
    if s1TimeCount.get() <= 5:
        messagebox.showwarning("Minimum Value has reached", "The minimum amount of time for washing is 5 minutes")
        s1TimeCount.set(5)
    else:
        s1TimeCount.set(s1TimeCount.get() - 5)


# Stage 2's Buttons
def s2TimeIncrease():
    if s2TimeCount.get() >= 25:
        messagebox.showwarning("Maximum Value Reached", "The maximum amount of time for rinsing is 25 minutes only")
        s2TimeCount.set(25)
    else:
        s2TimeCount.set(s2TimeCount.get() + 5)


def s2TimeDecrease():
    if s2TimeCount.get() <= 5:
        messagebox.showwarning("Minimum Value has reached", "The minimum amount of time for rinsing is 5 minutes")
        s2TimeCount.set(5)
    else:
        s2TimeCount.set(s2TimeCount.get() - 5)


# Stage 3's Buttons
def s3TimeIncrease():
    if s3TimeCount.get() >= 25:
        messagebox.showwarning("Maximum Value Reached", "The maximum amount of time for spinning is 25 minutes only")
        s3TimeCount.set(25)
    else:
        s3TimeCount.set(s3TimeCount.get() + 5)


def s3TimeDecrease():
    if s3TimeCount.get() <= 5:
        messagebox.showwarning("Minimum Value has reached", "The minimum amount of time for spinning is 5 minutes")
        s3TimeCount.set(5)
    else:
        s3TimeCount.set(s3TimeCount.get() - 5)


# Start function
def start():
    global countDown
    global isOff

    if modeList.get() == "Select a Mode" or detergentList.get() == "Select a Detergent":
        if modeList.get() != "Select a Mode" and detergentList.get() == "Select a Detergent":
            messagebox.showerror("Error", "Detergent not selected")
        elif modeList.get() == "Select a Mode" and detergentList.get() != "Select a Detergent":
            messagebox.showerror("Error", "Mode not selected")
        else:
            messagebox.showerror("Error", "Mode and Detergent not selected")
    else:
        startOp = messagebox.askquestion("Start Confirmation", "Are you sure you want to start?")
        if startOp == 'yes':
            countDown = True
            additionalInfoLabel.configure(text="Washing machine is running.\nPlease wait until the time is up.")
            StartButton.configure(state='disable')
            ResetButton.configure(state='disable')
            PowerButton.configure(state='disable')
            modeList.configure(state='disable')
            detergentList.configure(state='disable')
            s1PlusButton.configure(state='disable')
            s1MinusButton.configure(state='disable')
            s2PlusButton.configure(state='disable')
            s2MinusButton.configure(state='disable')
            s3PlusButton.configure(state='disable')
            s3MinusButton.configure(state='disable')

            confirmS1Time.set(s1TimeCount.get())
            confirmS2Time.set(s2TimeCount.get())
            confirmS3Time.set(s3TimeCount.get())

            StopButton.configure(state='normal')

            selectedMode.configure(text=modeList.get())
            selectedDetergent.configure(text=detergentList.get())

            doorState.configure(text='LOCKED')

            dValveTime.set(3)
            dValveTCount = int(dValveTime.get())

            wValveTime.set(5)
            wValveTCount = int(wValveTime.get())

            confS1Time = int(confirmS1Time.get())
            confS2Time = int(confirmS2Time.get())
            confS3Time = int(confirmS3Time.get())

            secondTCount = dValveTCount + wValveTCount + (confS1Time*60) + (confS2Time*60) + (confS3Time*60)
            minuteTCount = int()
            hourTCount = int()

            while secondTCount >= 60:
                secondTCount -= 60
                minuteTCount += 1

            while minuteTCount >= 60:
                minuteTCount -= 60
                hourTCount += 1

            second.set(secondTCount)
            minute.set(minuteTCount)
            hour.set(hourTCount)

            while minuteTCount > 0 or secondTCount > 0 or hourTCount > 0:

                while dValveTCount > 0:
                    if countDown:
                        root.update()
                        time.sleep(1)

                        dCloseText.configure(text='Opened')

                        if dValveTCount == 3:
                            dImage.configure(image=smalldValveOpen1)
                        elif dValveTCount == 2:
                            dImage.configure(image=smalldValveOpen2)
                        elif dValveTCount == 1:
                            dImage.configure(image=smalldValveOpen3)

                        dValveTCount -= 1
                        dValveTime.set(dValveTCount)

                        if minuteTCount < 0:
                            minuteTCount += 60
                            hourTCount -= 1
                        if secondTCount < 1:
                            secondTCount += 60
                            minuteTCount -= 1
                        secondTCount -= 1
                        hour.set(hourTCount)
                        minute.set(minuteTCount)
                        second.set(secondTCount)
                    else:
                        break
                dImage.configure(image=smalldValveClosed)
                dCloseText.configure(text='Closed')

                while wValveTCount > 0:

                    root.update()
                    time.sleep(1)

                    if countDown:
                        wCloseText.configure(text='Opened')

                        if wValveTCount == 5 or wValveTCount == 2:
                            wImage.configure(image=smallwValveOpen1)
                        elif wValveTCount == 4 or wValveTCount == 1:
                            wImage.configure(image=smallwValveOpen2)
                        elif wValveTCount == 3:
                            wImage.configure(image=smallwValveOpen3)

                        wValveTCount -= 1
                        wValveTime.set(wValveTCount)

                        if minuteTCount < 0:
                            minuteTCount += 60
                            hourTCount -= 1
                        if secondTCount < 1:
                            secondTCount += 60
                            minuteTCount -= 1

                        secondTCount -= 1

                        hour.set(hourTCount)
                        minute.set(minuteTCount)
                        second.set(secondTCount)
                    else:
                        break
                wImage.configure(image=smallwValveClosed)
                wCloseText.configure(text='Closed')

                while confS1Time >= 0:

                    if countDown:
                        R1.select()
                        R1.configure(state='active', activebackground=DGRAY, activeforeground=MSGREEN, fg=GWHITE)

                        root.update()
                        time.sleep(0.01)

                        if (minuteTCount < confS2Time + confS3Time or minuteTCount == 0) and hourTCount > 0:
                            confS1Time = int((60+minuteTCount)-confS2Time-confS3Time)
                        else:
                            confS1Time = minuteTCount - confS2Time - confS3Time

                        if minuteTCount < 0:
                            minuteTCount += 60
                            hourTCount -= 1
                        if secondTCount < 1:
                            secondTCount += 60
                            minuteTCount -= 1
                            confS1Time -= 1

                        secondTCount -= 1

                        hour.set(hourTCount)
                        minute.set(minuteTCount)
                        second.set(secondTCount)

                        if confS1Time == 0:
                            confirmS1Time.set("<1")
                        elif confS1Time < 0:
                            confirmS1Time.set(0)
                        else:
                            confirmS1Time.set(confS1Time)
                    else:
                        break
                R1.deselect()
                R1.configure(state='disabled')

                while confS2Time >= 0:

                    if countDown:
                        R2.select()
                        R2.configure(state='active', activebackground=DGRAY, activeforeground=MSGREEN, fg=GWHITE)

                        root.update()
                        time.sleep(0.01)

                        if minuteTCount < 0:
                            minuteTCount += 60
                            hourTCount -= 1
                        if secondTCount < 1:
                            secondTCount += 60
                            minuteTCount -= 1

                        secondTCount -= 1
                        hour.set(hourTCount)
                        minute.set(minuteTCount)
                        second.set(secondTCount)

                        confS2Time = minuteTCount - confS3Time
                        if confS2Time == 0:
                            confirmS2Time.set("<1")
                        elif confS2Time < 0:
                            confirmS2Time.set(0)
                        else:
                            confirmS2Time.set(confS2Time)
                    else:
                        break
                R2.deselect()
                R2.configure(state='disabled')

                while secondTCount >= 0:

                    if countDown:
                        R3.select()
                        R3.configure(state='active', activebackground=DGRAY, activeforeground=MSGREEN, fg=GWHITE)

                        root.update()
                        time.sleep(0.01)

                        if minuteTCount < 0 < hourTCount:
                            minuteTCount += 60
                            hourTCount -= 1
                        if secondTCount < 1 and minuteTCount > 0:
                            secondTCount += 60
                            minuteTCount -= 1

                        secondTCount -= 1

                        confS3Time = minuteTCount

                        if confS3Time == 0:
                            confirmS3Time.set("<1")
                        else:
                            confirmS3Time.set(confS3Time)

                        hour.set(hourTCount)
                        minute.set(minuteTCount)

                        if secondTCount < 0:
                            confirmS3Time.set(0)
                            second.set(0)
                        else:
                            second.set(secondTCount)
                    else:
                        break
                R3.deselect()
                R3.configure(state='disabled')

            repeat = messagebox.askquestion("Finished", "The process is all done!\nThe door is unlocked.\nWould you like to repeat?")

            if repeat == 'yes':

                StartButton.configure(state='normal')
                ResetButton.configure(state='normal')
                PowerButton.configure(state='normal')
                modeList.configure(state='readonly')
                detergentList.configure(state='readonly')
                s1PlusButton.configure(state='normal')
                s1MinusButton.configure(state='normal')
                s2PlusButton.configure(state='normal')
                s2MinusButton.configure(state='normal')
                s3PlusButton.configure(state='normal')
                s3MinusButton.configure(state='normal')
                StopButton.configure(state='disabled')
                ContinueButton.configure(state='disabled')

                doorState.configure(text='UNLOCKED')

                selectedM.set("Select a Mode")
                selectedD.set("Select a Detergent")
                s1TimeCount.set(5)
                s2TimeCount.set(5)
                s3TimeCount.set(5)

                selectedMode.configure(text="Awaiting Selection")
                selectedDetergent.configure(text="Awaiting Selection")

                confirmS1Time.set(0)
                confirmS2Time.set(0)
                confirmS3Time.set(0)

                dValveTime.set(0)
                wValveTime.set(0)

                second.set(0)
                minute.set(0)
                hour.set(0)

                additionalInfoLabel.configure(text="Informative advices will be stated here.")
            else:
                countDown=False

                StartButton.configure(state='disable')
                ResetButton.configure(state='disable')
                modeList.configure(state='disable')
                detergentList.configure(state='disable')
                s1PlusButton.configure(state='disable')
                s1MinusButton.configure(state='disable')
                s2PlusButton.configure(state='disable')
                s2MinusButton.configure(state='disable')
                s3PlusButton.configure(state='disable')
                s3MinusButton.configure(state='disable')
                StopButton.configure(state="disabled")

                selectedM.set("Select a Mode")
                selectedD.set("Select a Detergent")
                s1TimeCount.set(5)
                s2TimeCount.set(5)
                s3TimeCount.set(5)

                selectedMode.configure(text="Awaiting Selection")
                selectedDetergent.configure(text="Awaiting Selection")

                confirmS1Time.set(0)
                confirmS2Time.set(0)
                confirmS3Time.set(0)

                dValveTime.set(0)
                wValveTime.set(0)

                second.set(0)
                minute.set(0)
                hour.set(0)

                doorState.configure(text="UNLOCKED")

                additionalInfoLabel.configure(text="Machine Offline")

                PowerButton.configure(image=smallPowerOffIcon, state='normal')
                isOff = True
        else:
            pass


# Resume Function
def cont():
    global countDown

    continueWashing = messagebox.askquestion("Continue?", "Are you sure you want to continue?")

    if continueWashing == 'yes':
        countDown = True
        StopButton.configure(state='normal')
        ResetButton.configure(state='disabled')
        ContinueButton.configure(state='disabled')
        doorState.configure(text="LOCKED")
        additionalInfoLabel.configure(text="Continued.Washing machine is running.\nPlease wait until the time is up.")
    else:
        countDown = False


# Reset Function
def reset():
    global countDown
    countDown = False
    root.update()
    PowerButton.configure(state='normal')
    StartButton.configure(state='normal')
    modeList.configure(state='readonly')
    detergentList.configure(state='readonly')
    s1PlusButton.configure(state='normal')
    s1MinusButton.configure(state='normal')
    s2PlusButton.configure(state='normal')
    s2MinusButton.configure(state='normal')
    s3PlusButton.configure(state='normal')
    s3MinusButton.configure(state='normal')
    ContinueButton.configure(state='disabled')
    wImage.configure(image=smallwValveClosed)
    dImage.configure(image=smalldValveClosed)

    selectedM.set("Select a Mode")
    selectedD.set("Select a Detergent")
    s1TimeCount.set(5)
    s2TimeCount.set(5)
    s3TimeCount.set(5)

    selectedMode.configure(text="Awaiting Selection")
    selectedDetergent.configure(text="Awaiting Selection")

    confirmS1Time.set(0)
    confirmS2Time.set(0)
    confirmS3Time.set(0)

    dValveTime.set(0)
    wValveTime.set(0)

    second.set(0)
    minute.set(0)
    hour.set(0)

    additionalInfoLabel.configure(text="Informative advices will be stated here.")


# Stop Function
def stop():
    global countDown
    emergency = messagebox.askquestion("Stop Confirmation", "Stop immediately?")

    if emergency == 'yes':
        countDown = False

        ResetButton.configure(state='normal')
        ContinueButton.configure(state='normal')
        StopButton.configure(state="disabled")

        additionalInfoLabel.configure(text="You've stopped the washing process.\nPress continue to proceed with the process or reset to start over.")

        R1.configure(state='disabled')
        R2.configure(state='disabled')
        R3.configure(state='disabled')

        doorState.configure(text='UNLOCKED')

    while not countDown:
        root.after(1000)
        root.update()


# Mode Select Function
def modeSelect(event):
    selected = event.widget.get()

    action = additionalInfoLabel.configure(text="The timer setting is automatically set to recommended value.\nBut you can still adjust to your own preferred timer setting.")
    if selected == "Fast":
        s1TimeCount.set(5)
        s2TimeCount.set(5)
        s3TimeCount.set(15)
        action
    elif selected == "Normal":
        s1TimeCount.set(15)
        s2TimeCount.set(10)
        s3TimeCount.set(25)
        action
    elif selected == "Heavy Cycle":
        s1TimeCount.set(20)
        s2TimeCount.set(15)
        s3TimeCount.set(25)
        action
    else:
        s1TimeCount.set(5)
        s2TimeCount.set(5)
        s3TimeCount.set(5)


# Widgets Declaration
frame = Frame(root, relief='sunken', bd=0, bg=DGRAY)
TFrame = Frame(frame, relief='flat', bd=0, padx=5, pady=5, bg=DGRAY)
Lframe = Frame(frame, relief='sunken', bd=2, padx=10, pady=30, bg=LGRAY)
tRframe = Frame(frame, relief='sunken', bd=2, padx=42, pady=5, bg=LGRAY)
BLFrame = Frame(frame, relief='flat', bd=0, padx=5, pady=15, bg=DGRAY)
BRFrame = Frame(frame, relief='flat', bd=0, padx=5, pady=15, bg=DGRAY)

detailFrame = LabelFrame(frame, text="Selection Details", relief="sunken", bd=2, bg=DGRAY, fg=GWHITE, pady=10, font=subtitleFont)

hourFrame = LabelFrame(TFrame, text="Hour", font=detailFont, bg=DGRAY, fg=GWHITE, labelanchor='n', relief="sunken")
minuteFrame = LabelFrame(TFrame, text="Minute", font=detailFont, bg=DGRAY, fg=GWHITE, labelanchor='n', relief="sunken")
secondFrame = LabelFrame(TFrame, text="Second", font=detailFont, bg=DGRAY, fg=GWHITE, labelanchor='n', relief="sunken")

DisplayPanel = LabelFrame(frame, text="Door", relief='sunken', labelanchor='n', width=20, bd=2, bg=DGRAY, fg=GWHITE, padx=15, pady=20, font=subtitleFont)

infoFrame = LabelFrame(frame, text="Additional Information", font=subtitleFont, bg=DGRAY, fg=GWHITE, relief="sunken")

# Labels
welcome = Label(frame, text="Welcome!", font=titleFont, bg=DGRAY, fg=GWHITE)

mSetting = Label(Lframe, text="Mode Setting", font=hFont, bg=LGRAY, fg=GWHITE)
dSelection = Label(Lframe, text="Detergent Selection", font=hFont, bg=LGRAY, fg=GWHITE)
tSetting = Label(Lframe, text="Timer Setting", font=hFont, bg=LGRAY, fg=GWHITE)

sOne = Label(Lframe, text="Washing", font=sFont, bg=LGRAY, fg=GWHITE, justify='left')
sTwo = Label(Lframe, text="Rinsing", font=sFont, bg=LGRAY, fg=GWHITE, justify='left')
sThree = Label(Lframe, text="Spinning", font=sFont, bg=LGRAY, fg=GWHITE, justify='left')

wValve = Label(tRframe, text="Water Valve", font=hFont, padx=10, pady=3, bg=LGRAY, fg=GWHITE)
wImage = Label(tRframe, padx=10, pady=15, bg=LGRAY, image=smallwValveClosed)
dValve = Label(tRframe, text="Detergent Valve", font=hFont, padx=10, pady=3, bg=LGRAY, fg=GWHITE)
dImage = Label(tRframe, padx=10, pady=15, bg=LGRAY, image=smalldValveClosed)

wCloseText = Label(tRframe, text='Closed', font=sFont, bg=LGRAY, fg=GWHITE)
dCloseText = Label(tRframe, text='Closed', font=sFont, bg=LGRAY, fg=GWHITE)

selectedModeLabel = Label(detailFrame, text=" Mode:", font=detailFont, bg=DGRAY, fg=GWHITE)
selectedMode = Label(detailFrame, text="Awaiting Selection", font=detailFont, bg=DGRAY, fg=GWHITE, width=18, anchor='w')
selectedDetergentLabel = Label(detailFrame, text=" Detergent:", font=detailFont, bg=DGRAY, fg=GWHITE)
selectedDetergent = Label(detailFrame, text="Awaiting Selection", font=detailFont, bg=DGRAY, fg=GWHITE, width=18, anchor='w')
stage = Label(detailFrame, text='Stage:', font=detailFont, bg=DGRAY, fg=GWHITE)
timer = Label(detailFrame, text='Timer:', font=detailFont, bg=DGRAY, fg=GWHITE)

space = Label(frame, text=" ", bg=DGRAY, padx=10)
space1 = Label(TFrame, text=" ", bg=DGRAY, width=10)

doorState = Label(DisplayPanel, text='UNLOCKED', font=detailFont, bg=DGRAY, fg=GWHITE, width=10, justify='center')

additionalInfoLabel = Label(infoFrame, text="Machine Offline", font=detailFont, bg=DGRAY, fg=GWHITE, justify='left', height=2)

# Combobox
selectedM = StringVar()
modeList = ttk.Combobox(Lframe, width=20, textvariable=selectedM, state='disabled', justify='center', font=sFont)
modeList['values'] = ('Select a Mode', 'Fast', 'Normal', 'Heavy Cycle')
modeList.bind('<<ComboboxSelected>>', modeSelect)

selectedD = StringVar()
detergentList = ttk.Combobox(Lframe, width=20, textvariable=selectedD, state='disabled', justify='center', font=sFont)
detergentList['values'] = ('Select a Detergent', 'Ajax', 'Tide', 'Top')

# Buttons
PowerButton = Button(TFrame, text="Power Up", image=smallPowerOffIcon, relief=FLAT,
                     border=0, command=power, bg=DGRAY, fg=DGRAY, activebackground=DGRAY)
StartButton = Button(BRFrame, text="Play/Pause", image=smallStartIcon, relief=FLAT, state='disabled',
                     border=0, command=start, bg=DGRAY, fg=DGRAY, activebackground=DGRAY)
ResetButton = Button(BRFrame, text="Reset", image=smallResetIcon, relief=FLAT, state='disabled',
                     border=0, command=reset, bg=DGRAY, fg=DGRAY, activebackground=DGRAY)
StopButton = Button(BLFrame, text="STOP", image=smalleStop, relief=FLAT, state='disabled',
                    border=0, command=stop, bg=DGRAY, fg=DGRAY, activebackground=DGRAY)
ContinueButton = Button(BLFrame, text="STOP", image=smallcontProcess, relief=FLAT, state='disabled',
                        border=0, command=cont, bg=DGRAY, fg=DGRAY, activebackground=DGRAY)

s1MinusButton = Button(Lframe, text="-", font=sFont, relief="raised", bd=0, height=1, state='disabled',
                       bg=LGRAY, fg=GWHITE, activebackground=LGRAY, command=s1TimeDecrease)
s1PlusButton = Button(Lframe, text="+", font=sFont, relief="raised", bd=0, height=1, state='disabled',
                      bg=LGRAY, fg=GWHITE, activebackground=LGRAY, command=s1TimeIncrease)
s2MinusButton = Button(Lframe, text="-", font=sFont, relief="raised", bd=0, height=1, state='disabled',
                       bg=LGRAY, fg=GWHITE, activebackground=LGRAY, command=s2TimeDecrease)
s2PlusButton = Button(Lframe, text="+", font=sFont, relief="raised", bd=0, height=1, state='disabled',
                      bg=LGRAY, fg=GWHITE, activebackground=LGRAY, command=s2TimeIncrease)
s3MinusButton = Button(Lframe, text="-", font=sFont, relief="raised", bd=0, height=1, state='disabled',
                       bg=LGRAY, fg=GWHITE, activebackground=LGRAY, command=s3TimeDecrease)
s3PlusButton = Button(Lframe, text="+", font=sFont, relief="raised", bd=0, height=1, state='disabled',
                      bg=LGRAY, fg=GWHITE, activebackground=LGRAY, command=s3TimeIncrease)

# Radios Buttons
radioVar = IntVar()
R1 = Radiobutton(detailFrame, text="Washing", state='disabled', variable=radioVar, value=1,
                 font=detailFont, bg=DGRAY, fg=GWHITE, justify='center')
R2 = Radiobutton(detailFrame, text="Rinsing", state='disabled', variable=radioVar, value=2,
                 font=detailFont, bg=DGRAY, fg=GWHITE, justify='center')
R3 = Radiobutton(detailFrame, text="Spinning", state='disabled', variable=radioVar, value=3,
                 font=detailFont, bg=DGRAY, fg=GWHITE, justify='center')

# Entries
s1Entry = Entry(Lframe, bd=1, font=sFont, state='readonly', selectbackground=LGRAY, fg=GWHITE, justify='center',
                width=5, relief=SUNKEN, readonlybackground=LGRAY, textvariable=s1TimeCount)

s2Entry = Entry(Lframe, bd=1, font=sFont, state='readonly', selectbackground=LGRAY, fg=GWHITE, justify='center',
                width=5, relief=SUNKEN, readonlybackground=LGRAY, textvariable=s2TimeCount)

s3Entry = Entry(Lframe, bd=1, font=sFont, state='readonly', selectbackground=LGRAY, fg=GWHITE, justify='center',
                width=5, relief=SUNKEN, readonlybackground=LGRAY, textvariable=s3TimeCount)

dValveTimer = Entry(tRframe, bd=1, font=sFont, state='readonly', selectbackground=LGRAY, justify='center',
                    width=5, relief=SUNKEN, fg=GWHITE, readonlybackground=LGRAY, textvariable=dValveTime)
wValveTimer = Entry(tRframe, bd=1, font=sFont, state='readonly', selectbackground=LGRAY, justify='center',
                    width=5, relief=SUNKEN, fg=GWHITE, readonlybackground=LGRAY, textvariable=wValveTime)

s1Timer = Entry(detailFrame, bd=1, font=sFont, state='readonly', selectbackground=DGRAY, fg=GWHITE, justify='center',
                width=8, relief=SUNKEN, readonlybackground=DGRAY, textvariable=confirmS1Time)
s2Timer = Entry(detailFrame, bd=1, font=sFont, state='readonly', selectbackground=DGRAY, fg=GWHITE, justify='center',
                width=8, relief=SUNKEN, readonlybackground=DGRAY, textvariable=confirmS2Time)
s3Timer = Entry(detailFrame, bd=1, font=sFont, state='readonly', selectbackground=DGRAY, fg=GWHITE, justify='center',
                width=8, relief=SUNKEN, readonlybackground=DGRAY, textvariable=confirmS3Time)

hourBox = Entry(hourFrame, bd=0, font=hFont, state='readonly', selectbackground=DGRAY, fg=GWHITE, justify='center',
                width=5, relief=FLAT, readonlybackground=DGRAY, textvariable=hour)
minuteBox = Entry(minuteFrame, bd=0, font=hFont, state='readonly', selectbackground=DGRAY, fg=GWHITE, justify='center',
                  width=5, relief=FLAT, readonlybackground=DGRAY, textvariable=minute)
secondBox = Entry(secondFrame, bd=0, font=hFont, state='readonly', selectbackground=DGRAY, fg=GWHITE, justify='center',
                  width=5, relief=FLAT, readonlybackground=DGRAY, textvariable=second)

# Widgets Placements
frame.pack(fill='both', expand=True, padx=30, pady=20)
TFrame.grid(row=1, column=3, sticky='e', pady=5)
Lframe.grid(rowspan=3, column=1, sticky='w')
space.grid(row=1, column=2)
tRframe.grid(row=3, column=3, sticky='nw')
detailFrame.grid(row=4, column=3, sticky='sw')
BLFrame.grid(row=5, column=1, sticky='sw')
DisplayPanel.grid(row=5, columnspan=4)
BRFrame.grid(row=5, column=3, sticky='se')

welcome.grid(row=1, column=1, sticky='w')

hourFrame.grid(row=1, column=1, padx=3, sticky='nw')
minuteFrame.grid(row=1, column=2, padx=3, sticky='nw')
secondFrame.grid(row=1, column=3, padx=3, sticky='nw')

hourBox.grid(row=1, column=1, padx=3)
minuteBox.grid(row=1, column=1, padx=3)
secondBox.grid(row=1, column=1, padx=3)

space1.grid(row=1, column=4)

PowerButton.grid(row=1, column=5, padx=5)

mSetting.grid(row=1, columnspan=5)
modeList.grid(row=2, columnspan=5)
modeList.current(0)

dSelection.grid(row=3, columnspan=5)
detergentList.grid(row=4, columnspan=5)
detergentList.current(0)

tSetting.grid(row=5, columnspan=3)
sOne.grid(row=6, column=1, sticky='w', pady=5)
s1MinusButton.grid(row=6, column=2, padx=3, pady=5)
s1Entry.grid(row=6, column=3, pady=5)
s1PlusButton.grid(row=6, column=4, padx=3, pady=5)

sTwo.grid(row=7, column=1, sticky='w', pady=5)
s2MinusButton.grid(row=7, column=2, padx=3, pady=5)
s2Entry.grid(row=7, column=3, pady=5)
s2PlusButton.grid(row=7, column=4, padx=3, pady=5)

sThree.grid(row=8, column=1, sticky='w', pady=5)
s3MinusButton.grid(row=8, column=2, padx=3, pady=5)
s3Entry.grid(row=8, column=3, pady=5)
s3PlusButton.grid(row=8, column=4, padx=3, pady=5)

dValve.grid(row=1, column=1)
dImage.grid(row=2, column=1)
dCloseText.grid(row=3, column=1)
dValveTimer.grid(row=4, column=1, pady=2)

wValve.grid(row=1, column=2)
wImage.grid(row=2, column=2)
wCloseText.grid(row=3, column=2)
wValveTimer.grid(row=4, column=2, pady=2)

selectedModeLabel.grid(row=1, column=1, sticky="e")
selectedMode.grid(row=1, column=2, sticky='w')
selectedDetergentLabel.grid(row=2, column=1, sticky="e")
selectedDetergent.grid(row=2, column=2, sticky='w')
stage.grid(row=3, column=1, sticky="e")
R1.grid(row=4, column=1, padx=8)
R2.grid(row=4, column=2, padx=8)
R3.grid(row=4, column=3, padx=8)
s1Timer.grid(row=5, column=1, padx=5)
s2Timer.grid(row=5, column=2, padx=5)
s3Timer.grid(row=5, column=3, padx=5)

doorState.grid(row=1, column=1, sticky='n')

StartButton.grid(row=1, column=1, padx=10)
ResetButton.grid(row=1, column=2, padx=10)
StopButton.grid(row=1, column=1, padx=10)
ContinueButton.grid(row=1, column=2, padx=10)

infoFrame.grid(row=6, columnspan=4, sticky='nesw', padx=10, pady=10)
additionalInfoLabel.grid(row=1, column=1, padx=5, pady=5)

mainloop()

# Additional Info
# Programmer Name: Ooi Zi Sheng | Student ID: 0202150
# Subject Code and Name: CPR3014 Programming for IS
# Teacher's Name: Dr. Ooi Woi Seng
