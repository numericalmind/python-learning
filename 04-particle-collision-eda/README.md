# Particle Collision EDA ⚛️

A beginner-friendly exploratory data analysis project using simulated high-energy physics collision data from the HIGGS dataset.

The goal of this project is to practice exploratory data analysis (EDA) with Python while exploring differences between simulated **signal** and **background** collision events.

## Dataset

This project uses a 10,000-event subset of the **HIGGS dataset**.

The dataset was generated using Monte Carlo simulations and contains:

* 10,000 collision events
* 29 columns
* 1 binary event label
* 21 low-level kinematic features
* 7 high-level physics features

The event labels are:

* `1` — Signal
* `0` — Background

## Analysis

The project explores the dataset using:

* Descriptive statistics
* Signal and background event counts
* Grouping and aggregation
* Comparison of selected physics features
* Pearson correlation analysis
* Scatter plot visualization

## Key Findings

The dataset contains:

- **5,295 signal events**
- **4,705 background events**

The classes are therefore relatively balanced.

For the initially investigated features, the mean values of `lepton_pt`, `missing_energy`, and `m_wwbb` differ between signal and background events.

Among these three features, `missing_energy` showed the largest absolute difference in mean values.

### Correlation Analysis

For the three investigated features:

- `lepton_pt` and `missing_energy`: **r ≈ -0.147**
- `lepton_pt` and `m_wwbb`: **r ≈ 0.142**
- `missing_energy` and `m_wwbb`: **r ≈ 0.313**

The strongest linear relationship among these selected variables was between `missing_energy` and `m_wwbb`, showing a positive but not strong correlation.

### Signal vs Background

The `m_wwbb` distributions for signal and background events overlap substantially, indicating that this feature alone does not clearly separate the two event classes.

However, the distributions are not identical. Signal events are more concentrated around lower `m_wwbb` values, while the background distribution extends further toward higher values.

This suggests that `m_wwbb` contains some information related to event type, although additional features would be needed for clearer separation.

## Signal vs Background Analysis

The dataset contains two event classes:

- **Signal:** 5,295 events
- **Background:** 4,705 events

To explore whether physical features differ between the two event types, the distribution of `m_wwbb` was compared for signal and background events.

![Signal vs Background m_wwbb Distribution](m_wwbb_signal_vs_background.png)

The two distributions overlap substantially, which suggests that `m_wwbb` alone is not sufficient to clearly separate signal and background events.

However, the distributions are not identical. Signal events are more concentrated around lower `m_wwbb` values, while the background distribution extends further toward higher values.

This suggests that `m_wwbb` may contain useful information when combined with other collision features.

## Visualization

The scatter plot below shows the relationship between `missing_energy` and `m_wwbb`.

![Missing Energy vs m_wwbb](correlation_plot.png)

The plot suggests a positive but relatively weak linear relationship, consistent with the Pearson correlation coefficient of approximately **0.313**.

## Technologies

* Python
* Pandas
* Matplotlib

## What I Practiced

This project was created to practice newly learned exploratory data analysis concepts on a scientific dataset, including `describe()`, `value_counts()`, `groupby()`, correlation analysis, and data visualization.

## Data Source

HIGGS Dataset — UCI Machine Learning Repository

The dataset consists of simulated particle collision events generated using Monte Carlo methods.
