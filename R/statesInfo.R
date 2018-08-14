getwd()

statesInfo <- read.csv('stateData.csv')

subset(statesInfo, state.region == 1)
statesInfo[statesInfo$state.region == 1, )

stateSubsetBracket <- statesInfo[statesInfo$state.region==1, ]
head(stateSubsetBracket,2)
dim(stateSubsetBracket)

stateIllit <- subset(statesInfo, illiteracy >= 1.5)
stateIllit

stateGrads <- subset(statesInfo, highSchoolGrad > 55)
stateGrads

stateMaxPop <- subset(statesInfo, max(population))
?max.col


install.packages('knitr', dependencies = T)
library(knitr)