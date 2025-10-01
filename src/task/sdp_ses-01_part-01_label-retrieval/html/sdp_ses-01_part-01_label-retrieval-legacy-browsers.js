/******************************************* 
 * Sdp_Ses-01_Part-01_Label-Retrieval Test *
 *******************************************/

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
let expName = 'sdp_ses-01_part-01_label-retrieval';  // from the Builder filename that created this script
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
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
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
var story_rec_dur;
var central_recall_dur;
var ending_recall_dur;
var target_trial_dur;
var fix_dur;
var choice_size;
var pos_left;
var pos_center;
var pos_right;
var prompt_pos;
var prompt_size;
var afc_cue_size;
var afc_cue_pos;
var inst_file;
var cond_file;
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
var WelcomeClock;
var text;
var welcome_resp1;
var readyClock;
var warning;
var key_resp_6;
var fixcross_displayClock;
var fix;
var story_recClock;
var cue_slide;
var story_rec_prompt;
var story_rec_resp;
var central_recallClock;
var cue_slide_2;
var central_recall_resp;
var central_recall_textbox;
var central_recall_prompt;
var ending_recallClock;
var cue_slide_3;
var ending_rec_prompt;
var ending_rec_resp;
var target_trialClock;
var target_trial_cue;
var choice_left_disp;
var choice_center_disp;
var choice_right_disp;
var afc_prompt;
var afc_resp;
var reminder_1;
var reminder_2;
var reminder_3;
var endClock;
var end_text;
var key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "initialize"
  initializeClock = new util.Clock();
  obj_size = [0.4,0.3];
  scn_size = [.8,0.6];
  story_rec_dur=10;
  central_recall_dur=10;
  ending_recall_dur=10;
  target_trial_dur=10;
  fix_dur=0.5;
  choice_size=(0.3,0.3);
  pos_left=(-0.5,-0.3);
  pos_center=(0,-0.3);
  pos_right=(0.5,-0.3);
  prompt_pos=(0,-0.4);
  prompt_size=0.025;
  afc_cue_size=(0.7,0.5);
  afc_cue_pos=(0,.2);
  inst_file='condition_files/instructions.xlsx'
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
                          }
                          if (((Number.parseInt(expInfo["participant"]) % 12) === 10)) {
                             cond_file = (("condition_files/enc_10_list.csv"));
                          }
                          if (((Number.parseInt(expInfo["participant"]) % 12) === 11)) {
                             cond_file = (("condition_files/enc_11_list.csv"));
                          }
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
  // Initialize components for Routine "hello"
  helloClock = new util.Clock();
  text_hi = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_hi',
    text: 'Liebe/r Teilnehmer/in,\n\nbevor wir anfangen, werden wir die Größe Ihres Monitors bestimmen. Danach werden Sie Instruktionen für die Studie bekommen und schließlich mit der Aufgabe beginnen.\n\n< Drücken Sie die Leertaste um fortzufahren >',
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
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
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
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixcross_display"
  fixcross_displayClock = new util.Clock();
  fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "story_rec"
  story_recClock = new util.Clock();
  cue_slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cue_slide', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.2], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  story_rec_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'story_rec_prompt',
    text: 'Haben Sie diese Geschichte schon einmal gesehen?\n\nlinks = "ja"; rechts = "nein"',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.15)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  story_rec_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "central_recall"
  central_recallClock = new util.Clock();
  cue_slide_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cue_slide_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.2], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  central_recall_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  central_recall_textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'central_recall_textbox',
    text: '',
    font: 'Open Sans',
    pos: [0, (- 0.3)], letterHeight: 0.025,
    size: [0.5, 0.2],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: undefined,
    padding: undefined,
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  central_recall_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'central_recall_prompt',
    text: 'Welcher Gegenstand wurde in diesem Comic ausgetauscht?\nGeben Sie unten ein oder zwei Wörter ein oder drücken Sie ENTER, wenn Sie sich nicht erinnern können.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.15)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "ending_recall"
  ending_recallClock = new util.Clock();
  cue_slide_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cue_slide_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.2], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  ending_rec_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'ending_rec_prompt',
    text: 'Hat das Objekt die gewünschte Person erreicht?\n\nlinks = "ja"; rechts = "nein"',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.15)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  ending_rec_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "target_trial"
  target_trialClock = new util.Clock();
  target_trial_cue = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_trial_cue', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0.2], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  choice_left_disp = new visual.ImageStim({
    win : psychoJS.window,
    name : 'choice_left_disp', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.5), (- 0.3)], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  choice_center_disp = new visual.ImageStim({
    win : psychoJS.window,
    name : 'choice_center_disp', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, (- 0.3)], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  choice_right_disp = new visual.ImageStim({
    win : psychoJS.window,
    name : 'choice_right_disp', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.5, (- 0.3)], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -3.0 
  });
  afc_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'afc_prompt',
    text: 'Wie ist die Geschichte ausgegangen?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.1)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  afc_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  reminder_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminder_1',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.5), (- 0.125)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  reminder_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminder_2',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.125)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  reminder_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'reminder_3',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, (- 0.125)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: 'Herzlichen Glückwunsch!\n\nSie haben die Aufgabe abgeschlossen.\n\nDenken Sie daran, dass die Daten gespeichert werden, nachdem Sie den Vollbildschirm verlassen haben. Bitte schließen Sie das Fenster nicht manuell, bevor die Daten gespeichert sind.\n\nVielen Dank für Ihre Teilnahme.\n\nDrücken Sie eine beliebige Taste, um den Vollbildmodus zu verlassen.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
    
    initializeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    initializeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    initializeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    helloComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    helloComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    helloComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    screen_scaleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    screen_scaleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    screen_scaleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
  welcome_loop.forEach(function() {
    const snapshot = welcome_loop.getSnapshot();

    welcome_loopLoopScheduler.add(importConditions(snapshot));
    welcome_loopLoopScheduler.add(WelcomeRoutineBegin(snapshot));
    welcome_loopLoopScheduler.add(WelcomeRoutineEachFrame(snapshot));
    welcome_loopLoopScheduler.add(WelcomeRoutineEnd(snapshot));
    welcome_loopLoopScheduler.add(endLoopIteration(welcome_loopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function welcome_loopLoopEnd() {
  psychoJS.experiment.removeLoop(welcome_loop);

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
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(fixcross_displayRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixcross_displayRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixcross_displayRoutineEnd(snapshot));
    trialsLoopScheduler.add(story_recRoutineBegin(snapshot));
    trialsLoopScheduler.add(story_recRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(story_recRoutineEnd(snapshot));
    trialsLoopScheduler.add(central_recallRoutineBegin(snapshot));
    trialsLoopScheduler.add(central_recallRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(central_recallRoutineEnd(snapshot));
    trialsLoopScheduler.add(ending_recallRoutineBegin(snapshot));
    trialsLoopScheduler.add(ending_recallRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(ending_recallRoutineEnd(snapshot));
    trialsLoopScheduler.add(target_trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(target_trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(target_trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var _welcome_resp1_allKeys;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome'-------
    t = 0;
    WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text.setText(inst_text);
    welcome_resp1.keys = undefined;
    welcome_resp1.rt = undefined;
    _welcome_resp1_allKeys = [];
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(text);
    WelcomeComponents.push(welcome_resp1);
    
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome'-------
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
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
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome'-------
    WelcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    welcome_resp1.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
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
    warning.setText('Sind Sie bereit?');
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    readyComponents = [];
    readyComponents.push(warning);
    readyComponents.push(key_resp_6);
    
    readyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    readyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    readyComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    fixcross_displayComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    fixcross_displayComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    fixcross_displayComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _story_rec_resp_allKeys;
var story_recComponents;
function story_recRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'story_rec'-------
    t = 0;
    story_recClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    cue_slide.setSize([(14 * x_scale), (10 * y_scale)]);
    cue_slide.setImage(cue_file);
    story_rec_resp.keys = undefined;
    story_rec_resp.rt = undefined;
    _story_rec_resp_allKeys = [];
    // keep track of which components have finished
    story_recComponents = [];
    story_recComponents.push(cue_slide);
    story_recComponents.push(story_rec_prompt);
    story_recComponents.push(story_rec_resp);
    
    story_recComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function story_recRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'story_rec'-------
    // get current time
    t = story_recClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cue_slide* updates
    if (t >= 0.0 && cue_slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_slide.tStart = t;  // (not accounting for frame time here)
      cue_slide.frameNStart = frameN;  // exact frame index
      
      cue_slide.setAutoDraw(true);
    }

    
    // *story_rec_prompt* updates
    if (t >= 0.0 && story_rec_prompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      story_rec_prompt.tStart = t;  // (not accounting for frame time here)
      story_rec_prompt.frameNStart = frameN;  // exact frame index
      
      story_rec_prompt.setAutoDraw(true);
    }

    
    // *story_rec_resp* updates
    if (t >= 0.0 && story_rec_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      story_rec_resp.tStart = t;  // (not accounting for frame time here)
      story_rec_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { story_rec_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { story_rec_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { story_rec_resp.clearEvents(); });
    }

    if (story_rec_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = story_rec_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _story_rec_resp_allKeys = _story_rec_resp_allKeys.concat(theseKeys);
      if (_story_rec_resp_allKeys.length > 0) {
        story_rec_resp.keys = _story_rec_resp_allKeys[_story_rec_resp_allKeys.length - 1].name;  // just the last key pressed
        story_rec_resp.rt = _story_rec_resp_allKeys[_story_rec_resp_allKeys.length - 1].rt;
        // was this correct?
        if (story_rec_resp.keys == story_rec_corr) {
            story_rec_resp.corr = 1;
        } else {
            story_rec_resp.corr = 0;
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
    story_recComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function story_recRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'story_rec'-------
    story_recComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (story_rec_resp.keys === undefined) {
      if (['None','none',undefined].includes(story_rec_corr)) {
         story_rec_resp.corr = 1;  // correct non-response
      } else {
         story_rec_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('story_rec_resp.keys', story_rec_resp.keys);
    psychoJS.experiment.addData('story_rec_resp.corr', story_rec_resp.corr);
    if (typeof story_rec_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('story_rec_resp.rt', story_rec_resp.rt);
        routineTimer.reset();
        }
    
    story_rec_resp.stop();
    // the Routine "story_rec" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _central_recall_resp_allKeys;
var central_recallComponents;
function central_recallRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'central_recall'-------
    t = 0;
    central_recallClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    cue_slide_2.setSize([(14 * x_scale), (10 * y_scale)]);
    cue_slide_2.setImage(cue_file);
    central_recall_resp.keys = undefined;
    central_recall_resp.rt = undefined;
    _central_recall_resp_allKeys = [];
    central_recall_textbox.text = "";
    if (OvsN_code === 0) {
        continueRoutine = false;
    }
    // keep track of which components have finished
    central_recallComponents = [];
    central_recallComponents.push(cue_slide_2);
    central_recallComponents.push(central_recall_resp);
    central_recallComponents.push(central_recall_textbox);
    central_recallComponents.push(central_recall_prompt);
    
    central_recallComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function central_recallRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'central_recall'-------
    // get current time
    t = central_recallClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cue_slide_2* updates
    if (t >= 0.0 && cue_slide_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_slide_2.tStart = t;  // (not accounting for frame time here)
      cue_slide_2.frameNStart = frameN;  // exact frame index
      
      cue_slide_2.setAutoDraw(true);
    }

    
    // *central_recall_resp* updates
    if (t >= 0.0 && central_recall_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      central_recall_resp.tStart = t;  // (not accounting for frame time here)
      central_recall_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { central_recall_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { central_recall_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { central_recall_resp.clearEvents(); });
    }

    if (central_recall_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = central_recall_resp.getKeys({keyList: ['return'], waitRelease: false});
      _central_recall_resp_allKeys = _central_recall_resp_allKeys.concat(theseKeys);
      if (_central_recall_resp_allKeys.length > 0) {
        central_recall_resp.keys = _central_recall_resp_allKeys.map((key) => key.name);  // storing all keys
        central_recall_resp.rt = _central_recall_resp_allKeys.map((key) => key.rt);
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *central_recall_textbox* updates
    if (t >= 0.0 && central_recall_textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      central_recall_textbox.tStart = t;  // (not accounting for frame time here)
      central_recall_textbox.frameNStart = frameN;  // exact frame index
      
      central_recall_textbox.setAutoDraw(true);
    }

    
    // *central_recall_prompt* updates
    if (t >= 0.0 && central_recall_prompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      central_recall_prompt.tStart = t;  // (not accounting for frame time here)
      central_recall_prompt.frameNStart = frameN;  // exact frame index
      
      central_recall_prompt.setAutoDraw(true);
    }

    if (OvsN_code === 0) {
        continueRoutine = false;
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
    central_recallComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function central_recallRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'central_recall'-------
    central_recallComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('central_recall_resp.keys', central_recall_resp.keys);
    if (typeof central_recall_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('central_recall_resp.rt', central_recall_resp.rt);
        routineTimer.reset();
        }
    
    central_recall_resp.stop();
    psychoJS.experiment.addData('central_recall_textbox.text',central_recall_textbox.text)
    central_recall_textbox.reset()
    // the Routine "central_recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ending_rec_resp_allKeys;
var ending_recallComponents;
function ending_recallRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ending_recall'-------
    t = 0;
    ending_recallClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    cue_slide_3.setSize([(14 * x_scale), (10 * y_scale)]);
    cue_slide_3.setImage(cue_file);
    ending_rec_resp.keys = undefined;
    ending_rec_resp.rt = undefined;
    _ending_rec_resp_allKeys = [];
    if (OvsN_code === 0) {
        continueRoutine = false;
    }
    // keep track of which components have finished
    ending_recallComponents = [];
    ending_recallComponents.push(cue_slide_3);
    ending_recallComponents.push(ending_rec_prompt);
    ending_recallComponents.push(ending_rec_resp);
    
    ending_recallComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ending_recallRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ending_recall'-------
    // get current time
    t = ending_recallClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cue_slide_3* updates
    if (t >= 0.0 && cue_slide_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_slide_3.tStart = t;  // (not accounting for frame time here)
      cue_slide_3.frameNStart = frameN;  // exact frame index
      
      cue_slide_3.setAutoDraw(true);
    }

    
    // *ending_rec_prompt* updates
    if (t >= 0.0 && ending_rec_prompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ending_rec_prompt.tStart = t;  // (not accounting for frame time here)
      ending_rec_prompt.frameNStart = frameN;  // exact frame index
      
      ending_rec_prompt.setAutoDraw(true);
    }

    
    // *ending_rec_resp* updates
    if (t >= 0.0 && ending_rec_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ending_rec_resp.tStart = t;  // (not accounting for frame time here)
      ending_rec_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ending_rec_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ending_rec_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ending_rec_resp.clearEvents(); });
    }

    if (ending_rec_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = ending_rec_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _ending_rec_resp_allKeys = _ending_rec_resp_allKeys.concat(theseKeys);
      if (_ending_rec_resp_allKeys.length > 0) {
        ending_rec_resp.keys = _ending_rec_resp_allKeys[_ending_rec_resp_allKeys.length - 1].name;  // just the last key pressed
        ending_rec_resp.rt = _ending_rec_resp_allKeys[_ending_rec_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    if (OvsN_code === 0) {
        continueRoutine = false;
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
    ending_recallComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ending_recallRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ending_recall'-------
    ending_recallComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ending_rec_resp.keys', ending_rec_resp.keys);
    if (typeof ending_rec_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ending_rec_resp.rt', ending_rec_resp.rt);
        routineTimer.reset();
        }
    
    ending_rec_resp.stop();
    // the Routine "ending_recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _afc_resp_allKeys;
var target_trialComponents;
function target_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'target_trial'-------
    t = 0;
    target_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    target_trial_cue.setSize([(14 * x_scale), (10 * y_scale)]);
    target_trial_cue.setImage(cue_file);
    choice_left_disp.setSize([(8 * x_scale), (7 * y_scale)]);
    choice_left_disp.setImage(choice_left);
    choice_center_disp.setSize([(8 * x_scale), (7 * y_scale)]);
    choice_center_disp.setImage(choice_center);
    choice_right_disp.setSize([(8 * x_scale), (7 * y_scale)]);
    choice_right_disp.setImage(choice_right);
    afc_resp.keys = undefined;
    afc_resp.rt = undefined;
    _afc_resp_allKeys = [];
    if (OvsN_code === 0) {
        continueRoutine = false;
    }
    // keep track of which components have finished
    target_trialComponents = [];
    target_trialComponents.push(target_trial_cue);
    target_trialComponents.push(choice_left_disp);
    target_trialComponents.push(choice_center_disp);
    target_trialComponents.push(choice_right_disp);
    target_trialComponents.push(afc_prompt);
    target_trialComponents.push(afc_resp);
    target_trialComponents.push(reminder_1);
    target_trialComponents.push(reminder_2);
    target_trialComponents.push(reminder_3);
    
    target_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *target_trial_cue* updates
    if (t >= 0.0 && target_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_trial_cue.tStart = t;  // (not accounting for frame time here)
      target_trial_cue.frameNStart = frameN;  // exact frame index
      
      target_trial_cue.setAutoDraw(true);
    }

    
    // *choice_left_disp* updates
    if (t >= 0.0 && choice_left_disp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_left_disp.tStart = t;  // (not accounting for frame time here)
      choice_left_disp.frameNStart = frameN;  // exact frame index
      
      choice_left_disp.setAutoDraw(true);
    }

    
    // *choice_center_disp* updates
    if (t >= 0.0 && choice_center_disp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_center_disp.tStart = t;  // (not accounting for frame time here)
      choice_center_disp.frameNStart = frameN;  // exact frame index
      
      choice_center_disp.setAutoDraw(true);
    }

    
    // *choice_right_disp* updates
    if (t >= 0.0 && choice_right_disp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_right_disp.tStart = t;  // (not accounting for frame time here)
      choice_right_disp.frameNStart = frameN;  // exact frame index
      
      choice_right_disp.setAutoDraw(true);
    }

    
    // *afc_prompt* updates
    if (t >= 0.0 && afc_prompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      afc_prompt.tStart = t;  // (not accounting for frame time here)
      afc_prompt.frameNStart = frameN;  // exact frame index
      
      afc_prompt.setAutoDraw(true);
    }

    
    // *afc_resp* updates
    if (t >= 0.0 && afc_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      afc_resp.tStart = t;  // (not accounting for frame time here)
      afc_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { afc_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { afc_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { afc_resp.clearEvents(); });
    }

    if (afc_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = afc_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _afc_resp_allKeys = _afc_resp_allKeys.concat(theseKeys);
      if (_afc_resp_allKeys.length > 0) {
        afc_resp.keys = _afc_resp_allKeys[_afc_resp_allKeys.length - 1].name;  // just the last key pressed
        afc_resp.rt = _afc_resp_allKeys[_afc_resp_allKeys.length - 1].rt;
        // was this correct?
        if (afc_resp.keys == afc_corr) {
            afc_resp.corr = 1;
        } else {
            afc_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *reminder_1* updates
    if (t >= 0.0 && reminder_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder_1.tStart = t;  // (not accounting for frame time here)
      reminder_1.frameNStart = frameN;  // exact frame index
      
      reminder_1.setAutoDraw(true);
    }

    
    // *reminder_2* updates
    if (t >= 0.0 && reminder_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder_2.tStart = t;  // (not accounting for frame time here)
      reminder_2.frameNStart = frameN;  // exact frame index
      
      reminder_2.setAutoDraw(true);
    }

    
    // *reminder_3* updates
    if (t >= 0.0 && reminder_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder_3.tStart = t;  // (not accounting for frame time here)
      reminder_3.frameNStart = frameN;  // exact frame index
      
      reminder_3.setAutoDraw(true);
    }

    if (OvsN_code === 0) {
        continueRoutine = false;
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
    target_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    target_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (afc_resp.keys === undefined) {
      if (['None','none',undefined].includes(afc_corr)) {
         afc_resp.corr = 1;  // correct non-response
      } else {
         afc_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('afc_resp.keys', afc_resp.keys);
    psychoJS.experiment.addData('afc_resp.corr', afc_resp.corr);
    if (typeof afc_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('afc_resp.rt', afc_resp.rt);
        routineTimer.reset();
        }
    
    afc_resp.stop();
    // the Routine "target_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var endComponents;
function endRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(end_text);
    endComponents.push(key_resp);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 0.0 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
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
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
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
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end'-------
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp.stop();
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
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
