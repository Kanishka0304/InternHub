import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse


class WebsiteData:
    """
    Central structured data container.
    All 15 layers must use this object only.
    """

    def __init__(
        self,
        url,
        domain,
        html,
        text,
        title,
        meta_description,
        emails,
        phone_numbers,
        internal_links
    ):
        self.url = url
        self.domain = domain
        self.html = html
        self.text = text
        self.title = title
        self.meta_description = meta_description
        self.emails = emails
        self.phone_numbers = phone_numbers
        self.internal_links = internal_links
        self.internal_link_count = len(internal_links)


def scrape_website(url):

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        text = re.sub(r"\s+", " ", text).strip()

        # Extract domain
        parsed = urlparse(url)
        domain = parsed.netloc

        # Extract title
        title = soup.title.string.strip() if soup.title else ""

        # Extract meta description
        meta_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = meta_tag["content"].strip() if meta_tag and "content" in meta_tag.attrs else ""

        # Extract emails
        email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        emails = list(set(re.findall(email_pattern, text)))

        # Extract phone numbers
        phone_pattern = r"\+?\d[\d\s\-]{8,15}"
        phone_numbers = list(set(re.findall(phone_pattern, text)))

        # Extract internal links
        internal_links = []
        for tag in soup.find_all("a", href=True):
            full_link = urljoin(url, tag["href"])
            if urlparse(full_link).netloc == domain:
                internal_links.append(full_link)

        internal_links = list(set(internal_links))

        return WebsiteData(
            url=url,
            domain=domain,
            html=html,
            text=text,
            title=title,
            meta_description=meta_description,
            emails=emails,
            phone_numbers=phone_numbers,
            internal_links=internal_links
        )

    except Exception as e:
        print(f"[ERROR] Scraping failed: {e}")
        return None
