//@version=4
study("Multiple Screeners with Alerts", shorttitle = 'MultScreener[QN]', overlay = false)

////////////
// INPUTS //

// Styling
bars_apart = input(20, title = "Labels Bars Apart", group = "Style")

// RSI Params
rsi_length      = input(14, title = "Length",           group = 'RSI', inline = 'RSI')
rsi_overbought  = input(70, title = "Overbought Level", group = 'RSI', inline = 'RSI2')
rsi_oversold    = input(30, title = "Oversold Level",   group = 'RSI', inline = 'RSI2')

// TSI Params
tsi_long        = input(25,  title = "Long Length",      group = "TSI", inline = "TSI0")
tsi_short       = input(13,  title = "Short Length",     group = "TSI", inline = "TSI1")
tsi_signal      = input(13,  title = "Signal Length",    group = "TSI", inline = "TSI1")
tsi_overbought  = input(30,  title = "Overbought Level", group = 'TSI', inline = 'TSI2')
tsi_oversold    = input(-30, title = "Oversold Level",   group = 'TSI', inline = 'TSI2')

// ADX Params
adx_smooth      = input(14, title = "ADX Smoothing",     group = 'ADX', inline = 'ADX')
adx_dilen       = input(14, title = "DI Length",         group = 'ADX', inline = 'ADX')
adx_level       = input(40, title = "ADX Level",         group = 'ADX', inline = 'ADX2')

// MACD Params
macd_fast_len   = input(12, title = "Fast Length",      group = 'MACD', inline = 'MACD')
macd_slow_len   = input(26, title = "Slow Length",      group = 'MACD', inline = 'MACD')
macd_signal_len = input(9,  title = "Signal Smoothing", group = 'MACD', inline = 'MACD2')

// Awesome Oscillator
ao_fast_len   = input(5,  title="Fast Length",     group = 'Awesome Oscillator', inline = 'AO')
ao_slow_len   = input(34, title="Fast Length",     group = 'Awesome Oscillator', inline = 'AO')

// Symbols 
// There is a limit of 40 security calls so only 40 symbols at the same time is possible
s01 = input('XRPUSDT',  type=input.symbol, group = "Symbols")
s02 = input('BTCUSDT',  type=input.symbol, group = "Symbols")
s03 = input('DOGEUSDT', type=input.symbol, group = "Symbols")
s04 = input('BNBUSDT',  type=input.symbol, group = "Symbols")
s05 = input('ETHUSDT',  type=input.symbol, group = "Symbols")
s06 = input('ADAUSDT',  type=input.symbol, group = "Symbols")
s07 = input('XRPBTC',   type=input.symbol, group = "Symbols")
s08 = input('DOGEBTC',  type=input.symbol, group = "Symbols")
s09 = input('TRXUSDT',  type=input.symbol, group = "Symbols")
s10 = input('BTCBUSD',  type=input.symbol, group = "Symbols")
s11 = input('ETHBUSD',  type=input.symbol, group = "Symbols")
s12 = input('BNBBUSD',  type=input.symbol, group = "Symbols")
s13 = input('VETUSDT',  type=input.symbol, group = "Symbols")
s14 = input('ETHBTC',   type=input.symbol, group = "Symbols")
s15 = input('BNBBTC',   type=input.symbol, group = "Symbols")
s16 = input('EOSUSDT',  type=input.symbol, group = "Symbols")
s17 = input('XLMUSDT',  type=input.symbol, group = "Symbols")
s18 = input('LTCUSDT',  type=input.symbol, group = "Symbols")
s19 = input('XRPBUSD',  type=input.symbol, group = "Symbols")
s20 = input('WINUSDT',  type=input.symbol, group = "Symbols")
s21 = input('DOTUSDT',  type=input.symbol, group = "Symbols")
s22 = input('BTTUSDT',  type=input.symbol, group = "Symbols")
s23 = input('BCHUSDT',  type=input.symbol, group = "Symbols")
s24 = input('ADABTC',   type=input.symbol, group = "Symbols")
s25 = input('IOSTUSDT', type=input.symbol, group = "Symbols")
s26 = input('CHZUSDT',  type=input.symbol, group = "Symbols")
s27 = input('LINKUSDT', type=input.symbol, group = "Symbols")
s28 = input('TRXBTC',   type=input.symbol, group = "Symbols")
s29 = input('DOGEBUSD', type=input.symbol, group = "Symbols")
s30 = input('BTCEUR',   type=input.symbol, group = "Symbols")
s31 = input('FILUSDT',  type=input.symbol, group = "Symbols")
s32 = input('HOTUSDT',  type=input.symbol, group = "Symbols")
s33 = input('SXPUSDT',  type=input.symbol, group = "Symbols")
s34 = input('ADABUSD',  type=input.symbol, group = "Symbols")
s35 = input('RVNUSDT',  type=input.symbol, group = "Symbols")
s36 = input('ATOMUSDT', type=input.symbol, group = "Symbols")
s37 = input('XRPBNB',   type=input.symbol, group = "Symbols")
s38 = input('LTCBTC',   type=input.symbol, group = "Symbols")
s39 = input('IOSTBTC',  type=input.symbol, group = "Symbols")
s40 = input('GRTUSDT',  type=input.symbol, group = "Symbols")

///////////////
// FUNCTIONS //

// Rounding Function
roundn(x, n) => 
    mult = 1 
    if n != 0
        for i = 1 to abs(n)
            mult := mult * 10
    
    n >= 0 ? round(x * mult) / mult : round(x / mult) * mult 

// Function for TSI
double_smooth(src, long, short) =>
	fist_smooth = ema(src, long)
	ema(fist_smooth, short)

// Function for ADX
dirmov(len) =>
	up   = change(high)
	down = -change(low)
	plusDM  = na(up)   ? na : (up > down and up > 0   ? up   : 0)
	minusDM = na(down) ? na : (down > up and down > 0 ? down : 0)
	truerange = rma(tr, len)
	plus  = fixnan(100 * rma(plusDM,  len) / truerange)
	minus = fixnan(100 * rma(minusDM, len) / truerange)
	[plus, minus]

