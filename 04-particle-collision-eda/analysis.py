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