library(tidyverse)

df <- read.csv("data/LAPTOP-126V4913_2021-11-18/measurements_14_59.csv", sep=",")
# plot(df$Size, df$Time, col=c("red","blue","green")[df$Type])
new_df <- df %>% group_by(Size, Type) %>% summarise(mean=mean(Time), sd=sd(Time), n=n())
ggplot(new_df, aes(x=Size, y=mean, color=Type))+ geom_point() + geom_ribbon(aes(ymin=mean-sd/sqrt(n), ymax=mean+sd/sqrt(n)), alpha=0.1) + geom_line()

df <- read.csv("data/LAPTOP-126V4913_2021-11-18/measurements_16_02.csv", sep=",")
# plot(df$Size, df$Time, col=c("red","blue","green")[df$Type])
new_df <- df %>% group_by(Size, Type) %>% summarise(mean=mean(Time), sd=sd(Time), n=n())
ggplot(new_df, aes(x=Size, y=mean, color=Type))+ geom_point() + geom_ribbon(aes(ymin=mean-sd/sqrt(n), ymax=mean+sd/sqrt(n)), alpha=0.1) + geom_line()

ggplot(new_df, aes(x=Size, y=mean, color=Type))+ geom_point() + geom_smooth(method='lm')

df <- read.csv("data/LAPTOP-126V4913_2021-11-25/measurements_10_20.csv", sep=",")
new_df <- df %>% group_by(Size, Type) %>% summarise(mean=mean(Time), sd=sd(Time), n=n())
ggplot(new_df, aes(x=Size, y=mean, color=Type))+ geom_point() + geom_ribbon(aes(ymin=mean-sd/sqrt(n), ymax=mean+sd/sqrt(n)), alpha=0.1) + geom_line()
