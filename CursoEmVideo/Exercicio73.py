times = ("Man. City","Liverpool","Chelsea","Tottenham Hotspur","Arsenal","Man. Utd","West Ham","Leicester","Brighton & Hove Albion","Wolves","Newcastle","Crystal Palace","Brentford","Aston Villa","Southampton","Everton","Leeds United","Burnley","Watford","Norwich City")
print("Os times classificados pra champions são: {}\n".format(times[0:5]))
print("Os times que cairam foram: {}\n".format(times[-3:]))
print("Os times em ordem alfabética {}\n".format(sorted(times)))
pos = times.index("Chelsea")+1
print("O Chelsea terminou em {}º lugar".format(times.index("Chelsea")+1))