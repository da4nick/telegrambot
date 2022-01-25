import mainbot
import pytest
import unittest.mock
import asyncio

def test_bot():
    with unittest.mock.patch('mainbot.bot'):
        message = unittest.mock.Mock()
        mainbot.find_anekdot(message)
        message.send.asser_called_with('Я тебя не понимаю, напиши /help')
