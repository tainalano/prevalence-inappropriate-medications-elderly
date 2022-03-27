import pandas as pd
import matplotlib.pyplot as plt

drug_file = pd.read_csv('drugs.csv', header=None).values.tolist()
drug_list = drug_file[0]

for i in range(len(drug_list)):
    drug_list[i] = drug_list[i].lower()

columns = ["drug_name_A",	"drug_name_B",	"drug_name_C",	"drug_name_D",	"drug_name_E",	"drug_name_F",	"drug_name_G",	"drug_name_H",	"drug_name_I",	"drug_name_J"]
patient_list = pd.read_csv('data.csv', skipinitialspace=True, usecols=columns)

drug_counter = {}

for drug_column in patient_list.values:
  for drug_name in drug_column:
    if str(drug_name).lower() in drug_list:
        if str(drug_name).lower() not in drug_counter:
            drug_counter[str(drug_name).lower()] = 0
        drug_counter[str(drug_name).lower()] += 1

print(drug_counter)

l = list(drug_counter.items())
l.sort(reverse=True)
dict = dict(l)

plt.barh(*zip(*dict.items()))
plt.show()