import NewModule
streetnames=['Огарёва','Житная','Жулебино','Грузинский вал','Тихоходная','Никонова','переулок Красный','Ленина','Техническая','Арбат']
streets=11
players=int(input("Введите количество игроков: "))
while streets<1 or streets>10:
    streets=int(input("Введите количество улиц (до 10!): "))

game = NewModule.MyGame(players,streets)
game.start_game()


