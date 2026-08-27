# Tableau Dashboard — Simple Build Guide

**Tableau Public link:** _<paste your published URL here when you're done>_

**Time needed:** about 45 minutes
**What you're building:** 4 charts + 3 number tiles, combined into 1 dashboard

---

## Before you start

**File to use:** `student_performance_tableau.csv` (22 columns — this is the simple one)

> There's also `student_performance_full.csv` with all 52 columns. **Ignore it.** It's only there
> if someone asks a question you want to dig into later.

**The 6 fields you'll actually use:**

| Field | What it is |
|---|---|
| `Failed` | 1 = student failed, 0 = passed. **Average this to get a failure rate.** |
| `Passed` | 1 = passed, 0 = failed. **Average this to get a pass rate.** |
| `Course` | Mathematics or Portuguese |
| `Risk Band` | Low / Moderate / Elevated / High — what the model predicted |
| `Segment` | The 4 student types (A, B, C, D) |
| `Has Past Failure` | Yes / No — did they fail a class before |

**The one trick to remember:** `Passed` and `Failed` are 1s and 0s. When you average a column of
1s and 0s, you get a percentage. That's how every chart here works.

---

## Step 1 — Connect the data

1. Open **Tableau Public Desktop**
2. Left side: **Connect → To a File → Text file**
3. Pick `student_performance_tableau.csv`
4. Click **Sheet 1** at the bottom

Done. You should see your field names on the left.

---

## Step 2 — Chart 1: Maths is harder than Portuguese

**This is your opener. It's simple and everyone gets it instantly.**

1. Drag **`Course`** → the **Columns** shelf (top)
2. Drag **`Passed`** → the **Rows** shelf
3. On the green `SUM(Passed)` pill in Rows: **right-click → Measure → Average**
4. Right-click the left axis → **Format** → under Numbers pick **Percentage** → set decimals to 1
5. Drag **`Passed`** onto the **Label** button (in the Marks card) → right-click that pill →
   **Measure → Average**
6. Rename the tab at the bottom: double-click "Sheet 1" → type `Pass Rate by Course`

**You should see:** Mathematics ≈ **67.1%**, Portuguese ≈ **84.6%**

If your numbers don't match, you forgot to change SUM to **Average**.

---

## Step 3 — Chart 2: Does the model actually work?

**This is your most important chart. Spend the most time here.**

1. New sheet (the **+** tab at the bottom)
2. Drag **`Risk Band`** → **Columns**
3. Drag **`Failed`** → **Rows** → right-click the pill → **Measure → Average**
4. Format the axis as a **Percentage** (same as before)
5. Drag **`Failed`** onto **Label** → set it to **Average** too
6. Drag **`Failed`** onto **Color** → set to **Average** → pick a red-ish palette
7. **Fix the order** (important — Tableau sorts alphabetically by default):
   - Right-click the `Risk Band` pill → **Sort**
   - Choose **Manual**
   - Drag them into this order: **Low → Moderate → Elevated → High**
8. Rename the tab: `Risk Bands`

**You should see bars climbing left to right:**

| Risk Band | Failure rate |
|---|---|
| Low | **2.9%** |
| Moderate | 13.0% |
| Elevated | 31.1% |
| High | **57.6%** |

**Why this matters:** the model sorted students into 4 groups *before* seeing their grades, and the
groups really do fail at different rates. That's the whole project in one picture.

---

## Step 4 — Chart 3: The biggest warning sign

1. New sheet
2. Drag **`Has Past Failure`** → **Columns**
3. Drag **`Failed`** → **Rows** → **Measure → Average**
4. Format axis as **Percentage**, add the **Label** like before
5. Rename the tab: `Past Failures`

**You should see:**

| Failed a class before? | Students | Failure rate |
|---|---:|---:|
| No | 861 | **15.0%** |
| Yes | 183 | **55.2%** |

Students who have failed a class before are **more than 3½ times as likely** to fail again.

---

## Step 5 — Chart 4: The four student types

1. New sheet
2. Drag **`Segment`** → **Columns**
3. Drag **`Failed`** → **Rows** → **Measure → Average**
4. Format as **Percentage**, add **Label**
5. Drag **`Segment`** onto **Color**
6. Rename the tab: `Student Segments`

