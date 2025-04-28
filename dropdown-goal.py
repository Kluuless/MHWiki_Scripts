import tkinter as tk

window = tk.Tk()
window.geometry("1000x500")
window.title("Dropdown test")

counter_charm_costs = {
    "Counter Charm I": "3000z\nRathian Webbing x3\nGypceros Head x3\nTalioth Scale x5\nBird Wyvern Gem x1",
    "Counter Charm II": "6000z\nBlangonga Pelt+ x6\nBlangonga Whisker x5\nBlango Pelt+ x5\nBeast Gem x1",
    "Counter Charm III": "9000z\nHunter Symbol III x3\nGuardian Rathalos Wing x4\nRathalos Ruby x1"
}

counter_charm_mats_txt = tk.StringVar(value=counter_charm_costs["Counter Charm I"])
counter_charm_mats = tk.Label(textvariable=counter_charm_mats_txt)
counter_charm_mats.place(x=250,y=100)

fury_charms = ["Fury Charm I", "Fury Charm II"]
counterattack_charms = ["Counterattack Charm I", "Counterattack Charm II"]
unscathed_charms = ["Unscathed Charm I", "Unscathed Charm II"]
counter_charms = ["Counter Charm I", "Counter Charm II", "Counter Charm III"]

fury_charms_opt = tk.StringVar(value="Fury Charm I")
counterattack_charms_opt = tk.StringVar(value="Counterattack Charm I")
unscathed_charms_opt = tk.StringVar(value="Unscathed Charm I")
counter_charms_opt = tk.StringVar(value="Counter Charm I")


def counter_charm_change(a):
    counter_charm_mats_txt.set(counter_charm_costs[a])


counter_charm = tk.OptionMenu(window, counter_charms_opt, *counter_charms, command=counter_charm_change)
counter_charm.place(x=100,y=100)


window.mainloop()