// ADX
adx(dilen, adxlen) =>
	[plus, minus] = dirmov(dilen)
	sum = plus + minus
	adx = 100 * rma(abs(plus - minus) / (sum == 0 ? 1 : sum), adxlen)

// Main Screener functions 
// Inside you can calcuate multiple indicator and outout all of them
// Currently it works with 5 indicator
// For every inicator I output 2 values
// - value to display in hte screener
// - TRUE/FASLE condition I use to filter instruments in a screener. 

screenerFunc() => 
    // RSI
    rsi     = rsi(close, rsi_length)
    rsi_cond    = rsi > rsi_overbought or rsi < rsi_oversold
    
    // TSI
    pc = change(close)
    double_smoothed_pc = double_smooth(pc, tsi_long, tsi_short)
    double_smoothed_abs_pc = double_smooth(abs(pc), tsi_long, tsi_short)
    tsi = 100 * (double_smoothed_pc / double_smoothed_abs_pc)
    tsi_sig = ema(tsi, tsi_signal)
    tsi_cond   = tsi > tsi_overbought or tsi < tsi_oversold
    
    // ADX
    adx      = adx(adx_dilen, adx_smooth)
    adx_cond = adx > adx_level
    
    // MACD 
    [macd, macd_signal, macd_hist] = macd(close, 12, 26, 9)
    
    macd_cond  = cross(macd, macd_signal)
    
    macd_value = crossover( macd, macd_signal) ?  1 : 
                 crossunder(macd, macd_signal) ? -1 :
                 0
    
    // Awesome Oscillator
    ao = sma(hl2, ao_fast_len) - sma(hl2, ao_slow_len)
    
    ao_cond = cross(ao, 0)
    
    ao_value = crossover( ao, 0) ?  1 : 
               crossunder(ao, 0) ? -1 :
               0
    
    [rsi, rsi_cond, tsi, tsi_cond, adx, adx_cond, macd_value, macd_cond, ao_value, ao_cond]

////////////////////////////////////////////////////
// Running Functions for all sybmols / indicators //

[v01_1, c01_1, v01_2, c01_2, v01_3, c01_3, v01_4, c01_4, v01_5, c01_5] = security(s01, timeframe.period, screenerFunc())
[v02_1, c02_1, v02_2, c02_2, v02_3, c02_3, v02_4, c02_4, v02_5, c02_5] = security(s02, timeframe.period, screenerFunc())
[v03_1, c03_1, v03_2, c03_2, v03_3, c03_3, v03_4, c03_4, v03_5, c03_5] = security(s03, timeframe.period, screenerFunc())
[v04_1, c04_1, v04_2, c04_2, v04_3, c04_3, v04_4, c04_4, v04_5, c04_5] = security(s04, timeframe.period, screenerFunc())
[v05_1, c05_1, v05_2, c05_2, v05_3, c05_3, v05_4, c05_4, v05_5, c05_5] = security(s05, timeframe.period, screenerFunc())
[v06_1, c06_1, v06_2, c06_2, v06_3, c06_3, v06_4, c06_4, v06_5, c06_5] = security(s06, timeframe.period, screenerFunc())
[v07_1, c07_1, v07_2, c07_2, v07_3, c07_3, v07_4, c07_4, v07_5, c07_5] = security(s07, timeframe.period, screenerFunc())
[v08_1, c08_1, v08_2, c08_2, v08_3, c08_3, v08_4, c08_4, v08_5, c08_5] = security(s08, timeframe.period, screenerFunc())
[v09_1, c09_1, v09_2, c09_2, v09_3, c09_3, v09_4, c09_4, v09_5, c09_5] = security(s09, timeframe.period, screenerFunc())
[v10_1, c10_1, v10_2, c10_2, v10_3, c10_3, v10_4, c10_4, v10_5, c10_5] = security(s10, timeframe.period, screenerFunc())
[v11_1, c11_1, v11_2, c11_2, v11_3, c11_3, v11_4, c11_4, v11_5, c11_5] = security(s11, timeframe.period, screenerFunc())
[v12_1, c12_1, v12_2, c12_2, v12_3, c12_3, v12_4, c12_4, v12_5, c12_5] = security(s12, timeframe.period, screenerFunc())
[v13_1, c13_1, v13_2, c13_2, v13_3, c13_3, v13_4, c13_4, v13_5, c13_5] = security(s13, timeframe.period, screenerFunc())
[v14_1, c14_1, v14_2, c14_2, v14_3, c14_3, v14_4, c14_4, v14_5, c14_5] = security(s14, timeframe.period, screenerFunc())
[v15_1, c15_1, v15_2, c15_2, v15_3, c15_3, v15_4, c15_4, v15_5, c15_5] = security(s15, timeframe.period, screenerFunc())
[v16_1, c16_1, v16_2, c16_2, v16_3, c16_3, v16_4, c16_4, v16_5, c16_5] = security(s16, timeframe.period, screenerFunc())
[v17_1, c17_1, v17_2, c17_2, v17_3, c17_3, v17_4, c17_4, v17_5, c17_5] = security(s17, timeframe.period, screenerFunc())
[v18_1, c18_1, v18_2, c18_2, v18_3, c18_3, v18_4, c18_4, v18_5, c18_5] = security(s18, timeframe.period, screenerFunc())
[v19_1, c19_1, v19_2, c19_2, v19_3, c19_3, v19_4, c19_4, v19_5, c19_5] = security(s19, timeframe.period, screenerFunc())
[v20_1, c20_1, v20_2, c20_2, v20_3, c20_3, v20_4, c20_4, v20_5, c20_5] = security(s20, timeframe.period, screenerFunc())
[v21_1, c21_1, v21_2, c21_2, v21_3, c21_3, v21_4, c21_4, v21_5, c21_5] = security(s21, timeframe.period, screenerFunc())
[v22_1, c22_1, v22_2, c22_2, v22_3, c22_3, v22_4, c22_4, v22_5, c22_5] = security(s22, timeframe.period, screenerFunc())
[v23_1, c23_1, v23_2, c23_2, v23_3, c23_3, v23_4, c23_4, v23_5, c23_5] = security(s23, timeframe.period, screenerFunc())
[v24_1, c24_1, v24_2, c24_2, v24_3, c24_3, v24_4, c24_4, v24_5, c24_5] = security(s24, timeframe.period, screenerFunc())
[v25_1, c25_1, v25_2, c25_2, v25_3, c25_3, v25_4, c25_4, v25_5, c25_5] = security(s25, timeframe.period, screenerFunc())
[v26_1, c26_1, v26_2, c26_2, v26_3, c26_3, v26_4, c26_4, v26_5, c26_5] = security(s26, timeframe.period, screenerFunc())
[v27_1, c27_1, v27_2, c27_2, v27_3, c27_3, v27_4, c27_4, v27_5, c27_5] = security(s27, timeframe.period, screenerFunc())
[v28_1, c28_1, v28_2, c28_2, v28_3, c28_3, v28_4, c28_4, v28_5, c28_5] = security(s28, timeframe.period, screenerFunc())
[v29_1, c29_1, v29_2, c29_2, v29_3, c29_3, v29_4, c29_4, v29_5, c29_5] = security(s29, timeframe.period, screenerFunc())
[v30_1, c30_1, v30_2, c30_2, v30_3, c30_3, v30_4, c30_4, v30_5, c30_5] = security(s30, timeframe.period, screenerFunc())
[v31_1, c31_1, v31_2, c31_2, v31_3, c31_3, v31_4, c31_4, v31_5, c31_5] = security(s31, timeframe.period, screenerFunc())
[v32_1, c32_1, v32_2, c32_2, v32_3, c32_3, v32_4, c32_4, v32_5, c32_5] = security(s32, timeframe.period, screenerFunc())
[v33_1, c33_1, v33_2, c33_2, v33_3, c33_3, v33_4, c33_4, v33_5, c33_5] = security(s33, timeframe.period, screenerFunc())
[v34_1, c34_1, v34_2, c34_2, v34_3, c34_3, v34_4, c34_4, v34_5, c34_5] = security(s34, timeframe.period, screenerFunc())
[v35_1, c35_1, v35_2, c35_2, v35_3, c35_3, v35_4, c35_4, v35_5, c35_5] = security(s35, timeframe.period, screenerFunc())
[v36_1, c36_1, v36_2, c36_2, v36_3, c36_3, v36_4, c36_4, v36_5, c36_5] = security(s36, timeframe.period, screenerFunc())
[v37_1, c37_1, v37_2, c37_2, v37_3, c37_3, v37_4, c37_4, v37_5, c37_5] = security(s37, timeframe.period, screenerFunc())
[v38_1, c38_1, v38_2, c38_2, v38_3, c38_3, v38_4, c38_4, v38_5, c38_5] = security(s38, timeframe.period, screenerFunc())
[v39_1, c39_1, v39_2, c39_2, v39_3, c39_3, v39_4, c39_4, v39_5, c39_5] = security(s39, timeframe.period, screenerFunc())
[v40_1, c40_1, v40_2, c40_2, v40_3, c40_3, v40_4, c40_4, v40_5, c40_5] = security(s40, timeframe.period, screenerFunc())


