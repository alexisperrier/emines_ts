# TODO

- Load the time series
    - pd.Series
    - index = date, temps
    - values
- plot
- white noise testing with ljung box
- stationarity testing, ADF, KPSS

# AR(p) ?

- analyse PACF (partial autocorrelation)
- set the order p of the AR(p) process

- Estimate the AR(p) coefficients with Yule Walker equations

# MA(q) ?

- Analyse ACF ( autocorrelation)
- set the order q of the MA(q) process

- Use statsmodel to fit an ARMA process

# Differencing - stationarisation

processus $d_t = x_t - x_{t-1}$
