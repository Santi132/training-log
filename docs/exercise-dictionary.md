# Exercise dictionary

Every exercise the app knows about, grouped by family. The app's `EXERCISES` table in `index.html` mirrors
this file: change both together. Safety and pain guidance lives in [training-plan.md](training-plan.md),
not here. These entries only describe setup, execution and the muscles worked.

- **Id** (in backticks): the stable key history is saved under. It never changes and never shows in the app.
  Rename an exercise by changing its name and moving the old name into `aka`.
- **↳** marks a variant of the exercise above it (it has that exercise as its parent and inherits its
  tracking, equipment and muscles unless it sets its own).
- **Next** is the next progression. **Swap** is an alternative the plan lists. Both show in the app's
  "Doing" menu for that slot. The slot's sets and reps stay as the plan prescribes.

## Squat

Hips and knees bend together with the chest up. Front-loaded versions keep the torso upright.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Goblet box squat** `goblet_box_squat` | Weight and reps per set | Kettlebell | quads, glutes | adductors, core | A · 1 | next: Double-KB front squat |
| **Double-KB front squat** `double_kb_front_squat` | Weight and reps per set | Kettlebell | quads, glutes | adductors, core |  | swap: Barbell front squat |
| **Barbell front squat** `bb_front_squat` | Weight and reps per set | Barbell | quads, glutes | adductors, core |  |  |
| **Cossack squat** `cossack` | Reps per set, optional added load, per side | Bodyweight | adductors, quads, glutes | core | C · 4 |  |

- **Goblet box squat:** Hold a kettlebell or dumbbell at your chest, sit back and down until you lightly touch a box, then stand. The box sets your depth; lower it over time.
- **Double-KB front squat:** Two kettlebells in the front rack, elbows tucked in. Squat to depth and stand.
- **Barbell front squat:** Bar resting on the front of the shoulders, elbows high. Squat to depth and stand.
- **Cossack squat:** Wide stance. Shift down into one leg while the other stays straight with its toes up, then switch sides. Progression: hold a light KB.

## Hinge

The hips push back while the knees stay softly bent and the spine stays neutral. Glutes and hamstrings do the work.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **DB or KB Romanian deadlift** `db_rdl` | Weight and reps per set | Dumbbells | glutes, hamstrings | lower back, grip | B · 1 | swap: Barbell RDL |
| **Barbell RDL** `bb_rdl` | Weight and reps per set | Barbell | glutes, hamstrings | lower back, grip |  |  |
| **KB single-leg RDL** `kb_sl_rdl` | Weight and reps per set, per side | Kettlebell | glutes, hamstrings | core, grip | A · 3 |  |
| **KB deadlift** `kb_deadlift` | Weight and reps per set | Kettlebell | glutes, hamstrings | lower back, grip |  |  |
| **Cable pull-through** `pull_through` | Weight and reps per set | Cable | glutes, hamstrings | core | B · 5 |  |

- **DB or KB Romanian deadlift:** Weights in front of your thighs. Push your hips back and slide the weights down to about mid-shin with a neutral spine, then stand by squeezing the glutes.
- **Barbell RDL:** The same hinge with a barbell, kept light and form-first.
- **KB single-leg RDL:** Hold a kettlebell and hinge forward on one leg while the other leg reaches back, hips square to the floor. Hold a support for balance if you need it.
- **KB deadlift:** Kettlebell between your feet. Hinge down, stand up tall, then lower it under control.
- **Cable pull-through:** Face away from a low cable with the rope between your legs. Hinge back, then drive the hips forward to stand tall.

## Single-leg

One leg does most of the work, which also trains balance and knee control.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **DB Bulgarian split squat** `bss` | Weight and reps per set, per side | Dumbbells | quads, glutes | adductors, core | B · 3 |  |
| **DB reverse lunge or step-up** `reverse_lunge` | Weight and reps per set, per side | Dumbbells | quads, glutes | adductors, core | C · 3 | swap: Front-foot-elevated split squat |
| **Front-foot-elevated split squat** `ffe_split_squat` | Weight and reps per set, per side | Dumbbells | quads, glutes | adductors, core |  |  |
| **Knee care: slow step-downs or wall sit** `knee_care` | Reps per set, optional added load, per side | Bodyweight | quads | glutes | C · 7 |  |

