import random
quotes = ["Fortune favors the bold.",
"I think, therefore I am.",
"Time is money.",
"I came, I saw, I conquered",
"Knowledge is power."
# You can add More quotes if you want! I found some of these
]
# print(quotes)
qlen = len(quotes)
qrandom = random.randrange(qlen)
print(quotes[qrandom])