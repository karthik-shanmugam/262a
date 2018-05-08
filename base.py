class User:
    def __init__(self, name, initial_funds, resources):
        self.name = name
        self.funds = initial_funds
        self.resources = resources

    def add_funds(self, amount):
        self.fund += amount

    def do_client_bids(self, auctions):
        pass

    def do_server_bids(self, auctions):
        pass

    def __str__(self):
        return self.name + " (" + self.funds + " credits, " + self.resources + " cpus)"

class Auction:
    def __init__(self);
        pass
    
    def client_bid(self, client, num_resources, unit_price):
        pass

    def server_bid(self, server, num_resources, unit_price):
        pass

    def do_auction(self):
        pass

