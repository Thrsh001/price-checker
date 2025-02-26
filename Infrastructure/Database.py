class Database:
    # OVO DOK NE NAPRAVIM ORM TABELE
    def __init__(self):
        self.shops = {
            "tehnomedia": {
                "strategy": "playwright",
                "url": "https://tehnomedia.rs/search/find.html?rec=",
                }
        }
        self.data = []

    def save(self, record):
        print("[DB] Saving:", record)
        self.data.append(record)

    def get_shop(self, shop_name):
        return self.shops.get(shop_name)
