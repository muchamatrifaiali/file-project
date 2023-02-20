// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © LonesomeTheBlue

//@version=4
study("Support Resistance - Dynamic", overlay = true, max_bars_back = 600)
rb = input(10, title = "Period for Pivot Points", minval = 10)
prd = input(284, title = "Loopback Period", minval = 100, maxval = 500)
nump = input(2, title ="S/R strength", minval = 1)
ChannelW = input(10, title = "Channel Width %", minval = 5)
label_location = input(10, title = "Label Location +-", tooltip = "0 means last bar. for example if you set it -5 then label is shown on last 5. bar. + means future bars")
linestyle = input('Dashed', title = "Line Style", options = ['Solid', 'Dotted', 'Dashed'])
LineColor = input(color.blue, title = "Line Color", type = input.color)
drawhl = input(true, title = "Draw Highest/Lowest Pivots in Period")
showpp = input(false, title = "Show Point Points")
 
ph = pivothigh(rb, rb)
pl = pivotlow(rb, rb)
plotshape(ph and showpp, text="PH",  style=shape.labeldown, color=color.new(color.white, 100), textcolor = color.red, location=location.abovebar, offset = -rb)
plotshape(pl and showpp, text="PL",  style=shape.labelup, color=color.new(color.white, 100), textcolor = color.lime, location=location.belowbar, offset = -rb)

// S/R levels
sr_levels = array.new_float(21, na)

// if number of bars is less then the loop then pine highest() fundtion brings 'na'. we need highest/lowest to claculate channel size
// so you cannot see S/R until the number of bars is equal/greater then the "Loopback Period" 
prdhighest =  highest(prd)
prdlowest = lowest(prd)
cwidth = (prdhighest - prdlowest) * ChannelW / 100

//availability of the PPs
aas = array.new_bool(41, true)

// last privot points have more priority to be support/resistance, so we start from them
// if we met new Pivot Point then we calculate all supports/resistances again
u1 = 0.0, u1 := nz(u1[1])
d1 = 0.0, d1 := nz(d1[1])
highestph = 0.0
lowestpl = 0.0
highestph := highestph[1]
lowestpl := lowestpl[1]
if ph or pl 
    //old S/Rs not valid anymore
    for x = 0 to array.size(sr_levels) - 1
        array.set(sr_levels, x, na)

    highestph := prdlowest
    lowestpl := prdhighest
    countpp = 0 // keep position of the PP
    for x = 0 to prd
        if na(close[x])
            break
        if not na(ph[x]) or not na(pl[x]) // is it PP?
            highestph := max(highestph, nz(ph[x], prdlowest), nz(pl[x], prdlowest))
            lowestpl := min(lowestpl, nz(ph[x], prdhighest), nz(pl[x], prdhighest))
            countpp := countpp + 1
            if countpp > 40
                break
            if array.get(aas, countpp) // if PP is not used in a channel
                upl = (ph[x] ? high[x+rb] : low[x+rb]) + cwidth
                dnl = (ph[x] ? high[x+rb] : low[x+rb]) - cwidth 
                u1 := countpp == 1 ? upl : u1
                d1 := countpp == 1 ? dnl : d1
                // to keep the PPs which will be in current channel
                tmp = array.new_bool(41, true)
                
                cnt = 0  // keep which pivot point we are on
                tpoint = 0 // number of PPs in the channel 
                for xx = 0 to prd
                    if na(close[xx])
                        break
                    if not na(ph[xx]) or not na(pl[xx])
                        chg = false
                        cnt := cnt + 1
                        if cnt > 40
                            break
                        if array.get(aas, cnt) // if PP not used in other channels
                            if not na(ph[xx])
                                if high[xx+rb] <= upl and high[xx+rb] >= dnl // PP is in the channel?
                                    tpoint := tpoint + 1
                                    chg := true
                                
                            if not na(pl[xx])
                                if low[xx+rb] <= upl and low[xx+rb] >= dnl   // PP is in the channel?
                                    tpoint := tpoint + 1
                                    chg := true
                        // set if PP is used in the channel
                        if chg and cnt < 41
                            array.set(tmp, cnt, false)
                            
                if tpoint >= nump // met enough PP in the channel? mark the PP as used for a channel and set the SR level
                    for g = 0 to 40
                        if not array.get(tmp, g)
                            array.set(aas, g, false)
                            
                    if ph[x] and countpp < 21
                        array.set(sr_levels, countpp, high[x+rb])
                    if pl[x] and countpp < 21
                        array.set(sr_levels, countpp, low[x+rb])

