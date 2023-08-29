import requests
response = requests.get('https://github.com/danielduartt')
print("Status code:", response.status_code)
print("=================================Header=======================================")
print(response.headers)
print("================================Conteudo======================================")
print(response.content) #retorna toda a parte do html da página

