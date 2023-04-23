

##freq detetction

df1 = pd.read_csv('delhi_hotels_details_final.csv')


amenities = df1.iloc[:, -161:]

amen_sums = amenities.sum()


amen_names = amenities.columns.tolist()


amen = dict(zip(amen_names, amen_sums))
print(amen)
# sorted_amen=sorted(amen)
# sorted_amen = sorted(amen.items(), key=lambda x:x[1])

keys = list(amen.keys())
values = list(amen.values())
sorted_value_index = np.argsort(values)
sorted_amen = {keys[i]: values[i] for i in sorted_value_index}
 
print(sorted_amen)
print(len(sorted_amen))
# print(sorted_amen)