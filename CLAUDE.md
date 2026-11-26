# Training Log PWA

Personal workout tracker for one user (Santi, senior SWE: Python, distributed systems, AWS). Be concise; skip beginner explanations.

## Source of truth
- `docs/training-plan.md` is the domain spec. If the app and the plan disagree, the plan wins. If the user's PT disagrees with the plan, the PT wins. Never add medical advice beyond what the plan says.
- `SESSIONS`, `WARM` and `WARM_FOCUS` in `index.html` mirror the plan. Change them only when the plan changes.
- `EXERCISES` in `index.html` mirrors `docs/exercise-dictionary.md` (descriptions, muscles, families, progressions, swaps). Change both together. Descriptions cover setup and execution only; safety and pain guidance comes only from the plan. Progressions (`next`, `up`) and swaps (`alt`) must be ones the plan names.

## Stack and layout
- `index.html` holds the whole app: inline CSS and vanilla JS (plain functions, delegated events through `ACT` (clicks) and `INP` (inputs)). No framework, no build step, no dependencies. Ask before adding any.
- `sw.js` (service worker), `manifest.json`, `icon-180.png` (apple-touch-icon, must be PNG), `icon-192.png`, `icon-512.png` (also maskable).
- Fonts: Barlow (body) and Barlow Condensed (headings, numerals) from Google Fonts.

## UX structure
- **Phone (<900px):** four tabs. Primary actions live in a fixed dock above the tab bar, within thumb reach.
  - **Today (`home`):** a coach view. It shows a hero card (in progress / done today / today / rest day), a "This week" strip with "N of M sessions" (no streaks), coach notes for the next session, then the interval timer card, the month calendar, a tapped day's details, and the "Up next" agenda. The dock holds Start/Resume.
  - **Train:** two views, toggled by `prefs.tview`.
    - **Focus** (default): one step per screen. Steps are 0 = warm-up, 1..N = exercises, N+1 = wrap-up (pain + finish).
      - The dock's big button ticks the next set and auto-advances after 450ms. It alternates superset members (2A ↔ 2B, via `group()`/`nextStep()`) and then moves forward. Optional exercises are skipped on auto-advance.
      - Navigation: swipe left/right, the ‹ › buttons, or ←/→ and Space on a keyboard.
      - The current step lives in `S.fi` and isn't persisted. On reload, `resumeStep()` picks the first incomplete exercise.
    - **List:** all cards on one page.
  - **History:** a logbook (sessions grouped by week) and lift progress.
  - **Settings:** training days, weight unit (lb/kg), theme, timers, backup.
- **Exercise dictionary** (`DX`, full-screen `#dict`, built like `#hiit`): opened from the Train header button, any exercise name on a Train card, or "About this exercise" in Lift progress. A list grouped by family with a muscle filter, and a detail page per exercise or family: description, muscles, logged-as, equipment, plan slots and notes, next level / comes after / swaps / variants, and history (family pages pool every member). `DX.stack` drives Back; Escape goes back.
- **Warm-up:** six blocks (`WARM`), one tick per block, with the block's exercises listed under it. The `focus` block's exercises come from `WARM_FOCUS[session]`. Switching sessions keeps the shared block ticks and clears `focus`.
- **Per-set logging:** one row per set: a tick circle, a weight box when the exercise is loaded, and a value stepper when its track counts something. Exercises with neither (track `check`) keep plain circles.
  - `measure(x)` comes from the slot's track (`TRACK[x.track].v`: reps, rounds, s, m, min) with `x.rx[0]` as the default. Rep values prefill from this session, else last time's same set, else `rx[0]`.
  - Weight kinds (`wkind(x)`): `load` = a box per set (lb/kg); `add` (bodyweight: optional added load) and `level` (cardio, unitless) = one box under the rows that applies to every set; null = none. `wVal()` prefill: this set, else carried from the nearest earlier set typed this session, else old `cur.w` text, else last time's same set converted to `prefs.unit`. Defaults show muted (`.dflt`) and are saved as shown at finish, like rep defaults.
  - **Doing** menu (`swapSel`): a slot can log its plan swaps (`alt`) or its next level instead (`cur.sw[i]`). The prescription (sets, `rx`, track, weight kind) stays the slot's; the record is saved under the variant's id with `p` = the planned id. Nudges only show for the planned exercise.
- **Rest timer:** starts when a set is ticked (circle or big button). There's no rest after single-set items or the session's final set.
  - Duration is `prefs.restMain` for exercise 1 in A–C and `prefs.restAcc` for everything else. ±15s and Skip are on the bar.
  - Undo or untick cancels it. It's timestamp-based and only beeps live (not after a background gap).
