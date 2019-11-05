from release.My_TF_IDF import FullProcess
from release import toMidData


midpath=toMidData.processToMiddata('Data/review_Phoenix.csv',"New.csv")
FullProcess(midpath)