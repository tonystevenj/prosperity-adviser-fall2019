from release.My_TF_IDF import FullProcess
from release import toMidData


# toMidData.processToMiddata('Data/review_Phoenix.csv')
# to_csv(f'midDataes/{toName}{i}.csv')

for i in range(41):
    FullProcess(f"midDataes/midData{i}.csv",i)
# FullProcess(f"midDataes/midData0.csv",0)