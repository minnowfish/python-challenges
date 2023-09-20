from random import randint
response = ["Yes", "For sure","Without a doubt","Uncertain","Ask me later","Best not to say now","No","Doubtful","Outlook not so good"]
while True:
  question = input("Input your question ")
  num = randint(0,8)
  print(response[num])
