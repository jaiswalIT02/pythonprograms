
menu_bar=Menu(compiler)
run_bar=Menu(menu_bar)
run_bar.add_command(label='Run')
menu_bar.add_cascade(label='Run',menu=menu_bar)
compiler.config(menu=menu_bar)