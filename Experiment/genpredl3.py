#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Experiment on predictive processing (gender in L3 Spanish)
# Jorge Gonzalez Alonso
# LAVA Research Group, UiT The Arctic University of Norway, 2017

# Modified from a script compiled in PsychoPy2 Experiment Builder (v1.84.2),
# combined with code from sample files in SMI's iViewX SDK

# Experiment written for use with an SMI RED 500 eye-tracker 

# ---------------------------------------------
#---- Import all necessary libraries
# ---------------------------------------------

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
from iViewXAPI import  *            #iViewX library. Make sure this file and next (return codes) are in the same folder!
from iViewXAPIReturnCodes import * 
import psychopy.logging              #import like this so it doesn't interfere with numpy.log

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'predictive_final'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
path = os.getcwd() + "\\data\\"
description = expInfo['session']
user = expInfo['participant']

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

def CalibrationRoutine():
	
    calibrationData = CCalibration(5, 1, 1, 0, 1, 250, 220, 2, 20, b"") # NB! 3rd parameter is displayDevice. '0' = primary, '1' = secondary (e.g. to run on eye-tracker's screen)
    res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
    print("iV_SetupCalibration " + str(res))
    res = iViewXAPI.iV_Calibrate()

    res = iViewXAPI.iV_Validate()
    print("iV_Validate " + str(res))

    res = iViewXAPI.iV_GetAccuracy(byref(accuracyData), 1)
    print("iV_GetAccuracy " + str(res))
    print("deviationXLeft " + str(accuracyData.deviationLX) + " deviationYLeft " + str(accuracyData.deviationLY))
    print("deviationXRight " + str(accuracyData.deviationRX) + " deviationYRight " + str(accuracyData.deviationRY))
    
    acc = accuracyData
	
    answer = raw_input("Accept calibration? (y/n):")
    answer = answer.lstrip()
	
    if(answer == "y"):
	    print("Calibration accepted, continuing...")
	    return
    else:
        CalibrationRoutine()

# ---------------------------------------------
#---- connect to iViewX 
# ---------------------------------------------

res = iViewXAPI.iV_SetLogger(c_int(1), c_char_p(filename+'.log'))
res = iViewXAPI.iV_Connect(c_char_p('127.0.0.1'), c_int(4444), c_char_p('127.0.0.1'), c_int(5555))
if res != 1:
    HandleError(res)
    exit(0)
    
res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
print("iV_GetSystemInfo: " + str(res))
print("Samplerate: " + str(systemData.samplerate))
print("iViewX Version: " + str(systemData.iV_MajorVersion) + "." + str(systemData.iV_MinorVersion) + "." + str(systemData.iV_Buildnumber))
print("iViewX API Version: " + str(systemData.API_MajorVersion) + "." + str(systemData.API_MinorVersion) + "." + str(systemData.API_Buildnumber))

# ---------------------------------------------
#---- configure and start calibration
# ---------------------------------------------

#calibrationData = CCalibration(5, 1, 1, 0, 1, 250, 220, 2, 20, b"") 

# res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
# print("iV_SetupCalibration " + str(res))
# res = iViewXAPI.iV_Calibrate()
# print("iV_Calibrate " + str(res))

# res = iViewXAPI.iV_Validate()
# print("iV_Validate " + str(res))

# res = iViewXAPI.iV_GetAccuracy(byref(accuracyData), 1)
# print("iV_GetAccuracy " + str(res))
# print("deviationXLeft " + str(accuracyData.deviationLX) + " deviationYLeft " + str(accuracyData.deviationLY))
# print("deviationXRight " + str(accuracyData.deviationRX) + " deviationYRight " + str(accuracyData.deviationRY))

# res = iViewXAPI.iV_ShowTrackingMonitor()
# print("iV_ShowTrackingMonitor " + str(res))
CalibrationRoutine()
    
# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=1, # adjust to actual resolution of your display screen
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# -------------------------------
#---- Pre-load routines
# -------------------------------
    
# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
inst1 = visual.TextStim(win=win, name='inst1',
    text=u'\xa1Gracias por participar! Av\xedsanos cuando est\xe9s lista/o para empezar.\n\nThank you for participating! Let us know you are ready to start.\n\nTakk for \xe5 delta! Gi oss beskjed n\xe5r du er klar til \xe5 starte.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
inst11 = visual.TextStim(win=win, name='inst11',
    text=u'For n\xe5, se bare p\xe5 disse bildene og h\xf8re p\xe5 navnene deres.\n\nPor ahora, s\xf3lo mira a estas im\xe1genes y escucha sus nombres.\n\nFor now, just look at these pictures and listen to their names.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "training"
trainingClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
picname = sound.Sound('A', secs=-1)
picname.setVolume(1)

# Initialize components for Routine "trans1"
trans1Clock = core.Clock()
inst2 = visual.TextStim(win=win, name='inst2',
    text=u'Ahora di t\xfa el nombre de cada imagen.\n\nNow name each picture yourself.\n\nN\xe5 m\xe5 du navngi hvert bilde.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practice1"
practice1Clock = core.Clock()
pimage = visual.ImageStim(
    win=win, name='pimage',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "practice2"
practice2Clock = core.Clock()
fimage = visual.ImageStim(
    win=win, name='fimage',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
feedsound = sound.Sound('A', secs=-1)
feedsound.setVolume(1)

# Initialize components for Routine "trans2_1"
trans2_1Clock = core.Clock()
inst3 = visual.TextStim(win=win, name='inst3',
    text=u'End of practice!\n\n\xa1Fin de la pr\xe1ctica!\n\nSlutt p\xe5 \xf8veblokken!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trans2_2"
trans2_2Clock = core.Clock()
inst4 = visual.TextStim(win=win, name='inst4',
    text=u'Durante el experimento ver\xe1s primero dos im\xe1genes, una a cada lado, durante unos segundos.\n\nI eksperimentet skal du f\xf8rst se to bilder, side om side, noen f\xe5 sekunder.\n\nIn the experiment, you will first see two pictures side by side for a few seconds.',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
instpic1 = visual.ImageStim(
    win=win, name='instpic1',units='pix', 
    image='silla.jpg', mask=None,
    ori=0, pos=(-400, -200), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instpic2 = visual.ImageStim(
    win=win, name='instpic2',units='pix', 
    image='perro.jpg', mask=None,
    ori=0, pos=(400, -200), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "trans2_3"
trans2_3Clock = core.Clock()
inst5 = visual.TextStim(win=win, name='inst5',
    text=u'Cuando desaparezcan, debes mirar a la cruz en el centro de la pantalla.\n\nN\xe5r de forsvinner m\xe5 du se p\xe5 korset i midten av skjermen.\n\nWhen they disappear, you must look at the cross in the middle of the screen.',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
instfix = visual.ImageStim(
    win=win, name='instfix',units='pix', 
    image='fixation.png', mask=None,
    ori=0, pos=(0, -100), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trans2_4"
trans2_4Clock = core.Clock()
inst6 = visual.TextStim(win=win, name='inst6',
    text=u'Oir\xe1s "Haz click en..." o "Selecciona..."\njusto antes de que las im\xe1genes vuelvan a aparecer en el mismo sitio.\n\n\nYou will hear "Haz click en..." (Click on...) or "Selecciona..." (Select...) right before\nthe images reappear in the same place. ',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
instfix2 = visual.ImageStim(
    win=win, name='instfix2',units='pix', 
    image='fixation.png', mask=None,
    ori=0, pos=(0, -100), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
loudsp = visual.ImageStim(
    win=win, name='loudsp',units='pix', 
    image='loudspeaker.png', mask=None,
    ori=0, pos=(0, -300), size=(100, 100),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "trans2_5"
trans2_5Clock = core.Clock()
inst7 = visual.TextStim(win=win, name='inst7',
    text=u'Tu tarea es hacer click en la imagen que nombre la voz tan r\xe1pido como\npuedas. Nosotros no te diremos si has acertado.\n\n\nYour task is to click on the picture that is named\nby the voice as quickly as you can. We will not tell you if you were right.',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
instpic3 = visual.ImageStim(
    win=win, name='instpic3',units='pix', 
    image='silla.jpg', mask=None,
    ori=0, pos=(-400, -200), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instpic4 = visual.ImageStim(
    win=win, name='instpic4',units='pix', 
    image='perro.jpg', mask=None,
    ori=0, pos=(400, -200), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
cursor = visual.ImageStim(
    win=win, name='cursor',units='pix', 
    image='cursor.jpg', mask=None,
    ori=0, pos=(-280, -300), size=(40, 34),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "trans2_6"
trans2_6Clock = core.Clock()
inst8 = visual.TextStim(win=win, name='inst8',
    text=u'\xbfEst\xe1s preparada/o? Si tienes cualquier pregunta, hazla ahora. Despu\xe9s empezaremos.\n\nFerdig? Dersom du har noen sp\xf8rsmaler, vennligst sp\xf8r n\xe5. Etterp\xe5 skal vi starte.\n\nReady? If you have any questions, please ask them now. Afterwards we will start.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
prev = visual.ImageStim(
    win=win, name='prev',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0,0), size=(1680, 1050),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
prevsound1 = sound.Sound('A', secs=-1)
prevsound1.setVolume(1)
prevsound2 = sound.Sound('A', secs=-1)
prevsound2.setVolume(1)
fixation = visual.ImageStim(
    win=win, name='fixation',units='pix', 
    image=u'fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(300, 300),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
frsound = sound.Sound('A', secs=-1)
frsound.setVolume(1)
targ = visual.ImageStim(
    win=win, name='targ',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0,0), size=(1680, 1050),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sentence = sound.Sound('A', secs=-1)
sentence.setVolume(1)
mouse = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "end_scr"
end_scrClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text=u'That is all. Thank you!\n\nDet var alt. Takk!\n\nEso es todo. \xa1Gracias!\n\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instr1Components = [inst1, key_resp_2]
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst1* updates
    if t >= 0.0 and inst1.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst1.tStart = t
        inst1.frameNStart = frameN  # exact frame index
        inst1.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr2"-------
t = 0
instr2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
instr2Components = [inst11, key_resp_11]
for thisComponent in instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr2"-------
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst11* updates
    if t >= 0.0 and inst11.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst11.tStart = t
        inst11.frameNStart = frameN  # exact frame index
        inst11.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
		
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys=None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
train = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('training.xlsx'),
    seed=None, name='train')
thisExp.addLoop(train)  # add the loop to the experiment
thisTrain = train.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrain.rgb)
if thisTrain != None:
    for paramName in thisTrain.keys():
        exec(paramName + '= thisTrain.' + paramName)

for thisTrain in train:
    currentLoop = train
    # abbreviate parameter names if possible (e.g. rgb = thisTrain.rgb)
    if thisTrain != None:
        for paramName in thisTrain.keys():
            exec(paramName + '= thisTrain.' + paramName)
    
    # ------Prepare to start Routine "training"-------
    t = 0
    trainingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(picture)
    image.setSize(psize)
    picname.setSound(sound, secs=-1)
    # keep track of which components have finished
    trainingComponents = [image, picname]
    for thisComponent in trainingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "training"-------
    while continueRoutine:
        # get current time
        t = trainingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        # start/stop picname
        if t >= 0.0 and picname.status == NOT_STARTED:
            # keep track of start time/frame for later
            picname.tStart = t
            picname.frameNStart = frameN  # exact frame index
            picname.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        
    # -------Ending Routine "training"-------
    for thisComponent in trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    picname.stop()  # ensure sound has stopped at end of routine
    # the Routine "training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'train'


# ------Prepare to start Routine "trans1"-------
t = 0
trans1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
trans1Components = [inst2, key_resp_4]
for thisComponent in trans1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trans1"-------
while continueRoutine:
    # get current time
    t = trans1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst2* updates
    if t >= 0.0 and inst2.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst2.tStart = t
        inst2.frameNStart = frameN  # exact frame index
        inst2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trans1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trans1"-------
for thisComponent in trans1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "trans1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pract = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.xlsx'),
    seed=None, name='pract')
thisExp.addLoop(pract)  # add the loop to the experiment
thisPract = pract.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPract.rgb)
if thisPract != None:
    for paramName in thisPract.keys():
        exec(paramName + '= thisPract.' + paramName)

for thisPract in pract:
    currentLoop = pract
    # abbreviate parameter names if possible (e.g. rgb = thisPract.rgb)
    if thisPract != None:
        for paramName in thisPract.keys():
            exec(paramName + '= thisPract.' + paramName)
    
    # ------Prepare to start Routine "practice1"-------
    if event.getKeys(keyList=["p"]):
        CalibrationRoutine()
    t = 0
    practice1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    pimage.setImage(ppicture)
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    practice1Components = [pimage, key_resp_5]
    for thisComponent in practice1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice1"-------
    while continueRoutine:
        # get current time
        t = practice1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pimage* updates
        if t >= 0.0 and pimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            pimage.tStart = t
            pimage.frameNStart = frameN  # exact frame index
            pimage.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice1"-------
    for thisComponent in practice1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    pract.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        pract.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice2"-------
    t = 0
    practice2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    fimage.setImage(fpicture)
    fimage.setSize(fpsize)
    feedsound.setSound(fsound, secs=-1)
    # keep track of which components have finished
    practice2Components = [fimage, feedsound]
    for thisComponent in practice2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice2"-------
    while continueRoutine:
        # get current time
        t = practice2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fimage* updates
        if t >= 0.0 and fimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            fimage.tStart = t
            fimage.frameNStart = frameN  # exact frame index
            fimage.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fimage.status == STARTED and t >= frameRemains:
            fimage.setAutoDraw(False)
        # start/stop feedsound
        if t >= 0.0 and feedsound.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedsound.tStart = t
            feedsound.frameNStart = frameN  # exact frame index
            feedsound.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice2"-------
    for thisComponent in practice2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    feedsound.stop()  # ensure sound has stopped at end of routine
    # the Routine "practice2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'pract'


# ------Prepare to start Routine "trans2_1"-------
t = 0
trans2_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
trans2_1Components = [inst3]
for thisComponent in trans2_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trans2_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trans2_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst3* updates
    if t >= 0.0 and inst3.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst3.tStart = t
        inst3.frameNStart = frameN  # exact frame index
        inst3.setAutoDraw(True)
    frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if inst3.status == STARTED and t >= frameRemains:
        inst3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trans2_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
	
	if event.getKeys(keyList=["p"]):
	    CalibrationRoutine()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trans2_1"-------
for thisComponent in trans2_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "trans2_2"-------
t = 0
trans2_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
trans2_2Components = [inst4, instpic1, instpic2, key_resp_6]
for thisComponent in trans2_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trans2_2"-------
while continueRoutine:
    # get current time
    t = trans2_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst4* updates
    if t >= 0.0 and inst4.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst4.tStart = t
        inst4.frameNStart = frameN  # exact frame index
        inst4.setAutoDraw(True)
    
    # *instpic1* updates
    if t >= 0.0 and instpic1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instpic1.tStart = t
        instpic1.frameNStart = frameN  # exact frame index
        instpic1.setAutoDraw(True)
    
    # *instpic2* updates
    if t >= 0.0 and instpic2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instpic2.tStart = t
        instpic2.frameNStart = frameN  # exact frame index
        instpic2.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trans2_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trans2_2"-------
for thisComponent in trans2_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys=None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "trans2_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trans2_3"-------
t = 0
trans2_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
trans2_3Components = [inst5, instfix, key_resp_7]
for thisComponent in trans2_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trans2_3"-------
while continueRoutine:
    # get current time
    t = trans2_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst5* updates
    if t >= 0.0 and inst5.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst5.tStart = t
        inst5.frameNStart = frameN  # exact frame index
        inst5.setAutoDraw(True)
    
    # *instfix* updates
    if t >= 0.0 and instfix.status == NOT_STARTED:
        # keep track of start time/frame for later
        instfix.tStart = t
        instfix.frameNStart = frameN  # exact frame index
        instfix.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trans2_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trans2_3"-------
for thisComponent in trans2_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "trans2_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trans2_4"-------
t = 0
trans2_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
trans2_4Components = [inst6, instfix2, loudsp, key_resp_8]
for thisComponent in trans2_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trans2_4"-------
while continueRoutine:
    # get current time
    t = trans2_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst6* updates
    if t >= 0.0 and inst6.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst6.tStart = t
        inst6.frameNStart = frameN  # exact frame index
        inst6.setAutoDraw(True)
    
    # *instfix2* updates
    if t >= 0.0 and instfix2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instfix2.tStart = t
        instfix2.frameNStart = frameN  # exact frame index
        instfix2.setAutoDraw(True)
    
    # *loudsp* updates
    if t >= 0.0 and loudsp.status == NOT_STARTED:
        # keep track of start time/frame for later
        loudsp.tStart = t
        loudsp.frameNStart = frameN  # exact frame index
        loudsp.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trans2_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trans2_4"-------
for thisComponent in trans2_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "trans2_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trans2_5"-------
t = 0
trans2_5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
trans2_5Components = [inst7, instpic3, instpic4, cursor, key_resp_9]
for thisComponent in trans2_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trans2_5"-------
while continueRoutine:
    # get current time
    t = trans2_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst7* updates
    if t >= 0.0 and inst7.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst7.tStart = t
        inst7.frameNStart = frameN  # exact frame index
        inst7.setAutoDraw(True)
    
    # *instpic3* updates
    if t >= 0.0 and instpic3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instpic3.tStart = t
        instpic3.frameNStart = frameN  # exact frame index
        instpic3.setAutoDraw(True)
    
    # *instpic4* updates
    if t >= 0.0 and instpic4.status == NOT_STARTED:
        # keep track of start time/frame for later
        instpic4.tStart = t
        instpic4.frameNStart = frameN  # exact frame index
        instpic4.setAutoDraw(True)
    
    # *cursor* updates
    if t >= 0.0 and cursor.status == NOT_STARTED:
        # keep track of start time/frame for later
        cursor.tStart = t
        cursor.frameNStart = frameN  # exact frame index
        cursor.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trans2_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trans2_5"-------
for thisComponent in trans2_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "trans2_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trans2_6"-------
t = 0
trans2_6Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
trans2_6Components = [inst8, key_resp_10]
for thisComponent in trans2_6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trans2_6"-------
while continueRoutine:
    # get current time
    t = trans2_6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst8* updates
    if t >= 0.0 and inst8.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst8.tStart = t
        inst8.frameNStart = frameN  # exact frame index
        inst8.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trans2_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trans2_6"-------
for thisComponent in trans2_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
# the Routine "trans2_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trials.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    if event.getKeys(keyList=["p"]):
        CalibrationRoutine()
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    prev.setImage(picture)
    prevsound1.setSound(psound1, secs=-1)
    prevsound2.setSound(psound2, secs=-1)
    frsound.setSound(frame, secs=-1)
    targ.setImage(picture)
    sentence.setSound(tsound, secs=-1)
    # setup some python lists for storing info about the mouse
    # keep track of which components have finished
    trialComponents = [prev, prevsound1, prevsound2, fixation, frsound, targ, sentence, mouse]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    iViewXAPI.iV_StartRecording()
    
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
		
        # *prev* updates
        if t >= 0.0 and prev.status == NOT_STARTED:
            # keep track of start time/frame for later
            prev.tStart = t
            prev.frameNStart = frameN  # exact frame index
            prev.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if prev.status == STARTED and t >= frameRemains:
            prev.setAutoDraw(False)
        # start/stop prevsound1
        if t >= 0.0 and prevsound1.status == NOT_STARTED:
            # keep track of start time/frame for later
            prevsound1.tStart = t
            prevsound1.frameNStart = frameN  # exact frame index
            prevsound1.play()  # start the sound (it finishes automatically)
        # start/stop prevsound2
        if (prevsound1.status==FINISHED) and prevsound2.status == NOT_STARTED:
            core.wait(0.5) # give it 500 ms before starting
            # keep track of start time/frame for later
            prevsound2.tStart = t
            prevsound2.frameNStart = frameN  # exact frame index
            prevsound2.play()  # start the sound (it finishes automatically)
        
        # *fixation* updates
        if (prev.status==FINISHED) and fixation.status == NOT_STARTED:
            core.wait(0.2)
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        if fixation.status == STARTED and bool(frsound.status==FINISHED):
            fixation.setAutoDraw(False)
        # start/stop frsound
        if (fixation.status==STARTED) and frsound.status == NOT_STARTED:
            # keep track of start time/frame for later
            frsound.tStart = t
            frsound.frameNStart = frameN  # exact frame index
            frsound.play()  # start the sound (it finishes automatically)
        
        # *targ* updates
        if (frsound.status==FINISHED) and targ.status == NOT_STARTED:
            # keep track of start time/frame for later
            targ.tStart = t
            targ.frameNStart = frameN  # exact frame index
            iViewXAPI.iV_SendImageMessage(c_char_p(picture))
            targ.setAutoDraw(True)
        # start/stop sentence
        if (targ.status==STARTED) and sentence.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence.tStart = t
            sentence.frameNStart = frameN  # exact frame index
            sentence.play()  # start the sound (it finishes automatically)
        # *mouse* updates
        if (frsound.status==FINISHED) and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if sum(buttons) > 0:  # ie if any button is pressed
                # abort routine on response
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    prevsound1.stop()  # ensure sound has stopped at end of routine
    prevsound2.stop()  # ensure sound has stopped at end of routine
    frsound.stop()  # ensure sound has stopped at end of routine
    sentence.stop()  # ensure sound has stopped at end of routine
    # store data for trials (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    trials.addData('mouse.x', x)
    trials.addData('mouse.y', y)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# stop and disconnect eye-tracker, save data
iViewXAPI.iV_StopRecording()
outputfile = filename + ".idf"
res = iViewXAPI.iV_SaveData(str(outputfile), str(description), str(user), 1)
print "iV_SaveData " + str(res)
print "data saved to: " + outputfile

iViewXAPI.iV_Disconnect()


# ------Prepare to start Routine "end_scr"-------
t = 0
end_scrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
end_scrComponents = [thanks, key_resp_3]
for thisComponent in end_scrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_scr"-------
while continueRoutine:
    # get current time
    t = end_scrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if t >= 0.0 and thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks.tStart = t
        thanks.frameNStart = frameN  # exact frame index
        thanks.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_scrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_scr"-------
for thisComponent in end_scrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "end_scr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
