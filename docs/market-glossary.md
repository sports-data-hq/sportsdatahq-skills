# Market Glossary

Quick reference for odds and probability terms used across the SportsDataHQ skills. Prices are information about the market. The skills never size stakes or recommend wagers.

## Odds Formats

| Term | Definition |
|------|-----------|
| **American odds** | +150 means a $150 gain on a $100 stake. -180 means a $180 stake gains $100. Standard in the US. |
| **Decimal odds** | 2.50 means $2.50 returned per $1 staked ($1.50 gain). Standard internationally. |
| **Fractional odds** | 3/2 means a $3 gain per $2 staked. Standard in the UK. |
| **Implied probability** | The probability embedded in a price, margin included. -180 implies about 64.3%. |

## Margin and Fair Probability

| Term | Definition |
|------|-----------|
| **Vig (vigorish)** | The sportsbook's margin built into the prices. Also called juice, overround or margin. A -110/-110 line carries about 4.5%. |
| **Overround** | Total implied probability across all outcomes. A market with no margin sums to 100%. A typical two-way hockey moneyline sums to 104-106%. |
| **Fair (no-margin) probability** | The implied probability after the margin is removed, so the outcomes sum to 100%. This is the number to compare a model against. |
| **Devig** | The step that removes the margin. Common methods: multiplicative, power, Shin, worst-case. |
| **Shin method** | A devig method that allows for informed trading. Often the most accurate on lopsided prices. |
| **Power method** | A devig method that raises each implied probability to a common exponent. Simple, and steadier than multiplicative on lopsided lines. |

## Model vs Market

| Term | Definition |
|------|-----------|
| **Model vs market gap** | Our probability minus the market's fair probability for the same outcome. A description of how the two differ, not an instruction. |
| **Line movement** | How a price or number changed between opening and close. |
| **Opening line** | The first price captured for a market. |
| **Closing line** | The last price captured before the game starts. It is the market's final pre-game estimate. |
| **Closing-line comparison** | Whether the closing fair probability moved toward or away from the model's earlier number. Over a large sample it is a measure of model quality. |
| **Steam move** | Rapid line movement across several books at once. |

## Market Types

| Term | Definition |
|------|-----------|
| **Moneyline (ML)** | Which team wins outright. |
| **Puck line / spread** | A winning margin threshold (hockey standard: -1.5 / +1.5 goals). |
| **Total (over/under)** | Combined score against a number. |
| **Prop** | A market on one player's stat (goals, assists, shots, saves). |
| **Same-game combination** | Several outcomes from one game priced together. The legs are correlated, so their probabilities do not multiply independently. |
| **Futures** | Long-term markets (division winner, championship, award). |
| **Alternate line** | The same market at a different number, such as a ladder of totals. |

## Statistical Terms

| Term | Definition |
|------|-----------|
| **Brier score** | Mean squared error of probability forecasts. Lower is better. Splits into reliability, resolution and uncertainty. |
| **Log loss** | Penalizes confident wrong forecasts heavily. Common training objective. |
| **Calibration** | Whether predicted probabilities match outcomes: 60% forecasts should happen about 60% of the time. |
| **Confidence interval** | The range a measured rate plausibly falls in given the sample size. Report it with every backtest. |
| **Sample size** | The number of events behind a result. Small samples give wide intervals. |
| **Per-season breakdown** | The same metric reported season by season, to show whether a result is stable or driven by one year. |
| **Regression to the mean** | Extreme results tend to move toward the average. High PDO regresses. Hot streaks cool. |
