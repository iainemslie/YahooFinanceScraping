-- Get daily gain or loss as percent
SELECT Date, Open, High, Low, Close, Volume, ((Close / Open) - 1) * 100 AS gain_or_loss_percent FROM yfinance.aapl ORDER BY gain_or_loss_percent DESC;

-- 