////////////////////////////
// Compose screener label //

scr_label1 = ''

scr_label1 := c01_1  ? scr_label1 + s01 + ' ' + tostring(roundn(v01_1, 2)) +  '\n'  : scr_label1
scr_label1 := c02_1  ? scr_label1 + s02 + ' ' + tostring(roundn(v02_1, 2)) +  '\n'  : scr_label1
scr_label1 := c03_1  ? scr_label1 + s03 + ' ' + tostring(roundn(v03_1, 2)) +  '\n'  : scr_label1
scr_label1 := c04_1  ? scr_label1 + s04 + ' ' + tostring(roundn(v04_1, 2)) +  '\n'  : scr_label1
scr_label1 := c05_1  ? scr_label1 + s05 + ' ' + tostring(roundn(v05_1, 2)) +  '\n'  : scr_label1
scr_label1 := c06_1  ? scr_label1 + s06 + ' ' + tostring(roundn(v06_1, 2)) +  '\n'  : scr_label1
scr_label1 := c07_1  ? scr_label1 + s07 + ' ' + tostring(roundn(v07_1, 2)) +  '\n'  : scr_label1
scr_label1 := c08_1  ? scr_label1 + s08 + ' ' + tostring(roundn(v08_1, 2)) +  '\n'  : scr_label1
scr_label1 := c09_1  ? scr_label1 + s09 + ' ' + tostring(roundn(v09_1, 2)) +  '\n'  : scr_label1
scr_label1 := c10_1  ? scr_label1 + s10 + ' ' + tostring(roundn(v10_1, 2)) +  '\n'  : scr_label1
scr_label1 := c11_1  ? scr_label1 + s11 + ' ' + tostring(roundn(v11_1, 2)) +  '\n'  : scr_label1
scr_label1 := c12_1  ? scr_label1 + s12 + ' ' + tostring(roundn(v12_1, 2)) +  '\n'  : scr_label1
scr_label1 := c13_1  ? scr_label1 + s13 + ' ' + tostring(roundn(v13_1, 2)) +  '\n'  : scr_label1
scr_label1 := c14_1  ? scr_label1 + s14 + ' ' + tostring(roundn(v14_1, 2)) +  '\n'  : scr_label1
scr_label1 := c15_1  ? scr_label1 + s15 + ' ' + tostring(roundn(v15_1, 2)) +  '\n'  : scr_label1
scr_label1 := c16_1  ? scr_label1 + s16 + ' ' + tostring(roundn(v16_1, 2)) +  '\n'  : scr_label1
scr_label1 := c17_1  ? scr_label1 + s17 + ' ' + tostring(roundn(v17_1, 2)) +  '\n'  : scr_label1
scr_label1 := c18_1  ? scr_label1 + s18 + ' ' + tostring(roundn(v18_1, 2)) +  '\n'  : scr_label1
scr_label1 := c19_1  ? scr_label1 + s19 + ' ' + tostring(roundn(v19_1, 2)) +  '\n'  : scr_label1
scr_label1 := c20_1  ? scr_label1 + s20 + ' ' + tostring(roundn(v20_1, 2)) +  '\n'  : scr_label1
scr_label1 := c21_1  ? scr_label1 + s21 + ' ' + tostring(roundn(v21_1, 2)) +  '\n'  : scr_label1
scr_label1 := c22_1  ? scr_label1 + s22 + ' ' + tostring(roundn(v22_1, 2)) +  '\n'  : scr_label1
scr_label1 := c23_1  ? scr_label1 + s23 + ' ' + tostring(roundn(v23_1, 2)) +  '\n'  : scr_label1
scr_label1 := c24_1  ? scr_label1 + s24 + ' ' + tostring(roundn(v24_1, 2)) +  '\n'  : scr_label1
scr_label1 := c25_1  ? scr_label1 + s25 + ' ' + tostring(roundn(v25_1, 2)) +  '\n'  : scr_label1
scr_label1 := c26_1  ? scr_label1 + s26 + ' ' + tostring(roundn(v26_1, 2)) +  '\n'  : scr_label1
scr_label1 := c27_1  ? scr_label1 + s27 + ' ' + tostring(roundn(v27_1, 2)) +  '\n'  : scr_label1
scr_label1 := c28_1  ? scr_label1 + s28 + ' ' + tostring(roundn(v28_1, 2)) +  '\n'  : scr_label1
scr_label1 := c29_1  ? scr_label1 + s29 + ' ' + tostring(roundn(v29_1, 2)) +  '\n'  : scr_label1
scr_label1 := c30_1  ? scr_label1 + s30 + ' ' + tostring(roundn(v30_1, 2)) +  '\n'  : scr_label1
scr_label1 := c31_1  ? scr_label1 + s31 + ' ' + tostring(roundn(v31_1, 2)) +  '\n'  : scr_label1
scr_label1 := c32_1  ? scr_label1 + s32 + ' ' + tostring(roundn(v32_1, 2)) +  '\n'  : scr_label1
scr_label1 := c33_1  ? scr_label1 + s33 + ' ' + tostring(roundn(v33_1, 2)) +  '\n'  : scr_label1
scr_label1 := c34_1  ? scr_label1 + s34 + ' ' + tostring(roundn(v34_1, 2)) +  '\n'  : scr_label1
scr_label1 := c35_1  ? scr_label1 + s35 + ' ' + tostring(roundn(v35_1, 2)) +  '\n'  : scr_label1
scr_label1 := c36_1  ? scr_label1 + s36 + ' ' + tostring(roundn(v36_1, 2)) +  '\n'  : scr_label1
scr_label1 := c37_1  ? scr_label1 + s37 + ' ' + tostring(roundn(v37_1, 2)) +  '\n'  : scr_label1
scr_label1 := c38_1  ? scr_label1 + s38 + ' ' + tostring(roundn(v38_1, 2)) +  '\n'  : scr_label1
scr_label1 := c39_1  ? scr_label1 + s39 + ' ' + tostring(roundn(v39_1, 2)) +  '\n'  : scr_label1
scr_label1 := c40_1  ? scr_label1 + s40 + ' ' + tostring(roundn(v40_1, 2)) +  '\n'  : scr_label1