- **Interval timer** (`H`, full-screen `#hiit`): work/rest/rounds plus get-ready. Work 0 = untimed ("Round done").
  - Launch points: the Today presets (Boxing, HIIT, Tabata, Complex, last used), which aren't saved to history, or an exercise with `iv` in `SESSIONS`, which logs rounds to the current session (`log: 'sets'` ticks a set per round; `'rounds'` puts the count in the one set's value).
  - It catches up through phases missed while backgrounded. Wake lock is held while it's open.
- Cues are Web Audio beeps (unlocked on the first pointer/key) plus a screen flash. The 3-2-1 countdown is quieter.
- **Desktop (≥900px, `S.wide`):** a dashboard with no tabs or dock. It has three independently scrolling columns: Today + Settings | Train (always the list view) | History. `render()` preserves each column's scroll position.
- **Coach notes** (`coachNotes`) use only logged data and plan text:
  - Week-1 calibration, when there's no history.
  - The pain rule, when the last session's pain was >3.
  - Double-progression nudges (`nudgeFor`/`nudgeText`). With per-set reps from last time, a nudge is definite ("hit 10 on all sets: add 5 lb") or a build note ("last time 10, 9, 8: build toward 10"). Entries from before per-set logging keep the conditional wording.
- Hosted on GitHub Pages under a subpath (`/training-log/`). **Every asset path stays relative**: no leading `/`.

## Run and test
- Live reload: `python dev.py` (localhost), or `python dev.py --bind <LAN IP>` to test on the iPhone over Wi-Fi. `dev.py` is a stdlib-only dev tool, not part of the app. It injects a reload snippet into served HTML and sends `no-store`. Plain HTTP on a LAN IP isn't a secure context, so the service worker, wake lock, and Web Share are off there.
- To test under the Pages subpath, run `python -m http.server 8000 --bind 127.0.0.1` from the repo's parent folder and open `http://localhost:8000/training-log/`.
- Add `?nosw` to the URL to unregister the service worker while iterating. Otherwise stale-while-revalidate serves the previous build.
- Check in a phone viewport (375×812, plus 320 wide) in light and dark. Requirements: no horizontal scroll, tap targets ≥44px, no console errors.
- Real target: iPhone, installed to the Home Screen from Safari, used one-handed with spotty signal. Mac Safari "Add to Dock" is secondary. Desktop checks don't replace testing in the installed iPhone app.
- Small commits with clear messages. Run the app locally before each commit.

## Exercise model
- `EXERCISES` (keyed by permanent id) holds families (`kind: 'pattern'`: Squat, Hinge, …; never logged) and exercises. `parent` links an exercise to its family or to the exercise it's a variant of. `exDef(id)` resolves inheritance of `track`, `equip`, `side`, `wt` and `muscles` (muscles replace as a whole). `family(id)` = top pattern; `ancestors(id)` for breadcrumbs.
- `TRACK`: `load_reps`, `reps`, `time`, `carry`, `rounds`, `duration`, `load` (weight per round, no count), `check`. Each sets the value unit and the default weight kind. Muscles come from `MUSCLES`, equipment from `EQUIP`. Boot logs a console error for any unknown id, track, muscle or equipment.
- `SESSIONS` slots reference `id` and hold the plan's prescription: `sets`, `reps` (display text), `rx: [low, high]`, `nn`, `opt`, `iv`, `note`. Boot copies `n` and `track` from the library onto each slot. `effId(s, i)`/`effName(s, i)` give the exercise actually logged (a swapped-in variant, else the planned one).

## Data model (localStorage, every access wrapped in try/catch)
| Key | Shape |
|---|---|
| `hist` | Array, newest first: `{d: ms timestamp, s: "A"\|"B"\|"C"\|"D", v?: 3, pain: 0-10, loc: string, ex}`. **v3 entries** (`v: 3`): `ex: {[exerciseId]: {n: setsDone, r?: [valuePerSet], w?: [weightPerSet \| null], u: "lb"\|"kg", nm: nameWhenLogged, p?: plannedId, t?: oldText}}`. **Older entries** (no `v`): `ex: {[exerciseName]: {n, w: weightText, r?}}`. They are never rewritten |
| `cur` | In-progress session or `null`: `{s, done: {[exIndex]: setsDone}, reps: {[exIndex]: {[setIndex]: number}}, wv: {[exIndex]: {[setIndex]: number\|null}}, sw: {[exIndex]: exerciseId}, w: {[exIndex]: weightText}, warm: {[blockId]: bool}, pain, loc}`. `wv` holds only weights typed (null = cleared on purpose). `w` exists only in sessions started before per-set weights and is read as a default. `warm` was keyed by index before the block warm-up; old numeric keys are ignored. `reps` holds only values the user changed or the interval timer wrote. The record is built at finish by `curRec()` |
| `days` | Weekday numbers (0 = Sun) used for suggestions. Default `[1,3,5]` |
| `prefs` | UI preferences only, not exported: `{skin: "slate"\|"iron"\|"hv"\|"term"\|"amber"\|"phos"\|"frost"\|"ember"\|"synth", mode: "auto"\|"light"\|"dark", focusHv: bool, tview: "focus"\|"list", restAuto: bool, restMain: s, restAcc: s, sound: bool, iv: {w, r, n, prep}\|null, unit: "lb"\|"kg"}` |
| `<key>.corrupt` | Raw copy of a value that failed to parse, kept so the next save doesn't destroy it |