**You should see:**

| Segment | Failure rate |
|---|---|
| A - Supported achievers | 14.6% |
| B - Steady middle | 21.4% |
| C - Disengaged social | 34.2% |
| D - High-risk repeaters | 34.7% |

---

## Step 6 — The three number tiles

These are just big numbers. Make one sheet for each:

**Tile 1 — Overall pass rate**
1. New sheet
2. Drag **`Passed`** → the **Text** button on the Marks card
3. Right-click the pill → **Measure → Average**
4. Click **Text** → click the **…** box → make the font big (28pt) → type ` overall pass rate` after it
5. Rename tab: `KPI Overall` → **should show 78.0%**

**Tile 2 — Students flagged**
1. New sheet
2. Drag **`Flagged At Risk`** → **Filter** → tick only **Yes** → OK
3. Drag **`Student ID`** → **Text** → right-click pill → **Measure → Count**
4. Rename tab: `KPI Flagged` → **should show 406**

**Tile 3 — Number of students**
1. New sheet
2. Drag **`Student ID`** → **Text** → **Measure → Count**
3. Rename tab: `KPI Total` → **should show 1,044**

---

## Step 7 — Build the dashboard

1. Click the **New Dashboard** icon at the bottom (next to the + for a new sheet)
2. Left panel → **Size** → choose **Automatic**
3. Drag your sheets from the left onto the canvas in this layout:

```
┌──────────────────────────────────────────────┐
│  KPI Total   KPI Overall   KPI Flagged       │   <- the 3 tiles, side by side
├─────────────────────┬────────────────────────┤
│  Risk Bands         │  Pass Rate by Course   │
├─────────────────────┼────────────────────────┤
│  Past Failures      │  Student Segments      │
└─────────────────────┴────────────────────────┘
```

4. **Add a title:** drag a **Text** object to the top → type
   *"Student Performance: Who Is At Risk of Failing?"*

5. **Add a filter** (so you can click through it live in your presentation):
   - Click on the **Risk Bands** chart
   - Click the small ▾ arrow in its top-right corner → **Filters → Course**
   - A filter box appears → click **its** ▾ arrow → **Apply to Worksheets → All Using This Data Source**

   Now clicking "Mathematics" filters every chart at once. **This is a great live demo moment.**

6. **Add the caveat box** (do not skip this — it's what keeps the project honest):
   Drag a **Text** object to the bottom and paste:

   > **How to read this:** the risk score estimates how likely a student is to fail, using only
   > information known at enrolment — no grades. It helps a school decide **where to send tutoring
   > support.** It is not a judgement about any individual student. About 3 in 5 flagged students
   > would have passed anyway, and 42% of "High" risk students still pass.

---

## Step 8 — Publish

1. **File → Save to Tableau Public As…**
2. Sign in (make a free account if you don't have one)
3. Name it: `Student Performance - Who Is At Risk`
4. It opens in your browser once saved — **copy that URL**
5. Paste the URL:
   - at the top of this file
   - in `reports/final_report.md`, section 5

**Screenshots for the repo:** in Tableau, **Dashboard → Export Image…** → save into
`dashboard/screenshots/` as `dashboard_full.png`.

---

## If something looks wrong

| Problem | Fix |
|---|---|
| Numbers are huge (like 814 instead of 78%) | You left it on SUM. Right-click pill → **Measure → Average** |
| Shows a decimal (0.78) instead of 78% | Right-click axis → **Format → Numbers → Percentage** |
| Risk bands are in the wrong order | Right-click the pill → **Sort → Manual** → drag into Low, Moderate, Elevated, High |
| A chart is blank | You probably dragged a field to the wrong shelf. Undo (Ctrl+Z) and retry |
| Filter only changes one chart | Filter ▾ → **Apply to Worksheets → All Using This Data Source** |

---

## Optional extras (only if you have spare time)

- **Grade distribution:** `Final Grade` on Columns, `Student ID` (Count) on Rows, `Result` on Color.
  Shows the spike of students who scored 0 — the ones who dropped out or never sat the exam.
- **Model accuracy:** `Prediction Outcome` on Columns, `Student ID` (Count) on Rows. Shows the
  true/false positives and negatives.

Skip both if you're short on time. The 4 main charts tell the story on their own.
