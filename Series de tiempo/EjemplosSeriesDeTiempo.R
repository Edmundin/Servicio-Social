
library(tseries)
data(bev)
plot(bev, xlab = "Year", ylab = "Wheat price index", xaxt = "n")
x.pos <- c(1500, 1560, 1620, 1680, 1740, 1800, 1869)
axis(1, x.pos, x.pos)