- **Read every history entry through `recsOf(e)`**, never `e.ex` directly. It returns a cached `Map(id → {n, r, w[], u, p, nm, txt})` for both formats: old names map through `ALIAS` (every exercise's `n` plus its `aka`), old text weights become a per-set array from `firstNum` (unit `kg` if the text says so, else `lb`) and keep the text in `txt` for display. A name no exercise claims becomes the id `?name`: still shown, listed under Other in Lift progress, never lost.
- Exercise ids are permanent. **To rename, change `n` and move the old name into `aka`.** Never reuse or delete an id that has history.
- `cur` is keyed by exercise **index**: reordering a session list mid-session misattributes sets.
- Weight units: each v3 record keeps the unit it was entered in. Display and charts convert to `prefs.unit` (`conv()`, rounded to 0.5). Switching units converts the weights typed in `cur.wv` (not levels).
- Export format: `{app: "training-log", v: 3, exported, hist, days}`. v3 = id-keyed entries; v2 added the optional `r`. Import accepts any version or a bare `hist` array. It de-dupes on `d + s`, keeps unknown fields, and never overwrites `days`.
- Calendar day keys come from `dk()`: `YYYY-M-D`, no zero padding (computed at runtime, never stored).
- **Existing user data must never be lost.** Ask before any data-model change. Any change needs a backward-compatible read or a migration, plus a bump of `EXPORT_V`. Old backup files must still import.

## Domain rules the app implements
- Sessions run as a **rotation, not fixed weekdays**. Next = the session after the last logged one (`nextAfter`), or `cur.s` if a session is in progress. The cycle is A→B→C, or A→B→C→D when 4+ training days are selected.
- Suggestions fill selected weekdays from today for `SUGGEST_DAYS` (70), skipping days that are already logged. A skipped suggested day disappears because the rotation moves on.
- Double progression is implemented via per-set reps and coach nudges. Phases (week 1 calibrate, 2-3 build, 4-6 push, 7 deload, 8-13 block 2) and 6-week retests are in the plan, but the user decided **not** to track them in the app.
- Pain rule: up to 3/10 that settles within 24h is fine. Above 3, the Train tab shows the plan's reduce-or-swap guidance.
- Pull-ups are "per plan" and the set count changes by week. Fixed rows for now (A: 5, C: 6), with the weekly scheme in the note, and no nudge (`nn: 1`, also on knee care and Y-T-W, whose prescriptions aren't a single range).
- Nudges (`nudgeFor`): rep-tracked slots with `rx` only. Bodyweight exercises (`equip: 'bw'`) use the plan's `up` wording, else "move up to <next>", else "move up a level". Loaded ones need a logged weight and say +5 lb (DB) / +5–10 lb (barbell) / add weight, in kg when that's the unit.
- Session C has two optional cards from the plan: pike push-ups (busy 2-day weeks) and KB complex (3-day weeks without D). Optional cards count toward totals only when ticked.

## Quirks to preserve
- Lift progress plots the heaviest set per session, converted to `prefs.unit` (levels unconverted), grouped by family. Old text weights chart through `firstNum` ("135 lb" → 135; "BW" is skipped but still shown in the logbook).
- Set-circle taps patch the DOM (`updateCard`) and text inputs never trigger `render()`, so focus is never lost. Weight boxes (`INP.wv`) update the later sets' defaults in place. Keep it that way. `render()` replaces `#app` wholesale and restores focus via `focusKey`.
- The in-progress session survives reloads and app kills. The app opens on Train when `cur` exists.
- Wake lock is held only on the phone Train tab (never on the desktop dashboard) and is re-acquired on `visibilitychange`.
- Don't name a CSS class `.big` for anything except the focus dock button: it sets `flex-direction: column`. (The set circles' large size is `.sets.lg`.)

## Design language
- **Themes** are CSS variable sets selected by `<html data-skin>`:
  - Every theme has a light and a dark palette. `applyTheme()` (and the `<head>` script) always sets `data-theme` to the effective mode: `prefs.mode`, or the system setting when it's `auto`. Dark is each theme's base block; light lives under `[data-theme=light]`.
  - **Classic:** Slate and teal (default, no `data-skin` attribute), Iron and chalk (`iron`, 5px radius), High-vis (`hv`, larger type).
  - **Terminal family** (`term`, `amber`, `phos`, `frost`, `ember`, `synth`): the same palette slots plus `data-mono` on `<html>`, which gives hairlines, a 2px radius and monospace headings (`--fh: var(--fm)`). Mono is wider than Barlow Condensed, so `[data-mono]` scales headings down; check 320px when adding large text.
  - `SKINS` lists every theme with its group, and Settings renders it as a `<select>` with optgroups plus a live swatch. The palettes were contrast-checked by script: text colours on `--surf`/`--surf2`/`--bg`, `--on-acc` on `--acc`, `--warn` on `--warn-bg`, and `--on-c` on each session colour, all ≥4.5.
- `--fm` is the system monospace stack (`ui-monospace`, SF Mono on iOS; no download). Every theme uses it for numbers (steppers, timers, pain, stats, day numbers, `.mono`) and for micro-labels (`.lab`, `.wkh`, `.dow`, `.nl`, `.ag-h`, legend).
- Calendar: a hairline grid (1px gaps over `--line`), weekend columns on `--surf2`, today as a solid accent square. Days carry an event bar (`.ev`): a session-coloured left rule plus a letter, tinted when logged and dashed when suggested. A short focus word (`SHORT`) appears when the grid is ≥470px (container query).
- Today ends with the "Up next" agenda (`agendaHTML`), built from `suggestions()`. The selected-day card shows only when a non-today day is tapped or today has a logged session.
- Coach notes and logbook rows use the same left-rule pattern: the colour carries meaning, with a mono label or date beside it.
- `prefs.focusHv` swaps to high-vis while phone focus mode is showing. `applyTheme()` runs on every render and syncs `<meta name=theme-color>`. A tiny `<head>` script applies the saved theme before first paint.
- A new theme must define every color variable the slate dark block sets, and must pass WCAG AA in its own right.
- Session colors: `--ca` teal, `--cb` blue, `--cc` orange, `--cd` purple. The `.cA`-`.cD` classes set `--c`, and badges, chips, and cards use `var(--c)`, with `--on-c` for text on a fill.
- Logged days get a tinted event bar on the calendar (a solid badge in day details and the logbook). Suggested days get a dashed bar.
- Barlow Condensed for headings and numerals, Barlow for body. Cards: 1px border, 10px radius. Tap targets ≥44px. Inputs ≥16px font, so iOS doesn't zoom. Mobile-first, with safe-area insets respected. Primary actions sit near the bottom for thumb reach.
- Accessibility: aria labels on icon/letter buttons, `aria-pressed` on toggles, WCAG AA contrast (re-check whenever a color changes), motion only under `prefers-reduced-motion: no-preference`.

## Platform constraints (iOS Safari / installed PWA)
- Storage is separate for a Safari tab, the Home Screen app, and Mac Safari. There is no sync, which is why export/import exists.
- iOS has no Vibration API. Timers use sound plus a visual flash, and Web Audio must be unlocked by a user gesture. JS is suspended when the app is backgrounded, so timers must be timestamp-based.
- iOS has no Background Sync and no Web Bluetooth. Web Push works only in the installed app, needs a user tap to grant permission, and needs a server to send.
- **Every release: bump `V` in `sw.js`.** Install pre-caches the shell with `cache: 'reload'` and activate deletes old caches. With SWR, users see a new build on the second launch.
- Everything must work offline after the first load (fonts included, via SWR).

## Working agreements
- Ask before changing the data model, adding dependencies or a build step, or deviating from the plan.
- Plan before building roadmap items, and wait for a go-ahead.

## Roadmap (priority order)
1. ~~Rest timer~~ done, plus an interval timer (boxing / HIIT / complexes).
2. ~~Per-set logging~~ done, including per-set weight for loaded exercises.
3. ~~Home hero card~~ done as the Today/coach view.
4. Pain by body area (lower back / knee / neck) with a trend chart. Pain >3 suggests the plan's alternative next time.
5. ~~Theme picker~~ done: 9 themes (Classic and Terminal families), each with Auto/Light/Dark. ~~lb/kg units~~ done.
6. ~~Phase tracking~~: dropped by the user.
7. ~~Swap-to-alternative per exercise~~ done (Doing menu, from the library's `alt`/`next`). Not done: suggesting the swap automatically after pain >3.
8. Edit past sessions, undo, notes, first-run setup.
9. Optional sync backend. Discuss before building and weigh it against export/import.