- **DB Bulgarian split squat:** Rear foot on a bench, dumbbells at your sides. Lower straight down on the front leg. A slight forward lean puts more of the work on the glutes.
- **DB reverse lunge or step-up:** Reverse lunge: step back, lower the back knee toward the floor, then drive up through the front heel. Step-up: drive up onto a box through the front leg.
- **Front-foot-elevated split squat:** A split squat with the front foot on a low step or plate for more range.
- **Knee care: slow step-downs or wall sit:** Step-down: stand on a step and slowly lower the other heel to the floor, then come back up. Wall sit: back flat against a wall, hold a seated position.

## Glute bridge and thrust

The hips extend from a bent position with the upper back or shoulders supported.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Barbell hip thrust** `bb_hip_thrust` | Weight and reps per set | Barbell | glutes | hamstrings, core | C · 1 |  |
| **Single-leg glute bridge or B-stance hip thrust** `sl_bridge` | Reps per set, optional added load, per side | Dumbbells | glutes | hamstrings, core | D · 2A |  |
| **Cable glute kickback or hip abduction** `glute_kickback` | Weight and reps per set, per side | Cable | glutes |  | D · 3A |  |

- **Barbell hip thrust:** Upper back on a bench, bar across your hips. Drive the hips up until shoulders, hips and knees line up, and pause at the top.
- **Single-leg glute bridge or B-stance hip thrust:** A bridge or hip thrust where one leg does most of the work: the other foot is lifted, or just rests on its heel (B-stance).
- **Cable glute kickback or hip abduction:** Kickback: ankle strap on a low cable, push the straight leg back. Abduction: lift the leg out to the side against the cable.

## Horizontal push

Pressing away from the chest: push-ups and presses. The push-up ladder follows plan §5: deficit → paused → tempo → archer → weighted.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Push-ups** `pushup` | Reps per set, optional added load | Bodyweight | chest, triceps | shoulders, core | D · 2B | swap: Weighted push-ups |
| **Deficit push-ups** `deficit_pushup` | Reps per set, optional added load | Bodyweight | chest, triceps | shoulders, core | A · 2B | next: Paused push-ups |
| **Paused push-ups** `paused_pushup` | Reps per set, optional added load | Bodyweight | chest, triceps | shoulders, core | C · 2B | next: Tempo push-ups |
| **Tempo push-ups** `tempo_pushup` | Reps per set, optional added load | Bodyweight | chest, triceps | shoulders, core |  | next: Archer push-ups |
| **Archer push-ups** `archer_pushup` | Reps per set, optional added load, per side | Bodyweight | chest, triceps | shoulders, core |  | next: Weighted push-ups |
| **Weighted push-ups** `weighted_pushup` | Weight and reps per set | Plate or weighted vest | chest, triceps | shoulders, core |  |  |
| **DB incline press** `db_incline_press` | Weight and reps per set | Dumbbells | chest, shoulders | triceps | A · 4A |  |

- **Push-ups:** Hands under the shoulders and the body in one straight line. Lower your chest to just above the floor and press back up.
- **Deficit push-ups:** Push-ups with your hands on dumbbells or plates, so the chest can drop below hand level.
- **Paused push-ups:** Push-ups with a 2-second pause just above the floor.
- **Tempo push-ups:** Push-ups at tempo 3-1-1: 3 seconds down, a 1-second pause, 1 second up.
- **Archer push-ups:** Hands wide. Lower toward one hand while the other arm straightens out to the side, then alternate.
- **Weighted push-ups:** Push-ups with a plate on your upper back or a weighted vest.
- **DB incline press:** Lying on a bench set to about 30–45°, press the dumbbells up from your upper chest.

## Vertical push

Pressing upward. The plan uses angled presses and pike push-ups rather than strict overhead pressing.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Feet-elevated pike push-ups** `fe_pike` | Reps per set, optional added load | Bodyweight | shoulders, triceps | upper back, core | B · 2A, C (optional) | next: Deficit pike push-ups |
| **Deficit pike push-ups** `deficit_pike` | Reps per set, optional added load | Bodyweight | shoulders, triceps | upper back, core |  |  |
| **Half-kneeling landmine press** `landmine_press` | Weight and reps per set, per side | Barbell | shoulders, triceps | chest, core | B · 4A |  |

- **Feet-elevated pike push-ups:** Feet on a box, hips high, hands on the floor. Lower your head forward of your hands to form a tripod, then press back up. Progression: raise the box, then deficit pikes (hands on plates).
- **Deficit pike push-ups:** Feet-elevated pike push-ups with your hands on plates for extra range.
- **Half-kneeling landmine press:** Kneel on one knee. With one arm, press the end of a barbell anchored in a corner up and forward.

