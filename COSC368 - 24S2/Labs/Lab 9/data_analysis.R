# !/usr/bin/env Rscript

  

library(ez)

data <- read.table("oneway-within.txt", header=TRUE)
novice_data <- data[which(data$block == 0),]
expert_data <- data[which(data$block == 9),]


print("NOVICE ANALYSIS")

ezANOVA(data=novice_data, dv=time, within=condition, wid=subject)

ezStats(data=novice_data, dv=time, within=condition, wid=subject)

# Alternatively, if ezANOVA fails to work (I hear there is a problem in the labs):

# wfit <- aov(time ~ condition +Error(subject/condition), data=novice_data)

# summary(wfit)

# print(model.tables(wfit,"means"),digits=3)  

print("EXPERT ANALYSIS")

ezANOVA(data=expert_data, dv=time, within=condition, wid=subject)

ezStats(data=expert_data, dv=time, within=condition, wid=subject)

# Alternatively, if ezANOVA fails to work (I hear there is a problem in the labs):

# wfit <- aov(time ~ condition +Error(subject/condition), data=expert_data)

# summary(wfit)

# print(model.tables(wfit,"means"),digits=3)