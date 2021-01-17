import internetspeedtwitterbot


PROMISED_DOWN = 50
PROMISED_UP = 50
bot = internetspeedtwitterbot.InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider(PROMISED_DOWN, PROMISED_UP)
    bot.driver.quit()