scr_label2 = ''

scr_label2 := c01_2  ? scr_label2 + s01 + ' ' + tostring(roundn(v01_2, 2)) +  '\n'  : scr_label2
scr_label2 := c02_2  ? scr_label2 + s02 + ' ' + tostring(roundn(v02_2, 2)) +  '\n'  : scr_label2
scr_label2 := c03_2  ? scr_label2 + s03 + ' ' + tostring(roundn(v03_2, 2)) +  '\n'  : scr_label2
scr_label2 := c04_2  ? scr_label2 + s04 + ' ' + tostring(roundn(v04_2, 2)) +  '\n'  : scr_label2
scr_label2 := c05_2  ? scr_label2 + s05 + ' ' + tostring(roundn(v05_2, 2)) +  '\n'  : scr_label2
scr_label2 := c06_2  ? scr_label2 + s06 + ' ' + tostring(roundn(v06_2, 2)) +  '\n'  : scr_label2
scr_label2 := c07_2  ? scr_label2 + s07 + ' ' + tostring(roundn(v07_2, 2)) +  '\n'  : scr_label2
scr_label2 := c08_2  ? scr_label2 + s08 + ' ' + tostring(roundn(v08_2, 2)) +  '\n'  : scr_label2
scr_label2 := c09_2  ? scr_label2 + s09 + ' ' + tostring(roundn(v09_2, 2)) +  '\n'  : scr_label2
scr_label2 := c10_2  ? scr_label2 + s10 + ' ' + tostring(roundn(v10_2, 2)) +  '\n'  : scr_label2
scr_label2 := c11_2  ? scr_label2 + s11 + ' ' + tostring(roundn(v11_2, 2)) +  '\n'  : scr_label2
scr_label2 := c12_2  ? scr_label2 + s12 + ' ' + tostring(roundn(v12_2, 2)) +  '\n'  : scr_label2
scr_label2 := c13_2  ? scr_label2 + s13 + ' ' + tostring(roundn(v13_2, 2)) +  '\n'  : scr_label2
scr_label2 := c14_2  ? scr_label2 + s14 + ' ' + tostring(roundn(v14_2, 2)) +  '\n'  : scr_label2
scr_label2 := c15_2  ? scr_label2 + s15 + ' ' + tostring(roundn(v15_2, 2)) +  '\n'  : scr_label2
scr_label2 := c16_2  ? scr_label2 + s16 + ' ' + tostring(roundn(v16_2, 2)) +  '\n'  : scr_label2
scr_label2 := c17_2  ? scr_label2 + s17 + ' ' + tostring(roundn(v17_2, 2)) +  '\n'  : scr_label2
scr_label2 := c18_2  ? scr_label2 + s18 + ' ' + tostring(roundn(v18_2, 2)) +  '\n'  : scr_label2
scr_label2 := c19_2  ? scr_label2 + s19 + ' ' + tostring(roundn(v19_2, 2)) +  '\n'  : scr_label2
scr_label2 := c20_2  ? scr_label2 + s20 + ' ' + tostring(roundn(v20_2, 2)) +  '\n'  : scr_label2
scr_label2 := c21_2  ? scr_label2 + s21 + ' ' + tostring(roundn(v21_2, 2)) +  '\n'  : scr_label2
scr_label2 := c22_2  ? scr_label2 + s22 + ' ' + tostring(roundn(v22_2, 2)) +  '\n'  : scr_label2
scr_label2 := c23_2  ? scr_label2 + s23 + ' ' + tostring(roundn(v23_2, 2)) +  '\n'  : scr_label2
scr_label2 := c24_2  ? scr_label2 + s24 + ' ' + tostring(roundn(v24_2, 2)) +  '\n'  : scr_label2
scr_label2 := c25_2  ? scr_label2 + s25 + ' ' + tostring(roundn(v25_2, 2)) +  '\n'  : scr_label2
scr_label2 := c26_2  ? scr_label2 + s26 + ' ' + tostring(roundn(v26_2, 2)) +  '\n'  : scr_label2
scr_label2 := c27_2  ? scr_label2 + s27 + ' ' + tostring(roundn(v27_2, 2)) +  '\n'  : scr_label2
scr_label2 := c28_2  ? scr_label2 + s28 + ' ' + tostring(roundn(v28_2, 2)) +  '\n'  : scr_label2
scr_label2 := c29_2  ? scr_label2 + s29 + ' ' + tostring(roundn(v29_2, 2)) +  '\n'  : scr_label2
scr_label2 := c30_2  ? scr_label2 + s30 + ' ' + tostring(roundn(v30_2, 2)) +  '\n'  : scr_label2
scr_label2 := c31_2  ? scr_label2 + s31 + ' ' + tostring(roundn(v31_2, 2)) +  '\n'  : scr_label2
scr_label2 := c32_2  ? scr_label2 + s32 + ' ' + tostring(roundn(v32_2, 2)) +  '\n'  : scr_label2
scr_label2 := c33_2  ? scr_label2 + s33 + ' ' + tostring(roundn(v33_2, 2)) +  '\n'  : scr_label2
scr_label2 := c34_2  ? scr_label2 + s34 + ' ' + tostring(roundn(v34_2, 2)) +  '\n'  : scr_label2
scr_label2 := c35_2  ? scr_label2 + s35 + ' ' + tostring(roundn(v35_2, 2)) +  '\n'  : scr_label2
scr_label2 := c36_2  ? scr_label2 + s36 + ' ' + tostring(roundn(v36_2, 2)) +  '\n'  : scr_label2
scr_label2 := c37_2  ? scr_label2 + s37 + ' ' + tostring(roundn(v37_2, 2)) +  '\n'  : scr_label2
scr_label2 := c38_2  ? scr_label2 + s38 + ' ' + tostring(roundn(v38_2, 2)) +  '\n'  : scr_label2
scr_label2 := c39_2  ? scr_label2 + s39 + ' ' + tostring(roundn(v39_2, 2)) +  '\n'  : scr_label2
scr_label2 := c40_2  ? scr_label2 + s40 + ' ' + tostring(roundn(v40_2, 2)) +  '\n'  : scr_label2

