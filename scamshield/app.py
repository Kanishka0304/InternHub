from scraper.scraper_layer import scrape_website
from feature_engine.timeline_layer import check_domain_age


def main():
    print("\n=== ScamShield Analyzer ===\n")

    url = input("Enter internship website URL: ").strip()

    if not url.startswith("http"):
        print("[ERROR] Invalid URL. Must start with http or https.")
        return

    website_data = scrape_website(url)

    if website_data is None:
        print("[ERROR] Scraping failed.")
        return

    # Call Timeline Layer
    timeline_result = check_domain_age(website_data)

    # Just print what layer returns
    print("\n--- Timeline Layer Output ---")
    print(timeline_result)


if __name__ == "__main__":
    main()
