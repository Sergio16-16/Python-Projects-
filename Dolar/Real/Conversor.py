import requests 
quest = int(input("Digite um numero que deseja converter pra real"))
r = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
valor_dolar = r.json()['USD']['high']
print({quest} * {valor_dolar})

