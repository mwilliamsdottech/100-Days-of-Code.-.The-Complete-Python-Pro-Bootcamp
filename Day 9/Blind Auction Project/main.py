# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {
    "name": "",
    "bid_amount": 0,
}

while new_bid != "no":
    name = input("What is your name? ")
    bid_amount = input("What's your bid? ")

    #add name and bid amount to dictionary
    bids["name"] = name
    bids["bid_amount"] = bid_amount

    print(bids)

new_bid = input("Are there more bidders? Yes? No? ").lower()

