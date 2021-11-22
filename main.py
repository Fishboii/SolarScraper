import scrape
import time
while True:
    scrape.scrape(True)
    print("\nwaiting for image update")
    time.sleep(300)