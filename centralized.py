from base import User, Auction
from collections import namedtuple


Bid = namedtuple("Bid", ["price_per_resource", "num_resources"])

def dictargmax(d):
    assert len(d) > 0, "cannot find max of an empty dictionary"
    currarg, currmax = next(iter(d.items()))
    for k, v in d.items():
        if v > currmax:
            currarg = k
            currmax = v
    return currarg

class CentralizedAuction:
    def __init__(self):
        self.client_bids = {}
    
    def client_bid(self, client, bid):
        self.client_bids[client] = bid

    def do_auction(self):
        if not len(self.client_bids):
            assert False, "No one bid :("
        else:
            winner = dictargmax(self.client_bids)
            winning_bid = self.client_bids[winner]
            winner.funds -= winning_bid[0] * winning_bid[1]
            for client in self.client_bids:
                client.notify_winning_bid(self, winning_bid)
            print(winning_bid)


class Client:
    def __init__(self, name, initial_funds):
        self.name = name
        self.funds = initial_funds
        self.auctions = {}
        self.last_winning_price = 0

    def notify_winning_bid(self, auction, bid):
        self.last_winning_price = bid.price_per_resource


class SimpleClient(Client):
    def __init__(self, name, initial_funds, max_price):



        super().__init__(name, initial_funds)
        self.max_price = max_price

    def bid_in_auction(self, auction):
        auction.client_bid(
            self,
            Bid(min(self.max_price, self.last_winning_price + 1, self.funds), 1)
        )


def shitty_simulation():
    clients = [SimpleClient("client%d" % i, 2000, 10+i) for i in range(10)]
    for _ in range(1000):
        auction = CentralizedAuction()
        for client in clients:
            client.bid_in_auction(auction)
        auction.do_auction()


shitty_simulation()





    #     class CentralizedAuction:
    # def __init__(self, clients);
    #     self.bids = {}
    #     self.clients = list(clients)
    
    # def client_bid(self, client, num_resources, unit_price):
    #     self.client_bids[client] = (unit_price, num_resources)
    #     pass

    # def do_auction(self):
    #     for client in self.clients:
    #         self.client_bid(client, client.)
    #     winner = dictargmax(self.bids)


    #     pass