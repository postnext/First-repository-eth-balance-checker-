from web3 import Web3

# Подключаемся к публичному Ethereum-узлу (например, Infura)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY"
w3 = Web3(Web3.HTTPProvider(infura_url))

# Проверяем подключение
if not w3.is_connected():
    print("Ошибка: не удалось подключиться к Ethereum")
    exit()

# Введи адрес кошелька для проверки баланса
eth_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Пример: Binance Wallet

# Получаем баланс
balance = w3.eth.get_balance(eth_address)

# Конвертируем баланс из Wei в ETH
eth_balance = w3.from_wei(balance, 'ether')

print(f"Баланс {eth_address}: {eth_balance} ETH")
