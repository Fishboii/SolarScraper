import scrape
import time
while True:
    scrape.scrape(True)
    time.sleep(300)
    print("\nwaiting for image update")