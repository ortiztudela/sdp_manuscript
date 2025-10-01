/****************************************** 
 * Sdp_Ses-01_Part-01_Label-Encoding Test *
 ******************************************/

import { PsychoJS } from './lib/core-2021.1.4.js';
import * as core from './lib/core-2021.1.4.js';
import { TrialHandler } from './lib/data-2021.1.4.js';
import { Scheduler } from './lib/util-2021.1.4.js';
import * as visual from './lib/visual-2021.1.4.js';
import * as sound from './lib/sound-2021.1.4.js';
import * as util from './lib/util-2021.1.4.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('gray'),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'sdp_ses-01_part-01_label-encoding';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(initializeRoutineBegin());
flowScheduler.add(initializeRoutineEachFrame());
flowScheduler.add(initializeRoutineEnd());
flowScheduler.add(helloRoutineBegin());
flowScheduler.add(helloRoutineEachFrame());
flowScheduler.add(helloRoutineEnd());
flowScheduler.add(screen_scaleRoutineBegin());
flowScheduler.add(screen_scaleRoutineEachFrame());
flowScheduler.add(screen_scaleRoutineEnd());
const welcome_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(welcome_loopLoopBegin, welcome_loopLoopScheduler);
flowScheduler.add(welcome_loopLoopScheduler);
flowScheduler.add(welcome_loopLoopEnd);
flowScheduler.add(readyRoutineBegin());
flowScheduler.add(readyRoutineEachFrame());
flowScheduler.add(readyRoutineEnd());
const practice_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_trialsLoopBegin, practice_trialsLoopScheduler);
flowScheduler.add(practice_trialsLoopScheduler);
flowScheduler.add(practice_trialsLoopEnd);
flowScheduler.add(practice_endRoutineBegin());
flowScheduler.add(practice_endRoutineEachFrame());
flowScheduler.add(practice_endRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(byeRoutineBegin());
flowScheduler.add(byeRoutineEachFrame());
flowScheduler.add(byeRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var initializeClock;
var obj_size;
var scn_size;
var cue_dur;
var action_dur;
var target_dur;
var fix_dur;
var prompt_pos;
var prompt_size;
var inst_file;
var cond_file;
var trial_index;
var helloClock;
var text_hi;
var key_resp_hi;
var screen_scaleClock;
var event;
var thisExp;
var win;
var oldt;
var x_size;
var y_size;
var screen_height;
var x_scale;
var y_scale;
var dbase;
var unittext;
var vsize;
var text_top;
var text_bottom;
var ccimage;
var welcomeClock;
var text_comp;
var welcome_resp1;
var readyClock;
var warning;
var key_resp_6;
var ready_text;
var fixcross_displayClock;
var fix;
var cue_trialClock;
var cue_slide;
var action1_trialClock;
var slide_1;
var action2_trialClock;
var slide_2;
var action3_trialClock;
var slide_3;
var target_trialClock;
var target_slide;
var responseClock;
var prompt_target;
var target_resp;
var feedbackClock;
var feedb_text_obj;
var practice_endClock;
var warning_2;
var key_resp;
var ready_text_2;
var byeClock;
var text_2;
var welcome_resp1_2;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "initialize"
  initializeClock = new util.Clock();
  obj_size = [0.4,0.3];
  scn_size = [.8,0.6];
  cue_dur = 2.5;
  action_dur = 0.85;
  target_dur = 2.5;
  fix_dur = 0.5;
  
  prompt_pos = [0, 0];
  prompt_size = 0.025;
  inst_file = ("condition_files/instructions.xlsx");
  if (((Number.parseInt(expInfo["participant"]) % 12) === 1)) {
     cond_file = (("condition_files/enc_1_list.csv"));
  } else {
     if (((Number.parseInt(expInfo["participant"]) % 12) === 2)) {
        cond_file = (("condition_files/enc_2_list.csv"));
     } else {
        if (((Number.parseInt(expInfo["participant"]) % 12) === 3)) {
           cond_file = (("condition_files/enc_3_list.csv"));
        } else {
           if (((Number.parseInt(expInfo["participant"]) % 12) === 4)) {
              cond_file = (("condition_files/enc_4_list.csv"));
           } else {
              if (((Number.parseInt(expInfo["participant"]) % 12) === 5)) {
                 cond_file = (("condition_files/enc_5_list.csv"));
              } else {
                 if (((Number.parseInt(expInfo["participant"]) % 12) === 6)) {
                    cond_file = (("condition_files/enc_6_list.csv"));
                 } else {
                    if (((Number.parseInt(expInfo["participant"]) % 12) === 7)) {
                       cond_file = (("condition_files/enc_7_list.csv"));
                    } else {
                       if (((Number.parseInt(expInfo["participant"]) % 12) === 8)) {
                          cond_file = (("condition_files/enc_8_list.csv"));
                       } else {
                          if (((Number.parseInt(expInfo["participant"]) % 12) === 9)) {
                             cond_file = (("condition_files/enc_9_list.csv"));
                          } else {
                             if (((Number.parseInt(expInfo["participant"]) % 12) === 10)) {
                                cond_file = (("condition_files/enc_10_list.csv"));
                             } else {
                                if (((Number.parseInt(expInfo["participant"]) % 12) === 11)) {
                                   cond_file = (("condition_files/enc_11_list.csv"));
                                } else {
                                   if (((Number.parseInt(expInfo["participant"]) % 12) === 0)) {
                                      cond_file = (("condition_files/enc_12_list.csv"));
                                   }
                                }
                             }
                          }
                       }
                    }
                 }
              }
           }
        }
     }
  }
  trial_index = 0;
  // Initialize components for Routine "hello"
  helloClock = new util.Clock();
  text_hi = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_hi',
    text: 'Liebe/r Teilnehmer/in,\n\nbevor wir anfangen, werden wir die Größe Ihres Monitors bestimmen. Danach werden Sie Instruktionen für die Studie bekommen und schließlich mit der Aufgabe beginnen.\n\n< Drücken Sie die Leertaste um fortzufahren >\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.02,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_hi = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "screen_scale"
  screen_scaleClock = new util.Clock();
  event=psychoJS.eventManager;
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  
  
  oldt = 0;
  x_size = 8.56;
  y_size = 5.398;
  screen_height = 0;
  if ((win.units === "norm")) {
      x_scale = 0.05;
      y_scale = 0.1;
      dbase = 0.0001;
      unittext = " norm units";
      vsize = 2;
  } else {
      if ((win.units === "pix")) {
          x_scale = 60;
          y_scale = 40;
          dbase = 0.1;
          unittext = " pixels";
          vsize = win.size[1];
      } else {
          x_scale = 0.05;
          y_scale = 0.05;
          dbase = 0.0001;
          unittext = " height units";
          vsize = 1;
      }
  }
  
  text_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_top',
    text: 'Skalieren Sie bitte dieses Bild so, dass es der Größe einer Kreditkarte entspricht.\nPfeiltaste nach oben für höher\nPfeiltaste nach unten für kürzer\nPfeiltaste nach links für schmaler\nPfeiltaste nach rechts für breiter',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.7], height: 0.05,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_bottom = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_bottom',
    text: 'Drücken Sie die Leertaste, wenn Sie fertig sind.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.6)], height: 0.05,  wrapWidth: 1.5, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  ccimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ccimage', units : undefined, 
    image : 'bank-1300155_640.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [(x_size * x_scale), (y_size * y_scale)],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  text_comp = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_comp',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  welcome_resp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ready"
  readyClock = new util.Clock();
  warning = new visual.TextStim({
    win: psychoJS.window,
    name: 'warning',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ready_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ready_text',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.25)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixcross_display"
  fixcross_displayClock = new util.Clock();
  fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "cue_trial"
  cue_trialClock = new util.Clock();
  cue_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cue_slide', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "action1_trial"
  action1_trialClock = new util.Clock();
  slide_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slide_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "action2_trial"
  action2_trialClock = new util.Clock();
  slide_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slide_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "action3_trial"
  action3_trialClock = new util.Clock();
  slide_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slide_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "target_trial"
  target_trialClock = new util.Clock();
  target_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_slide', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "response"
  responseClock = new util.Clock();
  prompt_target = new visual.TextStim({
    win: psychoJS.window,
    name: 'prompt_target',
    text: 'Hat das Objekt die gewünschte Person erreicht?\n\nlinks = “ja”; rechts = “nein”',
    font: 'Arial',
    units: 'height', 
    pos: prompt_pos, height: prompt_size,  wrapWidth: 1, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  target_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedb_text_obj = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedb_text_obj',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice_end"
  practice_endClock = new util.Clock();
  warning_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'warning_2',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ready_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ready_text_2',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.25)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixcross_display"
  fixcross_displayClock = new util.Clock();
  fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "cue_trial"
  cue_trialClock = new util.Clock();
  cue_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cue_slide', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "action1_trial"
  action1_trialClock = new util.Clock();
  slide_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slide_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "action2_trial"
  action2_trialClock = new util.Clock();
  slide_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slide_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "action3_trial"
  action3_trialClock = new util.Clock();
  slide_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slide_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "target_trial"
  target_trialClock = new util.Clock();
  target_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_slide', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "response"
  responseClock = new util.Clock();
  prompt_target = new visual.TextStim({
    win: psychoJS.window,
    name: 'prompt_target',
    text: 'Hat das Objekt die gewünschte Person erreicht?\n\nlinks = “ja”; rechts = “nein”',
    font: 'Arial',
    units: 'height', 
    pos: prompt_pos, height: prompt_size,  wrapWidth: 1, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  target_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "bye"
  byeClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  welcome_resp1_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var initializeComponents;
function initializeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'initialize'-------
    t = 0;
    initializeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    initializeComponents = [];
    
    for (const thisComponent of initializeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function initializeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'initialize'-------
    // get current time
    t = initializeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of initializeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function initializeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'initialize'-------
    for (const thisComponent of initializeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "initialize" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_hi_allKeys;
var helloComponents;
function helloRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'hello'-------
    t = 0;
    helloClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_hi.keys = undefined;
    key_resp_hi.rt = undefined;
    _key_resp_hi_allKeys = [];
    // keep track of which components have finished
    helloComponents = [];
    helloComponents.push(text_hi);
    helloComponents.push(key_resp_hi);
    
    for (const thisComponent of helloComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function helloRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'hello'-------
    // get current time
    t = helloClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_hi* updates
    if (t >= 0.0 && text_hi.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_hi.tStart = t;  // (not accounting for frame time here)
      text_hi.frameNStart = frameN;  // exact frame index
      
      text_hi.setAutoDraw(true);
    }

    
    // *key_resp_hi* updates
    if (t >= 0.0 && key_resp_hi.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_hi.tStart = t;  // (not accounting for frame time here)
      key_resp_hi.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_hi.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_hi.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_hi.clearEvents(); });
    }

    if (key_resp_hi.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_hi.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_hi_allKeys = _key_resp_hi_allKeys.concat(theseKeys);
      if (_key_resp_hi_allKeys.length > 0) {
        key_resp_hi.keys = _key_resp_hi_allKeys[_key_resp_hi_allKeys.length - 1].name;  // just the last key pressed
        key_resp_hi.rt = _key_resp_hi_allKeys[_key_resp_hi_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of helloComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function helloRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'hello'-------
    for (const thisComponent of helloComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_hi.stop();
    // the Routine "hello" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var screen_scaleComponents;
function screen_scaleRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'screen_scale'-------
    t = 0;
    screen_scaleClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    event.clearEvents();
    
    // keep track of which components have finished
    screen_scaleComponents = [];
    screen_scaleComponents.push(text_top);
    screen_scaleComponents.push(text_bottom);
    screen_scaleComponents.push(ccimage);
    
    for (const thisComponent of screen_scaleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var keys;
var dscale;
function screen_scaleRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'screen_scale'-------
    // get current time
    t = screen_scaleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys();
    if (keys.length) {
        if (((t - oldt) < 0.5)) {
            dscale = (5 * dbase);
            oldt = t;
        } else {
            dscale = dbase;
            oldt = t;
        }
        if ((_pj.in_es6("space", keys) && (t > 1))) {
            continueRoutine = false;
        } else {
            if (_pj.in_es6("up", keys)) {
                y_scale = (round(((y_scale + dscale) * 10000)) / 10000);
            } else {
                if (_pj.in_es6("down", keys)) {
                    y_scale = (round(((y_scale - dscale) * 10000)) / 10000);
                } else {
                    if (_pj.in_es6("left", keys)) {
                        x_scale = (round(((x_scale - dscale) * 10000)) / 10000);
                    } else {
                        if (_pj.in_es6("right", keys)) {
                            x_scale = (round(((x_scale + dscale) * 10000)) / 10000);
                        }
                    }
                }
            }
        }
        screen_height = (round(((vsize * 10) / y_scale)) / 10);
        text_bottom.text = (((((((("X Scale = " + x_scale.toString()) + unittext) + " per cm, Y Scale = ") + y_scale.toString()) + unittext) + " per cm\nScreen height = ") + screen_height.toString()) + " cm\n\nPress the space bar when done");
        ccimage.size = [(x_size * x_scale), (y_size * y_scale)];
    }
    
    
    // *text_top* updates
    if (t >= 0.0 && text_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_top.tStart = t;  // (not accounting for frame time here)
      text_top.frameNStart = frameN;  // exact frame index
      
      text_top.setAutoDraw(true);
    }

    
    // *text_bottom* updates
    if (t >= 0.0 && text_bottom.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_bottom.tStart = t;  // (not accounting for frame time here)
      text_bottom.frameNStart = frameN;  // exact frame index
      
      text_bottom.setAutoDraw(true);
    }

    
    // *ccimage* updates
    if (t >= 0.0 && ccimage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ccimage.tStart = t;  // (not accounting for frame time here)
      ccimage.frameNStart = frameN;  // exact frame index
      
      ccimage.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of screen_scaleComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function screen_scaleRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'screen_scale'-------
    for (const thisComponent of screen_scaleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    thisExp.addData("X Scale", x_scale);
    thisExp.addData("Y Scale", y_scale);
    
    // the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var welcome_loop;
var currentLoop;
function welcome_loopLoopBegin(welcome_loopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  welcome_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: inst_file,
    seed: undefined, name: 'welcome_loop'
  });
  psychoJS.experiment.addLoop(welcome_loop); // add the loop to the experiment
  currentLoop = welcome_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisWelcome_loop of welcome_loop) {
    const snapshot = welcome_loop.getSnapshot();
    welcome_loopLoopScheduler.add(importConditions(snapshot));
    welcome_loopLoopScheduler.add(welcomeRoutineBegin(snapshot));
    welcome_loopLoopScheduler.add(welcomeRoutineEachFrame(snapshot));
    welcome_loopLoopScheduler.add(welcomeRoutineEnd(snapshot));
    welcome_loopLoopScheduler.add(endLoopIteration(welcome_loopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function welcome_loopLoopEnd() {
  psychoJS.experiment.removeLoop(welcome_loop);

  return Scheduler.Event.NEXT;
}


var practice_trials;
function practice_trialsLoopBegin(practice_trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_files/practice_trials.csv',
    seed: undefined, name: 'practice_trials'
  });
  psychoJS.experiment.addLoop(practice_trials); // add the loop to the experiment
  currentLoop = practice_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractice_trial of practice_trials) {
    const snapshot = practice_trials.getSnapshot();
    practice_trialsLoopScheduler.add(importConditions(snapshot));
    practice_trialsLoopScheduler.add(fixcross_displayRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(fixcross_displayRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(fixcross_displayRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(cue_trialRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(cue_trialRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(cue_trialRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(action1_trialRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(action1_trialRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(action1_trialRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(action2_trialRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(action2_trialRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(action2_trialRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(action3_trialRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(action3_trialRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(action3_trialRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(target_trialRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(target_trialRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(target_trialRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(responseRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(responseRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(responseRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
    practice_trialsLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    practice_trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
    practice_trialsLoopScheduler.add(endLoopIteration(practice_trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function practice_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(practice_trials);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: cond_file,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(fixcross_displayRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixcross_displayRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixcross_displayRoutineEnd(snapshot));
    trialsLoopScheduler.add(cue_trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(cue_trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(cue_trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(action1_trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(action1_trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(action1_trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(action2_trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(action2_trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(action2_trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(action3_trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(action3_trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(action3_trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(target_trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(target_trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(target_trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(responseRoutineBegin(snapshot));
    trialsLoopScheduler.add(responseRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(responseRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var _welcome_resp1_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'welcome'-------
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_comp.setText(inst_text);
    welcome_resp1.keys = undefined;
    welcome_resp1.rt = undefined;
    _welcome_resp1_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(text_comp);
    welcomeComponents.push(welcome_resp1);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'welcome'-------
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_comp* updates
    if (t >= 0.0 && text_comp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_comp.tStart = t;  // (not accounting for frame time here)
      text_comp.frameNStart = frameN;  // exact frame index
      
      text_comp.setAutoDraw(true);
    }

    
    // *welcome_resp1* updates
    if (t >= 0.0 && welcome_resp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_resp1.tStart = t;  // (not accounting for frame time here)
      welcome_resp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_resp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_resp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_resp1.clearEvents(); });
    }

    if (welcome_resp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_resp1.getKeys({keyList: ['space'], waitRelease: false});
      _welcome_resp1_allKeys = _welcome_resp1_allKeys.concat(theseKeys);
      if (_welcome_resp1_allKeys.length > 0) {
        welcome_resp1.keys = _welcome_resp1_allKeys[_welcome_resp1_allKeys.length - 1].name;  // just the last key pressed
        welcome_resp1.rt = _welcome_resp1_allKeys[_welcome_resp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'welcome'-------
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    welcome_resp1.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var readyComponents;
function readyRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ready'-------
    t = 0;
    readyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    warning.setText('Sie beginnen jetzt mit den Übungsversuchen.\n\n');
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    ready_text.setText('<Drücken Sie die Leertaste, wenn Sie fertig sind>');
    // keep track of which components have finished
    readyComponents = [];
    readyComponents.push(warning);
    readyComponents.push(key_resp_6);
    readyComponents.push(ready_text);
    
    for (const thisComponent of readyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function readyRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ready'-------
    // get current time
    t = readyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *warning* updates
    if (t >= 0.0 && warning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      warning.tStart = t;  // (not accounting for frame time here)
      warning.frameNStart = frameN;  // exact frame index
      
      warning.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *ready_text* updates
    if (t >= 0.0 && ready_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_text.tStart = t;  // (not accounting for frame time here)
      ready_text.frameNStart = frameN;  // exact frame index
      
      ready_text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of readyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function readyRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ready'-------
    for (const thisComponent of readyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_6.stop();
    // the Routine "ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var fixcross_displayComponents;
function fixcross_displayRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fixcross_display'-------
    t = 0;
    fixcross_displayClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixcross_displayComponents = [];
    fixcross_displayComponents.push(fix);
    
    for (const thisComponent of fixcross_displayComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixcross_displayRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fixcross_display'-------
    // get current time
    t = fixcross_displayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix* updates
    if (t >= 0.0 && fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix.tStart = t;  // (not accounting for frame time here)
      fix.frameNStart = frameN;  // exact frame index
      
      fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixcross_displayComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixcross_displayRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fixcross_display'-------
    for (const thisComponent of fixcross_displayComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var cue_trialComponents;
function cue_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'cue_trial'-------
    t = 0;
    cue_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    cue_slide.setSize([(16 * x_scale), (12 * y_scale)]);
    cue_slide.setImage(cue_file);
    // keep track of which components have finished
    cue_trialComponents = [];
    cue_trialComponents.push(cue_slide);
    
    for (const thisComponent of cue_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function cue_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'cue_trial'-------
    // get current time
    t = cue_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cue_slide* updates
    if (t >= 0.0 && cue_slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_slide.tStart = t;  // (not accounting for frame time here)
      cue_slide.frameNStart = frameN;  // exact frame index
      
      cue_slide.setAutoDraw(true);
    }

    frameRemains = 0.0 + cue_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue_slide.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue_slide.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of cue_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function cue_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'cue_trial'-------
    for (const thisComponent of cue_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "cue_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var action1_trialComponents;
function action1_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'action1_trial'-------
    t = 0;
    action1_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slide_1.setSize([(16 * x_scale), (12 * y_scale)]);
    slide_1.setImage(action1);
    // keep track of which components have finished
    action1_trialComponents = [];
    action1_trialComponents.push(slide_1);
    
    for (const thisComponent of action1_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function action1_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'action1_trial'-------
    // get current time
    t = action1_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_1* updates
    if (t >= 0.0 && slide_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_1.tStart = t;  // (not accounting for frame time here)
      slide_1.frameNStart = frameN;  // exact frame index
      
      slide_1.setAutoDraw(true);
    }

    frameRemains = 0.0 + action_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (slide_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      slide_1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of action1_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function action1_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'action1_trial'-------
    for (const thisComponent of action1_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "action1_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var action2_trialComponents;
function action2_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'action2_trial'-------
    t = 0;
    action2_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slide_2.setSize([(16 * x_scale), (12 * y_scale)]);
    slide_2.setImage(action2);
    // keep track of which components have finished
    action2_trialComponents = [];
    action2_trialComponents.push(slide_2);
    
    for (const thisComponent of action2_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function action2_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'action2_trial'-------
    // get current time
    t = action2_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_2* updates
    if (t >= 0.0 && slide_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_2.tStart = t;  // (not accounting for frame time here)
      slide_2.frameNStart = frameN;  // exact frame index
      
      slide_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + action_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (slide_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      slide_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of action2_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function action2_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'action2_trial'-------
    for (const thisComponent of action2_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "action2_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var action3_trialComponents;
function action3_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'action3_trial'-------
    t = 0;
    action3_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slide_3.setSize([(16 * x_scale), (12 * y_scale)]);
    slide_3.setImage(action3);
    // keep track of which components have finished
    action3_trialComponents = [];
    action3_trialComponents.push(slide_3);
    
    for (const thisComponent of action3_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function action3_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'action3_trial'-------
    // get current time
    t = action3_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slide_3* updates
    if (t >= 0.0 && slide_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slide_3.tStart = t;  // (not accounting for frame time here)
      slide_3.frameNStart = frameN;  // exact frame index
      
      slide_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + action_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (slide_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      slide_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of action3_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function action3_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'action3_trial'-------
    for (const thisComponent of action3_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "action3_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var target_trialComponents;
function target_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'target_trial'-------
    t = 0;
    target_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    target_slide.setSize([(16 * x_scale), (12 * y_scale)]);
    target_slide.setImage(target_file);
    // keep track of which components have finished
    target_trialComponents = [];
    target_trialComponents.push(target_slide);
    
    for (const thisComponent of target_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function target_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'target_trial'-------
    // get current time
    t = target_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_slide* updates
    if (t >= 0.0 && target_slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_slide.tStart = t;  // (not accounting for frame time here)
      target_slide.frameNStart = frameN;  // exact frame index
      
      target_slide.setAutoDraw(true);
    }

    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target_slide.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target_slide.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of target_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function target_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'target_trial'-------
    for (const thisComponent of target_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "target_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _target_resp_allKeys;
var responseComponents;
function responseRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'response'-------
    t = 0;
    responseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    target_resp.keys = undefined;
    target_resp.rt = undefined;
    _target_resp_allKeys = [];
    // keep track of which components have finished
    responseComponents = [];
    responseComponents.push(prompt_target);
    responseComponents.push(target_resp);
    
    for (const thisComponent of responseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function responseRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'response'-------
    // get current time
    t = responseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prompt_target* updates
    if (t >= 0.0 && prompt_target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prompt_target.tStart = t;  // (not accounting for frame time here)
      prompt_target.frameNStart = frameN;  // exact frame index
      
      prompt_target.setAutoDraw(true);
    }

    
    // *target_resp* updates
    if (t >= 0.0 && target_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_resp.tStart = t;  // (not accounting for frame time here)
      target_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { target_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { target_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { target_resp.clearEvents(); });
    }

    if (target_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = target_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _target_resp_allKeys = _target_resp_allKeys.concat(theseKeys);
      if (_target_resp_allKeys.length > 0) {
        target_resp.keys = _target_resp_allKeys[_target_resp_allKeys.length - 1].name;  // just the last key pressed
        target_resp.rt = _target_resp_allKeys[_target_resp_allKeys.length - 1].rt;
        // was this correct?
        if (target_resp.keys == corr_ans) {
            target_resp.corr = 1;
        } else {
            target_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of responseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var msg;
function responseRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'response'-------
    for (const thisComponent of responseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (target_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_ans)) {
         target_resp.corr = 1;  // correct non-response
      } else {
         target_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('target_resp.keys', target_resp.keys);
    psychoJS.experiment.addData('target_resp.corr', target_resp.corr);
    if (typeof target_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('target_resp.rt', target_resp.rt);
        routineTimer.reset();
        }
    
    target_resp.stop();
    if ((! target_resp.keys)) {
        msg = "Failed to respond";
    } else {
        if (target_resp.corr) {
            msg = "Correct!";
        } else {
            msg = "Oops! That was wrong.";
        }
    }
    
    // the Routine "response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedb_text_obj.setText(msg);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedb_text_obj);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedb_text_obj* updates
    if (t >= 0.0 && feedb_text_obj.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedb_text_obj.tStart = t;  // (not accounting for frame time here)
      feedb_text_obj.frameNStart = frameN;  // exact frame index
      
      feedb_text_obj.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedb_text_obj.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedb_text_obj.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var practice_endComponents;
function practice_endRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practice_end'-------
    t = 0;
    practice_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    warning_2.setText('Sie haben alle Übungsaufgaben gelöst. Jetzt beginnt die eigentliche Aufgabe.\n\nSind Sie bereit?');
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    ready_text_2.setText('< Drücken Sie die Leertaste um fortzufahren >');
    // keep track of which components have finished
    practice_endComponents = [];
    practice_endComponents.push(warning_2);
    practice_endComponents.push(key_resp);
    practice_endComponents.push(ready_text_2);
    
    for (const thisComponent of practice_endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_endRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practice_end'-------
    // get current time
    t = practice_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *warning_2* updates
    if (t >= 0.0 && warning_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      warning_2.tStart = t;  // (not accounting for frame time here)
      warning_2.frameNStart = frameN;  // exact frame index
      
      warning_2.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *ready_text_2* updates
    if (t >= 0.0 && ready_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_text_2.tStart = t;  // (not accounting for frame time here)
      ready_text_2.frameNStart = frameN;  // exact frame index
      
      ready_text_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_endRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practice_end'-------
    for (const thisComponent of practice_endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp.stop();
    // the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _welcome_resp1_2_allKeys;
var byeComponents;
function byeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'bye'-------
    t = 0;
    byeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_2.setText('Gut gemacht!\nDieser erste Teil ist abgeschlossen. Gehen Sie zurück in den Online-Raum, um die Anweisungen für die nächste Phase zu erhalten.\n\nDenken Sie daran, dass die Daten gespeichert werden, nachdem Sie den Vollbildschirm verlassen haben. Bitte schließen Sie das Fenster nicht manuell, bevor die Daten gespeichert sind.\n\nDrücken Sie eine beliebige Taste, um den Vollbildmodus zu verlassen.');
    welcome_resp1_2.keys = undefined;
    welcome_resp1_2.rt = undefined;
    _welcome_resp1_2_allKeys = [];
    // keep track of which components have finished
    byeComponents = [];
    byeComponents.push(text_2);
    byeComponents.push(welcome_resp1_2);
    
    for (const thisComponent of byeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function byeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'bye'-------
    // get current time
    t = byeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *welcome_resp1_2* updates
    if (t >= 0.0 && welcome_resp1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_resp1_2.tStart = t;  // (not accounting for frame time here)
      welcome_resp1_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_resp1_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_resp1_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_resp1_2.clearEvents(); });
    }

    if (welcome_resp1_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_resp1_2.getKeys({keyList: ['space'], waitRelease: false});
      _welcome_resp1_2_allKeys = _welcome_resp1_2_allKeys.concat(theseKeys);
      if (_welcome_resp1_2_allKeys.length > 0) {
        welcome_resp1_2.keys = _welcome_resp1_2_allKeys[_welcome_resp1_2_allKeys.length - 1].name;  // just the last key pressed
        welcome_resp1_2.rt = _welcome_resp1_2_allKeys[_welcome_resp1_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of byeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function byeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'bye'-------
    for (const thisComponent of byeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    welcome_resp1_2.stop();
    // the Routine "bye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
