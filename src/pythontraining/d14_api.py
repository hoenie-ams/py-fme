"""
Demo of requests
"""
import requests

url = "https://api.exchangerate.host/latest"

r = requests.get(url).json()
