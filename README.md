# emines_ts

This repo holds the students work for the course on times series I gave at [Emines School of Industrial Management](https://www.emines-ingenieur.org/) de l'université Mohammed VI Polytechnique (UM6P) in January 2021.

The curriculum covered
- white noise and random walk
- stationarity, definition
- Ljung-box, KPSS and ADF statistical tests
- Autocorrelation (ACF) and partial autocorrelation (PACF)
- ARIMA models
- Yule Walker equations
- Facebook's Prophet
- Decomposition, seasonal and STL
- Exponential smoothing, Holt and Holt Winters
- VAR and the Granger Causality test

We mostly worked with statsmodel python library.

The students were asked to find times series online and apply the concepts and methods on their time own dataset. This way, the students worked on noisy datasets that did not always comply with the theory.

We also worked on the [Predict Future Sales](https://www.kaggle.com/c/competitive-data-science-predict-future-sales)  Kaggle time serie competition. The goal is to predict monthly sales for 1000s of products in many stores. We focused on a few products with large volumes of sales aggregated across the stores.

## Resources

We mostly used the excellent and classic book [Forecasting: Principles and Practice](https://otexts.com/fpp2/) by Rob J Hyndman and George Athanasopoulos which is available online for free.

And we worked on the examples and implementations from the following posts

* [White Noise and Random Walks in Time Series Analysis](https://www.quantstart.com/articles/White-Noise-and-Random-Walks-in-Time-Series-Analysis/)

* [Algorithm Breakdown: AR, MA and ARIMA models](https://www.ritchievink.com/blog/2018/09/26/algorithm-breakdown-ar-ma-and-arima-models/) by [Ritchie Vink](https://github.com/ritchie46)

* [Time Series Analysis (TSA) in Python - Linear Models to GARCH](http://www.blackarbs.com/blog/time-series-analysis-in-python-linear-models-to-garch/11/1/2016#AR) by [@BLACKARBSCEO](https://twitter.com/BLACKARBSCEO) and more particularly on

    - Autoregressive Models - AR(p)
    - Moving Average Models - MA(q)
    - Autoregressive Moving Average Models - ARMA(p, q)
    - Autoregressive Integrated Moving Average Models - ARIMA(p, d, q)


* [Open Machine Learning Course. Topic 9. Part 1. Time series analysis in Python]
(https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-9-time-series-analysis-in-python-a270cb05e0b3) by [Dmitry Sergeyev](https://github.com/DmitrySerg).

More specifically, the following part:

    — Rolling window estimations
    — Exponential smoothing, Holt-Winters model
    — Time-series cross validation, parameters selection

* [Time Series Analysis in Python](https://www.machinelearningplus.com/time-series/time-series-analysis-python/)

* [How to Decompose Time Series Data into Trend and Seasonality](https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/)

* [A Gentle Introduction to Exponential Smoothing for Time Series Forecasting in Python](https://machinelearningmastery.com/exponential-smoothing-for-time-series-forecasting-in-python/) by Jason Brownlee

* [A Multivariate Time Series Guide to Forecasting and Modeling](https://www.analyticsvidhya.com/blog/2018/09/multivariate-time-series-guide-forecasting-modeling-python-codes/) for VAR models.

* [Forecasting with sktime](https://github.com/alan-turing-institute/sktime/blob/master/examples/01_forecasting.ipynb)

We did not have time to explore [sktime](https://github.com/alan-turing-institute/sktime) a very promising "unified framework for machine learning with time series"

## Youtube

I recommend this excellent Youtube channel

* [Morten Nyboe Tabor](https://www.youtube.com/c/MortenNyboeTabor/videos)
Econometrics II course at the Economics program, University of Copenhagen.
