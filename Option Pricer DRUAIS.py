#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import QuantLib as ql
import tkinter as tk
import customtkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

def binomial_price (option, bsm_process, steps):
    binomial_engine = ql.BinomialVanillaEngine(bsm_process, "crr", steps)
    option.setPricingEngine(binomial_engine)
    return option.NPV()

def calculation():
    """
    """

    if type_option2.get()== 'Call' and type_option.get()== 'EUROPEENE' :
        
        maturity_entree=mat.get()
        maturity_date= ql.Date(int(maturity_entree[0:2]),int(maturity_entree[3:5]),int(maturity_entree[6:10]))
        
        spot_price=float(spot.get())
        
        strike_price = float(strike.get())
        
        volatility= float(vol.get())
        
        dividend_rate= 0.05
        
        option_type=ql.Option.Call
        
        risk_free_rate = 0.00
        
        day_count = ql.Actual365Fixed()
        
        calendar=ql.France()
        
        calculation_date=ql.Date.todaysDate()
        
        ql.Settings.instance().evaluationDate = calculation_date
        
        payoff=ql.PlainVanillaPayoff(option_type,strike_price)
        
        exercise= ql.EuropeanExercise(maturity_date)
        
        european_option=ql.VanillaOption(payoff,exercise)
        
        steps=range(2,200,1)
        
        spot_handle=ql.QuoteHandle(ql.SimpleQuote(spot_price))
        
        flat_ts=ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, risk_free_rate, day_count))
        
        dividend_yield = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, dividend_rate, day_count))
        
        flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calculation_date, calendar, volatility, day_count))
        
        bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)
        
        eu_prices = [binomial_price(european_option, bsm_process, step) for step in steps]
        
        bin_tree_price = eu_prices[197]
        
        european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
        
        bs_price = european_option.NPV()
        
        plt.plot(steps, eu_prices, label="Prix Arbre Binomial {bin_tree_price:.3f}", lw=2, alpha=0.6)
        plt.plot([0,200], [bs_price, bs_price],"r--", label=f" Prix BSM {bs_price:.3f}", lw=2, alpha=0.6)
        plt.xlabel("Steps", size=14)
        plt.ylabel("Prix", size=14)
        plt.title("Prix de l’arbre binomial pour différents steps", size=14)
        plt.legend()
        plt.show()
    
    if type_option2.get()== 'Call'  and type_option.get()== 'AMERICAINE' :
        
        maturity_entree=mat.get()
        maturity_date= ql.Date(int(maturity_entree[0:2]),int(maturity_entree[3:5]),int(maturity_entree[6:10]))
        
        spot_price=float(spot.get())
        
        strike_price = float(strike.get())
        
        volatility= float(vol.get())
        
        dividend_rate= 0.05
        
        option_type=ql.Option.Call
        
        risk_free_rate = 0.00
        
        day_count = ql.Actual365Fixed()
        
        calendar=ql.France()
        
        calculation_date=ql.Date.todaysDate()
        
        ql.Settings.instance().evaluationDate = calculation_date
        
        payoff = ql.PlainVanillaPayoff(option_type, strike_price)
        
        settlement=calculation_date
        
        am_exercise=ql.AmericanExercise(settlement, maturity_date)
        
        american_option= ql.VanillaOption(payoff, am_exercise)
        
        steps=range(2,200,1)
        
        spot_handle=ql.QuoteHandle(ql.SimpleQuote(spot_price))
        
        flat_ts=ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, risk_free_rate, day_count))
        
        dividend_yield = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, dividend_rate, day_count))
        
        flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calculation_date, calendar, volatility, day_count))
        
        bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)
        
        am_prices = [binomial_price(american_option, bsm_process, step) for step in steps]
        
        bin_tree_price = am_prices[197]

        plt.plot(steps, am_prices, label="Prix Arbre Binomial {bin_tree_price:.3f}", lw=2, alpha=0.6)
        plt.xlabel("Steps", size=14)
        plt.ylabel("Prix", size=14)
        plt.title("Prix de l’arbre binomial pour différents steps", size=14)
        plt.legend()
        plt.show()
        
    if type_option2.get()== 'Put'  and type_option.get()== 'EUROPEENE' :
        
        maturity_entree=mat.get()
        maturity_date= ql.Date(int(maturity_entree[0:2]),int(maturity_entree[3:5]),int(maturity_entree[6:10]))
        
        spot_price=float(spot.get())
        
        strike_price = float(strike.get())
        
        volatility= float(vol.get())
        
        dividend_rate= 0.05
        
        option_type=ql.Option.Put
        
        risk_free_rate = 0.00
        
        day_count = ql.Actual365Fixed()
        
        calendar=ql.France()
        
        calculation_date=ql.Date.todaysDate()
        
        ql.Settings.instance().evaluationDate = calculation_date
        
        payoff=ql.PlainVanillaPayoff(option_type,strike_price)
        
        exercise= ql.EuropeanExercise(maturity_date)
        
        european_option=ql.VanillaOption(payoff,exercise)
        
        steps=range(2,200,1)
        
        spot_handle=ql.QuoteHandle(ql.SimpleQuote(spot_price))
        
        flat_ts=ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, risk_free_rate, day_count))
        
        dividend_yield = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, dividend_rate, day_count))
        
        flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calculation_date, calendar, volatility, day_count))
        
        bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)
        
        eu_prices = [binomial_price(european_option, bsm_process, step) for step in steps]
        
        bin_tree_price = eu_prices[197]
        
        european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
        
        bs_price = european_option.NPV()

        plt.plot(steps, eu_prices, label="Prix Arbre Binomial {bin_tree_price:.3f}", lw=2, alpha=0.6)
        plt.plot([0,200], [bs_price, bs_price],"r--", label=f" Prix BSM {bs_price:.3f}", lw=2, alpha=0.6)
        plt.xlabel("Steps", size=14)
        plt.ylabel("Prix", size=14)
        plt.title("Prix de l’arbre binomial pour différents steps", size=14)
        plt.legend()
        plt.show()
        
    if type_option2.get()== 'Put'  and type_option.get()== 'AMERICAINE' :
        
        maturity_entree=mat.get()
        maturity_date= ql.Date(int(maturity_entree[0:2]),int(maturity_entree[3:5]),int(maturity_entree[6:10]))
        
        spot_price=float(spot.get())
        
        strike_price = float(strike.get())
        
        volatility= float(vol.get())
        
        dividend_rate= 0.05
        
        option_type=ql.Option.Put
        
        risk_free_rate = 0.00
        
        day_count = ql.Actual365Fixed()
        
        calendar=ql.France()
        
        calculation_date=ql.Date.todaysDate()
        
        ql.Settings.instance().evaluationDate = calculation_date
        
        payoff = ql.PlainVanillaPayoff(option_type, strike_price)
        
        settlement=calculation_date
        
        am_exercise=ql.AmericanExercise(settlement, maturity_date)
        
        american_option= ql.VanillaOption(payoff, am_exercise)
        
        steps=range(2,200,1)
        
        spot_handle=ql.QuoteHandle(ql.SimpleQuote(spot_price))
        
        flat_ts=ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, risk_free_rate, day_count))
        
        dividend_yield = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, dividend_rate, day_count))
        
        flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calculation_date, calendar, volatility, day_count))
        
        bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)
        
        am_prices = [binomial_price(american_option, bsm_process, step) for step in steps]
        
        bin_tree_price = am_prices[197]

        plt.plot(steps, am_prices, label="Prix Arbre Binomial {bin_tree_price:.3f}", lw=2, alpha=0.6)
        plt.xlabel("Steps", size=14)
        plt.ylabel("Prix", size=14)
        plt.title("Prix de l’arbre binomial pour différents steps", size=14)
        plt.legend()
        plt.show()
         

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

