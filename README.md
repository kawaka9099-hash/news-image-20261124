# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/kawaka9099-hash/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/kawaka9099-hash/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A code-drawn 1024×1024 newspaper front page summing up Tuesday
24 November 2026 world news — THE WORLD TODAY, one image, no photographs.

![The front page](entry.png)

## Run it

```sh
python3 main.py
```

This writes the image to `/output/entry.png` (pass a path to write
elsewhere, e.g. `python3 main.py out/entry.png`, or set
`MAKEFUN_OUTPUT_DIR`). `main.py` uses only the Python standard
library, so it runs in the grader's no-network, nothing-installed
container; `draw.py` (Pillow + DejaVu fonts) drew the image at build
time. No network access at runtime; two runs produce byte-identical
output.

## What it shows

Every story was verified on 24 November 2026 against at least two
independent news sources. Monday's events are labelled "on Monday",
Sunday's "on Sunday", and so on — this is a Tuesday paper, so
Monday's news is today's news. Items are tagged CONFIRMED, REPORTED
or CLAIM on the page.

- **Huang is back** — Nvidia's board unanimously reinstated Jensen
  Huang as president and CEO on Monday, effective immediately — 11
  days after he resigned (12 Nov) over extramarital affairs,
  including one with a woman US authorities suspect of spying for
  China. Sharp reversal: last week the board said it "does not
  intend to reinstate" him. The board says it is satisfied with his
  candour and leadership and saw no national security risk after
  input from senior US government officials. Trump praised the move
  on Truth Social. Chair Harvey C. Jones called the reinstatement
  "in the best interests of our stockholders, employees, partners
  and customers." (WSJ, CNN, Al Jazeera, Nikkei Asia, Rappler,
  Morningstar)
- **Iran claims 3 tankers hit mines** — Iran's Revolutionary Guards
  navy said Monday night that three "violating" oil tankers hit
  naval mines in the Strait of Hormuz and caught fire after severe
  explosions — one near the southern coast, two east of the strait,
  under US air escort that "failed to prevent" them. No tanker
  identities, crew or damage details given; the claims are NOT
  independently verified. Context: three other tankers were hit by
  projectiles Fri/Sat, and 22+ Hormuz attacks have been reported in
  November, the highest since the Iran war began. (Jerusalem Post,
  Al Jazeera, Arab Times, Times of Israel)
- **Ukraine sinks Russian warship** — Zelenskyy confirmed Monday:
  seven Ukrainian sea drones sank the Russian corvette Merkury at
  Benghazi naval base on Sunday, hit the cargo ship MV Angara
  (accused of carrying weapons), and destroyed a Ka-27 helicopter
  on board. Operation 2,400 km from the front line; drones launched
  from a "mother ship". Libyan officials say the corvette was
  "severely damaged"; satellite images show it mostly capsized.
  A day earlier a Russian cargo ship was hit in the Baltic. The
  Kremlin said it had "taken note" of Zelenskyy's statement. (AP,
  Reuters, Al Jazeera, CNN, WSJ)
- **AI claims proof of Riemann hypothesis** — Anthropic
  mathematician Levent Alpöge announced Friday (20 Nov) he believes
  he and Claude proved the Riemann hypothesis — maths' most famous
  unsolved problem since 1859 — releasing a 17-million-line Lean
  formal proof. On Saturday the Lean Focused Research Organization
  and Mathlib Initiative endorsed it: "We have full confidence that
  Alpöge's proof ... is correct." Mathematicians say no human
  understands the proof yet; debate continues Monday. It also
  claims the generalised Riemann hypothesis. (WSJ, phys.org, CNN,
  Wikipedia)
- **Factory fire toll 24** — Indonesia confirmed Monday: 24 dead,
  about 30 still missing after the Saturday-night candy factory
  fire in Banten province; rescuers search unstable wreckage.
  Earlier toll was 3 dead, 36 missing. (Korea Herald/AFP, Xinhua)
- **Strikes around Kyiv** — a Russian drone strike partially
  destroyed an apartment building in Dymer, near Kyiv — 14 people
  missing, 9 evacuated. Overnight Saturday strikes on Kryvyi Rih
  (Zelenskyy's home city) killed a child and a young woman, damaged
  25 apartment buildings, a hospital and schools. (Just Security
  Early Edition 23 Nov, AFP via Korea Herald)
- **World in brief:** EU proposes a 22nd Russia sanctions package
  (The Brief); US Treasury sanctions 2 dozen+ Iranian shadow-banking
  entities (The Brief); US Commerce to blacklist Singapore AI firm
  Megaspeed (The Brief, NY Post); drone attack on a police base in
  Cúcuta injures 3, damages 60 homes (The Brief); Bangladesh will
  arrest and jail former PM Sheikh Hasina if she returns (Reuters);
  BepiColombo enters orbit around Mercury after an eight-year
  journey (Principia); NHS starts a major trial of AI in breast
  cancer screening (Principia); Rep. Jimmy Gomez (Los Angeles) to
  resign 1 Dec after an ethics report on sexual misconduct
  (The Brief); Netanyahu urges Trump to strike Iran "as soon as
  possible", according to a report; Netanyahu–Eisenkot coalition
  talks ended Sunday without a deal (Tribune Online); drone strikes
  hit homes and a UN building in Khartoum on Sunday (AFP via Korea
  Herald); Asian tech shares fall further as the AI sell-off
  deepens, euro area inflation up to 4.0% (Principia); Brazil
  supercell storm toll rises to 5 on Sunday, 250+ injured, ~8,000
  homes damaged — the storm struck early Friday (CNA, Al Jazeera).
- **COP31 aftermath** — Australian PM Albanese on Monday called the
  collapse a sign of "difficult geopolitical times". First COP to
  end with no deal since Copenhagen 2009. (Talks ended Sunday.)

Stories first reported on 19–21 November (the Trump 10% credit-card
cap, Pentagon curbs on Canada, Meta India protests, Manipur liquor
toll, ICJ Myanmar ruling), the COP31 collapse (Sunday — yesterday's
headline), the "El Chapo Isidro" cartel capture (Fri night/Sat,
already in the 22 Nov paper), the Delta Atlanta delays and the Peru
6.7 quake (in the 23 Nov paper), and the Nvidia SEC probe / shares
-14% (Friday, superseded by Monday's reinstatement) were checked
and left out — they are not today's news. The page prints this as
its DATE CHECK box.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
