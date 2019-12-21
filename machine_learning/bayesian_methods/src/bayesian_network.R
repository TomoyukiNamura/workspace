# ## try http:// if https:// URLs are not supported
# source("https://bioconductor.org/biocLite.R")
# biocLite("Rgraphviz")

#作業ディレクトリ
setwd("/Users/tomoyuki/desktop/ベイジアンネットワーク練習")
getwd()


#パッケージ読み込み
install.packages("bnlearn")
install.packages("forecast")
install.packages("ggplot2")

#library(Rgraphviz)
library(bnlearn)
library(forecast)
library(ggplot2)

help(bnlearn)

#データ確認
protein_dataset <-  read.csv(file = "data/protain_dataset.csv",as.is = TRUE)
head(protein_dataset,5)

### ベイジアンネットワークの学習
## １．構造学習：ヒルクライムアルゴリズム
# whitelist,blacklist
whitelist = blacklist <- NULL

# whitelist <- data.frame(from=c("PIP2"),
#                         to  =c("PKC"))

# blacklist <- data.frame(from=c("PIP3"),
#                         to  =c("plcg"))


hc.model <- hc(protein_dataset,whitelist=whitelist,blacklist=blacklist)
print(hc.model)

# 推定したネットワークを可視化
net.estimated = model2network(modelstring(hc.model))
class(net.estimated)
graphviz.plot(net.estimated, shape = "ellipse")

## ２．パラメータ学習
hc.model.fitted <- bn.fit(hc.model, protein_dataset, method = "mle")




## ベイジアンネットワークによる予測

training.set = protein_dataset[1:405, ] #パラメータ推定用の訓練用データ
test.set = protein_dataset[406:810, ]  #テスト用データ
baysian_structure = hc(training.set)   #訓練用データでベイジアンネットワークの構造を学習
fitted = bn.fit(baysian_structure, training.set,method = "mle")     #パラメータの学習
test.set2 <- test.set
test.set2$PKC <- 0 #本番想定でこの値を知らないということにしておく。
pred = predict(fitted, "PKC", test.set2)  #テストデータが与えられたもとでのPKCの予測
head(cbind(pred, test.set[, "PKC"]))      #予測値と実績値の比較
accuracy(f = pred, x = test.set[, "PKC"]) #正確度の算出

# 予測結果の可視化

df <- data.frame(prediction=pred,actual=test.set[, "PKC"])
p <- ggplot(df,aes(x = prediction,y = actual)) + geom_point() 
p <- p + geom_line(data = data.frame(x = c(0,40), y = c(0,40)),aes(x = x, y = y), colour = "red")
p