scr_label3 = ''

scr_label3:= c01_3  ? scr_label3 + s01 + ' ' + tostring(roundn(v01_3, 2)) +  '\n'  : scr_label3
scr_label3:= c02_3  ? scr_label3 + s02 + ' ' + tostring(roundn(v02_3, 2)) +  '\n'  : scr_label3
scr_label3:= c03_3  ? scr_label3 + s03 + ' ' + tostring(roundn(v03_3, 2)) +  '\n'  : scr_label3
scr_label3:= c04_3  ? scr_label3 + s04 + ' ' + tostring(roundn(v04_3, 2)) +  '\n'  : scr_label3
scr_label3:= c05_3  ? scr_label3 + s05 + ' ' + tostring(roundn(v05_3, 2)) +  '\n'  : scr_label3
scr_label3:= c06_3  ? scr_label3 + s06 + ' ' + tostring(roundn(v06_3, 2)) +  '\n'  : scr_label3
scr_label3:= c07_3  ? scr_label3 + s07 + ' ' + tostring(roundn(v07_3, 2)) +  '\n'  : scr_label3
scr_label3:= c08_3  ? scr_label3 + s08 + ' ' + tostring(roundn(v08_3, 2)) +  '\n'  : scr_label3
scr_label3:= c09_3  ? scr_label3 + s09 + ' ' + tostring(roundn(v09_3, 2)) +  '\n'  : scr_label3
scr_label3:= c10_3  ? scr_label3 + s10 + ' ' + tostring(roundn(v10_3, 2)) +  '\n'  : scr_label3
scr_label3:= c11_3  ? scr_label3 + s11 + ' ' + tostring(roundn(v11_3, 2)) +  '\n'  : scr_label3
scr_label3:= c12_3  ? scr_label3 + s12 + ' ' + tostring(roundn(v12_3, 2)) +  '\n'  : scr_label3
scr_label3:= c13_3  ? scr_label3 + s13 + ' ' + tostring(roundn(v13_3, 2)) +  '\n'  : scr_label3
scr_label3:= c14_3  ? scr_label3 + s14 + ' ' + tostring(roundn(v14_3, 2)) +  '\n'  : scr_label3
scr_label3:= c15_3  ? scr_label3 + s15 + ' ' + tostring(roundn(v15_3, 2)) +  '\n'  : scr_label3
scr_label3:= c16_3  ? scr_label3 + s16 + ' ' + tostring(roundn(v16_3, 2)) +  '\n'  : scr_label3
scr_label3:= c17_3  ? scr_label3 + s17 + ' ' + tostring(roundn(v17_3, 2)) +  '\n'  : scr_label3
scr_label3:= c18_3  ? scr_label3 + s18 + ' ' + tostring(roundn(v18_3, 2)) +  '\n'  : scr_label3
scr_label3:= c19_3  ? scr_label3 + s19 + ' ' + tostring(roundn(v19_3, 2)) +  '\n'  : scr_label3
scr_label3:= c20_3  ? scr_label3 + s20 + ' ' + tostring(roundn(v20_3, 2)) +  '\n'  : scr_label3
scr_label3:= c21_3  ? scr_label3 + s21 + ' ' + tostring(roundn(v21_3, 2)) +  '\n'  : scr_label3
scr_label3:= c22_3  ? scr_label3 + s22 + ' ' + tostring(roundn(v22_3, 2)) +  '\n'  : scr_label3
scr_label3:= c23_3  ? scr_label3 + s23 + ' ' + tostring(roundn(v23_3, 2)) +  '\n'  : scr_label3
scr_label3:= c24_3  ? scr_label3 + s24 + ' ' + tostring(roundn(v24_3, 2)) +  '\n'  : scr_label3
scr_label3:= c25_3  ? scr_label3 + s25 + ' ' + tostring(roundn(v25_3, 2)) +  '\n'  : scr_label3
scr_label3:= c26_3  ? scr_label3 + s26 + ' ' + tostring(roundn(v26_3, 2)) +  '\n'  : scr_label3
scr_label3:= c27_3  ? scr_label3 + s27 + ' ' + tostring(roundn(v27_3, 2)) +  '\n'  : scr_label3
scr_label3:= c28_3  ? scr_label3 + s28 + ' ' + tostring(roundn(v28_3, 2)) +  '\n'  : scr_label3
scr_label3:= c29_3  ? scr_label3 + s29 + ' ' + tostring(roundn(v29_3, 2)) +  '\n'  : scr_label3
scr_label3:= c30_3  ? scr_label3 + s30 + ' ' + tostring(roundn(v30_3, 2)) +  '\n'  : scr_label3
scr_label3:= c31_3  ? scr_label3 + s31 + ' ' + tostring(roundn(v31_3, 2)) +  '\n'  : scr_label3
scr_label3:= c32_3  ? scr_label3 + s32 + ' ' + tostring(roundn(v32_3, 2)) +  '\n'  : scr_label3
scr_label3:= c33_3  ? scr_label3 + s33 + ' ' + tostring(roundn(v33_3, 2)) +  '\n'  : scr_label3
scr_label3:= c34_3  ? scr_label3 + s34 + ' ' + tostring(roundn(v34_3, 2)) +  '\n'  : scr_label3
scr_label3:= c35_3  ? scr_label3 + s35 + ' ' + tostring(roundn(v35_3, 2)) +  '\n'  : scr_label3
scr_label3:= c36_3  ? scr_label3 + s36 + ' ' + tostring(roundn(v36_3, 2)) +  '\n'  : scr_label3
scr_label3:= c37_3  ? scr_label3 + s37 + ' ' + tostring(roundn(v37_3, 2)) +  '\n'  : scr_label3
scr_label3:= c38_3  ? scr_label3 + s38 + ' ' + tostring(roundn(v38_3, 2)) +  '\n'  : scr_label3
scr_label3:= c39_3  ? scr_label3 + s39 + ' ' + tostring(roundn(v39_3, 2)) +  '\n'  : scr_label3
scr_label3:= c40_3  ? scr_label3 + s40 + ' ' + tostring(roundn(v40_3, 2)) +  '\n'  : scr_label3

