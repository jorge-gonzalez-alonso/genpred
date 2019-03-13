# genpred
NOTE: Like an idiot, I just discovered that the SDK had a Python example of a gaze contingent paradigm. I don't think it is exactly what we're looking for, but it should give us the right tools (especially you, who are able to interpret these things and reuse them much more straightforwardly than I do). Check it out!

-----

Python script for L3 gender prediction experiment

The idea of this repo is for us to work together on making improvements to the python script.
I know that blind writing is annoying as hell, but this way you can do pull requests on potentially effective solutions,
and I can test the suggested changes in the lab and commit them if they work. Does that sound alright?

CURRENT PROBLEM:

Move from mouse clicks to 1-second fixations as a behavioural response. For this, we have to:

- Define the two picture areas. These are:

  LEFT: x1 = 270, x2 = 570; y1 = 675, y2 = 375
  RIGHT: x1 = 1110, x2 = 1410; y1 = 675, y2 =375
  
  where x1 and y1 are the start horizontal and vertical coordinates, respectively, x2 and y2 are the end horizontal and vertical coords.
  
- Set up the gaze trigger, such that a fixation of 1000 ms on either window ends the trial.

- Record which window that was, somehow (this is the least important, because they'll get it right 99% of the time, but we still want 
  the behavioural data).

I've uploaded the SDK manual to the master folder to have it handy, because we'll have to consult that quite often I think.
