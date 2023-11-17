import requests
import random

webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAbMvrJBE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=8s0aqBydgkSkWdApTmMoUVopYqnd2ZFGLpsrM0wkBbc'

def return_joke():
    with open('piadas.txt', 'r') as arquivo:
        # Obter todas as linhas do arquivo
        lines = arquivo.readlines()
        number_lines = len(lines)
        random_number = random.randint(0, number_lines)
        
        # Ler a segunda linha (índice 1, pois os índices começam do zero)
        linha_desejada = lines[random_number].strip()
    
    jokes = {
        "text": linha_desejada
    }

    return jokes

joke = return_joke()

answer = requests.post(webhook_url, json=joke)

if answer.status_code == 200:
    print("Pedido POST bem-sucedido!")
else:
    print(f"Erro no pedido POST. Código de status: {answer.status_code}")
    print(answer.text)