scr_label4 = ""

scr_label4:= c01_4  ? scr_label4 + s01 + ' ' + tostring(roundn(v01_4, 2)) +  '\n'  : scr_label4
scr_label4:= c02_4  ? scr_label4 + s02 + ' ' + tostring(roundn(v02_4, 2)) +  '\n'  : scr_label4
scr_label4:= c03_4  ? scr_label4 + s03 + ' ' + tostring(roundn(v03_4, 2)) +  '\n'  : scr_label4
scr_label4:= c04_4  ? scr_label4 + s04 + ' ' + tostring(roundn(v04_4, 2)) +  '\n'  : scr_label4
scr_label4:= c05_4  ? scr_label4 + s05 + ' ' + tostring(roundn(v05_4, 2)) +  '\n'  : scr_label4
scr_label4:= c06_4  ? scr_label4 + s06 + ' ' + tostring(roundn(v06_4, 2)) +  '\n'  : scr_label4
scr_label4:= c07_4  ? scr_label4 + s07 + ' ' + tostring(roundn(v07_4, 2)) +  '\n'  : scr_label4
scr_label4:= c08_4  ? scr_label4 + s08 + ' ' + tostring(roundn(v08_4, 2)) +  '\n'  : scr_label4
scr_label4:= c09_4  ? scr_label4 + s09 + ' ' + tostring(roundn(v09_4, 2)) +  '\n'  : scr_label4
scr_label4:= c10_4  ? scr_label4 + s10 + ' ' + tostring(roundn(v10_4, 2)) +  '\n'  : scr_label4
scr_label4:= c11_4  ? scr_label4 + s11 + ' ' + tostring(roundn(v11_4, 2)) +  '\n'  : scr_label4
scr_label4:= c12_4  ? scr_label4 + s12 + ' ' + tostring(roundn(v12_4, 2)) +  '\n'  : scr_label4
scr_label4:= c13_4  ? scr_label4 + s13 + ' ' + tostring(roundn(v13_4, 2)) +  '\n'  : scr_label4
scr_label4:= c14_4  ? scr_label4 + s14 + ' ' + tostring(roundn(v14_4, 2)) +  '\n'  : scr_label4
scr_label4:= c15_4  ? scr_label4 + s15 + ' ' + tostring(roundn(v15_4, 2)) +  '\n'  : scr_label4
scr_label4:= c16_4  ? scr_label4 + s16 + ' ' + tostring(roundn(v16_4, 2)) +  '\n'  : scr_label4
scr_label4:= c17_4  ? scr_label4 + s17 + ' ' + tostring(roundn(v17_4, 2)) +  '\n'  : scr_label4
scr_label4:= c18_4  ? scr_label4 + s18 + ' ' + tostring(roundn(v18_4, 2)) +  '\n'  : scr_label4
scr_label4:= c19_4  ? scr_label4 + s19 + ' ' + tostring(roundn(v19_4, 2)) +  '\n'  : scr_label4
scr_label4:= c20_4  ? scr_label4 + s20 + ' ' + tostring(roundn(v20_4, 2)) +  '\n'  : scr_label4
scr_label4:= c21_4  ? scr_label4 + s21 + ' ' + tostring(roundn(v21_4, 2)) +  '\n'  : scr_label4
scr_label4:= c22_4  ? scr_label4 + s22 + ' ' + tostring(roundn(v22_4, 2)) +  '\n'  : scr_label4
scr_label4:= c23_4  ? scr_label4 + s23 + ' ' + tostring(roundn(v23_4, 2)) +  '\n'  : scr_label4
scr_label4:= c24_4  ? scr_label4 + s24 + ' ' + tostring(roundn(v24_4, 2)) +  '\n'  : scr_label4
scr_label4:= c25_4  ? scr_label4 + s25 + ' ' + tostring(roundn(v25_4, 2)) +  '\n'  : scr_label4
scr_label4:= c26_4  ? scr_label4 + s26 + ' ' + tostring(roundn(v26_4, 2)) +  '\n'  : scr_label4
scr_label4:= c27_4  ? scr_label4 + s27 + ' ' + tostring(roundn(v27_4, 2)) +  '\n'  : scr_label4
scr_label4:= c28_4  ? scr_label4 + s28 + ' ' + tostring(roundn(v28_4, 2)) +  '\n'  : scr_label4
scr_label4:= c29_4  ? scr_label4 + s29 + ' ' + tostring(roundn(v29_4, 2)) +  '\n'  : scr_label4
scr_label4:= c30_4  ? scr_label4 + s30 + ' ' + tostring(roundn(v30_4, 2)) +  '\n'  : scr_label4
scr_label4:= c31_4  ? scr_label4 + s31 + ' ' + tostring(roundn(v31_4, 2)) +  '\n'  : scr_label4
scr_label4:= c32_4  ? scr_label4 + s32 + ' ' + tostring(roundn(v32_4, 2)) +  '\n'  : scr_label4
scr_label4:= c33_4  ? scr_label4 + s33 + ' ' + tostring(roundn(v33_4, 2)) +  '\n'  : scr_label4
scr_label4:= c34_4  ? scr_label4 + s34 + ' ' + tostring(roundn(v34_4, 2)) +  '\n'  : scr_label4
scr_label4:= c35_4  ? scr_label4 + s35 + ' ' + tostring(roundn(v35_4, 2)) +  '\n'  : scr_label4
scr_label4:= c36_4  ? scr_label4 + s36 + ' ' + tostring(roundn(v36_4, 2)) +  '\n'  : scr_label4
scr_label4:= c37_4  ? scr_label4 + s37 + ' ' + tostring(roundn(v37_4, 2)) +  '\n'  : scr_label4
scr_label4:= c38_4  ? scr_label4 + s38 + ' ' + tostring(roundn(v38_4, 2)) +  '\n'  : scr_label4
scr_label4:= c39_4  ? scr_label4 + s39 + ' ' + tostring(roundn(v39_4, 2)) +  '\n'  : scr_label4
scr_label4:= c40_4  ? scr_label4 + s40 + ' ' + tostring(roundn(v40_4, 2)) +  '\n'  : scr_label4