## Horizontal pull

Rowing a weight toward the torso.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Chest-supported DB row** `cs_db_row` | Weight and reps per set | Dumbbells | upper back, lats | rear delts, biceps | A · 4B |  |
| **Single-arm cable row** `sa_cable_row` | Weight and reps per set, per side | Cable | upper back, lats | rear delts, biceps | B · 4B |  |

- **Chest-supported DB row:** Lie face down on an incline bench and row the dumbbells toward your hips. The bench supports your torso.
- **Single-arm cable row:** Row a cable handle toward your hip with one arm, allowing a little controlled rotation.

## Vertical pull

Pulling the body up to a bar.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Pull-ups** `pullup` | Reps per set, optional added load | Bodyweight | lats, biceps | upper back, grip, core | A · 2A, C · 2A |  |
| ↳ **Chin-ups** `chinup` | Reps per set, optional added load | Bodyweight | lats, biceps | upper back, grip, core | B · 2B |  |

- **Pull-ups:** Hang from a bar with an overhand grip a little wider than your shoulders. Pull your chest toward the bar, then lower all the way under control. Strict: no kipping.
- **Chin-ups:** A pull-up with an underhand, shoulder-width grip. Progression: build toward 3 × 8 strict, then add a DB between your feet.

## Upper-back care

Light pulling for the back of the shoulders and the muscles between the shoulder blades.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Cable face pull** `cable_face_pull` | Weight and reps per set | Cable | rear delts, upper back | rotator cuff | A · 5 |  |
| **Prone Y-T-W or cable face pull** `ytw` | Reps per set, optional added load | Dumbbells | rear delts, upper back | rotator cuff | D · 3B |  |

- **Cable face pull:** Rope at face height. Pull it toward your forehead with the hands apart and elbows high.
- **Prone Y-T-W or cable face pull:** Lying face down on an incline bench, raise your arms into Y, T and W shapes with the thumbs up. Or do the cable face pull.

## Anti-extension core

Keeping the lower back from arching while the arms or legs move.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Dead bug** `dead_bug` | Reps per set, optional added load, per side | Bodyweight | core | hip flexors | A · 6A |  |
| **RKC plank** `rkc_plank` | Seconds per set | Bodyweight | core | hip flexors | A · 6B |  |
| **Hanging knee raise** `hanging_knee_raise` | Reps per set, optional added load | Bodyweight | core | hip flexors, grip | B · 6A | next: Hanging tuck-and-extend |
| ↳ **Hanging tuck-and-extend** `hanging_tuck_extend` | Reps per set, optional added load | Bodyweight | core | hip flexors, grip |  | next: Hanging straight-leg raise |
| ↳ **Hanging straight-leg raise** `hanging_leg_raise` | Reps per set, optional added load | Bodyweight | core | hip flexors, grip |  |  |

- **Dead bug:** On your back, arms up and knees over hips. Slowly lower the opposite arm and leg while your lower back stays pressed to the floor. Progression: hold a KB overhead, then banded or cable-resisted.
- **RKC plank:** A forearm plank where you squeeze glutes, quads and fists hard and pull the elbows toward the toes. Short and intense. Progression: long-lever plank, then plank with shoulder taps.
- **Hanging knee raise:** Hang from a bar with your shoulders active and slowly raise your knees toward your chest, without swinging.
- **Hanging tuck-and-extend:** From a hanging tuck, extend the legs out straight, then pull them back in.
- **Hanging straight-leg raise:** Raise straight legs while hanging, then lower them slowly.

## Anti-rotation and side core

Resisting being twisted or bent sideways.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Pallof press** `pallof` | Weight and reps per set, per side | Cable | obliques, core | glutes | B · 6B |  |
| **Side plank** `side_plank` | Seconds per set, per side | Bodyweight | obliques, core | glutes | C · 6A | next: Copenhagen plank |
| **Copenhagen plank** `copenhagen_plank` | Seconds per set, per side | Bodyweight | adductors, obliques | core |  |  |

- **Pallof press:** Stand side-on to a cable at chest height. Press the handle straight out and resist being turned toward the stack.
- **Side plank:** On one forearm with the body in a straight line and the hips lifted. Easier from the knees.
- **Copenhagen plank:** A side plank with the top leg on a bench and the bottom leg off the floor. Start with the knee on the bench (short lever), then the foot (long lever).

## Carry