# root window
root = customtkinter.CTk()
root.geometry("500x500")
root.resizable(False, False)
root.title("Option pricer")

mat= tk.StringVar()
spot=tk.StringVar()
strike = tk.StringVar()
vol = tk.StringVar()
div=tk.StringVar()
type_option = tk.StringVar()
type_option2 = tk.StringVar()

message = tk.Label(root, text="Choisir le type d'option :")
message.pack()

types = ('Call','Put')

# radio buttons
for i in types:
    r = ttk.Radiobutton(root, text=i, value=i, variable=type_option2  )
    r.pack(fill='x', padx=5, pady=5)

calculation2 = tk.Frame(root)
calculation2.pack(padx=10, pady=10, fill='x', expand=True)

message = tk.Label(root, text="Entrer les caracteristiques :")
message.pack()

# Maturité
maturity_label = ttk.Label(root, text="Date de Maturité (JJ/MM/AAAA) :")
maturity_label.pack(fill='x', expand=True)

maturity_entry = ttk.Entry(root, textvariable=mat)
maturity_entry.pack(fill='x', expand=True)
maturity_entry.focus()

# Prix Spot
spot_price_label = ttk.Label(root, text=" Prix Spot :")
spot_price_label.pack(fill='x', expand=True)

spot_price_entry = ttk.Entry(root, textvariable=spot)
spot_price_entry.pack(fill='x', expand=True)

# Prix Strike
strike_price_label = ttk.Label(root, text="Prix Strike :")
strike_price_label.pack(fill='x', expand=True)

strike_price_entry = ttk.Entry(root, textvariable=strike)
strike_price_entry.pack(fill='x', expand=True)

# Volatilité
volatility_label = ttk.Label(root, text="Volatilité :")
volatility_label.pack(fill='x', expand=True)

volatility_entry = ttk.Entry(root, textvariable=vol)
volatility_entry.pack(fill='x', expand=True)

calculation2 = tk.Frame(root)
calculation2.pack(padx=10, pady=10, fill='x', expand=True)

types = ('EUROPEENE','AMERICAINE')

# radio buttons
for i in types:
    r = ttk.Radiobutton(root, text=i, value=i, variable=type_option  )
    r.pack(fill='x', padx=5, pady=5)

print(type_option2.get())
print(type_option.get())    

# Pricer
calculation_button = customtkinter.CTkButton(master=root, text="Pricer",command=calculation)
calculation_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#tk.Button(signin, bg='yellow', fg='red',text="Let's price it", command=login_clicked)
calculation_button.pack(fill=None, expand=False, padx=5, pady=5)

root.mainloop()

