import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math

class SeparatorSizerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configure window
        self.geometry("1100x650")
        self.title("SEPARATOR SIZER")
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # Main frame
        self.main_frame = ctk.CTkFrame(master=self)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Tab view
        self.tabview = ctk.CTkTabview(
            master=self.main_frame,
            fg_color="lightgray",
            segmented_button_fg_color="lightgray",
            segmented_button_selected_color="white",
            segmented_button_selected_hover_color="lightblue",
            text_color="black"
        )
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)

        # Create tabs
        self.create_tabs()

    def create_tabs(self):
        self.tab_3ph_vert = self.tabview.add("3-Phase Vertical")
        self.tab_2ph_vert = self.tabview.add("2-Phase Vertical")
        self.tab_3ph_horizontal = self.tabview.add("3-Phase Horizontal")
        self.tab_2ph_horizontal = self.tabview.add("2-Phase Horizontal")

        self.create_3ph_vertical_tab(self.tab_3ph_vert)
        self.create_2ph_vertical_tab(self.tab_2ph_vert)
        self.create_3ph_horizontal_tab(self.tab_3ph_horizontal)
        self.create_2ph_horizontal_tab(self.tab_2ph_horizontal)
  

    def create_3ph_vertical_tab(self, parent):
        # Header
        header = ctk.CTkLabel(self.tab_3ph_vert, text="3-Phase Vertical Separator Sizing", text_color="black",
                               font=ctk.CTkFont(size=20, family="times new roman", weight="normal"))
        header.pack(pady=(10, 20))
        
        # Create input frame
        input_frame = ttk.Frame(self.tab_3ph_vert)
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Gas properties
        gas_frame = ttk.LabelFrame(input_frame, text="Gas Properties")
        gas_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(gas_frame, text="Gas Flow Rate (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_g_3v = ttk.Entry(gas_frame, width=15)
        self.w_g_3v.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Gas Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_g_3v = ttk.Entry(gas_frame, width=15)
        self.rho_g_3v.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Gas Viscosity (cp):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mu_g_3v = ttk.Entry(gas_frame, width=15)
        self.mu_g_3v.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Operating Pressure (psig):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.pressure_3v = ttk.Entry(gas_frame, width=15)
        self.pressure_3v.grid(row=3, column=1, padx=5, pady=5)
        
        # Light liquid properties
        liq_light_frame = ttk.LabelFrame(input_frame, text="Light Liquid Properties")
        liq_light_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(liq_light_frame, text="Light Liq Flow (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_li_3v = ttk.Entry(liq_light_frame, width=15)
        self.w_li_3v.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(liq_light_frame, text="Light Liq Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_li_3v = ttk.Entry(liq_light_frame, width=15)
        self.rho_li_3v.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(liq_light_frame, text="Light Liq Viscosity (cp):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mu_li_3v = ttk.Entry(liq_light_frame, width=15)
        self.mu_li_3v.grid(row=2, column=1, padx=5, pady=5)
        
        # Heavy liquid properties
        liq_heavy_frame = ttk.LabelFrame(input_frame, text="Heavy Liquid Properties")
        liq_heavy_frame.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(liq_heavy_frame, text="Heavy Liq Flow (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_hi_3v = ttk.Entry(liq_heavy_frame, width=15)
        self.w_hi_3v.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(liq_heavy_frame, text="Heavy Liq Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_hi_3v = ttk.Entry(liq_heavy_frame, width=15)
        self.rho_hi_3v.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(liq_heavy_frame, text="Heavy Liq Viscosity (cp):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mu_hi_3v = ttk.Entry(liq_heavy_frame, width=15)
        self.mu_hi_3v.grid(row=2, column=1, padx=5, pady=5)
        
        # Design parameters
        design_frame = ttk.LabelFrame(input_frame, text="Design Parameters")
        design_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
        
        ttk.Label(design_frame, text="Holdup Time (min):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.t_h_3v = ttk.Entry(design_frame, width=15)
        self.t_h_3v.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(design_frame, text="Surge Time (min):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.t_s_3v = ttk.Entry(design_frame, width=15)
        self.t_s_3v.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(design_frame, text="K Factor Method:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.k_method_3v = ttk.Combobox(design_frame, values=["GPSA", "Otto H. York"], width=15, state="readonly")
        self.k_method_3v.set("GPSA")
        self.k_method_3v.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(design_frame, text="Mist Eliminator:").grid(row=0, column=6, padx=5, pady=5, sticky="e")
        self.mist_eliminator_3v = ttk.Combobox(design_frame, values=["Yes", "No"], width=5, state="readonly")
        self.mist_eliminator_3v.set("Yes")
        self.mist_eliminator_3v.grid(row=0, column=7, padx=5, pady=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.tab_3ph_vert, text="Design Results")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.results_text_3v = scrolledtext.ScrolledText(results_frame, height=10, wrap=tk.WORD)
        self.results_text_3v.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.results_text_3v.config(state=tk.DISABLED)
        
        # Buttons
        button_frame = ttk.Frame(self.tab_3ph_vert)
        button_frame.pack(pady=3)
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate_3ph_vertical).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_3ph_vertical).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Example Values", command=self.example_3ph_vertical).grid(row=0, column=2, padx=5)
        
        # Configure grid weights
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)

    def create_2ph_vertical_tab(self,parent):
        # Header
        header = ctk.CTkLabel(self.tab_2ph_vert, text="2-Phase Vertical Separator Sizing", text_color="black",
                               font=ctk.CTkFont(size=20, family="times new roman", weight="normal"))
        header.pack(pady=(10, 20))
        
        # Create input frame
        input_frame = ttk.Frame(self.tab_2ph_vert)
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Gas properties
        gas_frame = ttk.LabelFrame(input_frame, text="Gas Properties")
        gas_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(gas_frame, text="Gas Flow Rate (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_g_2v = ttk.Entry(gas_frame, width=15)
        self.w_g_2v.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Gas Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_g_2v = ttk.Entry(gas_frame, width=15)
        self.rho_g_2v.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Gas Viscosity (cp):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mu_g_2v = ttk.Entry(gas_frame, width=15)
        self.mu_g_2v.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Operating Pressure (psig):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.pressure_2v = ttk.Entry(gas_frame, width=15)
        self.pressure_2v.grid(row=3, column=1, padx=5, pady=5)
        
        # Liquid properties
        liq_frame = ttk.LabelFrame(input_frame, text="Liquid Properties")
        liq_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(liq_frame, text="Liquid Flow (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_l_2v = ttk.Entry(liq_frame, width=15)
        self.w_l_2v.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(liq_frame, text="Liquid Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_l_2v = ttk.Entry(liq_frame, width=15)
        self.rho_l_2v.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(liq_frame, text="Liquid Viscosity (cp):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mu_l_2v = ttk.Entry(liq_frame, width=15)
        self.mu_l_2v.grid(row=2, column=1, padx=5, pady=5)
        
        # Design parameters
        design_frame = ttk.LabelFrame(input_frame, text="Design Parameters")
        design_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        ttk.Label(design_frame, text="Holdup Time (min):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.t_h_2v = ttk.Entry(design_frame, width=15)
        self.t_h_2v.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(design_frame, text="Surge Time (min):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.t_s_2v = ttk.Entry(design_frame, width=15)
        self.t_s_2v.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(design_frame, text="K Factor Method:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.k_method_2v = ttk.Combobox(design_frame, values=["GPSA", "Otto H. York"], width=15, state="readonly")
        self.k_method_2v.set("GPSA")
        self.k_method_2v.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(design_frame, text="Mist Eliminator:").grid(row=0, column=6, padx=5, pady=5, sticky="e")
        self.mist_eliminator_2v = ttk.Combobox(design_frame, values=["Yes", "No"], width=5, state="readonly")
        self.mist_eliminator_2v.set("Yes")
        self.mist_eliminator_2v.grid(row=0, column=7, padx=5, pady=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.tab_2ph_vert, text="Design Results")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.results_text_2v = scrolledtext.ScrolledText(results_frame, height=10, wrap=tk.WORD)
        self.results_text_2v.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.results_text_2v.config(state=tk.DISABLED)
        
        # Buttons
        button_frame = ttk.Frame(self.tab_2ph_vert)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate_2ph_vertical).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_2ph_vertical).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Example Values", command=self.example_2ph_vertical).grid(row=0, column=2, padx=5)
        
        # Configure grid weights
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
    
    def create_3ph_horizontal_tab(self,parent):
        # Header
        header = ctk.CTkLabel(self.tab_3ph_horizontal, text="3-Phase Horizontal Separator Sizing", text_color="black",
                               font=ctk.CTkFont(size=20, family="times new roman", weight="normal"))
        header.pack(pady=(10, 20))
        
        # Create input frame
        input_frame = ttk.Frame(self.tab_3ph_horizontal)
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Gas properties
        gas_frame = ttk.LabelFrame(input_frame, text="Gas Properties")
        gas_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(gas_frame, text="Gas Flow Rate (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_g_3h = ttk.Entry(gas_frame, width=15)
        self.w_g_3h.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Gas Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_g_3h = ttk.Entry(gas_frame, width=15)
        self.rho_g_3h.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Operating Pressure (psig):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.pressure_3h = ttk.Entry(gas_frame, width=15)
        self.pressure_3h.grid(row=2, column=1, padx=5, pady=5)
        
        # Light liquid properties
        liq_light_frame = ttk.LabelFrame(input_frame, text="Light Liquid Properties")
        liq_light_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(liq_light_frame, text="Light Liq Flow (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_li_3h = ttk.Entry(liq_light_frame, width=15)
        self.w_li_3h.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(liq_light_frame, text="Light Liq Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_li_3h = ttk.Entry(liq_light_frame, width=15)
        self.rho_li_3h.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(liq_light_frame, text="Light Liq Viscosity (cp):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mu_li_3h = ttk.Entry(liq_light_frame, width=15)
        self.mu_li_3h.grid(row=2, column=1, padx=5, pady=5)
        
        # Heavy liquid properties
        liq_heavy_frame = ttk.LabelFrame(input_frame, text="Heavy Liquid Properties")
        liq_heavy_frame.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(liq_heavy_frame, text="Heavy Liq Flow (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_hi_3h = ttk.Entry(liq_heavy_frame, width=15)
        self.w_hi_3h.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(liq_heavy_frame, text="Heavy Liq Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_hi_3h = ttk.Entry(liq_heavy_frame, width=15)
        self.rho_hi_3h.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(liq_heavy_frame, text="Heavy Liq Viscosity (cp):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mu_hi_3h = ttk.Entry(liq_heavy_frame, width=15)
        self.mu_hi_3h.grid(row=2, column=1, padx=5, pady=5)
        
        # Design parameters
        design_frame = ttk.LabelFrame(input_frame, text="Design Parameters")
        design_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
        
        ttk.Label(design_frame, text="Holdup Time (min):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.t_h_3h = ttk.Entry(design_frame, width=15)
        self.t_h_3h.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(design_frame, text="Surge Time (min):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.t_s_3h = ttk.Entry(design_frame, width=15)
        self.t_s_3h.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(design_frame, text="K Factor Method:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.k_method_3h = ttk.Combobox(design_frame, values=["GPSA", "Otto H. York"], width=15, state="readonly")
        self.k_method_3h.set("GPSA")
        self.k_method_3h.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(design_frame, text="L/D Ratio:").grid(row=0, column=6, padx=5, pady=5, sticky="e")
        self.ld_ratio_3h = ttk.Entry(design_frame, width=10)
        self.ld_ratio_3h.grid(row=0, column=7, padx=5, pady=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.tab_3ph_horizontal, text="Design Results")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.results_text_3h = scrolledtext.ScrolledText(results_frame, height=10, wrap=tk.WORD)
        self.results_text_3h.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.results_text_3h.config(state=tk.DISABLED)
        
        # Buttons
        button_frame = ttk.Frame(self.tab_3ph_horizontal)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate_3ph_horizontal).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_3ph_horizontal).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Example Values", command=self.example_3ph_horizontal).grid(row=0, column=2, padx=5)
        
        # Configure grid weights
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
    
    def create_2ph_horizontal_tab(self,parent):
        # Header
        header = ctk.CTkLabel(self.tab_2ph_horizontal, text="2-Phase Horizontal Separator Sizing", text_color="black",
                               font=ctk.CTkFont(size=20, family="times new roman", weight="normal"))
        header.pack(pady=(10, 20))
        
        # Create input frame
        input_frame = ttk.Frame(self.tab_2ph_horizontal)
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Gas properties
        gas_frame = ttk.LabelFrame(input_frame, text="Gas Properties")
        gas_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(gas_frame, text="Gas Flow Rate (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_g_2h = ttk.Entry(gas_frame, width=15)
        self.w_g_2h.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Gas Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_g_2h = ttk.Entry(gas_frame, width=15)
        self.rho_g_2h.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(gas_frame, text="Operating Pressure (psig):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.pressure_2h = ttk.Entry(gas_frame, width=15)
        self.pressure_2h.grid(row=2, column=1, padx=5, pady=5)
        
        # Liquid properties
        liq_frame = ttk.LabelFrame(input_frame, text="Liquid Properties")
        liq_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        
        ttk.Label(liq_frame, text="Liquid Flow (lb/h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.w_l_2h = ttk.Entry(liq_frame, width=15)
        self.w_l_2h.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(liq_frame, text="Liquid Density (lb/ft³):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.rho_l_2h = ttk.Entry(liq_frame, width=15)
        self.rho_l_2h.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(liq_frame, text="Liquid Viscosity (cp):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.mu_l_2h = ttk.Entry(liq_frame, width=15)
        self.mu_l_2h.grid(row=2, column=1, padx=5, pady=5)
        
        # Design parameters
        design_frame = ttk.LabelFrame(input_frame, text="Design Parameters")
        design_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        ttk.Label(design_frame, text="Holdup Time (min):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.t_h_2h = ttk.Entry(design_frame, width=15)
        self.t_h_2h.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(design_frame, text="Surge Time (min):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.t_s_2h = ttk.Entry(design_frame, width=15)
        self.t_s_2h.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(design_frame, text="K Factor Method:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.k_method_2h = ttk.Combobox(design_frame, values=["GPSA", "Otto H. York"], width=15, state="readonly")
        self.k_method_2h.set("GPSA")
        self.k_method_2h.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(design_frame, text="L/D Ratio:").grid(row=0, column=6, padx=5, pady=5, sticky="e")
        self.ld_ratio_2h = ttk.Entry(design_frame, width=10)
        self.ld_ratio_2h.grid(row=0, column=7, padx=5, pady=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.tab_2ph_horizontal, text="Design Results")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.results_text_2h = scrolledtext.ScrolledText(results_frame, height=10, wrap=tk.WORD)
        self.results_text_2h.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.results_text_2h.config(state=tk.DISABLED)
        
        # Buttons
        button_frame = ttk.Frame(self.tab_2ph_horizontal)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Calculate", command=self.calculate_2ph_horizontal).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_2ph_horizontal).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Example Values", command=self.example_2ph_horizontal).grid(row=0, column=2, padx=5)
        
        # Configure grid weights
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
    

    # Calculation methods for each separator type
    def calculate_3ph_vertical(self):
        try:
            # Get input values
            w_g = float(self.w_g_3v.get())
            rho_g = float(self.rho_g_3v.get())
            mu_g = float(self.mu_g_3v.get())
            w_li = float(self.w_li_3v.get())
            rho_li = float(self.rho_li_3v.get())
            mu_li = float(self.mu_li_3v.get())
            w_hi = float(self.w_hi_3v.get())
            rho_hi = float(self.rho_hi_3v.get())
            mu_hi = float(self.mu_hi_3v.get())
            pressure = float(self.pressure_3v.get())
            t_h = float(self.t_h_3v.get())
            t_s = float(self.t_s_3v.get())
            k_method = self.k_method_3v.get()
            mist_eliminator = self.mist_eliminator_3v.get() == "Yes"
            
            # Step 1: Calculate K factor based on method
            if k_method == "GPSA":
                k = 0.35 - 0.0001 * (pressure - 100)
            else:  # Otto H. York
                if 1 <= pressure <= 15:
                    k = 0.1821 + 0.0029 * pressure + 0.0461 * math.log(pressure)
                elif 15 < pressure <= 40:
                    k = 0.35
                else:  # 40 < pressure <= 5500
                    k = 0.43 - 0.023 * math.log(pressure)
            
            # Step 2: Calculate terminal velocity
            v_t = k * math.sqrt((rho_li - rho_g) / rho_g)
            v_v = 0.75 * v_t  # Conservative design
            
            # Step 3: Calculate vapor volumetric flow rate
            q_s = w_g / (3600 * rho_g)
            
            # Step 4: Calculate vessel internal diameter
            d_i = math.sqrt((4 * q_s) / (math.pi * v_v))
            
            # Add allowance for mist eliminator
            d = d_i
            if mist_eliminator:
                d = d_i + 0.25  # Add 3 inches (0.25 ft)
            
            # Round up to nearest half foot
            d = math.ceil(d * 2) / 2
            
            # Step 5: Calculate settling velocities
            # Using ks = 0.163 for hydrocarbon-water system (from Table 4-3)
            v_hi = (0.163 * (rho_hi - rho_li)) / mu_li  # Heavy liquid settling
            v_li = (0.163 * (rho_hi - rho_li)) / mu_hi  # Light liquid rising
            
            # Step 6: Calculate volumetric flow rates
            q_li = w_li / (60 * rho_li)
            q_hi = w_hi / (60 * rho_hi)
            
            # Step 7: Calculate settling times
            h_l = 1.0  # Minimum height (ft)
            h_h = 1.0  # Minimum height (ft)
            ts_hi = (12 * h_l) / v_hi  # in minutes
            ts_li = (12 * h_h) / v_li  # in minutes
            
            # Step 8: Calculate baffle plate area
            a = math.pi * d**2 / 4
            G = 9800 # G=9800 gph/ft2 it is the baffle liquid load gotten from the chart, im just assuming here
            a_d1 = 7.48 * 60 * ((q_li + q_hi) / G )
            Wd = 4 # assume 4 in
            x = Wd / d
            y = (-4.755930*10**-3) + (0.174875*x) + (5.668973*x**2) + (-4.916411*x**3) + (-0.145348*x**4) / 1 + (3.924091*x) + (-6.358805*x**2) + (4.018448*x**3) + (-1.801705*x**4)
            a_d2 = a * y

            if a_d1 > a_d2:
                a_l = a - a_d1
            else:
                a_l = a - a_d2
            
            # Step 9: Calculate the residence time (issue with a and a_L)
            h_l = 1.0  # Minimum height (ft)
            h_h = 1.0  # Minimum height (ft)
            tr_li = (h_l * a) / q_li
            tr_hi = (h_h * a) / q_hi
            
            # Step 10: Calculate holdup height and surge height
            H_R = (q_li * t_h) / a_l
            H_R = max(H_R, 1.0)  # Minimum of 1 ft
            
            H_s = (t_s * (q_li + q_hi)) / a
            H_s = max(H_s, 0.5)  # Minimum of 0.5 ft
            
            # Step 11: Calculate the total height
            h_a = 0.5 # Minimum of 0.5 ft
            H_T = H_R + h_h + h_l + h_a
            
            # Ensure H_T/D ratio is reasonable
            htd_ratio = H_T / d
            if htd_ratio < 1.5:
                H_T = 1.5 * d
            elif htd_ratio > 6.0:
                H_T = 6.0 * d
            
            # Prepare results
            result_text = f"3-PHASE VERTICAL SEPARATOR DESIGN RESULTS\n"
            result_text += "="*50 + "\n"
            result_text += f"Vessel Diameter (D): {d:.2f} ft\n"
            result_text += f"Terminal Velocity (v_T): {v_t:.2f} ft/s\n"
            result_text += f"Vapor Velocity (v_V): {v_v:.2f} ft/s\n"
            result_text += f"Vapor Volumetric Flow (Q_s): {q_s:.2f} ft³/s\n"
            result_text += f"K Factor ({k_method}): {k:.3f} ft/s\n"
            result_text += f"Settling Velocity Heavy Liquid (v_HI): {v_hi:.2f} in/min\n"
            result_text += f"Settling Velocity Light Liquid (v_LI): {v_li:.2f} in/min\n"
            result_text += f"Light Liquid Volumetric Flow (Q_LI): {q_li:.2f} ft³/min\n"
            result_text += f"Heavy Liquid Volumetric Flow (Q_HI): {q_hi:.2f} ft³/min\n"
            result_text += f"Settling Time Heavy Liquid (t_s_HI): {ts_hi:.2f} min\n"
            result_text += f"Settling Time Light Liquid (t_s_LI): {ts_li:.2f} min\n"
            result_text += f"Residence Time Heavy Liquid (t_r_HI): {tr_hi:.2f} min\n"
            result_text += f"Residence Time Light Liquid (t_r_LI): {tr_li:.2f} min\n"
            result_text += f"HoldUp Height (Hr): {H_R:.2f} ft\n"
            result_text += f"Surge Height (Hs): {H_s:.2f} ft\n"
            result_text += f"Total Height Of The Separator (H): {H_T:.2f} ft\n"
            result_text += "\nNOTE: Hakeem dont forget to look at step 8 (the baffle plate) and step 11 (HD and HBN)"
            
            # Display results
            self.results_text_3v.config(state=tk.NORMAL)
            self.results_text_3v.delete(1.0, tk.END)
            self.results_text_3v.insert(tk.END, result_text)
            self.results_text_3v.config(state=tk.DISABLED)
            

        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values in all fields")

    def calculate_2ph_vertical(self):
        try:
            # Get input values
            w_g = float(self.w_g_2v.get())
            rho_g = float(self.rho_g_2v.get())
            mu_g = float(self.mu_g_2v.get())
            w_l = float(self.w_l_2v.get())
            rho_l = float(self.rho_l_2v.get())
            mu_l = float(self.mu_l_2v.get())
            pressure = float(self.pressure_2v.get())
            t_h = float(self.t_h_2v.get())
            t_s = float(self.t_s_2v.get())
            k_method = self.k_method_2v.get()
            mist_eliminator = self.mist_eliminator_2v.get() == "Yes"
            
            # Step 1: Calculate K factor based on method
            if k_method == "GPSA":
                k = 0.35 - 0.0001 * (pressure - 100)
            else:  # Otto H. York
                if 1 <= pressure <= 15:
                    k = 0.1821 + 0.0029 * pressure + 0.0461 * math.log(pressure)
                elif 15 < pressure <= 40:
                    k = 0.35
                else:  # 40 < pressure <= 5500
                    k = 0.43 - 0.023 * math.log(pressure)
            
            # Step 2: Calculate terminal velocity
            v_t = k * math.sqrt((rho_l - rho_g) / rho_g)
            v_v = 0.75 * v_t  # Conservative design
            
            # Step 3: Calculate vapor volumetric flow rate
            q_s = w_g / (3600 * rho_g)
            
            # Step 4: Calculate vessel internal diameter
            d_i = math.sqrt((4 * q_s) / (math.pi * v_v))
            
            # Add allowance for mist eliminator
            d = d_i
            if mist_eliminator:
                d = d_i + 0.25  # Add 3 inches (0.25 ft)
            
            # Round up to nearest half foot
            d = math.ceil(d * 2) / 2
            
            # Step 5: Calculate liquid volumetric flow rate
            q_l = w_l / (60 * rho_l)
            
            # Step 6: Calculate holdup and surge volumes
            v_h = t_h * q_l
            v_s = t_s * q_l
            
            # Step 7: Calculate heights
            a = math.pi * d**2 / 4
            h_h = max(1.0, v_h / a)  # Holdup height (minimum 1 ft)
            h_s = max(0.5, v_s / a)  # Surge height (minimum 0.5 ft)
            
            # Step 8: Calculate disengagement height
            if mist_eliminator:
                h_d = 2.0 + 0.5 * (d/2)  # With mist eliminator
            else:
                h_d = 3.0 + 0.5 * (d/2)  # Without mist eliminator
            
            # Step 9: Calculate total height
            h_t = h_d + h_h + h_s + 1.5  # Additional height for nozzles, etc.
            
            # Prepare results
            result_text = f"2-PHASE VERTICAL SEPARATOR DESIGN RESULTS\n"
            result_text += "="*50 + "\n"
            result_text += f"Vessel Diameter (D): {d:.2f} ft\n"
            result_text += f"Total Height (H_T): {h_t:.2f} ft\n"
            result_text += f"Terminal Velocity (v_T): {v_t:.2f} ft/s\n"
            result_text += f"Vapor Volumetric Flow (Q_s): {q_s:.2f} ft³/s\n"
            result_text += f"Liquid Volumetric Flow (Q_l): {q_l:.2f} ft³/min\n"
            result_text += f"Holdup Volume (V_H): {v_h:.2f} ft³\n"
            result_text += f"Surge Volume (V_S): {v_s:.2f} ft³\n"
            result_text += f"Holdup Height (H_H): {h_h:.2f} ft\n"
            result_text += f"Surge Height (H_S): {h_s:.2f} ft\n"
            result_text += f"Disengagement Height (H_D): {h_d:.2f} ft\n"
            
            # Display results
            self.results_text_2v.config(state=tk.NORMAL)
            self.results_text_2v.delete(1.0, tk.END)
            self.results_text_2v.insert(tk.END, result_text)
            self.results_text_2v.config(state=tk.DISABLED)
            

        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values in all fields")

    
    def calculate_3ph_horizontal(self):
        try:
            # Get input values
            w_g = float(self.w_g_3h.get())
            rho_g = float(self.rho_g_3h.get())
            w_li = float(self.w_li_3h.get())
            rho_li = float(self.rho_li_3h.get())
            mu_li = float(self.mu_li_3h.get())
            w_hi = float(self.w_hi_3h.get())
            rho_hi = float(self.rho_hi_3h.get())
            mu_hi = float(self.mu_hi_3h.get())
            pressure = float(self.pressure_3h.get())
            t_h = float(self.t_h_3h.get())
            t_s = float(self.t_s_3h.get())
            k_method = self.k_method_3h.get()
            ld_ratio = float(self.ld_ratio_3h.get())
            
            # Step 1: Calculate K factor based on method
            if k_method == "GPSA":
                k = 0.35 - 0.0001 * (pressure - 100)
            else:  # Otto H. York
                if 1 <= pressure <= 15:
                    k = 0.1821 + 0.0029 * pressure + 0.0461 * math.log(pressure)
                elif 15 < pressure <= 40:
                    k = 0.35
                else:  # 40 < pressure <= 5500
                    k = 0.43 - 0.023 * math.log(pressure)
            
            # Step 2: Calculate terminal velocity
            v_t = k * math.sqrt((rho_li - rho_g) / rho_g)
            v_v = 0.75 * v_t  # Conservative design
            
            # Step 3: Calculate vapor volumetric flow rate
            q_s = w_g / (3600 * rho_g)
            
            # Step 4: Calculate liquid volumetric flow rates
            q_li = w_li / (60 * rho_li)
            q_hi = w_hi / (60 * rho_hi)
            
            # Step 5: Calculate holdup and surge volumes
            v_h = t_h * (q_li + q_hi)
            v_s = t_s * (q_li + q_hi)
            
            # Step 6: Calculate vessel diameter
            d = (4 * (v_h + v_s) / (0.5 * math.pi * ld_ratio)) ** (1/3)
            d = math.ceil(d * 2) / 2  # Round to nearest half foot
            
            # Step 7: Calculate vessel length
            l = ld_ratio * d
            
            # Step 8: Calculate settling velocities
            v_hi = (0.163 * (rho_hi - rho_li)) / mu_li  # Heavy liquid settling
            v_li = (0.163 * (rho_hi - rho_li)) / mu_hi  # Light liquid rising
            
            # Prepare results
            result_text = f"3-PHASE HORIZONTAL SEPARATOR DESIGN RESULTS\n"
            result_text += "="*50 + "\n"
            result_text += f"Vessel Diameter (D): {d:.2f} ft\n"
            result_text += f"Vessel Length (L): {l:.2f} ft\n"
            result_text += f"L/D Ratio: {ld_ratio:.2f}\n"
            result_text += f"Terminal Velocity (v_T): {v_t:.2f} ft/s\n"
            result_text += f"Vapor Volumetric Flow (Q_s): {q_s:.2f} ft³/s\n"
            result_text += f"Light Liquid Volumetric Flow (Q_LI): {q_li:.2f} ft³/min\n"
            result_text += f"Heavy Liquid Volumetric Flow (Q_HI): {q_hi:.2f} ft³/min\n"
            result_text += f"Holdup Volume (V_H): {v_h:.2f} ft³\n"
            result_text += f"Surge Volume (V_S): {v_s:.2f} ft³\n"
            result_text += f"Settling Velocity Heavy Liquid (v_HI): {v_hi:.2f} in/min\n"
            result_text += f"Settling Velocity Light Liquid (v_LI): {v_li:.2f} in/min\n"
            
            # Display results
            self.results_text_3h.config(state=tk.NORMAL)
            self.results_text_3h.delete(1.0, tk.END)
            self.results_text_3h.insert(tk.END, result_text)
            self.results_text_3h.config(state=tk.DISABLED)
            

        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values in all fields")

    
    def calculate_2ph_horizontal(self):
        try:
            # Get input values
            w_g = float(self.w_g_2h.get())
            rho_g = float(self.rho_g_2h.get())
            w_l = float(self.w_l_2h.get())
            rho_l = float(self.rho_l_2h.get())
            mu_l = float(self.mu_l_2h.get())
            pressure = float(self.pressure_2h.get())
            t_h = float(self.t_h_2h.get())
            t_s = float(self.t_s_2h.get())
            k_method = self.k_method_2h.get()
            ld_ratio = float(self.ld_ratio_2h.get())
            
            # Step 1: Calculate K factor based on method
            if k_method == "GPSA":
                k = 0.35 - 0.0001 * (pressure - 100)
            else:  # Otto H. York
                if 1 <= pressure <= 15:
                    k = 0.1821 + 0.0029 * pressure + 0.0461 * math.log(pressure)
                elif 15 < pressure <= 40:
                    k = 0.35
                else:  # 40 < pressure <= 5500
                    k = 0.43 - 0.023 * math.log(pressure)
            
            # Step 2: Calculate terminal velocity
            v_t = k * math.sqrt((rho_l - rho_g) / rho_g)
            v_v = 0.75 * v_t  # Conservative design
            
            # Step 3: Calculate vapor volumetric flow rate
            q_s = w_g / (3600 * rho_g)
            
            # Step 4: Calculate liquid volumetric flow rate
            q_l = w_l / (60 * rho_l)
            
            # Step 5: Calculate holdup and surge volumes
            v_h = t_h * q_l
            v_s = t_s * q_l
            
            # Step 6: Calculate vessel diameter
            d = (4 * (v_h + v_s) / (0.5 * math.pi * ld_ratio)) ** (1/3)
            d = math.ceil(d * 2) / 2  # Round to nearest half foot
            
            # Step 7: Calculate vessel length
            l = ld_ratio * d
            
            # Prepare results
            result_text = f"2-PHASE HORIZONTAL SEPARATOR DESIGN RESULTS\n"
            result_text += "="*50 + "\n"
            result_text += f"Vessel Diameter (D): {d:.2f} ft\n"
            result_text += f"Vessel Length (L): {l:.2f} ft\n"
            result_text += f"L/D Ratio: {ld_ratio:.2f}\n"
            result_text += f"Terminal Velocity (v_T): {v_t:.2f} ft/s\n"
            result_text += f"Vapor Volumetric Flow (Q_s): {q_s:.2f} ft³/s\n"
            result_text += f"Liquid Volumetric Flow (Q_l): {q_l:.2f} ft³/min\n"
            result_text += f"Holdup Volume (V_H): {v_h:.2f} ft³\n"
            result_text += f"Surge Volume (V_S): {v_s:.2f} ft³\n"
            
            # Display results
            self.results_text_2h.config(state=tk.NORMAL)
            self.results_text_2h.delete(1.0, tk.END)
            self.results_text_2h.insert(tk.END, result_text)
            self.results_text_2h.config(state=tk.DISABLED)
            

        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values in all fields")

    
    # Reset methods for each tab
    def reset_3ph_vertical(self):
        self.w_g_3v.delete(0, tk.END)
        self.rho_g_3v.delete(0, tk.END)
        self.mu_g_3v.delete(0, tk.END)
        self.w_li_3v.delete(0, tk.END)
        self.rho_li_3v.delete(0, tk.END)
        self.mu_li_3v.delete(0, tk.END)
        self.w_hi_3v.delete(0, tk.END)
        self.rho_hi_3v.delete(0, tk.END)
        self.mu_hi_3v.delete(0, tk.END)
        self.pressure_3v.delete(0, tk.END)
        self.t_h_3v.delete(0, tk.END)
        self.t_s_3v.delete(0, tk.END)
        self.k_method_3v.set("GPSA")
        self.mist_eliminator_3v.set("Yes")
        
        self.results_text_3v.config(state=tk.NORMAL)
        self.results_text_3v.delete(1.0, tk.END)
        self.results_text_3v.config(state=tk.DISABLED)
        

    
    def reset_2ph_vertical(self):
        self.w_g_2v.delete(0, tk.END)
        self.rho_g_2v.delete(0, tk.END)
        self.mu_g_2v.delete(0, tk.END)
        self.w_l_2v.delete(0, tk.END)
        self.rho_l_2v.delete(0, tk.END)
        self.mu_l_2v.delete(0, tk.END)
        self.pressure_2v.delete(0, tk.END)
        self.t_h_2v.delete(0, tk.END)
        self.t_s_2v.delete(0, tk.END)
        self.k_method_2v.set("GPSA")
        self.mist_eliminator_2v.set("Yes")
        
        self.results_text_2v.config(state=tk.NORMAL)
        self.results_text_2v.delete(1.0, tk.END)
        self.results_text_2v.config(state=tk.DISABLED)
        

    
    def reset_3ph_horizontal(self):
        self.w_g_3h.delete(0, tk.END)
        self.rho_g_3h.delete(0, tk.END)
        self.w_li_3h.delete(0, tk.END)
        self.rho_li_3h.delete(0, tk.END)
        self.mu_li_3h.delete(0, tk.END)
        self.w_hi_3h.delete(0, tk.END)
        self.rho_hi_3h.delete(0, tk.END)
        self.mu_hi_3h.delete(0, tk.END)
        self.pressure_3h.delete(0, tk.END)
        self.t_h_3h.delete(0, tk.END)
        self.t_s_3h.delete(0, tk.END)
        self.k_method_3h.set("GPSA")
        self.ld_ratio_3h.delete(0, tk.END)
        
        self.results_text_3h.config(state=tk.NORMAL)
        self.results_text_3h.delete(1.0, tk.END)
        self.results_text_3h.config(state=tk.DISABLED)
        

    
    def reset_2ph_horizontal(self):
        self.w_g_2h.delete(0, tk.END)
        self.rho_g_2h.delete(0, tk.END)
        self.w_l_2h.delete(0, tk.END)
        self.rho_l_2h.delete(0, tk.END)
        self.mu_l_2h.delete(0, tk.END)
        self.pressure_2h.delete(0, tk.END)
        self.t_h_2h.delete(0, tk.END)
        self.t_s_2h.delete(0, tk.END)
        self.k_method_2h.set("GPSA")
        self.ld_ratio_2h.delete(0, tk.END)
        
        self.results_text_2h.config(state=tk.NORMAL)
        self.results_text_2h.delete(1.0, tk.END)
        self.results_text_2h.config(state=tk.DISABLED)
        

    
    # Example methods for each tab
    def example_3ph_vertical(self):
        self.reset_3ph_vertical()
        self.w_g_3v.insert(0, "263150")
        self.rho_g_3v.insert(0, "0.72")
        self.mu_g_3v.insert(0, "0.0113")
        self.w_li_3v.insert(0, "11080")
        self.rho_li_3v.insert(0, "54.0")
        self.mu_li_3v.insert(0, "0.630")
        self.w_hi_3v.insert(0, "2770")
        self.rho_hi_3v.insert(0, "62.1")
        self.mu_hi_3v.insert(0, "0.764")
        self.pressure_3v.insert(0, "165")
        self.t_h_3v.insert(0, "25")
        self.t_s_3v.insert(0, "5")

    
    def example_2ph_vertical(self):
        self.reset_2ph_vertical()
        self.w_g_2v.insert(0, "263150")
        self.rho_g_2v.insert(0, "0.72")
        self.mu_g_2v.insert(0, "0.0113")
        self.w_l_2v.insert(0, "13850")
        self.rho_l_2v.insert(0, "54.0")
        self.mu_l_2v.insert(0, "0.630")
        self.pressure_2v.insert(0, "165")
        self.t_h_2v.insert(0, "25")
        self.t_s_2v.insert(0, "5")

    
    def example_3ph_horizontal(self):
        self.reset_3ph_horizontal()
        self.w_g_3h.insert(0, "263150")
        self.rho_g_3h.insert(0, "0.72")
        self.w_li_3h.insert(0, "11080")
        self.rho_li_3h.insert(0, "54.0")
        self.mu_li_3h.insert(0, "0.630")
        self.w_hi_3h.insert(0, "2770")
        self.rho_hi_3h.insert(0, "62.1")
        self.mu_hi_3h.insert(0, "0.764")
        self.pressure_3h.insert(0, "165")
        self.t_h_3h.insert(0, "10")
        self.t_s_3h.insert(0, "5")
        self.ld_ratio_3h.insert(0, "1.6")

    
    def example_2ph_horizontal(self):
        self.reset_2ph_horizontal()
        self.w_g_2h.insert(0, "263150")
        self.rho_g_2h.insert(0, "0.72")
        self.w_l_2h.insert(0, "13850")
        self.rho_l_2h.insert(0, "54.0")
        self.mu_l_2h.insert(0, "0.630")
        self.pressure_2h.insert(0, "165")
        self.t_h_2h.insert(0, "10")
        self.t_s_2h.insert(0, "5")
        self.ld_ratio_2h.insert(0, "3.0")



if __name__ == "__main__":
    app = SeparatorSizerApp()
    app.mainloop()