Walking with weight while staying tall.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Suitcase carry** `suitcase_carry` | Weight and metres per set, per side | Kettlebell | obliques, grip | core, upper back | C · 6B |  |
| **Farmer’s carry** `farmer_carry` | Weight and metres per set | Kettlebell | grip, core | upper back, obliques | D · 4 |  |

- **Suitcase carry:** Walk with one heavy weight in one hand, staying tall without leaning toward it.
- **Farmer’s carry:** Walk with a heavy weight in each hand, standing tall with the shoulders down.

## Kettlebell full-body

Kettlebell movements that link the hips, trunk and shoulders.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Turkish get-up** `tgu` | Weight and reps per set, per side | Kettlebell | shoulders, core | glutes, rotator cuff | C · 5 |  |
| **KB complex** `kb_complex` | Weight per round | Kettlebell | glutes, quads, shoulders | hamstrings, core, grip, heart and lungs | C (optional), D · 1 |  |

- **Turkish get-up:** Lying on your back with a kettlebell pressed up, stand up step by step while the bell stays locked out above you, then reverse back down.
- **KB complex:** Five moves back to back without setting the bell down: swing, goblet squat, single-arm clean, press, reverse lunge. One round is the whole sequence.

## Conditioning

Work and rest rounds, run with the interval timer.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Conditioning: KB swing intervals** `kb_swing_iv` | Rounds completed, plus the weight used | Kettlebell | glutes, hamstrings | core, grip, heart and lungs | A · 7 | swap: KB deadlift |
| **Conditioning: jump rope intervals** `jump_rope_iv` | Rounds completed | Jump rope | heart and lungs, calves |  | B · 7 | swap: Cardio: stairmaster |
| **Jump rope finisher** `jump_rope_fin` | Seconds per set | Jump rope | heart and lungs, calves |  | D · 5 |  |

- **Conditioning: KB swing intervals:** Two-hand kettlebell swings in timed rounds. The hips snap forward to float the bell; the arms only guide it.
- **Conditioning: jump rope intervals:** Jump rope in timed rounds with low, soft hops.
- **Jump rope finisher:** Continuous jump rope at an easy pace.

## Zone 2 cardio

Steady, easy-paced cardio: you can talk in full sentences.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Cardio: incline walk or stairmaster** `cardio_walk_stair` | Minutes, optional level | Treadmill or stairmaster | heart and lungs | calves, glutes | A · 8 |  |
| **Cardio: stairmaster** `stairmaster` | Minutes, optional level | Treadmill or stairmaster | heart and lungs | calves, glutes | B · 8 |  |
| **Cardio: incline walk** `incline_walk` | Minutes, optional level | Treadmill or stairmaster | heart and lungs | calves, glutes | C · 8 |  |

- **Cardio: incline walk or stairmaster:** Steady Zone 2 on a treadmill incline or the stairmaster.
- **Cardio: stairmaster:** Steady Zone 2 on the stairmaster.
- **Cardio: incline walk:** Steady Zone 2 walking on a treadmill incline.

## Mobility and cool-down

Stretches and holds, done slowly at the end of a session.

| Exercise | Logged as | Equipment | Primary | Secondary | In the plan | Next / swaps |
| --- | --- | --- | --- | --- | --- | --- |
| **Cool-down: couch stretch + deep squat hold** `cool_a` | Done or not done | None | hip flexors, quads | calves | A · 9 |  |
| **Cool-down: open books + doorway pec stretch** `cool_b` | Done or not done | None | upper back, chest |  | B · 9 |  |
| **Cool-down: pigeon or 90/90 holds + hamstring floss** `cool_c` | Done or not done | None | glutes, hamstrings | hip flexors | C · 9 |  |
| **Mobility flow** `mobility_flow` | Done or not done | None | hip flexors, hamstrings, upper back |  | D · 6 |  |

- **Cool-down: couch stretch + deep squat hold:** Couch stretch: back knee down by a wall or bench with the shin up behind you, glute squeezed. Then sit in a supported deep squat.
- **Cool-down: open books + doorway pec stretch:** Open books: lie on your side, knees bent, and rotate the top arm open toward the floor behind you. Then stretch the chest in a doorway.
- **Cool-down: pigeon or 90/90 holds + hamstring floss:** Hold pigeon or a 90/90 position on each side. Then floss the hamstrings: lying down, gently straighten and bend one raised leg.
- **Mobility flow:** World’s greatest stretch, couch stretch, thread-the-needle and a deep squat hold, done slowly.
