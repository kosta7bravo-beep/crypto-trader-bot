import os
import threading
import telebot
from flask import Flask

TOKEN = "8798719747:AAEPtqn-V6h10N1Tjye9GCpvvLR6LqU-5YE"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "OK", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Трейдинг-бот успешно запущен!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Получено: {message.text}")