scr_label5 = ""

scr_label5:= c01_5  ? scr_label5 + s01 + ' ' + tostring(roundn(v01_5, 2)) +  '\n'  : scr_label5
scr_label5:= c02_5  ? scr_label5 + s02 + ' ' + tostring(roundn(v02_5, 2)) +  '\n'  : scr_label5
scr_label5:= c03_5  ? scr_label5 + s03 + ' ' + tostring(roundn(v03_5, 2)) +  '\n'  : scr_label5
scr_label5:= c04_5  ? scr_label5 + s04 + ' ' + tostring(roundn(v04_5, 2)) +  '\n'  : scr_label5
scr_label5:= c05_5  ? scr_label5 + s05 + ' ' + tostring(roundn(v05_5, 2)) +  '\n'  : scr_label5
scr_label5:= c06_5  ? scr_label5 + s06 + ' ' + tostring(roundn(v06_5, 2)) +  '\n'  : scr_label5
scr_label5:= c07_5  ? scr_label5 + s07 + ' ' + tostring(roundn(v07_5, 2)) +  '\n'  : scr_label5
scr_label5:= c08_5  ? scr_label5 + s08 + ' ' + tostring(roundn(v08_5, 2)) +  '\n'  : scr_label5
scr_label5:= c09_5  ? scr_label5 + s09 + ' ' + tostring(roundn(v09_5, 2)) +  '\n'  : scr_label5
scr_label5:= c10_5  ? scr_label5 + s10 + ' ' + tostring(roundn(v10_5, 2)) +  '\n'  : scr_label5
scr_label5:= c11_5  ? scr_label5 + s11 + ' ' + tostring(roundn(v11_5, 2)) +  '\n'  : scr_label5
scr_label5:= c12_5  ? scr_label5 + s12 + ' ' + tostring(roundn(v12_5, 2)) +  '\n'  : scr_label5
scr_label5:= c13_5  ? scr_label5 + s13 + ' ' + tostring(roundn(v13_5, 2)) +  '\n'  : scr_label5
scr_label5:= c14_5  ? scr_label5 + s14 + ' ' + tostring(roundn(v14_5, 2)) +  '\n'  : scr_label5
scr_label5:= c15_5  ? scr_label5 + s15 + ' ' + tostring(roundn(v15_5, 2)) +  '\n'  : scr_label5
scr_label5:= c16_5  ? scr_label5 + s16 + ' ' + tostring(roundn(v16_5, 2)) +  '\n'  : scr_label5
scr_label5:= c17_5  ? scr_label5 + s17 + ' ' + tostring(roundn(v17_5, 2)) +  '\n'  : scr_label5
scr_label5:= c18_5  ? scr_label5 + s18 + ' ' + tostring(roundn(v18_5, 2)) +  '\n'  : scr_label5
scr_label5:= c19_5  ? scr_label5 + s19 + ' ' + tostring(roundn(v19_5, 2)) +  '\n'  : scr_label5
scr_label5:= c20_5  ? scr_label5 + s20 + ' ' + tostring(roundn(v20_5, 2)) +  '\n'  : scr_label5
scr_label5:= c21_5  ? scr_label5 + s21 + ' ' + tostring(roundn(v21_5, 2)) +  '\n'  : scr_label5
scr_label5:= c22_5  ? scr_label5 + s22 + ' ' + tostring(roundn(v22_5, 2)) +  '\n'  : scr_label5
scr_label5:= c23_5  ? scr_label5 + s23 + ' ' + tostring(roundn(v23_5, 2)) +  '\n'  : scr_label5
scr_label5:= c24_5  ? scr_label5 + s24 + ' ' + tostring(roundn(v24_5, 2)) +  '\n'  : scr_label5
scr_label5:= c25_5  ? scr_label5 + s25 + ' ' + tostring(roundn(v25_5, 2)) +  '\n'  : scr_label5
scr_label5:= c26_5  ? scr_label5 + s26 + ' ' + tostring(roundn(v26_5, 2)) +  '\n'  : scr_label5
scr_label5:= c27_5  ? scr_label5 + s27 + ' ' + tostring(roundn(v27_5, 2)) +  '\n'  : scr_label5
scr_label5:= c28_5  ? scr_label5 + s28 + ' ' + tostring(roundn(v28_5, 2)) +  '\n'  : scr_label5
scr_label5:= c29_5  ? scr_label5 + s29 + ' ' + tostring(roundn(v29_5, 2)) +  '\n'  : scr_label5
scr_label5:= c30_5  ? scr_label5 + s30 + ' ' + tostring(roundn(v30_5, 2)) +  '\n'  : scr_label5
scr_label5:= c31_5  ? scr_label5 + s31 + ' ' + tostring(roundn(v31_5, 2)) +  '\n'  : scr_label5
scr_label5:= c32_5  ? scr_label5 + s32 + ' ' + tostring(roundn(v32_5, 2)) +  '\n'  : scr_label5
scr_label5:= c33_5  ? scr_label5 + s33 + ' ' + tostring(roundn(v33_5, 2)) +  '\n'  : scr_label5
scr_label5:= c34_5  ? scr_label5 + s34 + ' ' + tostring(roundn(v34_5, 2)) +  '\n'  : scr_label5
scr_label5:= c35_5  ? scr_label5 + s35 + ' ' + tostring(roundn(v35_5, 2)) +  '\n'  : scr_label5
scr_label5:= c36_5  ? scr_label5 + s36 + ' ' + tostring(roundn(v36_5, 2)) +  '\n'  : scr_label5
scr_label5:= c37_5  ? scr_label5 + s37 + ' ' + tostring(roundn(v37_5, 2)) +  '\n'  : scr_label5
scr_label5:= c38_5  ? scr_label5 + s38 + ' ' + tostring(roundn(v38_5, 2)) +  '\n'  : scr_label5
scr_label5:= c39_5  ? scr_label5 + s39 + ' ' + tostring(roundn(v39_5, 2)) +  '\n'  : scr_label5
scr_label5:= c40_5  ? scr_label5 + s40 + ' ' + tostring(roundn(v40_5, 2)) +  '\n'  : scr_label5

