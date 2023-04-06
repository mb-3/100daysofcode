from internet_speed_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 500
PROMISED_UP = 500

istb = InternetSpeedTwitterBot()

istb.get_internet_speed()

if istb.upload_val < PROMISED_UP or istb.download_val:

    istb.tweet_at_provider()
