// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © ceyhun

//@version=4

study("Overbought Oversold Indicator")

n = input(5, title="Length")
Barcolor=input(true,title="Barcolor")

ys1 = (high + low + close * 2) / 4
rk3 = ema(ys1, n)
rk4 = stdev(ys1, n)
rk5 = (ys1 - rk3) * 100 / rk4
rk6 = ema(rk5, n)
up = ema(rk6, n)
down = ema(up, n)
Oo = iff(up < down, up, down)
Hh = Oo
Ll = iff(up < down, down, up)
Cc = Ll

b_color = iff(Oo[1] < Oo and Cc < Cc[1], #FFFF00, iff(up > down, #008000, #FF0000))
barcolor(Barcolor ? b_color : na)

hline(0)
plot(Oo, style=plot.style_histogram, color=b_color)
plot(Ll, style=plot.style_histogram, color=b_color)

plot(up, color=b_color,title="Up")
plot(down, color=b_color,title="Down")

Buy = crossover(up, down)
Sell = crossunder(up, down)

plotshape(Buy, title="Buy", color=#008000, style=shape.triangleup, location=location.bottom, text="Buy",size=size.tiny)
plotshape(Sell, title="Sell", color=#FF0000, style=shape.triangledown, location=location.top, text="Sell",size=size.tiny)

alertcondition(Buy, title="Buy Signal", message="Buy")
alertcondition(Sell, title="Sell Signal", message="Sell")