// Add a header to every screener
scr_label1 := 'RSI  Screener: \n##########\n' + scr_label1
scr_label2 := 'TSI  Screener: \n##########\n' + scr_label2
scr_label3 := 'ADX  Screener: \n##########\n' + scr_label3
scr_label4 := 'MACD Screener: \n##########\n' + scr_label4
scr_label5 := 'AO   Screener: \n##########\n' + scr_label5

// Displays labels with screeners on the chart
lab_l1 = label.new(
          bar_index - 0 * bars_apart, 0, scr_label1, 
          color     = color(#ab3043), 
          textcolor = color.black, 
          style     = label.style_labeldown,
          yloc      = yloc.price)

lab_l2 = label.new(
          bar_index - 1 * bars_apart, 0, scr_label2, 
          color     = color(#247352), 
          textcolor = color.black, 
          style     = label.style_labeldown,
          yloc      = yloc.price)

lab_l3 = label.new(
          bar_index - 2 * bars_apart, 0, scr_label3, 
          color     = color(#80A1C1), 
          textcolor = color.black, 
          style     = label.style_labeldown,
          yloc      = yloc.price)

lab_l4 = label.new(
          bar_index - 3 * bars_apart, 0, scr_label4, 
          color     = color(#5DFDCB), 
          textcolor = color.black, 
          style     = label.style_labeldown,
          yloc      = yloc.price)

lab_l5 = label.new(
          bar_index - 4 * bars_apart, 0, scr_label5, 
          color     = color(#987284), 
          textcolor = color.black, 
          style     = label.style_labeldown,
          yloc      = yloc.price)

// Delete old labels so label should be visible only for the last bar
label.delete(lab_l1[1])
label.delete(lab_l2[1])
label.delete(lab_l3[1])
label.delete(lab_l4[1])
label.delete(lab_l5[1])

// Alert message as a combination of all screeners
alert_message = scr_label1 + "\n\n" + scr_label2 + "\n\n" + scr_label3 + "\n\n" + scr_label4 + "\n\n" + scr_label5

// Send an alert
alert(alert_message, freq = alert.freq_once_per_bar_close )
