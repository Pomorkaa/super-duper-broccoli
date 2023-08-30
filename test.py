# python
from requests import get
from requests.exceptions import RequestException
import base64

def get_block(block_number):
    """функция получения данных из data.txs"""

    url = f"https://akash-rest.publicnode.com/cosmos/base/tendermint/v1beta1/blocks/{block_number}"
    
    try:
        response = get(url)
        response.raise_for_status()                                                   # Проверяем, что ушел нормально
        data = response.json()["block"]["data"]["txs"]                                # Получаем данные, которые нам нужны
        if len(data) > 0:
            for tx in data:
                decoded_data = base64.b64decode(tx)
                print(decoded_data)
                print('------------------------------------------------------')
        else:
            print(f"В блоке {block_number} нет транзакций")
            
    except RequestException as err:
        print(f"Произошла ошибка при выполнении запроса: {err}")



get_block(11260637)
