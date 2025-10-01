#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Fri Sep 17 15:35:40 2021
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
expName = 'sdp_ses-01_part-01_label-retrieval'  # from the Builder filename that created this script
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
    originPath='/Users/javierortiz/pavlovia/sdp_ses-01_part-01_label-retrieval/sdp_ses-01_part-01_label-retrieval_lastrun.py',
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
    size=[1680, 1050], fullscr=True, screen=0, 
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
scn_size = (0.8,0.6)
story_rec_dur = 10
central_recall_dur = 10
ending_recall_dur = 10
target_trial_dur = 10
fix_dur = .5
choice_size = (0.3,0.3)
pos_left = (-0.5,-0.3)
pos_center = (0,-0.3)
pos_right = (0.5,-0.3)
prompt_pos = (0,-0.4)
prompt_size = 0.025
afc_cue_size = (0.7,0.5)
afc_cue_pos = (0,.2)
inst_file='condition_files/instructions.csv'
cond_file='condition_files/enc_1_list.csv'


# Initialize components for Routine "hello"
helloClock = core.Clock()
text_hi = visual.TextStim(win=win, name='text_hi',
    text='Dear participant,\n\nSame as in the previous task, before we start, we will determine your monitor size.  After this, you will read the new instructions and then we will proceed with the task.\n\n<Press the space bar to continue>\n',
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

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
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
    units='height', pos=(0,0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "fixcross_display"
fixcross_displayClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
#cue_file="stim/" + comic_name + "Slide-01.png"
#action1="stim/" + comic_name + "Slide-02.png"
#action2="stim/" + comic_name + "Slide-03.png"
#action3="stim/" + comic_name + "Slide-04.png"
#target_file="stim/" + comic_name + "Slide-06.png"

# Initialize components for Routine "story_rec"
story_recClock = core.Clock()
cue_slide = visual.ImageStim(
    win=win,
    name='cue_slide', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
story_rec_prompt = visual.TextStim(win=win, name='story_rec_prompt',
    text='Have you seen this story before?\n\nleft = "yes"; right = "no"',
    font='Open Sans',
    pos=(0,-0.15), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
story_rec_resp = keyboard.Keyboard()

# Initialize components for Routine "central_recall"
central_recallClock = core.Clock()
cue_slide_2 = visual.ImageStim(
    win=win,
    name='cue_slide_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
central_recall_resp = keyboard.Keyboard()
central_recall_textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0,-.3),     letterHeight=0.025,
     size=(0.5,0.2), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='central_recall_textbox',
     autoLog=True,
)
central_recall_prompt = visual.TextStim(win=win, name='central_recall_prompt',
    text='Which object was exchanged in this comic?\nType your one or two words below or press ENTER if you do not remember.',
    font='Open Sans',
    pos=(0,-0.15), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ending_recall"
ending_recallClock = core.Clock()
cue_slide_3 = visual.ImageStim(
    win=win,
    name='cue_slide_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
ending_rec_prompt_2 = visual.TextStim(win=win, name='ending_rec_prompt_2',
    text='Did the object reach the intended person?\n\nleft = "yes"; right = "no"',
    font='Open Sans',
    pos=(0,-0.15), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ending_rec_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "target_trial"
target_trialClock = core.Clock()
target_trial_cue = visual.ImageStim(
    win=win,
    name='target_trial_cue', 
    image='sin', mask=None,
    ori=0, pos=(0,0.2), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
choice_left_disp = visual.ImageStim(
    win=win,
    name='choice_left_disp', 
    image='sin', mask=None,
    ori=0, pos=(-0.5,-0.3), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
choice_center_disp = visual.ImageStim(
    win=win,
    name='choice_center_disp', 
    image='sin', mask=None,
    ori=0, pos=(0,-0.3), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
choice_right_disp = visual.ImageStim(
    win=win,
    name='choice_right_disp', 
    image='sin', mask=None,
    ori=0, pos=(0.5,-0.3), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
afc_prompt = visual.TextStim(win=win, name='afc_prompt',
    text='How did the story end?',
    font='Open Sans',
    pos=(0,-0.1), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
afc_resp = keyboard.Keyboard()
reminder_1 = visual.TextStim(win=win, name='reminder_1',
    text='1',
    font='Open Sans',
    pos=(-0.5,-0.125), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
reminder_2 = visual.TextStim(win=win, name='reminder_2',
    text='2',
    font='Open Sans',
    pos=(0,-0.125), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
reminder_3 = visual.TextStim(win=win, name='reminder_3',
    text='3',
    font='Open Sans',
    pos=(0.5,-0.125), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Congratulations!\n\nYou have completed the task.\n\nRemember that the data will be saved after you exit the fullscreen. Please, do not manually close the window until the data has finished saving.\n\nThank you very much for participating.\n\nPress any key to exit the fullscreen mode',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

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
thisExp.addData('text_hi.started', text_hi.tStartRefresh)
thisExp.addData('text_hi.stopped', text_hi.tStopRefresh)
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
    
    # ------Prepare to start Routine "Welcome"-------
    continueRoutine = True
    # update component parameters for each repeat
    text.setText(inst_text)
    welcome_resp1.keys = []
    welcome_resp1.rt = []
    _welcome_resp1_allKeys = []
    # keep track of which components have finished
    WelcomeComponents = [text, welcome_resp1]
    for thisComponent in WelcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Welcome"-------
    while continueRoutine:
        # get current time
        t = WelcomeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
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
        for thisComponent in WelcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Welcome"-------
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
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
warning.setText('Ready to start?')
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
readyComponents = [warning, key_resp_6]
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
    
    # ------Prepare to start Routine "story_rec"-------
    continueRoutine = True
    # update component parameters for each repeat
    cue_slide.setSize((14*x_scale, 10*y_scale))
    cue_slide.setImage(cue_file)
    story_rec_resp.keys = []
    story_rec_resp.rt = []
    _story_rec_resp_allKeys = []
    # keep track of which components have finished
    story_recComponents = [cue_slide, story_rec_prompt, story_rec_resp]
    for thisComponent in story_recComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    story_recClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "story_rec"-------
    while continueRoutine:
        # get current time
        t = story_recClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=story_recClock)
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
        
        # *story_rec_prompt* updates
        if story_rec_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            story_rec_prompt.frameNStart = frameN  # exact frame index
            story_rec_prompt.tStart = t  # local t and not account for scr refresh
            story_rec_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(story_rec_prompt, 'tStartRefresh')  # time at next scr refresh
            story_rec_prompt.setAutoDraw(True)
        
        # *story_rec_resp* updates
        waitOnFlip = False
        if story_rec_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            story_rec_resp.frameNStart = frameN  # exact frame index
            story_rec_resp.tStart = t  # local t and not account for scr refresh
            story_rec_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(story_rec_resp, 'tStartRefresh')  # time at next scr refresh
            story_rec_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(story_rec_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(story_rec_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if story_rec_resp.status == STARTED and not waitOnFlip:
            theseKeys = story_rec_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _story_rec_resp_allKeys.extend(theseKeys)
            if len(_story_rec_resp_allKeys):
                story_rec_resp.keys = _story_rec_resp_allKeys[-1].name  # just the last key pressed
                story_rec_resp.rt = _story_rec_resp_allKeys[-1].rt
                # was this correct?
                if (story_rec_resp.keys == str(story_rec_corr)) or (story_rec_resp.keys == story_rec_corr):
                    story_rec_resp.corr = 1
                else:
                    story_rec_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in story_recComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "story_rec"-------
    for thisComponent in story_recComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('story_rec_prompt.started', story_rec_prompt.tStartRefresh)
    trials.addData('story_rec_prompt.stopped', story_rec_prompt.tStopRefresh)
    # check responses
    if story_rec_resp.keys in ['', [], None]:  # No response was made
        story_rec_resp.keys = None
        # was no response the correct answer?!
        if str(story_rec_corr).lower() == 'none':
           story_rec_resp.corr = 1;  # correct non-response
        else:
           story_rec_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('story_rec_resp.keys',story_rec_resp.keys)
    trials.addData('story_rec_resp.corr', story_rec_resp.corr)
    if story_rec_resp.keys != None:  # we had a response
        trials.addData('story_rec_resp.rt', story_rec_resp.rt)
    # the Routine "story_rec" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "central_recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    cue_slide_2.setSize((14*x_scale, 10*y_scale))
    cue_slide_2.setImage(cue_file)
    central_recall_resp.keys = []
    central_recall_resp.rt = []
    _central_recall_resp_allKeys = []
    central_recall_textbox.text = ""
    if OvsN_code == 0:
        continue
    
    # keep track of which components have finished
    central_recallComponents = [cue_slide_2, central_recall_resp, central_recall_textbox, central_recall_prompt]
    for thisComponent in central_recallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    central_recallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "central_recall"-------
    while continueRoutine:
        # get current time
        t = central_recallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=central_recallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_slide_2* updates
        if cue_slide_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_slide_2.frameNStart = frameN  # exact frame index
            cue_slide_2.tStart = t  # local t and not account for scr refresh
            cue_slide_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_slide_2, 'tStartRefresh')  # time at next scr refresh
            cue_slide_2.setAutoDraw(True)
        
        # *central_recall_resp* updates
        waitOnFlip = False
        if central_recall_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            central_recall_resp.frameNStart = frameN  # exact frame index
            central_recall_resp.tStart = t  # local t and not account for scr refresh
            central_recall_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(central_recall_resp, 'tStartRefresh')  # time at next scr refresh
            central_recall_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(central_recall_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(central_recall_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if central_recall_resp.status == STARTED and not waitOnFlip:
            theseKeys = central_recall_resp.getKeys(keyList=['return'], waitRelease=False)
            _central_recall_resp_allKeys.extend(theseKeys)
            if len(_central_recall_resp_allKeys):
                central_recall_resp.keys = [key.name for key in _central_recall_resp_allKeys]  # storing all keys
                central_recall_resp.rt = [key.rt for key in _central_recall_resp_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # *central_recall_textbox* updates
        if central_recall_textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            central_recall_textbox.frameNStart = frameN  # exact frame index
            central_recall_textbox.tStart = t  # local t and not account for scr refresh
            central_recall_textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(central_recall_textbox, 'tStartRefresh')  # time at next scr refresh
            central_recall_textbox.setAutoDraw(True)
        
        # *central_recall_prompt* updates
        if central_recall_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            central_recall_prompt.frameNStart = frameN  # exact frame index
            central_recall_prompt.tStart = t  # local t and not account for scr refresh
            central_recall_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(central_recall_prompt, 'tStartRefresh')  # time at next scr refresh
            central_recall_prompt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in central_recallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "central_recall"-------
    for thisComponent in central_recallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if central_recall_resp.keys in ['', [], None]:  # No response was made
        central_recall_resp.keys = None
    trials.addData('central_recall_resp.keys',central_recall_resp.keys)
    if central_recall_resp.keys != None:  # we had a response
        trials.addData('central_recall_resp.rt', central_recall_resp.rt)
    trials.addData('central_recall_textbox.text',central_recall_textbox.text)
    central_recall_textbox.reset()
    trials.addData('central_recall_textbox.started', central_recall_textbox.tStartRefresh)
    trials.addData('central_recall_textbox.stopped', central_recall_textbox.tStopRefresh)
    trials.addData('central_recall_prompt.started', central_recall_prompt.tStartRefresh)
    trials.addData('central_recall_prompt.stopped', central_recall_prompt.tStopRefresh)
    # the Routine "central_recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ending_recall"-------
    continueRoutine = True
    # update component parameters for each repeat
    cue_slide_3.setSize((14*x_scale, 10*y_scale))
    cue_slide_3.setImage(cue_file)
    ending_rec_resp_2.keys = []
    ending_rec_resp_2.rt = []
    _ending_rec_resp_2_allKeys = []
    if OvsN_code == 0:
        continue
    # keep track of which components have finished
    ending_recallComponents = [cue_slide_3, ending_rec_prompt_2, ending_rec_resp_2]
    for thisComponent in ending_recallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ending_recallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ending_recall"-------
    while continueRoutine:
        # get current time
        t = ending_recallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ending_recallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_slide_3* updates
        if cue_slide_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_slide_3.frameNStart = frameN  # exact frame index
            cue_slide_3.tStart = t  # local t and not account for scr refresh
            cue_slide_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_slide_3, 'tStartRefresh')  # time at next scr refresh
            cue_slide_3.setAutoDraw(True)
        
        # *ending_rec_prompt_2* updates
        if ending_rec_prompt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ending_rec_prompt_2.frameNStart = frameN  # exact frame index
            ending_rec_prompt_2.tStart = t  # local t and not account for scr refresh
            ending_rec_prompt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ending_rec_prompt_2, 'tStartRefresh')  # time at next scr refresh
            ending_rec_prompt_2.setAutoDraw(True)
        
        # *ending_rec_resp_2* updates
        waitOnFlip = False
        if ending_rec_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ending_rec_resp_2.frameNStart = frameN  # exact frame index
            ending_rec_resp_2.tStart = t  # local t and not account for scr refresh
            ending_rec_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ending_rec_resp_2, 'tStartRefresh')  # time at next scr refresh
            ending_rec_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ending_rec_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ending_rec_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ending_rec_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = ending_rec_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _ending_rec_resp_2_allKeys.extend(theseKeys)
            if len(_ending_rec_resp_2_allKeys):
                ending_rec_resp_2.keys = _ending_rec_resp_2_allKeys[-1].name  # just the last key pressed
                ending_rec_resp_2.rt = _ending_rec_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ending_recallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ending_recall"-------
    for thisComponent in ending_recallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('ending_rec_prompt_2.started', ending_rec_prompt_2.tStartRefresh)
    trials.addData('ending_rec_prompt_2.stopped', ending_rec_prompt_2.tStopRefresh)
    # check responses
    if ending_rec_resp_2.keys in ['', [], None]:  # No response was made
        ending_rec_resp_2.keys = None
    trials.addData('ending_rec_resp_2.keys',ending_rec_resp_2.keys)
    if ending_rec_resp_2.keys != None:  # we had a response
        trials.addData('ending_rec_resp_2.rt', ending_rec_resp_2.rt)
    # the Routine "ending_recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "target_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    target_trial_cue.setSize((14*x_scale, 10*y_scale))
    target_trial_cue.setImage(cue_file)
    choice_left_disp.setSize((6*x_scale, 6*y_scale))
    choice_left_disp.setImage(choice_left)
    choice_center_disp.setSize((6*x_scale, 6*y_scale))
    choice_center_disp.setImage(choice_center)
    choice_right_disp.setSize((6*x_scale, 6*y_scale))
    choice_right_disp.setImage(choice_right)
    afc_resp.keys = []
    afc_resp.rt = []
    _afc_resp_allKeys = []
    if OvsN_code == 0:
        continue
    # keep track of which components have finished
    target_trialComponents = [target_trial_cue, choice_left_disp, choice_center_disp, choice_right_disp, afc_prompt, afc_resp, reminder_1, reminder_2, reminder_3]
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
        
        # *target_trial_cue* updates
        if target_trial_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_trial_cue.frameNStart = frameN  # exact frame index
            target_trial_cue.tStart = t  # local t and not account for scr refresh
            target_trial_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_trial_cue, 'tStartRefresh')  # time at next scr refresh
            target_trial_cue.setAutoDraw(True)
        
        # *choice_left_disp* updates
        if choice_left_disp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_left_disp.frameNStart = frameN  # exact frame index
            choice_left_disp.tStart = t  # local t and not account for scr refresh
            choice_left_disp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_left_disp, 'tStartRefresh')  # time at next scr refresh
            choice_left_disp.setAutoDraw(True)
        
        # *choice_center_disp* updates
        if choice_center_disp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_center_disp.frameNStart = frameN  # exact frame index
            choice_center_disp.tStart = t  # local t and not account for scr refresh
            choice_center_disp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_center_disp, 'tStartRefresh')  # time at next scr refresh
            choice_center_disp.setAutoDraw(True)
        
        # *choice_right_disp* updates
        if choice_right_disp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_right_disp.frameNStart = frameN  # exact frame index
            choice_right_disp.tStart = t  # local t and not account for scr refresh
            choice_right_disp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_right_disp, 'tStartRefresh')  # time at next scr refresh
            choice_right_disp.setAutoDraw(True)
        
        # *afc_prompt* updates
        if afc_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            afc_prompt.frameNStart = frameN  # exact frame index
            afc_prompt.tStart = t  # local t and not account for scr refresh
            afc_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_prompt, 'tStartRefresh')  # time at next scr refresh
            afc_prompt.setAutoDraw(True)
        
        # *afc_resp* updates
        waitOnFlip = False
        if afc_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            afc_resp.frameNStart = frameN  # exact frame index
            afc_resp.tStart = t  # local t and not account for scr refresh
            afc_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_resp, 'tStartRefresh')  # time at next scr refresh
            afc_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(afc_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(afc_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if afc_resp.status == STARTED and not waitOnFlip:
            theseKeys = afc_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _afc_resp_allKeys.extend(theseKeys)
            if len(_afc_resp_allKeys):
                afc_resp.keys = _afc_resp_allKeys[-1].name  # just the last key pressed
                afc_resp.rt = _afc_resp_allKeys[-1].rt
                # was this correct?
                if (afc_resp.keys == str(afc_corr)) or (afc_resp.keys == afc_corr):
                    afc_resp.corr = 1
                else:
                    afc_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *reminder_1* updates
        if reminder_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reminder_1.frameNStart = frameN  # exact frame index
            reminder_1.tStart = t  # local t and not account for scr refresh
            reminder_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminder_1, 'tStartRefresh')  # time at next scr refresh
            reminder_1.setAutoDraw(True)
        
        # *reminder_2* updates
        if reminder_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reminder_2.frameNStart = frameN  # exact frame index
            reminder_2.tStart = t  # local t and not account for scr refresh
            reminder_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminder_2, 'tStartRefresh')  # time at next scr refresh
            reminder_2.setAutoDraw(True)
        
        # *reminder_3* updates
        if reminder_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reminder_3.frameNStart = frameN  # exact frame index
            reminder_3.tStart = t  # local t and not account for scr refresh
            reminder_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reminder_3, 'tStartRefresh')  # time at next scr refresh
            reminder_3.setAutoDraw(True)
        
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
    trials.addData('afc_prompt.started', afc_prompt.tStartRefresh)
    trials.addData('afc_prompt.stopped', afc_prompt.tStopRefresh)
    # check responses
    if afc_resp.keys in ['', [], None]:  # No response was made
        afc_resp.keys = None
        # was no response the correct answer?!
        if str(afc_corr).lower() == 'none':
           afc_resp.corr = 1;  # correct non-response
        else:
           afc_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('afc_resp.keys',afc_resp.keys)
    trials.addData('afc_resp.corr', afc_resp.corr)
    if afc_resp.keys != None:  # we had a response
        trials.addData('afc_resp.rt', afc_resp.rt)
    trials.addData('reminder_1.started', reminder_1.tStartRefresh)
    trials.addData('reminder_1.stopped', reminder_1.tStopRefresh)
    trials.addData('reminder_2.started', reminder_2.tStartRefresh)
    trials.addData('reminder_2.stopped', reminder_2.tStopRefresh)
    trials.addData('reminder_3.started', reminder_3.tStartRefresh)
    trials.addData('reminder_3.stopped', reminder_3.tStopRefresh)
    # the Routine "target_trial" was not non-slip safe, so reset the non-slip timer
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

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
endComponents = [end_text, key_resp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
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
