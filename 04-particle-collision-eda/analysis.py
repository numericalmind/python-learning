import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("higgs_train_10k.csv" , header=None)
df.columns = ["label","lepton_pt","lepton_eta","lepton_phi","missing_energy","missing_energy_phi","jet1_pt","jet1_eta","jet1_phi","jet1_btag","jet2_pt","jet2_eta","jet2_phi","jet2_btag","jet3_pt","jet3_eta","jet3_phi","jet3_btag","jet4_pt","jet4_eta","jet4_phi","jet4_btag","m_jj","m_jjj","m_lv","m_jlv","m_bb","m_wbb","m_wwbb"]
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDescriptive statistics:")
print(df.describe())

df["label"].value_counts()
print("\nSignal vs Background:")
print(df["label"].value_counts())

print("\nMean features by event type:")
print(
    df.groupby("label")[
        ["lepton_pt","missing_energy","m_wwbb"]
    ].mean()
)

correlation = df[
    ["lepton_pt","missing_energy","m_wwbb"]
].corr()

print("\nCorrelation matrix:")
print(correlation)

plt.scatter(df["missing_energy"], df["m_wwbb"], alpha=0.3)

plt.xlabel("Missing Energy")
plt.ylabel("m_wwbb")
plt.title("Missing Energy vs m_wwbb")

plt.savefig("correlation_plot.png")
plt.show()

signal = df[df["label"] == 1]
background = df[df["label"] == 0]

print("\nSignal events:", len(signal))
print("Background events:", len(background))

plt.figure(figsize=(10,6))

plt.hist(
    background["m_wwbb"],
    bins=40,
    alpha=0.5,
    label="Background",
    density=True
)

plt.hist(
    signal["m_wwbb"],
    bins=40,
    alpha=0.5,
    label="Signal",
    density=True
)

plt.xlabel("m_wwbb")
plt.ylabel("Density")
plt.title("Signal vs Background: m_wwbb Distribution")
plt.legend()

plt.savefig("m_wwbb_signal_vs_background.png")
plt.show()

feature_means = df.groupby("label").mean()

mean_difference = (
    feature_means.loc[1] - feature_means.loc[0]
).abs().sort_values(ascending=False)

print("\nTop 10 features by absolute mean difference:")
print(mean_difference.head(10))

top_10_features = mean_difference.head(10)
plt.figure(figsize=(10,6))

top_10_features.sort_values().plot(
    kind="barh"
)

plt.xlabel("Absolute Mean Difference")
plt.ylabel("Feature")
plt.title("Top 10 Features Separating Signal and Background")

plt.tight_layout()

plt.savefig(
     "top_10_feature_differences.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.figure(figsize=(10,6))

plt.hist(
    background["m_bb"],
    bins=40,
    alpha=0.5,
    label="Background",
    density=True
)

plt.hist(
    signal["m_bb"],
    bins=40,
    alpha=0.5,
    label="Signal",
    density=True
)

plt.xlabel("m_bb")
plt.ylabel("Density")
plt.title("Signal vs Background: m_bb Distribution")

plt.legend()
plt.tight_layout()

plt.savefig(
    "m_bb_signal_vs_background.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

