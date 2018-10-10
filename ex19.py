def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")


print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def the_money_you_got(money_you_left, but_you_have_spent_some):
    print("You have %d NTD" % money_you_left)
    print("You have spent %d NTD" % but_you_have_spent_some)
    print("Not enough to buy cheese and crackers")

print("Let's pay for cheese and crackers")
money_You_have = 800
but_you_spent =799

the_money_you_got(money_You_have, but_you_spent)