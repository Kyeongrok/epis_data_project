# Latent Class ------------------------------------------------------------

library(dplyr)
library(tidyr)
library(randomLCA)


# Conducting each models setting number of classes
lca1random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=1,
                        probit=TRUE,
                        constload=FALSE)
lca2random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=2,
                        probit=TRUE,
                        constload=FALSE)
lca3random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=3,
                        probit=TRUE,
                        constload=FALSE)
lca4random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=4,
                        probit=TRUE,
                        constload=FALSE)
lca5random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=5,
                        probit=TRUE,
                        constload=FALSE)
lca6random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=6,
                        probit=TRUE,
                        constload=FALSE)
lca7random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=7,
                        probit=TRUE,
                        constload=FALSE)
lca8random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=8,
                        probit=TRUE,
                        constload=FALSE)
lca9random <- randomLCA(lca.mat,
                        freq=lca.mat$salu,
                        nclass=9,
                        probit=TRUE,
                        constload=FALSE)
lca10random <- randomLCA(lca.mat,
                         freq=lca.mat$salu,
                         nclass=10,
                         probit=TRUE,
                         constload=FALSE)


## Proper number of classes based on BIC
## Lower BIC values, better model

# Method 1
bic <- data.frame(classes=1:10,
                  bic=c(BIC(lca1random),
                        BIC(lca2random),
                        BIC(lca3random),
                        BIC(lca4random),
                        BIC(lca5random),
                        BIC(lca6random),
                        BIC(lca7random),
                        BIC(lca8random),
                        BIC(lca9random),
                        BIC(lca10random)))
print(bic, row.names=FALSE)

# Method 2
# summary(lca7random)
# 
# plot(lca7random,
#      graphtype="marginal",
#      type="b",
#      pch=1:7,
#      xlab="Dentist", ylab="Marginal Outcome Probability",
#      key=list(corner=c(0.05, .95),
#               border=TRUE,
#               cex=1.2,
#               text=list(c("Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7")),
#               col=trellis.par.get()$superpose.symbol$col[1:7],
#               points=list(pch=1:7)))


## Model outcomes using posterior probability
# lca7random <- randomLCA(lca.mat,
#                         freq=lca.mat$salu,
#                         nclass=7,
#                         probit=TRUE,
#                         quadpoints=70,
#                         constload=FALSE)
# probs <- outcomeProbs(lca7random, boot=TRUE)

# In the case of class 7
# summary(lca7random)
# a <- lca2random[13]
# a <- a[["classprob"]]
# 
# cl <- data.frame(C1 = a[1:2379, 1],
#                  C2 = a[1:2379, 2],
#                  C3 = a[1:2379, 3],
#                  C4 = a[1:2379, 4],
#                  C5 = a[1:2379, 5],
#                  C6 = a[1:2379, 6],
#                  C7 = a[1:2379, 7])
# index <- c()
# 
# for (i in 1:nrow(cl)) {
#   index[i] <- which.max(apply(cl[i, ], MARGIN = 2, max))
# }
# cl$index <- index
# table(cl$index)


# Latent class_2 ----------------------------------------------------------

library(poLCA)


options(scipen=100)

# Class 7
result <- poLCA(f, lca.mat_2, nclass=7, verbose=FALSE)
class <- result[7]
class <- class[["posterior"]]

cl <- data.frame(C1=class[1:1357, 1],
                 C2=class[1:1357, 2],
                 C3=class[1:1357, 3],
                 C4=class[1:1357, 4],
                 C5=class[1:1357, 5],
                 C6=class[1:1357, 6],
                 C7=class[1:1357, 7])
index <- c()

for (i in 1:nrow(cl)) {
  index[i] <- which.max(apply(cl[i, ], MARGIN=2, max))
}
cl$index <- index
table(cl$index)

cl$farm_id <- rownames(lca.mat_2)
cl <- cl[, c(length(cl), length(cl)-1)]
turn_farm_e <- merge(turn_farm_e, cl, by=c("farm_id"), all.x=TRUE)
colnames(turn_farm.e)[length(turn_farm.e)] <- 'index7'

















