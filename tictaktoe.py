# theBoard = {
#     'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
#     'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
#     'low_L': ' ', 'low_M': ' ', 'low_R': ' '
# }


# def printBoard(board):
#     print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
#     print('-+-+-')
#     print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
#     print('-+-+-')
#     print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'])


# turn = 'X'
# for i range(9):
#     printBoard(theBoard)
#     print(f"Turn the {turn}. Move in which space?")
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'

#     else:
#         turn == 'X'


# printBoard(theBoard)


stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.item_total():