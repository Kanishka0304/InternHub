from scraper.scraper_layer import scrape_website
import sys


def validate_url(url: str) -> bool:
    """
    Basic validation for URL format.
    """
    if not url.startswith("http://") and not url.startswith("https://"):
        return False
    return True


def display_scraped_summary(data: dict):
    """
    Display structured summary of scraped website data.
    """
    print("\n==============================")
    print("     SCRAPED WEBSITE DATA")
    print("==============================")

    print(f"\nURL: {data['url']}")
    print(f"\nEmails Found: {len(data['emails'])}")
    print(data["emails"])

    print(f"\nPhone Numbers Found: {len(data['phone_numbers'])}")
    print(data["phone_numbers"])

    print(f"\nInternal Links Found: {data['internal_link_count']}")

    print(f"\nExtracted Text Length: {len(data['text'])} characters")
    print("\n==============================\n")


def main():
    print("\n=== ScamShield Internship Website Analyzer ===\n")

    url = input("Enter internship website URL: ").strip()

    if not validate_url(url):
        print("\n[ERROR] Invalid URL format. Please include http:// or https://")
        sys.exit()

    print("\n[INFO] Scraping website...\n")

    data = scrape_website(url)

    if data is None:
        print("[ERROR] Failed to scrape website. Please check the URL.")
        sys.exit()

    display_scraped_summary(data)


if __name__ == "__main__":
    main()
