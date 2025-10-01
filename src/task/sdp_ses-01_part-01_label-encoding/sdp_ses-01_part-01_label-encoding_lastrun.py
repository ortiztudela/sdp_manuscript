#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Fri Sep 17 08:58:41 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'sdp_ses-01_part-01_label-encoding'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/javierortiz/pavlovia/sdp_ses-01_part-01_label-encoding/sdp_ses-01_part-01_label-encoding_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='gray', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "initialize"
initializeClock = core.Clock()
obj_size = (0.4,0.3)
scn_size = (.8,0.6)
cue_dur = 2
action_dur = .850
target_dur = 2
fix_dur = .5

prompt_pos = (0,0)
prompt_size = 0.025
cond_file='condition_files/enc_1_list.csv'
inst_file='condition_files/instructions.csv'

trial_index = 0

# Initialize components for Routine "hello"
helloClock = core.Clock()
text_hi = visual.TextStim(win=win, name='text_hi',
    text='Dear participant,\n\nBefore we start, we will determine your monitor size.  After this, you will read some instructions about the study and then we will proceed with the task.\n\n<Press the space bar to continue>\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_hi = keyboard.Keyboard()

# Initialize components for Routine "screen_scale"
screen_scaleClock = core.Clock()
oldt=0
x_size=8.560
y_size=5.398
screen_height=0

if win.units=='norm':
    x_scale=.05
    y_scale=.1
    dbase = .0001
    unittext=' norm units'
    vsize=2
elif win.units=='pix':
    x_scale=60
    y_scale=40
    dbase = .1
    unittext=' pixels'
    vsize=win.size[1]
else:
    x_scale=.05
    y_scale=.05
    dbase = .0001
    unittext=' height units'
    vsize=1
text_top = visual.TextStim(win=win, name='text_top',
    text='Resize this image to match the size of a credit card\nUp arrow for taller\nDown arrow for shorter\nLeft arrow for narrower\nRight arrow for wider',
    font='Arial',
    units='norm', pos=(0, .7), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_bottom = visual.TextStim(win=win, name='text_bottom',
    text='Press the space bar when done',
    font='Arial',
    units='norm', pos=(0, -.6), height=0.05, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ccimage = visual.ImageStim(
    win=win,
    name='ccimage', 
    image='bank-1300155_640.png', mask=None,
    ori=0.0, pos=(0, 0), size=(x_size*x_scale, y_size*y_scale),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text_comp = visual.TextStim(win=win, name='text_comp',
    text='',
    font='Arial',
    units='height', pos=(0,0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_resp1 = keyboard.Keyboard()

# Initialize components for Routine "ready"
readyClock = core.Clock()
warning = visual.TextStim(win=win, name='warning',
    text='',
    font='Arial',
    units='height', pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
ready_text = visual.TextStim(win=win, name='ready_text',
    text='',
    font='Arial',
    units='height', pos=(0,-.25), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixcross_display"
fixcross_displayClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
#cue_file="stim/" + comic_name + "Slide-01.png"
#action1="stim/" + comic_name + "Slide-02.png"
#action2="stim/" + comic_name + "Slide-03.png"
#action3="stim/" + comic_name + "Slide-04.png"
#target_file="stim/" + comic_name + "Slide-06.png"

# Initialize components for Routine "cue_trial"
cue_trialClock = core.Clock()
cue_slide = visual.ImageStim(
    win=win,
    name='cue_slide', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "action1_trial"
action1_trialClock = core.Clock()
slide_1 = visual.ImageStim(
    win=win,
    name='slide_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "action2_trial"
action2_trialClock = core.Clock()
slide_2 = visual.ImageStim(
    win=win,
    name='slide_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "action3_trial"
action3_trialClock = core.Clock()
slide_3 = visual.ImageStim(
    win=win,
    name='slide_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "target_trial"
target_trialClock = core.Clock()
target_slide = visual.ImageStim(
    win=win,
    name='target_slide', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "response"
responseClock = core.Clock()
prompt_target = visual.TextStim(win=win, name='prompt_target',
    text='Did the object reach the intended person?\n\nleft = "yes"; right = "no"',
    font='Arial',
    units='height', pos=prompt_pos, height=prompt_size, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
target_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedb_text_obj = visual.TextStim(win=win, name='feedb_text_obj',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_end"
practice_endClock = core.Clock()
warning_2 = visual.TextStim(win=win, name='warning_2',
    text='',
    font='Arial',
    units='height', pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
ready_text_2 = visual.TextStim(win=win, name='ready_text_2',
    text='',
    font='Arial',
    units='height', pos=(0,-.25), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixcross_display"
fixcross_displayClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
#cue_file="stim/" + comic_name + "Slide-01.png"
#action1="stim/" + comic_name + "Slide-02.png"
#action2="stim/" + comic_name + "Slide-03.png"
#action3="stim/" + comic_name + "Slide-04.png"
#target_file="stim/" + comic_name + "Slide-06.png"

# Initialize components for Routine "cue_trial"
cue_trialClock = core.Clock()
cue_slide = visual.ImageStim(
    win=win,
    name='cue_slide', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "action1_trial"
action1_trialClock = core.Clock()
slide_1 = visual.ImageStim(
    win=win,
    name='slide_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "action2_trial"
action2_trialClock = core.Clock()
slide_2 = visual.ImageStim(
    win=win,
    name='slide_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "action3_trial"
action3_trialClock = core.Clock()
slide_3 = visual.ImageStim(
    win=win,
    name='slide_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "target_trial"
target_trialClock = core.Clock()
target_slide = visual.ImageStim(
    win=win,
    name='target_slide', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "response"
responseClock = core.Clock()
prompt_target = visual.TextStim(win=win, name='prompt_target',
    text='Did the object reach the intended person?\n\nleft = "yes"; right = "no"',
    font='Arial',
    units='height', pos=prompt_pos, height=prompt_size, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
target_resp = keyboard.Keyboard()

# Initialize components for Routine "bye"
byeClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Arial',
    units='height', pos=(0,0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_resp1_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initialize"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
initializeComponents = []
for thisComponent in initializeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initializeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initialize"-------
while continueRoutine:
    # get current time
    t = initializeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initializeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initializeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initialize"-------
for thisComponent in initializeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initialize" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hello"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_hi.keys = []
key_resp_hi.rt = []
_key_resp_hi_allKeys = []
# keep track of which components have finished
helloComponents = [text_hi, key_resp_hi]
for thisComponent in helloComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
helloClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hello"-------
while continueRoutine:
    # get current time
    t = helloClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=helloClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_hi* updates
    if text_hi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_hi.frameNStart = frameN  # exact frame index
        text_hi.tStart = t  # local t and not account for scr refresh
        text_hi.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_hi, 'tStartRefresh')  # time at next scr refresh
        text_hi.setAutoDraw(True)
    
    # *key_resp_hi* updates
    waitOnFlip = False
    if key_resp_hi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_hi.frameNStart = frameN  # exact frame index
        key_resp_hi.tStart = t  # local t and not account for scr refresh
        key_resp_hi.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_hi, 'tStartRefresh')  # time at next scr refresh
        key_resp_hi.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_hi.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_hi.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_hi.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_hi.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_hi_allKeys.extend(theseKeys)
        if len(_key_resp_hi_allKeys):
            key_resp_hi.keys = _key_resp_hi_allKeys[-1].name  # just the last key pressed
            key_resp_hi.rt = _key_resp_hi_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in helloComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hello"-------
for thisComponent in helloComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "hello" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "screen_scale"-------
continueRoutine = True
# update component parameters for each repeat
event.clearEvents()
# keep track of which components have finished
screen_scaleComponents = [text_top, text_bottom, ccimage]
for thisComponent in screen_scaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screen_scaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screen_scale"-------
while continueRoutine:
    # get current time
    t = screen_scaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screen_scaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys=event.getKeys()
    
    if len(keys):
        if t-oldt<.5:
            dscale=5*dbase
            oldt=t
        else:
            dscale=dbase
            oldt=t
        if 'space' in keys and t > 1:
            continueRoutine=False
        elif 'up' in keys:
            y_scale=round((y_scale+dscale)*10000)/10000
        elif 'down' in keys:
            y_scale=round((y_scale-dscale)*10000)/10000
        elif 'left' in keys:
            x_scale=round((x_scale-dscale)*10000)/10000
        elif 'right' in keys:
            x_scale=round((x_scale+dscale)*10000)/10000
        screen_height=round(vsize*10/y_scale)/10
        text_bottom.text='X Scale = '+str(x_scale)+unittext+' per cm, Y Scale = '+str(y_scale)+unittext+' per cm\nScreen height = '+str(screen_height)+' cm\n\nPress the space bar when done'
        ccimage.size=[x_size*x_scale, y_size*y_scale]
        
    
    # *text_top* updates
    if text_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_top.frameNStart = frameN  # exact frame index
        text_top.tStart = t  # local t and not account for scr refresh
        text_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_top, 'tStartRefresh')  # time at next scr refresh
        text_top.setAutoDraw(True)
    
    # *text_bottom* updates
    if text_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_bottom.frameNStart = frameN  # exact frame index
        text_bottom.tStart = t  # local t and not account for scr refresh
        text_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_bottom, 'tStartRefresh')  # time at next scr refresh
        text_bottom.setAutoDraw(True)
    
    # *ccimage* updates
    if ccimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ccimage.frameNStart = frameN  # exact frame index
        ccimage.tStart = t  # local t and not account for scr refresh
        ccimage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ccimage, 'tStartRefresh')  # time at next scr refresh
        ccimage.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screen_scaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screen_scale"-------
for thisComponent in screen_scaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('X Scale',x_scale)
thisExp.addData('Y Scale',y_scale)

thisExp.addData('text_top.started', text_top.tStartRefresh)
thisExp.addData('text_top.stopped', text_top.tStopRefresh)
thisExp.addData('text_bottom.started', text_bottom.tStartRefresh)
thisExp.addData('text_bottom.stopped', text_bottom.tStopRefresh)
thisExp.addData('ccimage.started', ccimage.tStartRefresh)
thisExp.addData('ccimage.stopped', ccimage.tStopRefresh)
# the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
welcome_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(inst_file),
    seed=None, name='welcome_loop')
thisExp.addLoop(welcome_loop)  # add the loop to the experiment
thisWelcome_loop = welcome_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWelcome_loop.rgb)
if thisWelcome_loop != None:
    for paramName in thisWelcome_loop:
        exec('{} = thisWelcome_loop[paramName]'.format(paramName))

for thisWelcome_loop in welcome_loop:
    currentLoop = welcome_loop
    # abbreviate parameter names if possible (e.g. rgb = thisWelcome_loop.rgb)
    if thisWelcome_loop != None:
        for paramName in thisWelcome_loop:
            exec('{} = thisWelcome_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "welcome"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_comp.setText(inst_text)
    welcome_resp1.keys = []
    welcome_resp1.rt = []
    _welcome_resp1_allKeys = []
    # keep track of which components have finished
    welcomeComponents = [text_comp, welcome_resp1]
    for thisComponent in welcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "welcome"-------
    while continueRoutine:
        # get current time
        t = welcomeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_comp* updates
        if text_comp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_comp.frameNStart = frameN  # exact frame index
            text_comp.tStart = t  # local t and not account for scr refresh
            text_comp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_comp, 'tStartRefresh')  # time at next scr refresh
            text_comp.setAutoDraw(True)
        
        # *welcome_resp1* updates
        waitOnFlip = False
        if welcome_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_resp1.frameNStart = frameN  # exact frame index
            welcome_resp1.tStart = t  # local t and not account for scr refresh
            welcome_resp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_resp1, 'tStartRefresh')  # time at next scr refresh
            welcome_resp1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcome_resp1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcome_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcome_resp1.status == STARTED and not waitOnFlip:
            theseKeys = welcome_resp1.getKeys(keyList=['space'], waitRelease=False)
            _welcome_resp1_allKeys.extend(theseKeys)
            if len(_welcome_resp1_allKeys):
                welcome_resp1.keys = _welcome_resp1_allKeys[-1].name  # just the last key pressed
                welcome_resp1.rt = _welcome_resp1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "welcome"-------
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'welcome_loop'

# get names of stimulus parameters
if welcome_loop.trialList in ([], [None], None):
    params = []
else:
    params = welcome_loop.trialList[0].keys()
# save data for this loop
welcome_loop.saveAsExcel(filename + '.xlsx', sheetName='welcome_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "ready"-------
continueRoutine = True
# update component parameters for each repeat
warning.setText('You will start the practice trials now.\n\n')
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
ready_text.setText('<Press the space bar to continue>')
# keep track of which components have finished
readyComponents = [warning, key_resp_6, ready_text]
for thisComponent in readyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ready"-------
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=readyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *warning* updates
    if warning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        warning.frameNStart = frameN  # exact frame index
        warning.tStart = t  # local t and not account for scr refresh
        warning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(warning, 'tStartRefresh')  # time at next scr refresh
        warning.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ready_text* updates
    if ready_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready_text.frameNStart = frameN  # exact frame index
        ready_text.tStart = t  # local t and not account for scr refresh
        ready_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready_text, 'tStartRefresh')  # time at next scr refresh
        ready_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/practice_trials.csv'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixcross_display"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixcross_displayComponents = [fix]
    for thisComponent in fixcross_displayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixcross_displayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixcross_display"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixcross_displayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixcross_displayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixcross_displayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixcross_display"-------
    for thisComponent in fixcross_displayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "cue_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    cue_slide.setSize((16*x_scale, 12*y_scale))
    cue_slide.setImage(cue_file)
    # keep track of which components have finished
    cue_trialComponents = [cue_slide]
    for thisComponent in cue_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cue_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cue_trial"-------
    while continueRoutine:
        # get current time
        t = cue_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cue_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_slide* updates
        if cue_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_slide.frameNStart = frameN  # exact frame index
            cue_slide.tStart = t  # local t and not account for scr refresh
            cue_slide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_slide, 'tStartRefresh')  # time at next scr refresh
            cue_slide.setAutoDraw(True)
        if cue_slide.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_slide.tStartRefresh + cue_dur-frameTolerance:
                # keep track of stop time/frame for later
                cue_slide.tStop = t  # not accounting for scr refresh
                cue_slide.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_slide, 'tStopRefresh')  # time at next scr refresh
                cue_slide.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cue_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue_trial"-------
    for thisComponent in cue_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "cue_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "action1_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    slide_1.setSize((16*x_scale, 12*y_scale))
    slide_1.setImage(action1)
    # keep track of which components have finished
    action1_trialComponents = [slide_1]
    for thisComponent in action1_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    action1_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "action1_trial"-------
    while continueRoutine:
        # get current time
        t = action1_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=action1_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slide_1* updates
        if slide_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slide_1.frameNStart = frameN  # exact frame index
            slide_1.tStart = t  # local t and not account for scr refresh
            slide_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slide_1, 'tStartRefresh')  # time at next scr refresh
            slide_1.setAutoDraw(True)
        if slide_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slide_1.tStartRefresh + action_dur-frameTolerance:
                # keep track of stop time/frame for later
                slide_1.tStop = t  # not accounting for scr refresh
                slide_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(slide_1, 'tStopRefresh')  # time at next scr refresh
                slide_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in action1_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "action1_trial"-------
    for thisComponent in action1_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "action1_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "action2_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    slide_2.setSize((16*x_scale, 12*y_scale))
    slide_2.setImage(action2)
    # keep track of which components have finished
    action2_trialComponents = [slide_2]
    for thisComponent in action2_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    action2_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "action2_trial"-------
    while continueRoutine:
        # get current time
        t = action2_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=action2_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slide_2* updates
        if slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slide_2.frameNStart = frameN  # exact frame index
            slide_2.tStart = t  # local t and not account for scr refresh
            slide_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slide_2, 'tStartRefresh')  # time at next scr refresh
            slide_2.setAutoDraw(True)
        if slide_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slide_2.tStartRefresh + action_dur-frameTolerance:
                # keep track of stop time/frame for later
                slide_2.tStop = t  # not accounting for scr refresh
                slide_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(slide_2, 'tStopRefresh')  # time at next scr refresh
                slide_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in action2_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "action2_trial"-------
    for thisComponent in action2_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "action2_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "action3_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    slide_3.setSize((16*x_scale, 12*y_scale))
    slide_3.setImage(action3)
    # keep track of which components have finished
    action3_trialComponents = [slide_3]
    for thisComponent in action3_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    action3_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "action3_trial"-------
    while continueRoutine:
        # get current time
        t = action3_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=action3_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slide_3* updates
        if slide_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slide_3.frameNStart = frameN  # exact frame index
            slide_3.tStart = t  # local t and not account for scr refresh
            slide_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slide_3, 'tStartRefresh')  # time at next scr refresh
            slide_3.setAutoDraw(True)
        if slide_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slide_3.tStartRefresh + action_dur-frameTolerance:
                # keep track of stop time/frame for later
                slide_3.tStop = t  # not accounting for scr refresh
                slide_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(slide_3, 'tStopRefresh')  # time at next scr refresh
                slide_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in action3_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "action3_trial"-------
    for thisComponent in action3_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "action3_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "target_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_slide.setSize((16*x_scale, 12*y_scale))
    target_slide.setImage(target_file)
    # keep track of which components have finished
    target_trialComponents = [target_slide]
    for thisComponent in target_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    target_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "target_trial"-------
    while continueRoutine:
        # get current time
        t = target_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=target_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_slide* updates
        if target_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_slide.frameNStart = frameN  # exact frame index
            target_slide.tStart = t  # local t and not account for scr refresh
            target_slide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_slide, 'tStartRefresh')  # time at next scr refresh
            target_slide.setAutoDraw(True)
        if target_slide.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_slide.tStartRefresh + target_dur-frameTolerance:
                # keep track of stop time/frame for later
                target_slide.tStop = t  # not accounting for scr refresh
                target_slide.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_slide, 'tStopRefresh')  # time at next scr refresh
                target_slide.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in target_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "target_trial"-------
    for thisComponent in target_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "target_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_resp.keys = []
    target_resp.rt = []
    _target_resp_allKeys = []
    # keep track of which components have finished
    responseComponents = [prompt_target, target_resp]
    for thisComponent in responseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response"-------
    while continueRoutine:
        # get current time
        t = responseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt_target* updates
        if prompt_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_target.frameNStart = frameN  # exact frame index
            prompt_target.tStart = t  # local t and not account for scr refresh
            prompt_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_target, 'tStartRefresh')  # time at next scr refresh
            prompt_target.setAutoDraw(True)
        
        # *target_resp* updates
        waitOnFlip = False
        if target_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_resp.frameNStart = frameN  # exact frame index
            target_resp.tStart = t  # local t and not account for scr refresh
            target_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_resp, 'tStartRefresh')  # time at next scr refresh
            target_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(target_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(target_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if target_resp.status == STARTED and not waitOnFlip:
            theseKeys = target_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _target_resp_allKeys.extend(theseKeys)
            if len(_target_resp_allKeys):
                target_resp.keys = _target_resp_allKeys[-1].name  # just the last key pressed
                target_resp.rt = _target_resp_allKeys[-1].rt
                # was this correct?
                if (target_resp.keys == str(corr_ans)) or (target_resp.keys == corr_ans):
                    target_resp.corr = 1
                else:
                    target_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response"-------
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if target_resp.keys in ['', [], None]:  # No response was made
        target_resp.keys = None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           target_resp.corr = 1;  # correct non-response
        else:
           target_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('target_resp.keys',target_resp.keys)
    practice_trials.addData('target_resp.corr', target_resp.corr)
    if target_resp.keys != None:  # we had a response
        practice_trials.addData('target_resp.rt', target_resp.rt)
    if not target_resp.keys :
        msg="Failed to respond"
    elif target_resp.corr:#stored on last run routine
        msg="Correct!" 
    else:
        msg="Oops! That was wrong."
    # the Routine "response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedb_text_obj.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedb_text_obj]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedb_text_obj* updates
        if feedb_text_obj.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedb_text_obj.frameNStart = frameN  # exact frame index
            feedb_text_obj.tStart = t  # local t and not account for scr refresh
            feedb_text_obj.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedb_text_obj, 'tStartRefresh')  # time at next scr refresh
            feedb_text_obj.setAutoDraw(True)
        if feedb_text_obj.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedb_text_obj.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedb_text_obj.tStop = t  # not accounting for scr refresh
                feedb_text_obj.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedb_text_obj, 'tStopRefresh')  # time at next scr refresh
                feedb_text_obj.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice_trials'

# get names of stimulus parameters
if practice_trials.trialList in ([], [None], None):
    params = []
else:
    params = practice_trials.trialList[0].keys()
# save data for this loop
practice_trials.saveAsExcel(filename + '.xlsx', sheetName='practice_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "practice_end"-------
continueRoutine = True
# update component parameters for each repeat
warning_2.setText('You have completed all the practice trials. Now the actual task will begin. \n\nAre you ready?')
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
ready_text_2.setText('<Press the space bar to continue>')
# keep track of which components have finished
practice_endComponents = [warning_2, key_resp, ready_text_2]
for thisComponent in practice_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_end"-------
while continueRoutine:
    # get current time
    t = practice_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *warning_2* updates
    if warning_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        warning_2.frameNStart = frameN  # exact frame index
        warning_2.tStart = t  # local t and not account for scr refresh
        warning_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(warning_2, 'tStartRefresh')  # time at next scr refresh
        warning_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ready_text_2* updates
    if ready_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready_text_2.frameNStart = frameN  # exact frame index
        ready_text_2.tStart = t  # local t and not account for scr refresh
        ready_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready_text_2, 'tStartRefresh')  # time at next scr refresh
        ready_text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_end"-------
for thisComponent in practice_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixcross_display"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixcross_displayComponents = [fix]
    for thisComponent in fixcross_displayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixcross_displayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixcross_display"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixcross_displayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixcross_displayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixcross_displayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixcross_display"-------
    for thisComponent in fixcross_displayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "cue_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    cue_slide.setSize((16*x_scale, 12*y_scale))
    cue_slide.setImage(cue_file)
    # keep track of which components have finished
    cue_trialComponents = [cue_slide]
    for thisComponent in cue_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cue_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "cue_trial"-------
    while continueRoutine:
        # get current time
        t = cue_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cue_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_slide* updates
        if cue_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_slide.frameNStart = frameN  # exact frame index
            cue_slide.tStart = t  # local t and not account for scr refresh
            cue_slide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_slide, 'tStartRefresh')  # time at next scr refresh
            cue_slide.setAutoDraw(True)
        if cue_slide.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_slide.tStartRefresh + cue_dur-frameTolerance:
                # keep track of stop time/frame for later
                cue_slide.tStop = t  # not accounting for scr refresh
                cue_slide.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_slide, 'tStopRefresh')  # time at next scr refresh
                cue_slide.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cue_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue_trial"-------
    for thisComponent in cue_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "cue_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "action1_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    slide_1.setSize((16*x_scale, 12*y_scale))
    slide_1.setImage(action1)
    # keep track of which components have finished
    action1_trialComponents = [slide_1]
    for thisComponent in action1_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    action1_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "action1_trial"-------
    while continueRoutine:
        # get current time
        t = action1_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=action1_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slide_1* updates
        if slide_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slide_1.frameNStart = frameN  # exact frame index
            slide_1.tStart = t  # local t and not account for scr refresh
            slide_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slide_1, 'tStartRefresh')  # time at next scr refresh
            slide_1.setAutoDraw(True)
        if slide_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slide_1.tStartRefresh + action_dur-frameTolerance:
                # keep track of stop time/frame for later
                slide_1.tStop = t  # not accounting for scr refresh
                slide_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(slide_1, 'tStopRefresh')  # time at next scr refresh
                slide_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in action1_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "action1_trial"-------
    for thisComponent in action1_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "action1_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "action2_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    slide_2.setSize((16*x_scale, 12*y_scale))
    slide_2.setImage(action2)
    # keep track of which components have finished
    action2_trialComponents = [slide_2]
    for thisComponent in action2_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    action2_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "action2_trial"-------
    while continueRoutine:
        # get current time
        t = action2_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=action2_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slide_2* updates
        if slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slide_2.frameNStart = frameN  # exact frame index
            slide_2.tStart = t  # local t and not account for scr refresh
            slide_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slide_2, 'tStartRefresh')  # time at next scr refresh
            slide_2.setAutoDraw(True)
        if slide_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slide_2.tStartRefresh + action_dur-frameTolerance:
                # keep track of stop time/frame for later
                slide_2.tStop = t  # not accounting for scr refresh
                slide_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(slide_2, 'tStopRefresh')  # time at next scr refresh
                slide_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in action2_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "action2_trial"-------
    for thisComponent in action2_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "action2_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "action3_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    slide_3.setSize((16*x_scale, 12*y_scale))
    slide_3.setImage(action3)
    # keep track of which components have finished
    action3_trialComponents = [slide_3]
    for thisComponent in action3_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    action3_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "action3_trial"-------
    while continueRoutine:
        # get current time
        t = action3_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=action3_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slide_3* updates
        if slide_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slide_3.frameNStart = frameN  # exact frame index
            slide_3.tStart = t  # local t and not account for scr refresh
            slide_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slide_3, 'tStartRefresh')  # time at next scr refresh
            slide_3.setAutoDraw(True)
        if slide_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slide_3.tStartRefresh + action_dur-frameTolerance:
                # keep track of stop time/frame for later
                slide_3.tStop = t  # not accounting for scr refresh
                slide_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(slide_3, 'tStopRefresh')  # time at next scr refresh
                slide_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in action3_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "action3_trial"-------
    for thisComponent in action3_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "action3_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "target_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_slide.setSize((16*x_scale, 12*y_scale))
    target_slide.setImage(target_file)
    # keep track of which components have finished
    target_trialComponents = [target_slide]
    for thisComponent in target_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    target_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "target_trial"-------
    while continueRoutine:
        # get current time
        t = target_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=target_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_slide* updates
        if target_slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_slide.frameNStart = frameN  # exact frame index
            target_slide.tStart = t  # local t and not account for scr refresh
            target_slide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_slide, 'tStartRefresh')  # time at next scr refresh
            target_slide.setAutoDraw(True)
        if target_slide.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target_slide.tStartRefresh + target_dur-frameTolerance:
                # keep track of stop time/frame for later
                target_slide.tStop = t  # not accounting for scr refresh
                target_slide.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_slide, 'tStopRefresh')  # time at next scr refresh
                target_slide.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in target_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "target_trial"-------
    for thisComponent in target_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "target_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_resp.keys = []
    target_resp.rt = []
    _target_resp_allKeys = []
    # keep track of which components have finished
    responseComponents = [prompt_target, target_resp]
    for thisComponent in responseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response"-------
    while continueRoutine:
        # get current time
        t = responseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt_target* updates
        if prompt_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prompt_target.frameNStart = frameN  # exact frame index
            prompt_target.tStart = t  # local t and not account for scr refresh
            prompt_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_target, 'tStartRefresh')  # time at next scr refresh
            prompt_target.setAutoDraw(True)
        
        # *target_resp* updates
        waitOnFlip = False
        if target_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_resp.frameNStart = frameN  # exact frame index
            target_resp.tStart = t  # local t and not account for scr refresh
            target_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_resp, 'tStartRefresh')  # time at next scr refresh
            target_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(target_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(target_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if target_resp.status == STARTED and not waitOnFlip:
            theseKeys = target_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _target_resp_allKeys.extend(theseKeys)
            if len(_target_resp_allKeys):
                target_resp.keys = _target_resp_allKeys[-1].name  # just the last key pressed
                target_resp.rt = _target_resp_allKeys[-1].rt
                # was this correct?
                if (target_resp.keys == str(corr_ans)) or (target_resp.keys == corr_ans):
                    target_resp.corr = 1
                else:
                    target_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response"-------
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if target_resp.keys in ['', [], None]:  # No response was made
        target_resp.keys = None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           target_resp.corr = 1;  # correct non-response
        else:
           target_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('target_resp.keys',target_resp.keys)
    trials.addData('target_resp.corr', target_resp.corr)
    if target_resp.keys != None:  # we had a response
        trials.addData('target_resp.rt', target_resp.rt)
    if not target_resp.keys :
        msg="Failed to respond"
    elif target_resp.corr:#stored on last run routine
        msg="Correct!" 
    else:
        msg="Oops! That was wrong."
    # the Routine "response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "bye"-------
continueRoutine = True
# update component parameters for each repeat
text_2.setText('Well done!\nThis first part has finished. Go back to the online room to get the instructions for the next phase.\n\nRemember that the data will be saved after you exit the fullscreen. Please, do not manually close the window until the data has finished saving.\n\nPress any key to exit the fullscreen mode.')
welcome_resp1_2.keys = []
welcome_resp1_2.rt = []
_welcome_resp1_2_allKeys = []
# keep track of which components have finished
byeComponents = [text_2, welcome_resp1_2]
for thisComponent in byeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
byeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "bye"-------
while continueRoutine:
    # get current time
    t = byeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=byeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *welcome_resp1_2* updates
    waitOnFlip = False
    if welcome_resp1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp1_2.frameNStart = frameN  # exact frame index
        welcome_resp1_2.tStart = t  # local t and not account for scr refresh
        welcome_resp1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp1_2, 'tStartRefresh')  # time at next scr refresh
        welcome_resp1_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_resp1_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_resp1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_resp1_2.status == STARTED and not waitOnFlip:
        theseKeys = welcome_resp1_2.getKeys(keyList=['space'], waitRelease=False)
        _welcome_resp1_2_allKeys.extend(theseKeys)
        if len(_welcome_resp1_2_allKeys):
            welcome_resp1_2.keys = _welcome_resp1_2_allKeys[-1].name  # just the last key pressed
            welcome_resp1_2.rt = _welcome_resp1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in byeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bye"-------
for thisComponent in byeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "bye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
