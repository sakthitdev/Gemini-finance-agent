# Gemini-finance-agent
This is a capstone project as a part of 5-Day AI Agents Intensive Course with Google

# Working
Powered by Flask, Gemini AI, and Matplotlib

This project combines two powerful tools into one seamless web application:

    AI Topic Analyzer
    
    Takes any topic
    
    Generates a structured explanation using Google Gemini AI
    
    Determines if a graph is needed
    
    If yes → Generates data and auto-renders a visual graph
    
    All processed in real-time inside the browser
    
    Smart Monthly Expense Calculator
    
    Calculates salary, expenses, remaining balance
    
    Provides intelligent financial remarks
    
    Clean and responsive UI

# Features
   AI Topic Analyzer

Generates a clean, hierarchical explanation:

Topic
    Short Description
    Key Concepts
    How It Works
    Advantages
    Disadvantages
    Real-World Applications
    Example
    Summary


Always formatted with indentation and bullet points

Uses Gemini 1.5 Flash API

Fully modular code structure

# Automatic Graph Generator

Gemini decides if a graph is needed

Gemini produces JSON graph data

Matplotlib renders graph → converted to Base64 → displayed in browser

Graph never saved to disk

# Smart Expense Calculator

Input:

  Salary
  
  Food
  
  Rent
  
  Travel
  
  Bills
  
  Other expenses
  
  EMI?
  
  Life insurance?

Output:

  Total expenses
  
  Remaining balance
  
  Financial insights
  
  Emoji-based suggestions

# Project Structure
project/


├── Main.py                        # Main Flask backend


├── agents/

│      └── gemini_utils.py           # Gemini AI logic


├── tools/

│      └── graph_utils.py            # Graph generation utility


└── templates/

  └── index.html                # Web interface (HTML + JS)


This modular structure helps keep the logic clean and maintainable.

# Installation

# 1️) Clone this repository
    gh repo clone sakthitdev/Gemini-finance-agent
    https://github.com/sakthitdev/Gemini-finance-agent.git

# 2️) Install required packages
    pip install flask google-generativeai matplotlib
    
# 3) Get a API from google AI Studio and add to the gemini_util.py file:
    genai.configure(api_key="ADD THE AIP HERE")

# 4) Run the Application
    python Main.py

open this port in your browser:

http://127.0.0.1:5000/

# Woring

User enters a topic

Gemini generates:

Structured explanation

Decision: graph needed or not

If graph required:

Gemini outputs JSON:

{

  "x": [...],
  
  "y": [...],
  
  "xlabel": "...",

  "ylabel": "...",
  
  "topic": "..."
  
}


Matplotlib renders the graph

Graph sent to browser as Base64


Calculator Logic:

    Adds all expenses
    
    Subtracts from salary
    
    Determines financial health
    
    Adds intelligent suggestions

Technologies Used:

    Python 3
    
    Flask
    
    Google Gemini 1.5 Flash
    
    Matplotlib
    
    HTML / CSS / JavaScript


# License

MIT License © 2025
