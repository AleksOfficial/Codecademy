class Art:
    def __init__(self, artist, title, year, medium, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{}. {}. {}, {}. {}, {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)


class Marketplace():
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for i in self.listings:
            print(i)


class Client:
    def __init__(self, name, location, is_museum, wallet):
        self.name = name
        self.location = location
        self.is_museum = is_museum
        self.wallet = wallet
        self.wishlist = []

    def sell_artwork(self, artwork, price, calc_price):
        if(artwork.owner == self):
            veneer.add_listing(Listing(artwork, price, self, calc_price))

    def buy_artwork(self, artwork):
        if(self != artwork.owner):
            for i in veneer.listings:
                if(i.art == artwork):
                    if(i.calc_price <= self.wallet):
                        artwork.owner = self
                        i.seller.wallet += i.calc_price
                        self.wallet -= i.calc_price
                        veneer.remove_listing(i)
                        break
    
    def add_to_wishlist(self, artwork):
        if(self != artwork.owner):
            if(artwork not in self.wishlist):
                for i in veneer.listings:
                    if(i.art == artwork):
                        self.wishlist.append(i)
                        break

    def remove_from_wishlist(self, artwork):
        for i in self.wishlist:
            if(artwork == i.art):
                self.wishlist.remove(i)
        


    def __repr__(self):
        return "{} has $ {} in her wallet.".format(self.name, self.wallet)


class Listing:
    def __init__(self, art, price, seller, calc_price):
        self.art = art
        self.price = price
        self.seller = seller
        self.calc_price = calc_price

    def __repr__(self):
        return "{}, {}".format(self.art.title, self.price)


veneer = Marketplace()
# veneer.add_listing(girl_with_mandolin)

edytta = Client("Edytta Halpirt", "Private Collection", False, 0)
girl_with_mandolin = Art(
    "Picasso, Pablo", "\"Girl with a Mandolin (Fanny Tellier)\"", 1910, "oil on canvas", edytta)
moma = Client("The MOMA", "New York", True, 6000000)
# print(girl_with_mandolin)
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)", 6000000)
veneer.show_listings()
print(edytta)
print(moma)
moma.add_to_wishlist(girl_with_mandolin)

moma.buy_artwork(girl_with_mandolin)
moma.remove_from_wishlist(girl_with_mandolin)

print(girl_with_mandolin)
veneer.show_listings()
print(edytta)
print(moma)
# todo:
# Add a Wallet x 
# Create a wishlistx
# Create expiration Dates