setline( level) =>
    LineStyle = linestyle == 'Solid' ? line.style_solid : 
       linestyle == 'Dotted' ? line.style_dotted :
       line.style_dashed
    _ret = line.new(bar_index - 1 , level, bar_index , level, color = LineColor, width = 2, style = LineStyle, extend = extend.both)  

if ph or pl
    var line highest_ = na
    var line lowest_ = na
    line.delete(highest_)
    line.delete(lowest_)
    if drawhl
        highest_ := line.new(bar_index - 1 , highestph, bar_index , highestph, color = color.blue, style = line.style_dashed, width = 1, extend = extend.both) 
        lowest_ := line.new(bar_index - 1 , lowestpl, bar_index , lowestpl, color = color.blue, style = line.style_dashed, width = 1, extend = extend.both) 
    
    var sr_lines = array.new_line(21, na)
    for x = 0 to array.size(sr_lines) - 1
        line.delete(array.get(sr_lines, x))
        if array.get(sr_levels, x)
            array.set(sr_lines, x, setline(array.get(sr_levels, x)))

// set new labels if changed
var sr_levs = array.new_float(21, na)
if ph or pl
    for x = 0 to array.size(sr_levs) - 1
        array.set(sr_levs, x, array.get(sr_levels, x))

// define and delete old labels
label hlabel = na
label llabel = na
label.delete(hlabel[1])
label.delete(llabel[1])
var sr_labels = array.new_label(21, na)
bool resistance_broken = false
bool support_broken = false
float r_s_level = na
// set labels
for x = 0 to array.size(sr_labels) - 1
    label.delete(array.get(sr_labels, x))
    if array.get(sr_levs, x)
        if close[1] <= array.get(sr_levs, x) and close > array.get(sr_levs, x)
            resistance_broken := true
            r_s_level := array.get(sr_levs, x)
        if close[1] >= array.get(sr_levs, x) and close < array.get(sr_levs, x)
            support_broken := true
            r_s_level := array.get(sr_levs, x)
        lab_loc = (close >= array.get(sr_levs, x) ? label.style_labelup : label.style_labeldown)
        array.set(sr_labels, x,
                  label.new(x = bar_index + label_location, y = array.get(sr_levs, x), text = tostring(round_to_mintick(array.get(sr_levs, x))), color = color.lime, textcolor = color.black, style = lab_loc))

hlabel := drawhl ? label.new(x = bar_index + label_location + round(sign(label_location)) * 20, y = highestph, text = "Highest PH " + tostring(highestph), color = color.silver, textcolor=color.black, style=label.style_labeldown) : na
llabel := drawhl ? label.new(x = bar_index + label_location + round(sign(label_location)) * 20, y = lowestpl, text = "Lowest PL " + tostring(lowestpl), color = color.silver, textcolor=color.black, style=label.style_labelup) : na

plot(r_s_level, title = "RS_level", display = display.none)
alertcondition(resistance_broken, title='Resistance Broken', message='Resistance Broken, Close Price: {{close}}, Resistance level = {{plot("RS_level")}}')
alertcondition(support_broken, title='Support Broken', message='Support Broken, Close Price: {{close}}, Support level = {{plot("RS_level")}}')
