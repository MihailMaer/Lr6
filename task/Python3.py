from colorama import init, Fore, Back, Style

init(15)

print(Fore.RED + 'some red text\n' + Back.YELLOW + 'and with a yellow background')
print(Style.DIM + 'and in dim text\n' + Style.RESET_ALL + 'back to normal now')